// const HARD_CODED_FILENAME = 'myurls.txt';
// chrome.action.onClicked.addListener(() => {
//     chrome.tabs.query({ currentWindow: true }, (tabs) => {
//         let urls = tabs.map(tab => tab.url);
        
//         // Prompt user for filename (could be done via a notification or in the future UI)
//         // let filename = prompt("Enter the filename (without extension):", "myurls");
//         // if (!filename) {
//         //     console.error("Filename is required");
//         //     return;
//         // }
//         // filename = filename.trim() + ".txt";
        
//         // Send URLs and filename to the server
//         fetch('http://localhost:5000/save_urls', {
//             method: 'POST',
//             headers: {
//                 'Content-Type': 'application/json',
//             },
//             body: JSON.stringify({ urls: urls, filename: HARD_CODED_FILENAME }),
//         })
//         .then(response => response.json())
//         .then(data => {
//             if (data.status === 'success') {
//                 console.log("URLs saved successfully!");
//             } else {
//                 console.error("Error: " + data.message);
//             }
//         })
//         .catch(error => {
//             console.error("Error: " + error.message);
//         });
//     });
// });
const HARD_CODED_FILENAME = 'myurls.txt';
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.action === "fetch_and_save_urls") {
        chrome.tabs.query({ currentWindow: true }, (tabs) => {
            let urls = tabs.map(tab => tab.url);
            console.log("Well")

            fetch('http://localhost:5000/save_urls', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ urls: urls, filename: HARD_CODED_FILENAME }),
            })
            .then(response => response.json())
            .then(data => {
                if (data.status === 'success') {
                    console.log("URLs saved successfully!");
                } else {
                    console.error("Error: " + data.message);
                }
            })
            .catch(error => {
                console.error("Error: " + error.message);
            });
        });
    }
});
