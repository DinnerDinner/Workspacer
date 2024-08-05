const POLL_INTERVAL = 5000; // Poll every 5 seconds

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

// Start polling
setInterval(pollServer, POLL_INTERVAL);

