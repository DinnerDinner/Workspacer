import pyautogui
import subprocess
import time

def open_urls_in_new_chrome(file_path):
    # Open a new instance of Chrome



    # This is just testing for making it work in notepad, but next is pulling off alt + c in chrome and then ctrl + v into notepad automatically
    subprocess.Popen(['start', 'notepad', (f'{ina}.txt')], shell=True)
    time.sleep(3)
    pyautogui.hotkey('enter')
    time.sleep(3)
    pyautogui.hotkey('ctrl','v')
    time.sleep(2)
    pyautogui.hotkey('ctrl', 's')
    
    time.sleep(4)
    subprocess.Popen(['start', 'chrome'], shell=True)
    # time.sleep(2)  # Give Chrome some time to open
    
    # Read URLs from file
    with open(file_path, 'r') as f:
        urls = f.readlines()
        urls = [url.strip() for url in urls if url.strip()]  # Remove any empty lines and strip whitespace

    # Open each URL in the newly opened Chrome window
    for url in urls:
        subprocess.Popen(['start', 'chrome', url], shell=True)
    time.sleep(4)
    
    pyautogui.hotkey('ctrl', '1')
    time.sleep(2)
    pyautogui.hotkey('ctrl', 'w')
    time.sleep(2)

    print('Hello World !!')
    

if __name__ == "__main__":
    ina = input("Workspace name> ")
    if ina != '':
        file_path = (f'C:/Users/Pro/Desktop/THE SETUP/workspacer/{ina}.txt')  # Replace with the actual path to your file    
        open_urls_in_new_chrome(file_path)
