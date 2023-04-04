public class CProduce extends Thread{
    private double debit;
    private Account conta;
    
    public CProduce(Account cc){
        this.conta = cc;
        this.debit = 100;
    }

    public void run(){
        while(true){
            if(this.conta.getSaldo() == 0){
                this.conta.setSaldo(this.debit);           
            }
        }
    }
}