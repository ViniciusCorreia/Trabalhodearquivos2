import struct

registroCEP = struct.Struct("72s72s72s72s2s8s2s")
Coluna_CEP = 5
tamanho_da_linha = registroCEP.size
#arquivos de 10 linhas
'''
leitura1 = open("Novo_Documento_A.txt","rb")
leitura2 = open("Novo_Documento_B.txt","rb")
saida = open("Documento_Saida_1.txt","wb")

leitura1 = open("Novo_Documento_C.txt","rb")
leitura2 = open("Novo_Documento_D.txt","rb")
saida = open("Documento_Saida_2.txt","wb")

leitura1 = open("Novo_Documento_E.txt","rb")
leitura2 = open("Novo_Documento_F.txt","rb")
saida = open("Documento_Saida_3.txt","wb")

leitura1 = open("Novo_Documento_G.dat","rb")
leitura2 = open("Novo_Documento_H.dat","rb")
saida = open("Documento_Saida_4.txt","wb")
'''
#arquivos de 20 linhas
'''
leitura1 = open("Documento_Saida_1.txt","rb")
leitura2 = open("Documento_Saida_2.txt","rb")
saida = open("Documento_Saida_5.txt","wb")

leitura1 = open("Documento_Saida_3.txt","rb")
leitura2 = open("Documento_Saida_4.txt","rb")
saida = open("Documento_Saida_6.txt","wb")
'''
#arquivo de 40 linhas
'''
leitura1 = open("Documento_Saida_5.txt","rb")
leitura2 = open("Documento_Saida_6.txt","rb")
saida = open("Documento_Saida_Final.txt","wb")
'''

leitura1.seek(0,2)
num_linhas1 = leitura1.tell() / registroCEP.size
num_linhas2 = num_linhas1

leitura1.seek(0)
leitura2.seek(0)


while(num_linhas1 != 0 and num_linhas2 != 0 ):
    print("Número de linhas do primeiro arquivo: ",num_linhas1)
    print("Número de linhas do segundo arquivo: ",num_linhas2)
    
    linha1=leitura1.read(registroCEP.size)
    linha2=leitura2.read(registroCEP.size)
    
    
    linha1_fragmentada = registroCEP.unpack(linha1)
    cep1 = linha1_fragmentada[Coluna_CEP]
    print("cep 1--->",cep1)
    
    linha2_fragmentada = registroCEP.unpack(linha2)
    cep2 = linha2_fragmentada[Coluna_CEP]
    print("cep 2--->",cep2)

    if cep1 == cep2:
        
        saida.write(linha1)
        saida.write(linha2)
        num_linhas1 = num_linhas1 - 1
        num_linhas2 = num_linhas2 - 1
        
    if cep1 > cep2:
        
        saida.write(linha2)
        num_linhas2 = num_linhas2 - 1
        leitura1.seek(leitura1.tell() - tamanho_da_linha)
        
    else:
        saida.write(linha1)
        num_linhas1 = num_linhas1 - 1
        leitura2.seek(leitura2.tell() - tamanho_da_linha)
        
while(num_linhas1 != 0):
    
    print("Número de linhas do primeiro arquivo: ",num_linhas1)
    linha1=leitura1.read(registroCEP.size)
    saida.write(linha1)
    num_linhas1 = num_linhas1 - 1
    
while(num_linhas2 != 0):
    
    print("Número de linhas do segundo arquivo: ",num_linhas2)
    linha2=leitura2.read(registroCEP.size)
    saida.write(linha2)
    num_linhas2 = num_linhas2 - 1


leitura1.close()
leitura2.close()
saida.close()
print("Os dois documentos foram ordenados !")


#confirmação de que está ordenado
'''
leitura3 = open("Documento_Saida_Final.txt","rb")
for k in range(0,80):
    linha = leitura3.read(tamanho_da_linha)
    linha_fragmentada = registroCEP.unpack(linha)
    print(str(linha_fragmentada[Coluna_CEP],'latin1'))
print("As 80 linhas foram ordenadas !")
'''
    
    
