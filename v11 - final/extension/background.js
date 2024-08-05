const POLL_INTERVAL = 2000; // Poll every 2 seconds

function pollServer() {
    fetch('http://localhost:5000/trigger_extension')
        .then(response => response.json())
        .then(data => {
            if (data.action === 'fetch_urls') {
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
        })
        .catch(error => {
            console.error("Error: " + error.message);
        });
}

// Keep the background script running
function keepAlive() {
    setInterval(() => {
        console.log("Keeping the background script alive...");
    }, 1000); // Log every second to keep the script active
}
function reloadServiceWorker() {
    if (chrome.runtime && chrome.runtime.reload) {
        chrome.runtime.reload();
    }
}


// Start polling using setInterval
setInterval(pollServer, POLL_INTERVAL);

// Initialize the first poll
pollServer();

// Start the keep-alive mechanism
keepAlive();

setInterval(reloadServiceWorker, 75 * 1000);