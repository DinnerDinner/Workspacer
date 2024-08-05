// // Handle messages from the server
// chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
//     if (message.action === 'fetch_urls') {
//         chrome.tabs.query({ currentWindow: true }, (tabs) => {
//             let urls = tabs.map(tab => tab.url);

//             // Send URLs to the server
//             fetch('http://localhost:5000/save_urls', {
//                 method: 'POST',
//                 headers: {
//                     'Content-Type': 'application/json',
//                 },
//                 body: JSON.stringify({ urls: urls }),
//             })
//             console.log(121)
//             .then(response => response.json())
//             console.log(122)
//             .then(data => {
//                 if (data.status === 'success') {
//                     console.log("URLs saved successfully!");
//                 } else {
//                     console.error("Error: " + data.message);
//                 }
//             })
//             .catch(error => {
//                 console.error("Error: " + error.message);
//             });
//         });
//     }
// });
// console.log('Background script started');
// chrome.runtime.onMessageExternal.addListener((message, sender, sendResponse) => {
//     console.log('Message received:', message);

//     if (message.action === 'fetch_urls') {
//         chrome.tabs.query({ currentWindow: true }, (tabs) => {
//             let urls = tabs.map(tab => tab.url);

//             fetch('http://localhost:5000/save_urls', {
//                 method: 'POST',
//                 headers: {
//                     'Content-Type': 'application/json',
//                 },
//                 body: JSON.stringify({ urls: urls }),
//             })
//             .then(response => response.json())
//             .then(data => {
//                 if (data.status === 'success') {
//                     console.log("URLs saved successfully!");
//                 } else {
//                     console.error("Error: " + data.message);
//                 }
//                 sendResponse({ status: data.status });
//             })
//             .catch(error => {
//                 console.error("Error: " + error.message);
//                 sendResponse({ status: 'error', message: error.message });
//             });

//             return true; // Keep the message channel open for sendResponse
//         });
//     }
// });




// Directly fetch URLs when the extension is loaded
chrome.runtime.onStartup.addListener(() => {
    chrome.tabs.query({ currentWindow: true }, (tabs) => {
      let urls = tabs.map(tab => tab.url);
      fetch('http://localhost:5000/save_urls', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ urls: urls }),
      })
      .then(response => response.json())
      .then(data => {
        console.log("URLs saved successfully!");
      })
      .catch(error => {
        console.error("Error: " + error.message);
      });
    });
  });
  