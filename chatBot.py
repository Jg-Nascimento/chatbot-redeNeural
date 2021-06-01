#bibliotecas
import numpy as np
import tensorflow as tf
import re
import time

#carregando base de dados
#abre o arquivo, faz a leitura e pula linha onde tiver \n
linhas=open('movie_lines.txt', 
              encoding='utf-8',errors='ignore').read().split('\n')

conversas=open('movie_conversations.txt', 
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
#-1 exclui o ultimo registro
for conversa in conversas[:-1]:
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
  texto = re.sub(r"can't", "cannot", texto)
  texto = re.sub(r"[-()#/@;:<>[]{}~+=?.|,]", "", texto)
  
  return texto

'''
==============================================================
|++++++++++++ limpeza das perguntas e respostas +++++++++++++|
==============================================================
'''
#percorre todas as perguntas e envia para a função limpa_texto
perguntas_limpas = []
for pergunta in perguntas_limpas:
  perguntas_limpas.append(limpa_texto(pergunta))

#ocorrência de palavras
palavras_contagem = {}
for pergunta in perguntas_limpas:
  #print(pergunta)
  for palavra in pergunta.split():
    if palavra not in palavras_contagem:
      palavras_contagem[palavra] = 1
    else:
      palavras_contagem[palavra] += 1

respostas_limpas = []
for resposta in respostas_limpas:
  #print(pergunta)
  for palavra in resposta.split():
    if palavra not in palavras_contagem:
      palavras_contagem[palavra] = 1
    else:
      palavras_contagem[palavra] += 1

#relação de palavras não frequentes e tokenização (dois dicionários)
limite = 20
perguntas_palavras_int = {}
numero_palavra = 0

#retorna a palavra e a ocorrência
for palavra, contagem in palavras_contagem.items():
  if contagem >= limite:
    perguntas_palavras_int[palavra] = numero_palavra
    numero_palavra += 1

respostas_palavras_int = {}
numero_palavra = 0

#retorna a palavra e a ocorrência
for palavra, contagem in palavras_contagem.items():
  if contagem >= limite:
    respostas_palavras_int[palavra] = numero_palavra
    numero_palavra += 1

#adicionando tokens
tokens = ['<PAD>', '<EOS>', '<AUT>', '<SOS>']

for token in tokens:
  perguntas_palavras_int[token] = len(perguntas_palavras_int) + 1

for token in tokens:
  respostas_palavras_int[token] = len(respostas_palavras_int) + 1

#retorna a chave do indice
resposta_int_palavras = {p_i: p for p, p_i in respostas_palavras_int.items()}

#adiciona token no final da string <EOS> de cada resposta
for i in range(len(respostas_limpas)):
  respostas_limpas[i] += ' <EOS>'

perguntas_para_int = []
for pergunta in perguntas_limpas:
  ints = []
  for palavra in pergunta.split():
    if palavra not in perguntas_palavras_int:
      ints.append(perguntas_palavras_int['<OUT>'])
    else:
      ints.append(perguntas_palavras_int[palavra])

  perguntas_para_int.append(int)

respostas_para_int = []
for respostas in respostas_limpas:
  ints = []
  for palavra in respostas.split():
    if palavra not in respostas_palavras_int:
      ints.append(respostas_palavras_int['<OUT>'])
    else:
      ints.append(respostas_palavras_int[palavra])

  respostas_para_int.append(int)

#ordenação das perguntas
perguntas_limpas_ordenadas[]
respostas_limpas_ordenadas[]

for tamanho in range(1, 25 + 1):
  for i in enumerate(perguntas_para_int):
    #print(i[1])
    if len(i[1]) == tamanho:
      perguntas_limpas_ordenadas.append(perguntas_palavras_int[i[0]])
      respostas_limpas_ordenadas.append(respostas_palavras_int[i[0]])

print("DEBUG")