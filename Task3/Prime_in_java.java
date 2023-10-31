import java.util.Scanner;
class Prime_in_java{ 
    boolean printPrime(int num) {
        if (num <= 1) {
            return false; 
        }
        for (int i=2;i*i<=num;i++){
            if (num%i==0){
                return false;
            }
        }
        return true;
    }
    public static void main(String args[])  
    {    
     int i, num;
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter n ");
        num = sc.nextInt();
        System.out.print("Prime Numbers are \n");
        for(i=2;i<num;i++){
            if (new Prime_in_java().printPrime(i)) {
                System.out.print(i + " ");
            }
            sc.close();
        }
      
    }}