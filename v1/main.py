from workspace_manager.save_workspace import save_workspace
from workspace_manager.load_workspace import load_workspace, restore_workspace

def main():
    while True:
        print("\nWorkspace Manager")
        print("1. Save Workspace")
        print("2. Load Workspace")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            workspace_name = input("Enter the name of the workspace to save: ")
            save_workspace(workspace_name)
        elif choice == '2':
            workspace_name = input("Enter the name of the workspace to load: ")
            workspace = load_workspace(workspace_name)
            if workspace:
                restore_workspace(workspace)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
