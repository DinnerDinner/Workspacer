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
import subprocess
from flask import Flask, request, jsonify
import os
import subprocess
import time
from pywinauto import application

app = Flask(__name__)
CORS(app)


@app.route('/save_urls', methods=['POST'])
def save_urls():
    data = request.get_json()
    urls = data.get('urls')
    filename = data.get('filename', 'myurls.txt')
    file_path = os.path.join(r'C:\Users\Pro\~Work~\Programs\Workspacer\v6\new_files', filename)
    try:
        with open(file_path, 'w') as file:
            file.write('\n'.join(urls))
        return jsonify({"status": "success", "message": "URLs saved successfully!"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

@app.route('/trigger_extension', methods=['POST'])
def trigger_extension():
    try:
        app = application.Application().connect(title_re=".*Chrome.*")
        chrome_window = app.top_window()
        chrome_window.set_focus()
        
        time.sleep(1)  # Give Chrome some time to be in the foreground
        
        with open('extension_trigger.bat', 'w') as bat_file:
            bat_file.write(r'''
            @echo off
            start chrome-extension://kpcbodepepkjkekimepplmneglbihbgm/
            ''')
        subprocess.call(['extension_trigger.bat'])
        return jsonify({"status": "success", "message": "Extension triggered successfully!"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == "__main__":
    app.run(port=5000)
