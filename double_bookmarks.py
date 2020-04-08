#!/usr/bin/env python3
# coding: utf-8

from bs4 import BeautifulSoup
import pyparsing as pp
from pyparsing import Word, alphas

print("Insira abaixo o nome do arquivo html salvo do seu navegador.")
book_name = input("Nome do arquivo: ")
myFile = open(book_name, 'r') 
f = open("favoritos_naoduplicados.html", 'w')

#0    1    2     3      4     5     6
#num, mae, tipo, pasta, link, nome, icone
linha=[0,0,0,0,0,0,0]
lista=[]

#lista favoritos
pastas=[]
#lista de sites
sites=[]
dups=[]

a=0
b=0
c=1
d=0
e=0
h=0
k=0
pasta_listada=0

total=0
for line in myFile:
    j=BeautifulSoup(line, 'html.parser')
    if '<h3' in line.lower(): 
        
        if not j.get_text() in pastas:
            pasta_listada=0
            f.write(line)
            
            pastas.append(j.get_text())
            a+=1
#Planos pra próxima versão
#             linha[0]=a             #0
#             if c==1:
#                 linha[1]=a-e          #1
#                 b=a
#                 c=0
#             else:
#                 linha[1]=a-1
#             linha[2]="Pasta"       #2
#             linha[3]=j.get_text()  #3
#             linha[4]="None"        #4
#             linha[5]="None"        #5
#             linha[6]="None"        #6
        else:
            pasta_listada=1  
            
    elif "dl><p>" in line.lower() and pasta_listada==1:
            pass
        
    elif "<dt><a" in line.lower():
        t=j.find('a')
        total+=1
        if not t.get("href") in sites and pasta_listada==0:
            sites.append(t.get('href'))
            f.write(line)
            h+=1
        elif not t.get("href") in sites and pasta_listada==1:
            sites.append(t.get('href'))
            dups.append(line)
            k+=1
        else:
            pass        
   
    else:
        f.write(line)
        
f.write("""<DT><H3>Extras bookmarks</H3>
         <DL><p>""")
for dup in dups:
    #print(dup)
    f.write(dup)
f.write("""         </DL><p>
    </DL><p>
</DL><p>""")

#print(a, h, k, h+k)

print("\nForam encontradas " + str(a) + " pastas não repetidas no arquivo.")
print("Do total de " + str(total) + " favoritos salvos, " + str(h+k) + " não são repetidos.")
print("O que corresponde a %.2f%% do total." %((h+k)/total*100))

