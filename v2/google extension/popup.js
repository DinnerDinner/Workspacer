document.getElementById('saveUrls').addEventListener('click', () => {
    chrome.runtime.sendMessage({ action: 'saveUrls' }, (response) => {
      if (response.status === 'success') {
        alert('URLs saved successfully!');
      }
    });
  });
  