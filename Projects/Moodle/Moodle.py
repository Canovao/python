import requests
from bs4 import BeautifulSoup
import json

questoes = dict()

#questoes['Abacaxi é doce?'] = ['Sim', 'Não', 'Que?', 'Ontem']
#print(questoes)
#exit(0)


# ENUNCIADO: qtext
# ALTERNATIVAS: flex-fill ml-1

link = 'https://moodle.ggte.unicamp.br'#/mod/quiz/review.php?attempt=1366197&cmid=405405


page = requests.get(link)
soup = BeautifulSoup(page.text, 'html.parser')

print(soup)

#alternativas = soup.find_all('ml-1')

#print(alternativas)
exit(0)

links = list()
for alternativa in alternativas:
    links.append(alternativa.get('href'))
    if tag.get('href') != None or tag.get('href') != "#":
        links.append(tag.get('href'))

print(item, "|||", links, "|||")