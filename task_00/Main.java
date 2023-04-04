import java.lang.Thread;


public class Main { 
    public static void main(String[] args) { 
        Account cc1 = new Account("Conta 01", 100);

        Cliente c1 = new Cliente("pai", cc1, 10);
        Cliente c2 = new Cliente("filho1", cc1, -10);
        Cliente c3 = new Cliente("filho2", cc1, -10);
        
        c1.start();
        c2.start();
        c3.start();


        System.out.println("All Thread Started ...");


    } 
}