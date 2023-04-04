public class Cliente extends Thread{
    private String name;
    private Account conta;
    private double money;

    public Cliente(String name, Account cc, double x){
        this.name = name;
        this.conta = cc;
        this.money = x;
    }

    public void run(){
        //synchronized(this.conta){
            try{
                Account cc = this.conta;
                double total = 0;
                while(cc.debit(this.money)){
                    total += this.money;
                    Thread.sleep(1000);
                };
                System.out.println(Thread.currentThread().getName() + " sacou um total: " + total);
            }catch(Exception e){
                System.out.println("Erro: "+ e);
            }
        //}
    }
}