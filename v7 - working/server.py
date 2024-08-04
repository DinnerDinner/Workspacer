from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # Allow all origins. Customize if needed.

# Specify the directory to save the file
SAVE_DIRECTORY = r'C:\\Users\\Pro\\~Work~\\Programs\\Workspacer\\v7 - working\\new_files'

@app.route('/save_urls', methods=['POST'])
def save_urls():
    data = request.get_json()
    urls = data.get('urls', [])
    filename = data.get('filename', 'myurls.txt')
    
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

if __name__ == '__main__':
    app.run(port=5000)

