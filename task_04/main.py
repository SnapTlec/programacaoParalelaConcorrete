import threading
from datetime import datetime

lock = threading.Lock()

def dividirVetor(v,q):
    n = q
    splited = []
    len_v = len(v)
    for i in range(n):
        start = int(i*len_v/n)
        end = int((i+1)*len_v/n)
        splited.append(v[start:end])
    return splited

def criarVetor(v):
    for i in range(1000):
        x = datetime.timestamp(datetime.now())
        addLista(v,int(i*x))

def addLista(v, el):
    lock.acquire()
    #print(f'A thread {threading.current_thread().name} está utilizando a função')
    if(lock.locked()):
        v.append(el)
    lock.release()
    
def soma(v, s):
    soma = 0
    for i in range(len(v)):
        soma += v[i]
    addLista(s,soma)
    
if __name__ == "__main__":
    vetorMilhao = []
    SomaMilhao = []
    
    #Criar o vetor com 1.000.000 de elementos
    for i in range(1000):
        threading.Thread(target=criarVetor, args=(vetorMilhao,)).start()
    
    print(f'Quantidade de elementos da lista: {len(vetorMilhao)}')
    print(f'Soma dos elementos da lista [vetorMilhao]: {sum(vetorMilhao)}')
    
    subVetores = dividirVetor(vetorMilhao, 100)
    for subVetor in subVetores:
        threading.Thread(target=soma, args=(subVetor,SomaMilhao,)).start()
    
    print("\n===================================================\n")
    print(f'Quantidade de elementos da lista: {len(SomaMilhao)}')
    print(f'Soma dos elementos da lista [SomaMilhao]: {sum(SomaMilhao)}')
    
    
    
    
        
    
