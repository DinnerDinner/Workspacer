import subprocess

def main():
    # Ask the user for the filename
    filename = input("Please enter the filename: ")
    filename = str(filename + '.txt')

    # Start the server.py with the provided filename
    subprocess.run(["python", "server.py", filename])

if __name__ == "__main__":
    main()
