from http.server import BaseHTTPRequestHandler, HTTPServer
import shutil
import os
from pathlib import Path

# Define paths
downloads_folder = Path.home() / 'Downloads'
target_folder = Path('C:/Users/Pro/~Work~/Programs/Workspacer/V5/new_files')
file_name = 'myurls.txt'

# Ensure target folder exists
target_folder.mkdir(parents=True, exist_ok=True)

def move_file():
    # Define source file path
    source_file = downloads_folder / file_name
    # Check if file exists and move it
    if source_file.exists():
        destination_file = target_folder / file_name
        shutil.move(str(source_file), str(destination_file))
        print(f'File moved to {destination_file}')
        return 'File moved successfully'
    else:
        return 'File not found in Downloads folder.'

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/move_file':
            message = move_file()
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(message.encode())
        else:
            self.send_response(404)
            self.end_headers()

# Run the server
if __name__ == "__main__":
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, RequestHandler)
    print('Running server...')
    httpd.serve_forever()
