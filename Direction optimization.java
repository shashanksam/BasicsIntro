import java.io.*;
import java.util.*;

class GFG
{
	public static void main(String[] args)
	{
	    Scanner s = new Scanner(System.in);
		char[] a = s.next().toCharArray();
      int posx=0, posy=0;
      int len=a.length;
      for (int i = 0; i < len; i++) 
         if(  a[i]=='N'){
            posy++;
         }
        else if(a[i]=='S'){
            posy--;
        }
        else if(a[i]=='E'){
            posx++;
        }
        else {
            posx--;
        }
		//System.out.println(posx+" "+posy);
		//int lenght= Math.abs(posx)+Math.abs(posy);
		if(posx>0){
		while(posx>0){
		    System.out.print("E");
		    posx--;
		}}
		if(posy>0){
		while(posy>0){
		    System.out.print("N");
		    posy--;
		}}
		if(posx<0){
		while(posy<0){
		    System.out.print("S");
		    posy++;
		}}
		if(posx<0){
		while(posx<0){
		    System.out.print("W");
		    posx++;
		}}
	}
}

// This code is contributed by ssam
