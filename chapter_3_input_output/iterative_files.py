# Iterative Files
myFile = open('txt.txt', 'r')


# Read One Line at a Time
print(f'My one line: {myFile.readline()}')
myFile.seek(0) # Reset the pointer to the beginning of the file


# Iterate Through Each Line of a File
for line in myFile:
    print(line)

myFile.close()