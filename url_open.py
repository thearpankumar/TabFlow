import webbrowser

# Read URLs from the file
with open("tabs.txt", 'r') as file:
    urls = file.readlines()

# Open each URL in the browser
for url in urls:
    webbrowser.open(url.strip())