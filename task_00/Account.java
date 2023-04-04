import java.time.LocalDate;

public class Account extends Thread{
    private double availableMoney;


    public Account(String name, double avb){
        super(name);
        this.availableMoney = avb;
    }

    public double getSaldo(){
        double saldo = this.availableMoney;
        return saldo;
    }

    public void setSaldo(double valor){
        this.availableMoney += valor;
        System.out.println(Thread.currentThread().getName() + " depositou R$: "+ valor+". Saldo novo: R$ " + this.availableMoney);
    }

    public synchronized boolean debit(double value){
        double saldo = this.availableMoney;
        if(saldo < value){
            System.out.println("Saldo insuficiente");
            return false;
        }

        this.availableMoney += value;
        System.out.println(Thread.currentThread().getName() + " sacou R$: "+ value+". Saldo novo: R$ " + this.availableMoney);
        return true;
    }

}