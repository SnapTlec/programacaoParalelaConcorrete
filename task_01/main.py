import threading
from analyzer import addNomeListaFormando, analyzer

if __name__ == "__main__":
    t1 = threading.Thread(target=analyzer,args=("./COMPUTACAO.txt",))
    t2 = threading.Thread(target=analyzer, args=("./COMPUTACAOII.txt",))

    t1.start()
    t2.start()
    
    t1.join()
    t2.join()