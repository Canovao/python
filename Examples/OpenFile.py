#var_name = open(filename, mode) -> returns a handle use to manipulate the file

from fileinput import filename


example = open('Examples/text.txt', 'r')

print(example)

lineCount = 0
for line in example:
    print(line)
    lineCount += 1
print('Lines: '+str(lineCount))

getText = example.read()
print(getText)

file = input('Enter file name:')
try:
    fhand = open(file, 'r')
except:
    print('Failed to open the file: ' + file)
    quit()