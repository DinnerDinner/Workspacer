import sys
import json
import os

def save_urls_to_file(urls):
    file_path = os.path.join(os.path.expanduser('~'), 'Documents', 'urls.txt')
    with open(file_path, 'w') as f:
        for url in urls:
            f.write(url + '\n')

def main():
    try:
        message = json.loads(sys.stdin.read())
        urls = message.get('urls', [])
        save_urls_to_file(urls)
        response = {'status': 'success'}
    except Exception as e:
        response = {'status': 'error', 'message': str(e)}

    sys.stdout.write(json.dumps(response))
    sys.stdout.flush()

if __name__ == "__main__":
    main()
