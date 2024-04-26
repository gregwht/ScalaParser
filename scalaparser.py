# Read Scala file
with open("meanquar.scl", "r") as scl:
    file = scl.readlines()

# Filter out lines that start with '!'
no_comments = [line for line in file if not line.strip().startswith('!')]

# Now the first line will be a description of the scale and the second line will be the number of notes in the scale.
if len(no_comments) >=2:
    description = no_comments[0].strip()
    print("Description:", description)
    # Go to the second line and store that number as an int:
    num_degrees = int(no_comments[1].strip())
    print("Number of Degrees:", num_degrees)
else:
    print("Cannot read number of scale degrees. Is your scala file formatted correctly? Visit https://www.huygens-fokker.org/scala/scl_format.html for guidance.")
    sys.exit()

# Remove whitespace before or after pitches and store them in a list
pitches = [line.strip() for line in no_comments[2:]]

### Write isobar syntax:
## Degree
# Initialise a string
sequence = ""
# Print an ascending sequence of numbers, one for each degree in the scale
for i in range(num_degrees):
    if i < num_degrees - 1:
        sequence += str(i) + ", "
    else:
        sequence += str(i)
        
degree = '"degree": PSequence([' + sequence + ']),\n\t'

## Scale
# Convert list of pitches into a string
pitches = ', '.join(pitches)
scale = '"scale": Scale([' + pitches + ']),\n\t'

# Write the full syntax
syntax = 'timeline.schedule({ \n\t' + degree + scale + '"root_note" : 60,\n\t' + '"patch" : Sine,\n' + '})'
print(syntax)

# Write the isobar syntax to a new file
with open('scale.txt', 'w') as file:
    file.writelines(syntax)