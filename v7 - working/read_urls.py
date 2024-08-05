import webbrowser
import time
import subprocess
import keyboard

def open_urls_in_chrome(file_path):
    # Read URLs from file
    with open(file_path, 'r') as f:
        urls = f.readlines()
        urls = [url.strip() for url in urls if url.strip() and not url.strip().startswith('chrome://')] # Remove any empty lines and strip whitespace
    subprocess.Popen(['start', 'chrome'], shell=True)

    # Open each URL in the same Chrome window
    for url in urls:
        subprocess.Popen(['start', 'chrome', url], shell=True)
        time.sleep(0.5)  # Small delay to ensure each tab is opened properly
    # time.sleep(2)
    
    keyboard.press_and_release('ctrl+1')
    time.sleep(1)
    keyboard.press_and_release('ctrl+w')
    keyboard.press_and_release('ctrl+9')

if __name__ == "__main__":
    file_path = ("C:/Users/Pro/~Work~/Programs/Workspacer/v7 - working/new_files/book.txt")  # Example: 'C:/path/to/urls.txt'
    open_urls_in_chrome(file_path)
