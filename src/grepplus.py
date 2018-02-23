import re, sys
from os import listdir
from os.path import isfile

def getInput(string):
    if sys.version_info[0] < 3:
        return raw_input(string)
    return input(string)

print("----------------------------------\n"
      "This application will search all .txt files in the current directory for a matching "
      "string and print the filenames it finds matches for at the end.\n"
      "You can also print out all matching lines as it searches.\n")

string = getInput('Enter string to match: ')
verbose_mode = getInput('Print matching lines [Y]? ')

print("----------------------------------\n")

regex_filename = re.compile('^.*\.txt')
regex_string = re.compile('.*' + string + '.*')
matches = []

# Get all entries in this directory
for f in listdir('.'):
    # If its a file ending '.txt' process it
    if isfile(f) and regex_filename.search(f):
        found = False
        print( "Checking > "+f)
        # Iterate round all lines
        for i, line in enumerate(open(f)):
            line = line
            # Check each line for string
            for match in re.finditer(regex_string, line):
                found = True
                # if in verbose mode, show each line it found it at
                if verbose_mode == 'Y':
                    print('  [%s] %s' % (i+1, line.strip()))

        # If the string was found anywhere, add it to summary list
        if found:
            matches.append(f)

# Output all files where string existed
print("\nSUMMARY\n-------")
for f in matches:
    print(f)

