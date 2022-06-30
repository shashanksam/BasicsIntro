/*package whatever //do not write package name here */

import java.io.*;
import java.util.*;

class GFG {
	public static void main (String[] args) {
	//	System.out.println("GfG!");
		Scanner s=new Scanner(System.in);
		int in1=s.nextInt();
		int in2=s.nextInt();
		int k=s.nextInt();
		String s1=String.valueOf(in1); 
	    String s2=String.valueOf(in2);
// 	    12345678
// 	    k=2
// 	    12 34 56 78
// 	    0   1 2  3
// i=	    01 23 45 67
// i/k=    00 11 22 33         
	    int newlen=s1.length()/k;
	    String sk1[]=new String [newlen];
	    String sk2[]=new String [newlen];
	    int ar1[]=new int [newlen];
	    int ar2[]=new int [newlen];
	    for(int i=0;i<s1.length();i++){
	        sk1[i/k]=s1.substring(i,i+k);
	        sk2[i/k]=s2.substring(i,i+k);
	        ar1[i/k]=Integer.parseInt(sk1[i/k]);
            ar2[i/k]=Integer.parseInt(sk2[i/k]);
	        i+=k-1;
	    }
	     Arrays.sort(ar1);
	      Arrays.sort(ar2);
	      int sub=0;
	    for(int i=0;i<newlen;i++){
	        //System.out.println(ar1[i]);
	        int sub1=ar1[i]-ar2[i];
	        if(sub1<0){sub1*=-1;}
	        sub=sub+sub1;
	    }
	    System.out.println(sub);
	    
	    
	}
}

// input
//1921
// 8381
// 2


//output
//124
