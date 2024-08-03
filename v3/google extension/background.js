chrome.action.onClicked.addListener((tab) => {
    chrome.tabs.query({ currentWindow: true }, (tabs) => {
        let urls = tabs.map(tab => tab.url);
        chrome.runtime.sendNativeMessage('com.example.urlfetcher', { urls: urls }, (response) => {
            if (response && response.status === 'success') {
                console.log('URLs saved successfully');
            } else {
                console.error('Failed to save URLs:', response ? response.message : 'Unknown error');
            }
        });
    });
  });
  