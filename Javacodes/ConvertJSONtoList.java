import java.io.*;
import java.util.*;

//Regex feature needs to be added

class GFG {
	public static void main (String[] args) {
	    String plant;
	    Scanner s=new Scanner(System.in);
	    plant=s.next();
    
		////testing added
		String t=plant.toString().substring(10,plant.length()-2);
	
		System.out.println(plant);
		plant=plant.substring(10,plant.length()-2);
		plant=plant.replace("\"","");
		System.out.println(t);
// 		plant="("+plant+")";
        List<String> plantlist= new ArrayList<>();  
        plantlist= Arrays.asList(plant.split(",", -1));
        System.out.println(plantlist);
	}
}

//input is
//{"plant":["DE10","DE11","3912"]}
