// Export Tab URLs (Existing Code)
document.getElementById('exportButton').addEventListener('click', async () => {
    const filenameInput = document.getElementById('filename');
    let filename = filenameInput.value.trim();
  
    if (!filename) {
      filename = 'tabs.txt';
    }
  
    if (!filename.endsWith('.txt')) {
      filename += '.txt';
    }
  
    const tabs = await chrome.tabs.query({ currentWindow: true });
    const urls = tabs.map(tab => tab.url).join('\n');
  
    const blob = new Blob([urls], { type: 'text/plain' });
    const url = URL.createObjectURL(blob);
  
    chrome.downloads.download({
      url: url,
      filename: filename
    });
  });
  
  // Open Links from Text (Updated Code)
  document.getElementById('openLinksButton').addEventListener('click', () => {
    const fileContent = document.getElementById('fileContent').value.trim();
  
    if (!fileContent) {
      alert('Please paste the file content.');
      return;
    }
  
    const urls = fileContent.split('\n').filter(url => url.trim() !== '');
  
    if (urls.length === 0) {
      alert('No valid URLs found in the text.');
      return;
    }
  
    // Open each URL in a new tab
    urls.forEach(url => {
      chrome.tabs.create({ url: url });
    });
  });