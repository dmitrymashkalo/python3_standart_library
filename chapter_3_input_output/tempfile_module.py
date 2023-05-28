# Tempfile Module
import tempfile


# Create a Temporary File
tempFile = tempfile.TemporaryFile()

# Write to a Temporary File
tempFile.write(b'Save this string.')
tempFile.seek(0)

# Read the Temporary File
print(tempFile.read())

# Close the Temporary File
tempFile.close()