import threading, random
from time import sleep

class Equipe:
    def produzirPedido(self) -> bool:
        try:
            sleep(random.randint(1, 11))
            return True
        except:
            print("Erro ao produzir o pedido")
            return False
class Atendente:
    def __init__(self):
        self.equipe= Equipe()
        
    def fazerPedido(self) -> bool:
        print("Pedido recebido")

        t1 = threading.Thread(target=self.equipe.produzirPedido)
        t2 = threading.Thread(target=self.equipe.produzirPedido)
        
        t1.start()
        t2.start()
        
        sleep(1)
        print("Nossa equipe está preparando seu pedido")
        
        t1.join()
        t2.join()
        print("Pedido Pronto")
if __name__ == '__main__':
    
    atendente = Atendente()
    atendente.fazerPedido()