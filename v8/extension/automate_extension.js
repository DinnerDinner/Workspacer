const puppeteer = require('puppeteer');

const EXTENSION_PATH = "C:\\Users\\Pro\\~Work~\\Programs\\Workspacer\\v8\\extension"; // Path to the extension
const EXTENSION_ID = 'fabmlcinfpiankahccahonheeonjlnpk'; // Replace with your extension's ID

(async () => {
    try {
        // Launch Puppeteer and open Chrome with the extension
        const browser = await puppeteer.launch({
            headless: false, // Set to true if you do not need a visible browser window
            args: [`--disable-extensions-except=${EXTENSION_PATH}`, `--load-extension=${EXTENSION_PATH}`]
        });

        // Get all open pages (tabs) in the current window
        const pages = await browser.pages(); // This gets all the pages (tabs)

        // Loop through each page and click the extension button
        for (const page of pages) {
            // Focus on the page
            await page.bringToFront();

            // Click the extension button by simulating a click on the extension's action button
            // The selector needs to match the button's actual selector in the extension's UI
            // The selector can be modified according to your extension's action button
            const extensionButtonSelector = 'button[aria-label="Extension Button"]'; // Update the selector as needed
            await page.waitForSelector(extensionButtonSelector); // Ensure the button is available
            await page.click(extensionButtonSelector);
            console.log("Clicked the extension button on a tab");
        }

        // Notify the server to save the URLs (if needed)
        // Add your server request code here

        // Optionally, close the browser after actions
        // await browser.close();

    } catch (error) {
        console.error('Error occurred:', error);
    }
})();
