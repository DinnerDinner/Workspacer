# from flask import Flask, request, jsonify
# from flask_cors import CORS
# import os

# app = Flask(__name__)
# CORS(app)  # Allow all origins. Customize if needed.

# # Specify the directory to save the file
# SAVE_DIRECTORY = r'C:\\Users\\Pro\\~Work~\\Programs\\Workspacer\\v6\\new_files'

# @app.route('/save_urls', methods=['POST'])
# def save_urls():
#     data = request.get_json()
#     urls = data.get('urls', [])
#     filename = data.get('filename', 'myurls.txt')
    
#     if not urls:
#         return jsonify({'status': 'error', 'message': 'No URLs provided'})
    
#     try:
#         os.makedirs(SAVE_DIRECTORY, exist_ok=True)
#         file_path = os.path.join(SAVE_DIRECTORY, filename)

#         with open(file_path, 'w') as file:
#             file.write('\n'.join(urls))

#         return jsonify({'status': 'success'})
#     except Exception as e:
#         return jsonify({'status': 'error', 'message': str(e)})

# if __name__ == '__main__':
#     app.run(port=5000)


from flask import Flask, request, jsonify
from flask_cors import CORS
from pathlib import Path
import pygetwindow as gw
import pyautogui
import time

app = Flask(__name__)
CORS(app)  # Allow all CORS requests

# Define the hardcoded path for saving files
SAVE_DIR = Path("C:/Users/Pro/~Work~/Programs/Workspacer/v6/new_files")

# Ensure the directory exists
SAVE_DIR.mkdir(parents=True, exist_ok=True)

@app.route('/save_urls', methods=['POST'])
def save_urls():
    try:
        data = request.get_json()
        urls = data.get('urls', [])
        filename = data.get('filename', 'myurls.txt')

        # Construct the full path to save the file
        save_path = SAVE_DIR / filename

        # Save URLs to the file
        with open(save_path, 'w') as file:
            file.write('\n'.join(urls))

        return jsonify({"status": "success"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/trigger_extension', methods=['POST'])
def trigger_extension():
    try:
        # Focus the Chrome window and send a message to the extension
        chrome_windows = [window for window in gw.getWindowsWithTitle('Chrome') if window.visible]
        if chrome_windows:
            chrome_windows[0].activate()
            time.sleep(1)  # Small delay to ensure the window is focused

            # Trigger the extension action via keyboard shortcut
            pyautogui.hotkey('ctrl', 'shift', 'e')  # Example shortcut, modify as needed

        return jsonify({"status": "success"}), 200
    except Exception as e:
        print(f"Error triggering extension: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    app.run(port=5000, debug=True)
