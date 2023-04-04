import queue, threading, datetime, time

queue = queue.Queue()

lock = threading.Lock()

#Abrir o arquivo
def openFile(path) -> str:
    return "não"



#Identificar os alunos com flag CONCLUIDO
def analyzer(filePath):
    ##abrir o arquivo
    fileIn = open(filePath, 'r').read()
    ###Tranformar cada linha numa posição de uma lista
    listaAlunos = fileIn.split('\n')
    ##Identificar a flag
    for aluno in listaAlunos:
        flag = aluno.split(" ")
        if(flag[len(flag)-1]) == "CONCLUIDO":
            #Adiciona-los a uma lista
            nome = flag[1] +" " +flag[2] + " " + flag[-1]
            addNomeListaFormando(nome)
            
def addNomeListaFormando(nome) -> bool:
    #print(threading.current_thread().name + " tentando usando o recurso")
    lock.acquire()
    if(lock.locked()):
        try:
            with open("FORMANDOS.txt", "a") as my_file:
                my_file.write(nome)
                my_file.write("\n")
            return True
        except:
            print("Ocorreu um erro ao tentar adicionar nome a lista de formandos")
            return False

        finally:
            lock.release()

    else:
        print("Recurso bloqueado")

def salvarListaFormando(status, nameFile) -> bool:
    try:
        if(status):
            nFile = "./formandos/"+nameFile.replace(' ', '%20')+".txt"
            file = open(nFile, 'w')
            for i in list(queue.queue):
                file.write(i)
            file.close()
            print("Lista salva com sucesso!")
        else:
            print("Lista descartada!")
    except:
        print("Ocorreu um erro ao salvar a lista")

