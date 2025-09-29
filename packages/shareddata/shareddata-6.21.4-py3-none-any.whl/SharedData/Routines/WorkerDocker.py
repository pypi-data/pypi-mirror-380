# SharedData/Routines/WorkerDocker.py

# Implements a dockerized worker with Flask web interface for configuration
# Wraps the original Worker functionality with a web-based setup interface
# Allows initial configuration via web form and subsequent updates with authentication

import os
import sys
import time
import threading
import subprocess
import json
from pathlib import Path
try:
    from flask import Flask, request, render_template_string, jsonify, redirect, url_for
except ImportError:
    print("Flask is not installed. Please install it with: pip install flask")
    sys.exit(1)
import importlib.util

# Global variables
app = Flask(__name__)
worker_thread = None
worker_process = None
is_configured = False
config_lock = threading.Lock()

# HTML Templates
INITIAL_CONFIG_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>SharedData Worker - Initial Configuration</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 800px; margin: 50px auto; padding: 20px; }
        .container { background-color: #f9f9f9; padding: 20px; border-radius: 10px; }
        textarea { width: 100%; height: 400px; font-family: monospace; }
        button { background-color: #4CAF50; color: white; padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer; }
        button:hover { background-color: #45a049; }
        .info { background-color: #e7f3ff; padding: 15px; border-radius: 5px; margin-bottom: 20px; }
    </style>
</head>
<body>
    <div class="container">
        <h1>SharedData Worker Docker - Initial Configuration</h1>
        
        <div class="info">
            <h3>Instructions:</h3>
            <p>Enter your environment variables below, one per line in the format: VARIABLE_NAME=value</p>
            <p><strong>Required variables:</strong></p>
            <ul>
                <li>SHAREDDATA_TOKEN - Authentication token (will be used for future config updates)</li>
                <li>GIT_USER - Git username</li>
                <li>GIT_TOKEN - Git personal access token</li>
                <li>USERNAME - System username</li>
                <li>SOURCE_FOLDER - Source code folder path</li>
            </ul>
        </div>
        
        <form method="POST" action="/initialconfig">
            <h3>Environment Variables:</h3>
            <textarea name="env_vars" placeholder="SHAREDDATA_TOKEN=your_token_here
GIT_USER=your_username
GIT_TOKEN=your_token
GIT_EMAIL=your_email@example.com
USERNAME=worker
SOURCE_FOLDER=/home/worker/src
WORKERPOOL_STREAM=shareddata-workerpool
GIT_SERVER=github.com
GIT_PROTOCOL=https"></textarea>
            <br><br>
            <button type="submit">Save Configuration and Start Worker</button>
        </form>
    </div>
</body>
</html>
'''

UPDATE_CONFIG_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>SharedData Worker - Update Configuration</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 800px; margin: 50px auto; padding: 20px; }
        .container { background-color: #f9f9f9; padding: 20px; border-radius: 10px; }
        textarea { width: 100%; height: 300px; font-family: monospace; }
        input[type="password"] { width: 100%; padding: 10px; margin: 10px 0; }
        button { background-color: #4CAF50; color: white; padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer; }
        button:hover { background-color: #45a049; }
        .error { background-color: #ffebee; color: #c62828; padding: 10px; border-radius: 5px; margin-bottom: 20px; }
        .success { background-color: #e8f5e8; color: #2e7d32; padding: 10px; border-radius: 5px; margin-bottom: 20px; }
        .status { background-color: #fff3e0; padding: 15px; border-radius: 5px; margin-bottom: 20px; }
    </style>
</head>
<body>
    <div class="container">
        <h1>SharedData Worker Docker - Update Configuration</h1>
        
        <div class="status">
            <h3>Current Status:</h3>
            <p><strong>Worker Status:</strong> {{ worker_status }}</p>
            <p><strong>Configuration:</strong> {{ config_status }}</p>
        </div>
        
        {% if error %}
        <div class="error">{{ error }}</div>
        {% endif %}
        
        {% if success %}
        <div class="success">{{ success }}</div>
        {% endif %}
        
        <form method="POST" action="/updateconfig">
            <h3>Authentication Token:</h3>
            <input type="password" name="token" placeholder="Enter SHAREDDATA_TOKEN" required>
            
            <h3>Environment Variables:</h3>
            <textarea name="env_vars" placeholder="Enter environment variables, one per line:
VARIABLE_NAME=value">{{ current_env }}</textarea>
            <br><br>
            <button type="submit">Update Configuration</button>
        </form>
        
        <br>
        <form method="POST" action="/restart" style="display: inline;">
            <input type="hidden" name="token" id="restart_token">
            <button type="button" onclick="document.getElementById('restart_token').value=document.querySelector('input[name=token]').value; this.form.submit();">Restart Worker</button>
        </form>
        
        <form method="POST" action="/stop" style="display: inline; margin-left: 10px;">
            <input type="hidden" name="token" id="stop_token">
            <button type="button" onclick="document.getElementById('stop_token').value=document.querySelector('input[name=token]').value; this.form.submit();" style="background-color: #f44336;">Stop Worker</button>
        </form>
    </div>
</body>
</html>
'''

def parse_env_vars(env_text):
    """Parse environment variables from multi-line text format."""
    env_vars = {}
    for line in env_text.strip().split('\n'):
        line = line.strip()
        if line and '=' in line and not line.startswith('#'):
            key, value = line.split('=', 1)
            env_vars[key.strip()] = value.strip()
    return env_vars

def save_to_etc_environment(env_vars):
    """Save environment variables to /etc/environment."""
    try:
        # In Docker containers, we typically don't have permission to write to /etc/environment
        # So we'll just update the current process environment and let the env file handle persistence
        print("Updating current process environment (skipping /etc/environment in container)")
        os.environ.update(env_vars)
        return True
    except Exception as e:
        print(f"Error updating environment: {e}")
        # Always return True since we don't actually need /etc/environment in containers
        return True

def save_to_worker_env_file(env_vars):
    """Save environment variables to shareddata-worker.env file."""
    try:
        # In Docker container, save to home directory where we have write permissions
        # rather than trying to use the SOURCE_FOLDER which might be from host
        if os.path.exists('/home/worker'):
            env_file_path = Path('/home/worker/shareddata-worker.env')
        else:
            # Fallback for non-Docker environments
            source_folder = env_vars.get('SOURCE_FOLDER', os.environ.get('SOURCE_FOLDER', os.path.expanduser('~/src')))
            env_file_path = Path(source_folder).parent / 'shareddata-worker.env'
        
        # Ensure directory exists
        env_file_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Read current env file if it exists
        current_lines = []
        if env_file_path.exists():
            with open(env_file_path, 'r') as f:
                current_lines = f.readlines()
        
        # Update or add variables
        existing_keys = set()
        updated_lines = []
        
        for line in current_lines:
            line = line.strip()
            if line and '=' in line and not line.startswith('#'):
                key = line.split('=', 1)[0]
                if key in env_vars:
                    # Update existing variable
                    updated_lines.append(f"{key}={env_vars[key]}\n")
                    existing_keys.add(key)
                else:
                    # Keep existing variable
                    updated_lines.append(line + '\n')
            else:
                # Keep comments and empty lines
                updated_lines.append(line + '\n')
        
        # Add new variables
        for key, value in env_vars.items():
            if key not in existing_keys:
                updated_lines.append(f"{key}={value}\n")
        
        # Write to env file
        with open(env_file_path, 'w') as f:
            f.writelines(updated_lines)
        
        return True
    except Exception as e:
        print(f"Error saving to worker env file: {e}")
        return False

def load_current_env():
    """Load current environment variables for display."""
    # Try to load from shareddata-worker.env file
    # In Docker container, check home directory first
    if os.path.exists('/home/worker'):
        env_file_path = Path('/home/worker/shareddata-worker.env')
    else:
        # Fallback for non-Docker environments
        source_folder = os.environ.get('SOURCE_FOLDER', os.path.expanduser('~/src'))
        env_file_path = Path(source_folder).parent / 'shareddata-worker.env'
    
    env_vars = {}
    if env_file_path.exists():
        try:
            with open(env_file_path, 'r') as f:
                for line in f:
                    line = line.strip()
                    if line and '=' in line and not line.startswith('#'):
                        key, value = line.split('=', 1)
                        env_vars[key.strip()] = value.strip()
        except Exception as e:
            print(f"Error loading env file: {e}")
    
    # Convert to display format
    env_text = '\n'.join([f"{k}={v}" for k, v in env_vars.items()])
    return env_text

def authenticate_token(token):
    """Authenticate using SHAREDDATA_TOKEN."""
    stored_token = os.environ.get('SHAREDDATA_TOKEN')
    return stored_token and token == stored_token

def start_worker():
    """Start the SharedData worker in a separate process."""
    global worker_process
    
    try:
        if worker_process and worker_process.poll() is None:
            print("Worker is already running")
            return True
        
        # Import the worker module and run it
        source_folder = os.environ.get('SOURCE_FOLDER', os.path.expanduser('~/src'))
        python_path = os.path.join(source_folder, 'venv', 'bin', 'python')
        
        if not os.path.exists(python_path):
            python_path = sys.executable
        
        cmd = [python_path, '-m', 'SharedData.Routines.Worker', '--batchjobs', '4']
        
        # Set environment for the subprocess
        env = os.environ.copy()
        
        worker_process = subprocess.Popen(
            cmd,
            env=env,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            cwd=source_folder
        )
        
        print(f"Worker started with PID: {worker_process.pid}")
        return True
        
    except Exception as e:
        print(f"Error starting worker: {e}")
        return False

def stop_worker():
    """Stop the SharedData worker."""
    global worker_process
    
    try:
        if worker_process and worker_process.poll() is None:
            worker_process.terminate()
            try:
                worker_process.wait(timeout=10)
            except subprocess.TimeoutExpired:
                worker_process.kill()
                worker_process.wait()
            print("Worker stopped")
            return True
        else:
            print("Worker is not running")
            return True
    except Exception as e:
        print(f"Error stopping worker: {e}")
        return False

def get_worker_status():
    """Get current worker status."""
    global worker_process
    
    if worker_process is None:
        return "Not Started"
    elif worker_process.poll() is None:
        return "Running"
    else:
        return f"Stopped (exit code: {worker_process.returncode})"

@app.route('/')
def index():
    """Main page - redirect based on configuration status."""
    if is_configured:
        return redirect(url_for('update_config'))
    else:
        return redirect(url_for('initial_config'))

@app.route('/initialconfig', methods=['GET', 'POST'])
def initial_config():
    """Handle initial configuration setup."""
    global is_configured
    
    if is_configured:
        return redirect(url_for('update_config'))
    
    if request.method == 'GET':
        return render_template_string(INITIAL_CONFIG_TEMPLATE)
    
    # POST request - process configuration
    env_text = request.form.get('env_vars', '').strip()
    
    if not env_text:
        return render_template_string(INITIAL_CONFIG_TEMPLATE.replace(
            '<form method="POST"', 
            '<div class="error">Please provide environment variables.</div><form method="POST"'
        ))
    
    try:
        env_vars = parse_env_vars(env_text)
        
        # Validate required variables
        required_vars = ['SHAREDDATA_TOKEN', 'GIT_USER', 'GIT_TOKEN', 'USERNAME']
        missing_vars = [var for var in required_vars if var not in env_vars]
        
        if missing_vars:
            error_msg = f"Missing required variables: {', '.join(missing_vars)}"
            return render_template_string(INITIAL_CONFIG_TEMPLATE.replace(
                '<form method="POST"',
                f'<div class="error">{error_msg}</div><form method="POST"'
            ))
        
        with config_lock:
            # Save environment variables
            if save_to_etc_environment(env_vars) and save_to_worker_env_file(env_vars):
                is_configured = True
                # Start the worker
                if start_worker():
                    return redirect(url_for('update_config', success='Configuration saved and worker started successfully!'))
                else:
                    return redirect(url_for('update_config', error='Configuration saved but failed to start worker.'))
            else:
                return render_template_string(INITIAL_CONFIG_TEMPLATE.replace(
                    '<form method="POST"',
                    '<div class="error">Failed to save configuration. Please check permissions.</div><form method="POST"'
                ))
                
    except Exception as e:
        error_msg = f"Error processing configuration: {str(e)}"
        return render_template_string(INITIAL_CONFIG_TEMPLATE.replace(
            '<form method="POST"',
            f'<div class="error">{error_msg}</div><form method="POST"'
        ))

@app.route('/updateconfig', methods=['GET', 'POST'])
def update_config():
    """Handle configuration updates (requires authentication)."""
    global is_configured
    
    if not is_configured:
        return redirect(url_for('initial_config'))
    
    error = request.args.get('error')
    success = request.args.get('success')
    
    if request.method == 'GET':
        current_env = load_current_env()
        worker_status = get_worker_status()
        config_status = "Configured" if is_configured else "Not Configured"
        
        return render_template_string(UPDATE_CONFIG_TEMPLATE, 
                                    current_env=current_env,
                                    worker_status=worker_status,
                                    config_status=config_status,
                                    error=error,
                                    success=success)
    
    # POST request - process update
    token = request.form.get('token', '').strip()
    env_text = request.form.get('env_vars', '').strip()
    
    if not authenticate_token(token):
        return redirect(url_for('update_config', error='Invalid authentication token.'))
    
    if not env_text:
        return redirect(url_for('update_config', error='Please provide environment variables.'))
    
    try:
        env_vars = parse_env_vars(env_text)
        
        with config_lock:
            if save_to_etc_environment(env_vars) and save_to_worker_env_file(env_vars):
                # Restart worker to pick up new configuration
                stop_worker()
                time.sleep(2)
                if start_worker():
                    return redirect(url_for('update_config', success='Configuration updated and worker restarted successfully!'))
                else:
                    return redirect(url_for('update_config', error='Configuration updated but failed to restart worker.'))
            else:
                return redirect(url_for('update_config', error='Failed to save configuration updates.'))
                
    except Exception as e:
        return redirect(url_for('update_config', error=f'Error updating configuration: {str(e)}'))

@app.route('/restart', methods=['POST'])
def restart_worker():
    """Restart the worker (requires authentication)."""
    token = request.form.get('token', '').strip()
    
    if not authenticate_token(token):
        return redirect(url_for('update_config', error='Invalid authentication token.'))
    
    try:
        with config_lock:
            stop_worker()
            time.sleep(2)
            if start_worker():
                return redirect(url_for('update_config', success='Worker restarted successfully!'))
            else:
                return redirect(url_for('update_config', error='Failed to restart worker.'))
    except Exception as e:
        return redirect(url_for('update_config', error=f'Error restarting worker: {str(e)}'))

@app.route('/stop', methods=['POST'])
def stop_worker_route():
    """Stop the worker (requires authentication)."""
    token = request.form.get('token', '').strip()
    
    if not authenticate_token(token):
        return redirect(url_for('update_config', error='Invalid authentication token.'))
    
    try:
        with config_lock:
            if stop_worker():
                return redirect(url_for('update_config', success='Worker stopped successfully!'))
            else:
                return redirect(url_for('update_config', error='Failed to stop worker.'))
    except Exception as e:
        return redirect(url_for('update_config', error=f'Error stopping worker: {str(e)}'))

@app.route('/status')
def status():
    """Get worker status as JSON."""
    return jsonify({
        'configured': is_configured,
        'worker_status': get_worker_status(),
        'worker_pid': worker_process.pid if worker_process and worker_process.poll() is None else None
    })

@app.route('/api/config', methods=['POST'])
def api_config():
    """API endpoint to configure environment variables programmatically."""
    global is_configured
    
    try:
        # Parse JSON request
        config_data = request.get_json()
        if not config_data:
            return jsonify({'error': 'No JSON data provided'}), 400
        
        # Check if this is initial config or update
        if is_configured:
            # For updates, require authentication
            token = config_data.get('token') or request.headers.get('Authorization', '').replace('Bearer ', '')
            if not authenticate_token(token):
                return jsonify({'error': 'Invalid or missing authentication token'}), 401
        
        # Get environment variables from the request
        env_vars = config_data.get('env_vars', {})
        if not env_vars:
            return jsonify({'error': 'No environment variables provided'}), 400
        
        # Validate required variables for initial config
        if not is_configured:
            required_vars = ['SHAREDDATA_TOKEN', 'GIT_USER', 'GIT_TOKEN', 'USERNAME']
            missing_vars = [var for var in required_vars if var not in env_vars]
            
            if missing_vars:
                return jsonify({'error': f'Missing required variables: {", ".join(missing_vars)}'}), 400
        
        with config_lock:
            # Save environment variables
            if save_to_etc_environment(env_vars) and save_to_worker_env_file(env_vars):
                if not is_configured:
                    is_configured = True
                    # Start the worker for initial config
                    worker_started = start_worker()
                    return jsonify({
                        'success': True,
                        'message': 'Configuration saved successfully',
                        'worker_started': worker_started,
                        'initial_config': True
                    })
                else:
                    # Restart worker for updates
                    stop_worker()
                    time.sleep(2)
                    worker_started = start_worker()
                    return jsonify({
                        'success': True,
                        'message': 'Configuration updated successfully',
                        'worker_restarted': worker_started,
                        'initial_config': False
                    })
            else:
                return jsonify({'error': 'Failed to save configuration'}), 500
                
    except Exception as e:
        return jsonify({'error': f'Configuration error: {str(e)}'}), 500

@app.route('/api/worker', methods=['POST'])
def api_worker_control():
    """API endpoint to control worker (start/stop/restart)."""
    try:
        # Parse JSON request
        action_data = request.get_json()
        if not action_data:
            return jsonify({'error': 'No JSON data provided'}), 400
        
        # Require authentication
        token = action_data.get('token') or request.headers.get('Authorization', '').replace('Bearer ', '')
        if not authenticate_token(token):
            return jsonify({'error': 'Invalid or missing authentication token'}), 401
        
        action = action_data.get('action', '').lower()
        
        with config_lock:
            if action == 'start':
                if start_worker():
                    return jsonify({'success': True, 'message': 'Worker started successfully'})
                else:
                    return jsonify({'error': 'Failed to start worker'}), 500
                    
            elif action == 'stop':
                if stop_worker():
                    return jsonify({'success': True, 'message': 'Worker stopped successfully'})
                else:
                    return jsonify({'error': 'Failed to stop worker'}), 500
                    
            elif action == 'restart':
                stop_worker()
                time.sleep(2)
                if start_worker():
                    return jsonify({'success': True, 'message': 'Worker restarted successfully'})
                else:
                    return jsonify({'error': 'Failed to restart worker'}), 500
            else:
                return jsonify({'error': 'Invalid action. Use: start, stop, or restart'}), 400
                
    except Exception as e:
        return jsonify({'error': f'Worker control error: {str(e)}'}), 500

def check_initial_configuration():
    """Check if worker is already configured."""
    global is_configured
    
    # Check if SHAREDDATA_TOKEN is set and env file exists
    if os.environ.get('SHAREDDATA_TOKEN'):
        source_folder = os.environ.get('SOURCE_FOLDER', os.path.expanduser('~/src'))
        env_file_path = Path(source_folder).parent / 'shareddata-worker.env'
        
        if env_file_path.exists():
            is_configured = True
            print("Found existing configuration, starting worker...")
            start_worker()

if __name__ == '__main__':
    import argparse
    
    parser = argparse.ArgumentParser(description="WorkerDocker configuration")
    parser.add_argument('--host', default='0.0.0.0', help='Server host address')
    parser.add_argument('--port', type=int, default=8080, help='Server port number')
    parser.add_argument('--debug', action='store_true', help='Enable debug mode')
    
    args = parser.parse_args()
    
    # Check for existing configuration on startup
    check_initial_configuration()
    
    print(f"SharedData WorkerDocker starting on http://{args.host}:{args.port}")
    print(f"Configured: {is_configured}")
    
    try:
        app.run(host=args.host, port=args.port, debug=args.debug, threaded=True)
    finally:
        # Cleanup on exit
        if worker_process and worker_process.poll() is None:
            print("Stopping worker process...")
            stop_worker()