// document.getElementById('fetchUrls').addEventListener('click', () => {
//     chrome.tabs.query({ currentWindow: true }, (tabs) => {
//         let urls = tabs.map(tab => tab.url);
//         // Create a Blob with the URLs and specify the type as plain text
//         const blob = new Blob([urls.join('\n')], { type: 'text/plain' });
//         // Create a download link for the Blob
//         const url = URL.createObjectURL(blob);
//         // Create a temporary link element and click it to trigger the download
//         const a = document.createElement('a');
//         a.href = url;
//         a.download = 'myurls.txt';  // Specify the file name
//         document.body.appendChild(a);  // Append the link to the body
//         a.click();  // Click the link to start the download
//         document.body.removeChild(a);  // Remove the link from the document
//     });
// });


document.getElementById('fetchUrls').addEventListener('click', () => {
    chrome.tabs.query({ currentWindow: true }, (tabs) => {
        let urls = tabs.map(tab => tab.url);
        // Create a Blob with the URLs and specify the type as plain text
        const blob = new Blob([urls.join('\n')], { type: 'text/plain' });
        // Create a download link for the Blob
        const url = URL.createObjectURL(blob);
        
        // Use the chrome.downloads API to save the file to a specific location
        chrome.downloads.download({
            url: url,
            filename: 'C:/Users/Pro/~Work~/Programs/Workspacer/V5/new_files/myurls.txt',  // Specify the file path and name
            conflictAction: 'overwrite'
        }, (downloadId) => {
            if (downloadId) {
                console.log('Download initiated with ID:', downloadId);
            } else {
                console.error('Download failed.');
            }
            // Revoke the object URL to free up memory
            URL.revokeObjectURL(url);
        });
    });
});
