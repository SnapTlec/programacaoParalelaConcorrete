import random

fileIn = open('./COMPUTACAO.csv', 'r').read().split('\n')
fileMiddle = []
for i in fileIn:
    fileMiddle.append(i.split(','))

fileOut = open('./COMPUTACAO.txt', 'w')

for a in fileMiddle:
    x = random.randint(0,1)
    if x == 1: 
        fileOut.write(a[0] + ' ' + a[1] + ' COMPUTAÇÃO CURSANDO\n')
    else:
        fileOut.write(a[0] + ' ' + a[1] + ' COMPUTAÇÃO CONCLUIDO\n')

fileOut.close()