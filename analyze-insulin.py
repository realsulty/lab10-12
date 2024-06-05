filename = '/preproinsulin-seq.txt'
# Function to read the contents of the file
def read_file(filename):
    with open(filename, 'r') as file:
        contents = file.read()
    return contents

# Read the file
file_contents = read_file(filename)

# Print the contents of the file
print(file_contents)