nome = input('Qual é o seu nome? ')
print('Muito prazer em te conhecer {}{}{}!'. format('\033[4;34m', nome, '\033[m'))
idade = input('E qual é a sua idade? ')
cidade = input('Hum, legal e qual a sua cidade? ')
print('Dados cadastrados, nome {}{}{}, idade {}{}{} anos da cidade {}{}{}!'.format('\033[4;34m', nome, '\033[m','\033[4;34m', idade, '\033[m','\033[4;34m', cidade, '\033[m'))
