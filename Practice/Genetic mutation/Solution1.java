package src;

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Deque;
import java.util.HashMap;
import java.util.LinkedHashMap;
import java.util.LinkedHashSet;
import java.util.List;
import java.util.Map;
import java.util.Stack;
import java.util.Vector;

public class Solution1 {

	static int findMutationDistance(String start, String end, String[] bank) {
       List<String> mutationBank = Arrays.asList(bank);
       List<String> visited = new ArrayList<>();
       Deque<String> queue = new ArrayDeque<>();
       
       queue.push("0"+start);
       
       while(!queue.isEmpty()) {
    	   String str = queue.pop();
    	   String gene = str.substring(1);
    	   
    	   int path = Integer.parseInt(str.substring(0, 1));
    	   
    	   if(gene.equals(end))
    		   return path;
    	   
    	   visited.add(gene);
    	   
    	   for(String mutation : mutationBank) {
    		   if(!queue.contains(mutation) && !visited.contains(mutation) && isOneStepMutation(mutation, gene)) {
    			   int newPath = path+1;
    			   queue.push(String.valueOf(newPath)+mutation); 
    		   }
    	   }
       }
       return -1;
       
    }
    
    private static int stepMutation(String mutation1, String mutation2){
        int count = 0;
        for(int i = 0; i < mutation1.length(); i++){
            if(mutation1.charAt(i) != mutation2.charAt(i)){
                count++;
            }
        }
        
        return count;
    }
    
    private static boolean isOneStepMutation(String mutation1, String mutation2){
        int count = 0;
        for(int i = 0; i < mutation1.length(); i++){
            if(mutation1.charAt(i) != mutation2.charAt(i)){
                count++;
            }
        }
        
        return count == 1;
    }
    
//    public static void main(String[] args) {
//    	String start = "AAAAAAAA";
//    	String end =   "AAAAAATT";
//    	String[]	bank = {"AAAAAAAA","AAAAAAAT","AAAAAATT","AAAAATTT"};
//    	
//    	Solution1 sol = new Solution1();
//    	System.out.println(Solution1.findMutationDistance(start,  end,  bank));
//    	
//	}
}