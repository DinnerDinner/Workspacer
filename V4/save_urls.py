import sys
import json

def save_urls_to_file(urls):
    print(20)
    with open('C:\\Users\\Pro\\~Work~\\Programs\\Workspacer\\V4\\myurls.txt', 'w') as f:
        print(22)
        for url in urls:
            f.write(url + '\n')
    print('doen')

def main():
    try:
        print(222)
    
        message = json.loads(sys.stdin.read())
        urls = message.get('urls', [])
        save_urls_to_file(urls)
        response = {'status': 'success'}
        
    except Exception as e:
        print(32)

        response = {'status': 'error', 'message': str(e)}

    print(42)

    sys.stdout.write(json.dumps(response))
    sys.stdout.flush()

if __name__ == "__main__":
    print(12)
    main()
    