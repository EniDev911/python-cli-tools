import os 

## Create file
print('Create a file')
print('==============')

FILENAME = 'data.txt'

file = open(FILENAME, 'w') # open file data.txt
file.write('This is a test\nEnidev911')
file.close()

if FILENAME in os.listdir('.'):
    print('File created in the path: \n{0}/{1}'.format(
            os.getcwd(), FILENAME))

else:
    print('The file was not created!')

## Read file 
print('\n\nRead a file')
print('==============')

file = open(FILENAME, 'r')
print(file.read())
file.close()

# Iterate a file
print('\n\nIteare a file')
print('==============')

file = open(FILENAME, 'r')
for line in file:
    print(line)
file.close()


# Delete file
print('\n\nDelete a file')
print('==============')

os.remove(os.getcwd()+'/'+FILENAME)
print('Deleted file from path: \n{0}/{1}'.format(
        os.getcwd(), FILENAME))

