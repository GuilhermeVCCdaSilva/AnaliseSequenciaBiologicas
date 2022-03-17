#! /usr/bin/python
import sys
from Bio import Entrez
db = sys.argv[1]
term = sys.argv[2]

#Obtem o resultado de um ESearch feito à "Entrez API" com a "Data Base" e o "term" escritos pelo utilizador
def obterResultadoESearch():
    eSearch = Entrez.esearch(db=db, term=term, usehistory="y")
    resultado = Entrez.read(eSearch)
    return resultado

#Obtem o WebEnv a partir do resultado da função anterior
def obterWebEnv():
    resultado = obterResultadoESearch()
    webEnv = resultado["WebEnv"]
    return webEnv

#Obtem a QueryKey a partir do resultado da primeira função
def obteQueryKey():
    resultado = obterResultadoESearch()
    queryKey = resultado["QueryKey"]
    return queryKey

#Obtem a informação do EFetch a partir da "Data Base", da QueryKey e do WebEnv que veem das funções anteriores
def obterInformacaoEFetch():
    queryKey = obteQueryKey()
    webEnv = obterWebEnv()
    fetchHandle = Entrez.efetch(db=db, webenv=webEnv, query_key=queryKey, rettype='fasta')
    informacao = fetchHandle.read()
    return informacao

#Escreve a informação da função anterior num ficheiro Fasta na pasta onde se encontra o programa
def escreverFicheiroFasta():
    saveFasta = open(r'sequenciacao.fasta', 'w+')
    informacao = obterInformacaoEFetch()
    saveFasta.write(informacao)
    saveFasta.close()

#O main onde é executada a lógica das funções e programação
if __name__ == '__main__':
    obterResultadoESearch()
    obterWebEnv()
    obteQueryKey()
    obterInformacaoEFetch()
    print(obterInformacaoEFetch())
    escreverFicheiroFasta()
    print("Foi adicionado com sucesso um ficheiro sequenciacao.Fasta com o output: :)")

    #Feito por:
    #Marine Fournier 202000224
    #Guilherme Silva 202000178
    #Miguel 202101030
    
