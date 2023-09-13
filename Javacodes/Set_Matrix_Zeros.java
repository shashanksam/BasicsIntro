import java.io.*;
import java.util.* ;

public class Solution {
    public static void setZeros(int matrix[][]) {
        // Write your code here..

        int x=matrix.length;//2
        int y=matrix[0].length;//3
        int rows0[]=new int[y];
        int cols0[]=new int[x];

        // System.out.println(x+" "+y);
        for(int i=0;i<x;i++){
            for(int j=0;j<y;j++){
                if(matrix[i][j]==0){
                    rows0[j]=100;
                    cols0[i]=100;
                }
            }
        }
        for(int i=0;i<y;i++){
            // System.out.println(rows0[i]);
            if(rows0[i]==100){
                for(int a=0;a<x;a++){
                    matrix[a][i]=0;
                }
            }
        }
            // System.out.println();
            
        for(int i=0;i<x;i++){
            // System.out.println(cols0[i]);
            if(cols0[i]==100){
                for(int a=0;a<y;a++){
                    matrix[i][a]=0;
                }
            }
        }
            // System.out.println();
    }

}




//input
/*
4
2 3
7 19 3
4 21 0
3 3
1 2 3
4 0 6
7 8 9
4 2
1 0
2 7
3 0
4 8
3 3
0 2 3
1 0 3
1 2 0
  */


//output

/*

7 19 0 
0 0 0 
1 0 3 
0 0 0 
7 0 9 
0 0 
2 0 
0 0 
4 0 
0 0 0 
0 0 0 
0 0 0 
*/

