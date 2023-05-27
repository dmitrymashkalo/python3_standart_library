# Files and Files Writing
# Flags: r -> Read | w -> Write | r+ -> Read and Write | a -> Append  

# Open a File
myFile = open('txt.txt', 'w')


# Show Attributes and Properties of that File
print(f'File name: {myFile.name}')
print(f'Mode: {myFile.mode}')


# Wtire to a file
myFile.write('Player 1 Score: 99\nPlayer 2 Score: 101\nPlayer 3 Score: 87')
myFile.close()


# Read the File
myFile = open('txt.txt', 'r')
print(f'Reading ...\n{myFile.read()}')
