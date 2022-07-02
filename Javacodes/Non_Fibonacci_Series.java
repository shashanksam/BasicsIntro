import java.io.*;

class Non_Fibonacci_Series {
    
	public static void main (String[] args) {
		int count0100[]=new int[101];
		int count=10;
		int n3=0,n1=0,n2=1;
		count0100[n1]=-1;
		count0100[n2]=-1;
		System.out.println("Fibonacci Series ");
        System.out.print(n1+" "+n2);
		for(int i=2;i<count;++i){    
            n3=n1+n2;   
            System.out.print(" "+n3);    
            count0100[n3]=-1;
            n1=n2;    
            n2=n3;    
        }  
        System.out.println("\nNon-Fibonacci Series ");
        for(int i=0;i<n3;i++){
            if(count0100[i]>=0){
                System.out.print(" "+i);
            }
        }
		
	}
}

// //Output
// Fibonacci Series 
// 0 1 1 2 3 5 8 13 21 34
// Non-Fibonacci Series 
//  4 6 7 9 10 11 12 14 15 16 17 18 19 20 22 23 24 25 26 27 28 29 30 31 32 33
