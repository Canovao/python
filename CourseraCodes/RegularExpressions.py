import re
text = open('CourseraCodes/regex_sum_163604.txt', 'r')

soma = 0
for line in text:
    for numb in re.findall('[0-9]+', line):
        soma += int(numb)
        
print(soma)