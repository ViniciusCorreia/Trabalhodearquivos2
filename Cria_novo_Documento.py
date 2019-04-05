import struct
import random

registroCEP = struct.Struct("72s72s72s72s2s8s2s")
leitura = open("cep_ordenado.dat","rb")


#Criação de oito documentos de 10 linhas ordenadas
'''
leitura2 = open("Novo_Documento_A.txt","wb")
leitura2 = open("Novo_Documento_B.txt","wb")
leitura2 = open("Novo_Documento_C.txt","wb")
leitura2 = open("Novo_Documento_D.txt","wb")
leitura2 = open("Novo_Documento_E.txt","wb")
leitura2 = open("Novo_Documento_F.txt","wb")
leitura2 = open("Novo_Documento_G.txt","wb")
leitura2 = open("Novo_Documento_H.txt","wb")
'''

leitura.seek(0, 2)
tamanho_do_arquivo = leitura.tell()
num_linhas = tamanho_do_arquivo / registroCEP.size


leitura.seek(random.randint(0,num_linhas-11) * registroCEP.size)
linha = leitura.read(registroCEP.size*10)
leitura2.write(linha)
    
leitura2.seek(0,2)
tamanho=leitura2.tell() / registroCEP.size
leitura.close()
print("Novo arquivo com {} linhas está pronto!".format(tamanho))    

