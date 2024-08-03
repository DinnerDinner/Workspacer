# import json
# import os

# def load_workspace(workspace_name):
#     try:
#         with open(f'workspaces/{workspace_name}.json', 'r') as f:
#             workspace = json.load(f)
#         print(f"Workspace '{workspace_name}' loaded successfully.")
#         return workspace
#     except FileNotFoundError:
#         print(f"Workspace '{workspace_name}' does not exist.")
#         return None

# def restore_workspace(workspace):
#     applications = workspace.get('applications', [])
#     for app in applications:
#         print(f"Would restore application: {app['name']} (PID: {app['pid']})")

# if __name__ == "__main__":
#     workspace_name = input("Enter the name of the workspace to load: ")
#     workspace = load_workspace(workspace_name)
#     if workspace:
#         restore_workspace(workspace)

import json
import subprocess
import time

def load_workspace(workspace_name):
    try:
        with open(f'workspaces/{workspace_name}.json', 'r') as f:
            workspace = json.load(f)
        print(f"Workspace '{workspace_name}' loaded successfully.")
        return workspace
    except FileNotFoundError:
        print(f"Workspace '{workspace_name}' does not exist.")
        return None

def restore_workspace(workspace):
    urls = workspace.get('urls', [])
    for url in urls:
        subprocess.Popen(['chrome', url])
        time.sleep(1)  # Slight delay to ensure Chrome opens the URL

if __name__ == "__main__":
    workspace_name = input("Enter the name of the workspace to load: ")
    workspace = load_workspace(workspace_name)
    if workspace:
        restore_workspace(workspace)
