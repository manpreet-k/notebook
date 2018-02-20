import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

public class Solution {
	
	public static void main(String[] args) {
		try {
			Scanner in = new Scanner(System.in);
			int arrayLength = in.nextInt();
			Solution secMaxEle = new Solution();
			List<Integer> input = new ArrayList<Integer>();
			
			for(int i = 1; i <= arrayLength; i++) {
				input.add(in.nextInt());
			}
			
			in.close();
			
			System.out.println(Integer.toString(secMaxEle.secondMaximumElement(input)));		
			
		} catch (NumberFormatException e) {
			e.printStackTrace();
		} catch (ArrayIndexOutOfBoundsException e) {
			e.printStackTrace();
		}
	}
		
	public int secondMaximumElement(List<Integer> input) {
		try {
			if(input != null && input.size() > 0) {
				Collections.sort(input, Collections.reverseOrder());
				return input.get(1);
			}
			else return 0;
		} catch (Exception e) {
			e.printStackTrace();
			return 0;
		}		
	}
}
