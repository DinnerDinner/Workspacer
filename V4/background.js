// // Listener for incoming messages from the popup or content scripts
// chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
//     // Check if the action is to save URLs
//     if (message.action === 'saveUrls') {
//         // Call the function to save URLs to a file
//         saveUrlsToFile(message.urls);
//         // Send a success response back to the sender
//         sendResponse({ status: 'success' });
//     } else {
//         // Handle unknown actions
//         sendResponse({ status: 'error', message: 'Unknown action' });
//     }
// });

// // Function to save URLs to a file
// function saveUrlsToFile(urls) {
//     // Create a Blob with the URLs and specify the type as plain text
//     const blob = new Blob([urls.join('\n')], { type: 'text/plain' });

//     // Create a download link for the Blob
//     const url = URL.createObjectURL(blob);

//     // Create a temporary link element and click it to trigger the download
//     const a = document.createElement('a');
//     a.href = url;
//     a.download = 'myurls.txt';  // Specify the file name
//     document.body.appendChild(a);  // Append the link to the body
//     a.click();  //  click Programmaticallythe link to start the download
//     document.body.removeChild(a);  // Remove the link from the document
// }


chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
    // console.log('Received message:', message);
    // console.log('Sender:', sender);
    console.log(5);
    if (message.action === 'saveUrls') {
        // Handle saving URLs
        console.log(6);
        chrome.runtime.sendNativeMessage('V4\\com.example.urlfetcher', { urls: message.urls }, (response) => {
            console.log('Native message response:', response);
            
            if (response && response.status === 'success') {
                sendResponse({ status: 'success' });
                console.log(1);
            } else {
                sendResponse({ status: 'error', message: response ? response.message : 'Unknown error' });
                console.log(2);
            }
            console.log(3);
        });
        console.log(4);
        return true;  // Return true to indicate async response
        
    } else {
        sendResponse({ status: 'error', message: 'Unknown action' });
    }
});
