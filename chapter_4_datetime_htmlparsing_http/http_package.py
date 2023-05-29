# HTTP Package
import urllib.request
import json


url = "https://jsonplaceholder.typicode.com/posts"

with urllib.request.urlopen(url) as file: # Opening the URL url using urllib.request.urlopen()
    text = file.read()
    decoded_text = text.decode('utf-8') # Decoding the contents of the file from a byte string to a Unicode string using the UTF-8 encoding
    print(decoded_text)

obj = json.loads(decoded_text) # Parsing the decoded string decoded_text as JSON data using the json.loads()

print(obj[1]['title']) # Get value of the 'title' key of the item at index from the parsed obj data