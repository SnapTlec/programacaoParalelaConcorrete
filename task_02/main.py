import threading
from time import sleep

lock = threading.Lock()

def consumer(conta, value, time):
    while True:
        if(not conta.saldo - value < 0):
            try:
                lock.acquire()
                novoSaldo = conta.saldo - value
                conta.saldo = novoSaldo
                
                print(f'A Thread_Consumer {threading.current_thread().name} sacou: {value} e o saldo atual é: {conta.saldo}')
                
                lock.release()
                sleep(time)
                
            except(KeyboardInterrupt):
                print("Parando ...")
def producer(conta,value):
    while True:
        if(conta.saldo <= 0):
            try:
                lock.acquire()
                novoSaldo = conta.saldo + value
                conta.saldo = novoSaldo
                print(f'A Thread_Producer {threading.current_thread().name} depositou: {value} e o saldo atual é: {conta.saldo}')
                lock.release()
                sleep(1)
            except(KeyboardInterrupt):
                print("Erro")
                
    
class Conta:
    def __init__(self):
        self.saldo = 100

if __name__ == '__main__':
    conta = Conta()
    t3 = threading.Thread(target=producer, name="P1",args=(conta,100,))
    
    t1 = threading.Thread(target=consumer, name="C1",args=(conta,50,12,))
    t4 = threading.Thread(target=consumer, name="C3",args=(conta,5,6,))
    t2 = threading.Thread(target=consumer, name="C2",args=(conta,10,3,))
    
    
    t1.start()
    t2.start()
    t3.start()
    t4.start()

