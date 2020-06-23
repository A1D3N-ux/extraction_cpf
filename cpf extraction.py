from bs4 import BeautifulSoup as soup
import re
cpfs = []
with open(input("digite o nome dos dados: ")+'.txt','r') as arq:
    arqui = arq.read().strip()
    regex = re.findall('([0-9]{2}[\.]?[0-9]{3}[\.]?[0-9]{3}[\/]?[0-9]{4}[-]?[0-9]{2})|([0-9]{3}[\.]?[0-9]{3}[\.]?[0-9]{3}[-]?[0-9]{2})',arqui)
for dados in regex:
    cpfs.append(dados[1])
    for cpf in cpfs:
        cp = open('cpfs.txt', 'a')
        cp.write(cpf + '\n')
        print(cpf)
