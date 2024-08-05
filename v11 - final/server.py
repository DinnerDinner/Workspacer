from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import threading
import time
import sys
from werkzeug.serving import make_server

app = Flask(__name__)
CORS(app)  # Allow all origins. Customize if needed.

# Specify the directory to save the file
SAVE_DIRECTORY = r'C:\\Users\\Pro\\~Work~\\Programs\\Workspacer\\v11 - final\\new_files'

# Read the filename from the command line argument
filename = sys.argv[1] if len(sys.argv) > 1 else 'myurls.txt'

@app.route('/save_urls', methods=['POST'])
def save_urls():
    data = request.get_json()
    urls = data.get('urls', [])

    if not urls:
        return jsonify({'status': 'error', 'message': 'No URLs provided'})
    
    try:
        os.makedirs(SAVE_DIRECTORY, exist_ok=True)
        file_path = os.path.join(SAVE_DIRECTORY, filename)

        with open(file_path, 'w') as file:
            file.write('\n'.join(urls))

        return jsonify({'status': 'success'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

@app.route('/trigger_extension', methods=['GET'])
def trigger_extension():
    # Simply respond with the action to be performed
    return jsonify({'action': 'fetch_urls'})

def start_shutdown_timer(server):
    time.sleep(2)
    server.shutdown()

if __name__ == '__main__':
    # Create the server
    server = make_server('localhost', 5000, app)
    thread = threading.Thread(target=server.serve_forever)
    thread.start()

    # Start the shutdown timer
    threading.Thread(target=start_shutdown_timer, args=(server,)).start()

    print("Server running...")

    # Wait for the server thread to finish
    thread.join()
    print("Server shut down.")
