# import psutil
# import json
# import os

# # List of known applications (this can be expanded)
# KNOWN_APPLICATIONS = ["chrome", "vscode", "code", "unity", "teams"]

# def list_running_applications():
#     processes = []
#     for process in psutil.process_iter(['pid', 'name']):
#         process_name = process.info['name'].lower()
#         if any(app in process_name for app in KNOWN_APPLICATIONS):
#             processes.append({
#                 'pid': process.info['pid'],
#                 'name': process.info['name']
#             })
#     return processes

# def save_workspace(workspace_name):
#     applications = list_running_applications()
#     workspace = {
#         'name': workspace_name,
#         'applications': applications
#     }
    
#     os.makedirs('workspaces', exist_ok=True)
#     with open(f'workspaces/{workspace_name}.json', 'w') as f:
#         json.dump(workspace, f, indent=4)

#     print(f"Workspace '{workspace_name}' saved successfully.")

# if __name__ == "__main__":
#     workspace_name = input("Enter the name of the workspace to save: ")
#     save_workspace(workspace_name)

import json
import os
import pygetwindow as gw

def get_chrome_urls():
    chrome_windows = gw.getWindowsWithTitle("Chrome")
    urls = []

    for window in chrome_windows:
        if window.title != "Chrome":
            urls.append(window.title)
    
    return urls

def save_workspace(workspace_name):
    urls = get_chrome_urls()
    workspace = {
        'name': workspace_name,
        'urls': urls
    }
    
    os.makedirs('workspaces', exist_ok=True)
    with open(f'workspaces/{workspace_name}.json', 'w') as f:
        json.dump(workspace, f, indent=4)

    print(f"Workspace '{workspace_name}' saved successfully.")

if __name__ == "__main__":
    workspace_name = input("Enter the name of the workspace to save: ")
    save_workspace(workspace_name)
