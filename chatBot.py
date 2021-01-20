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
  #replace remove espaços vazios e aspas simples
 _conversa = conversa.split(' +++$+++ ')[-1][1:-1].replace("'", "").replace(" ", "")
  
 conversas_id.append(_conversa.split(","))
     
#separação de perguntas e respostas
perguntas = []
respostas = []

for conversa in conversas_id:
  #print(conversa)
  for i in range(len(conversa) - 1):
    #print(conversa)
    perguntas.append(id_para_linha[conversa[i]])
    respostas.append(id_para_linha[conversa[i + 1]])


#pré-processamento dos textos
def limpa_texto(texto):
  texto = texto.lower()
  texto = re.sub(r"i'm", "i am", texto)
  texto = re.sub(r"he's", "he is", texto)
  texto = re.sub(r"she's", "she is", texto)
  texto = re.sub(r"that's", "that is", texto)
  texto = re.sub(r"what's", "what is", texto)
  texto = re.sub(r"where's", "where is", texto)
  texto = re.sub(r"\'ll", " will", texto)
  texto = re.sub(r"\'ve", " have", texto)
  texto = re.sub(r"\'re", " are", texto)
  texto = re.sub(r"\'d", " would", texto)
  texto = re.sub(r"won't", "will not", texto)
  texto = re.sub(r"csn't", "cannot", texto)
  texto = re.sub(r"[-()#/@;:<>[]{}~+=?.|,]", "", texto)
  
  return texto