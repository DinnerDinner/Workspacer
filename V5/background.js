// Function to read a file and trigger URL saving
function checkForTrigger() {
    fetch('file:///C:/path/to/trigger.txt')
        .then(response => response.text())
        .then(text => {
            if (text.trim() === 'TRIGGER') {
                chrome.tabs.query({ currentWindow: true }, (tabs) => {
                    let urls = tabs.map(tab => tab.url);
                    chrome.runtime.sendMessage({ action: 'saveUrls', urls: urls }, (response) => {
                        console.log('Response:', response);
                    });
                });
                // Clear the trigger file after processing
                fetch('file:///C:/path/to/trigger.txt', { method: 'PUT', body: '' });
            }
        })
        .catch(error => console.error('Error reading trigger file:', error));
}

// Check the trigger file periodically
setInterval(checkForTrigger, 5000);  // Check every 5 seconds
