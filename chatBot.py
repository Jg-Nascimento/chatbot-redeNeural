#bibliotecas
import numpy as np
import tensorflow as tf
import re
import time

#carregando base de dados
#abre o arquivo, faz a leitura e pula linha onde tiver \n
linhas=open('/content/drive/MyDrive/Colab Notebooks/movie_lines.txt', 
              encoding='utf-8',errors='ignore').read().split('\n')

conversas=open('/content/drive/MyDrive/Colab Notebooks/movie_conversations.txt', 
              encoding='utf-8',errors='ignore').read().split('\n')

#dicionario para mapeamento de id's
id_para_linha = {}

for linha in linhas:
   # print(linha)
    _linha = linha.split(' +++$+++ ')
    print(linha)
    
     if len(_linha) == 5:
      print (linha[4])
      id_para_linha[_linha[0]] = _linha[4]

#lista de conversas
conversas_id = []
for conversa in conversas[:-1]:#-1 exclui o ultimo registro
  #print(conversa)
 _conversa = conversa.split(' +++$+++ ')[-1]
 print(conversa)
    

