import java.util.Scanner;


/**
 * The fast square root implemented here uses the Newton's method to calculate square roots.
 * We start with a guess of input/2 to check if that is the  best fit, if not, then iteratively move on 
 * to a value closer to the actual square root.
 * 
 * This implementation checks at most O(log n) values to arrive at the best possible match.
 * 
 * Also, it uses double variables input, i, sqrt, value and x to hold values. double is 8 bytes in size.
 * So this implementation requires 40 bytes.
 * This is a constant value irrespective of the size of the input or 
 * the number of iterations required to get the best possible match.
 * 
 * Hence,
 * 		Time complexity = O(log n)
 * 		Space complexity = constant or O(1)
 *
 */
public class Solution {

	public static void main(String[] args) {
		Solution sol  = new Solution();
		Scanner in = new Scanner(System.in);
		//double input = in.nextDouble();
		
		in.close();
		
		System.out.println(sol.ComputeSqrt(0.01));
	}
	
	/**
	 * @param x : Number for which square root has to be calculated
	 * @return : closest square root of x
	 */
	double ComputeSqrt(double x)
    {
		long startTime = System.currentTimeMillis();
		double sqrt = 0;
		double i = 0;
		    
	    i = x/2; // initial value for the i
	    i=1.0;
    
	    while (x > 0)
	    {
	    	sqrt = i - (i * i - x) / (2 * i); // take the current value for i and 
	    	                                  // reduce it to reach the next value for i
	    	double value = i - sqrt;  
	        
	        value = value < 0 ? value *= -1 : value;
	        
	        if (value < 0.01) // check tolerance of the calculated square root
	        {
	        	long endTime   = System.currentTimeMillis();
	        	long totalTime = endTime - startTime;
	        	System.out.print("compute sqrt : ");
	        	System.out.println(totalTime);
	            return sqrt;    
	        }
	        else 
	        	i = sqrt;
	    }
	    long endTime   = System.currentTimeMillis();
    	long totalTime = endTime - startTime;
    	System.out.print("compute sqrt : ");
    	System.out.println(totalTime);
	    return x;  
    } 	
}
