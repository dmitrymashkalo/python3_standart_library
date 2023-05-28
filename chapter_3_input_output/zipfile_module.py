# Zipfile Module
import zipfile


# Open and List
zip = zipfile.ZipFile('Archive.zip', 'r')
print(zip.namelist()) # Lists and prints the names of all files and directories within the zip archive


# Metadata in the Zip Folder
for metadata in zip.infolist():
    print(metadata)

print(zip.getinfo('purchased.txt')) # Prints the metadata information of the file named 'purchased.txt'
print(zip.getinfo('wishlist.txt')) # Prints the metadata information of the file named 'wishlist.txt'


# Access to File in Zip Folder
print(zip.read('purchased.txt'))
print(zip.read('wishlist.txt'))

with zip.open('purchased.txt') as file:
    print(file.read())

with zip.open('wishlist.txt') as file:
    print(file.read())


# Extracting All Files
zip.extractall() # Extracts all files and directories from the zip archive to the current working directory
# Or by File
zip.extract('purchased.txt') # Extracts the file named 'purchased.txt' from the zip archive to the current working directory
zip.extract('wishlist.txt') # Extracts the file named 'wishlist.txt' from the zip archive to the current working directory

# Closing the Zip
zip.close()