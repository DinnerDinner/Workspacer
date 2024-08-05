# import time
# import pygetwindow as gw
# import pyautogui
# import requests

# def trigger_extension():
#     # Focus the Chrome window
#     chrome_windows = [window for window in gw.getWindowsWithTitle('Chrome') if window.visible]
#     if chrome_windows:
#         chrome_windows[0].activate()
#         time.sleep(1)  # Small delay to ensure the window is focused

#         # Press the extension shortcut (assuming it's the first extension in the toolbar)
#         # Customize this according to your extension's shortcut
#         pyautogui.hotkey('ctrl', 'shift', 'e')  # Example shortcut, modify as needed

#         # Trigger the extension action
#         response = requests.post('http://localhost:5000/trigger_extension')
#         if response.status_code == 200:
#             print("Extension triggered successfully!")
#         else:
#             print(f"Failed to trigger extension: {response.json()}")

# if __name__ == "__main__":
#     trigger_extension()


import requests

def trigger_extension():
    try:
        response = requests.post('http://localhost:5000/trigger_extension')
        data = response.json()
        if data['status'] == 'success':
            print("Extension triggered successfully.")
        else:
            print("Failed to trigger extension:", data)
    except Exception as e:
        print("Error triggering extension:", e)

if __name__ == "__main__":
    trigger_extension()
