from urllib.parse import parse_qs, urlparse

nam = 'nome+do+jogo'
num = '1a23'

link = f"https://canova-games.web.app/games?name={nam}&abacate={num}"

link_tratado = urlparse(link)

parametros = parse_qs(link_tratado.query)
print(parametros)

#print(parametros) = {"game":[nome_do_jogo], "id_jogador":[ID]}
#print(parametors['q'])
