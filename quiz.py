print('Seja bem-vindo ao quiz do joão!')
inicio = input('Quer começar o jogo? (S/ N) ')

if inicio != 'S':
    quit(print('Volte Sempre'))
score = 0 
print('Começando....')

print('Pergunta 1 \n (a) \n (b) \n (c) \n (d)')
answer1 = input('Resposta: ')

if answer1 == 'a':
    print('Correto!')
    score = score + 1
else:
    print('Incorreto!')

print('Pergunta 2 \n (a) \n (b) \n (c) \n (d')
answer2 = input('Resposta: ')

if answer2 == 'c':
    print('Correto!')
    score = score + 1
else:
    print('Incorreto!')

... 

print(f'Quiz acabou... Pontuação{score}')