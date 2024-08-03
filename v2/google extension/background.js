chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.action === 'saveUrls') {
      chrome.tabs.query({}, (tabs) => {
        let urls = tabs.map(tab => tab.url);
        chrome.storage.local.set({ urls: urls }, () => {
          sendResponse({ status: 'success' });
        });
      });
      return true; // Indicates that sendResponse will be called asynchronously
    }
  });
  