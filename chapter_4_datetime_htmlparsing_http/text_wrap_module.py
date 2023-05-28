# Text Wrap Module
import textwrap

websiteText = """   Learning can happen anywhere with our apps on your computer, 
mobile device, and TV, featuring enhanced navigation and faster streaming for anytime learning, 
limitless possibilities."""

print('No Dedent: ')
print(textwrap.fill(websiteText)) # Printing the websiteText with default text wrapping, where long lines are broken into multiple lines to fit within the specified width
print()

print('Dedent: ')
dedent_text = textwrap.dedent(websiteText).strip() # Removing common leading whitespace from all lines in websiteText using dedent and then removing any leading or trailing whitespace using strip()
print(dedent_text)
print()

print('Fill: ')
print(textwrap.fill(dedent_text, width=50)) # Printing the dedent_text with text wrapping, limiting each line to a width of 50 characters
print()
print(textwrap.fill(dedent_text, width=100)) # Printing the dedent_text with text wrapping, limiting each line to a width of 100 characters
print()

print('Controlling Indent: ')
print(textwrap.fill(dedent_text, initial_indent='   ', subsequent_indent='      ')) # Printing the dedent_text with controlled indentation, where the initial line has an indent of 1 tab and subsequent lines have an indent of 2 tab
print()

print('Shortening Text: ')
print(textwrap.shorten('LinkedIn.com is great!', width=20, placeholder='...')) # Shortening the text to fit within a width of 20 characters, with an ellipsis placeholder '...'