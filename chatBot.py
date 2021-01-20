#bibliotecas
import numpy as np
import tensorflow as tf
import re
import time

#carregando base de dados
#abre o arquivo, faz a leitura e pula linha onde tiver \n
linhas=open('/recursos/movie_lines.txt', 
              encoding='utf-8',errors='ignore').read().split('\n')

linhas=open('/recursos/movie_conversations.txt', 
              encoding='utf-8',errors='ignore').read().split('\n')

#dicionario para mapeamento de id's
id_para_linha = {}

for linha in linhas:
   # print(linha)
    _linha = linha.split(' +++$+++ ')
    print(linha)