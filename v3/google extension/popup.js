document.getElementById('fetchUrls').addEventListener('click', () => {
    chrome.tabs.query({ currentWindow: true }, (tabs) => {
        let urls = tabs.map(tab => tab.url);
        chrome.runtime.sendNativeMessage('com.example.urlfetcher', { urls: urls }, (response) => {
            if (response && response.status === 'success') {
                alert('URLs saved successfully');
            } else {
                alert('Failed to save URLs: ' + (response && response.message ? response.message : 'Unknown error'));
            }
        });
    });
});
