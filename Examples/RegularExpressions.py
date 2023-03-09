#ALWAYS IMPORT "import re" TO USE REGULAR EXPRESSIONS
#^ Matches the beginning of a line
#$ Matches the end of the line
#. Matches any character
#\s Matches whitespace
#\S Matches any non-whitespace character
#* Repeats a character zero or more times
#*? Repeats a character zero or more times (non-greedy, prefer the shortest)
#+ Repeats a character one or more times
#+? Repeats a character one or more times (non-greedy, prefer the shortest)
#[aeiou] Matches a single character in the listed set
#[^XYZ] Matches a single character not in the listed set
#[a-z0-9] The set of characters can include a range
#( Indicates where string extraction is to start
#) Indicates where string extraction is to end
import re


#Like find() method
hand = open('some-file.txt')
for line in hand:
	line = line.strip()
	if re.search("text i want to search", line):
		print(line)

#Like startswith() method
hand = open('some-file.txt')
for line in hand:
	line = line.strip()
	if re.search("^text i want to search", line):
		print(line)


############
import re

string = 'hello 12 hi 89. Howdy 34'
pattern = '\d+'

result = re.findall(pattern, string) 
print(result)

# Output: ['12', '89', '34']


##################
import re

string = 'Twelve:12 Eighty nine:89.'
pattern = '\d+'

result = re.split(pattern, string) 
print(result)

# Output: ['Twelve:', ' Eighty nine:', '.']


##################
import re

# multiline string
string = 'abc 12\
de 23 \n f45 6'

# matches all whitespace characters
pattern = '\s+'

# empty string
replace = ''

new_string = re.sub(pattern, replace, string) 
print(new_string)

# Output: abc12de23f456


#################
import re

# multiline string
string = 'abc 12\
de 23 \n f45 6'

# matches all whitespace characters
pattern = '\s+'

# empty string
replace = ''

new_string = re.subn(pattern, replace, string) 
print(new_string)

# Output: ('abc12de23f456', 4)


#############################
import re

string = "Python is fun"

# check if 'Python' is at the beginning
match = re.search('\APython', string)

if match:
  print("pattern found inside the string")
else:
  print("pattern not found")  

# Output: pattern found inside the string


##########################
import re

string = '39801 356, 2102 1111'

# Three digit number followed by space followed by two digit number
pattern = '(\d{3}) (\d{2})'

# match variable contains a Match object.
match = re.search(pattern, string) 

if match:
  print(match.group())
else:
  print("pattern not found")

# Output: 801 35


############################
import re

string = '\n and \r are escape sequences.'

result = re.findall(r'[\n\r]', string) 
print(result)

# Output: ['\n', '\r']


##################
import re
x = 'My 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]+', x)
print(y)
# Output: ['2', '19', '42']
y = re.findall('[AEIOU]+', x)
print(y)
# Output: []


##EXAMPLE
import re

text = "2aizxcu120347128mnczxohalsd"

print(re.search("[a-z0-9]", text))
##EXAMPLE