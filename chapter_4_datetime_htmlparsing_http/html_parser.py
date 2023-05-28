# HTML Parser Module
from html.parser import HTMLParser


class HTMLParser(HTMLParser): # Defining the HTMLParser class that inherits from HTMLParser

    def handle_starttag(self, tag, attrs): # Overriding the handle_starttag method
        print(f'Start tag: {tag}') # Prints the encountered start tag and its attributes
        for a in attrs:
            print(f'Attr: {a}')

    def handle_endtag(self, tag): # Overriding the handle_endtag method
        print(f'End tag: {tag}') # Prints the encountered end tag

    def handle_comment(self, data): # Overriding the handle_comment method
        print(f'Comment: {data}') # Prints the encountered comment

    def handle_data(self, data): # Overriding the handle_data method
        print(f'Data: {data}') # Prints the encountered data


with open('index.html', 'r') as file: # Open HTML file
    html = file.read()


parser = HTMLParser()
parser.feed(html) # Feeds the HTML content to the parser instance, which triggers the parsing process