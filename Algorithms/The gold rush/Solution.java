import java.util.Scanner;

/*
 * The gold rush problem is solved using Dynamic Programming.
 * 
 * gold[i] : gold at coordinate i
 * dist[i j] : distance between coordinates j and i where j = 1 to i - 1
 * OPT[i] : maximum gold that can be collected till coordinate i
 * 
 * Recurrence :
 * 					
 * 				
 * OPT[i] = max (gold[i] - dist[0 i]
 * 				max(OPT[j] + gold[i] - dist[i j])  for all j = 1 to i-1
 * 
 * Base Case :
 * OPT[0] : gold at first coordinate
 * 
 * Time Complexity : 0(n^n)
 * Space Complexity : O(n)
 * 
 */
public class Solution {
	
	public static void main(String[] args) {
		
		Solution sol	= new Solution();
		Scanner in		= new Scanner(System.in);
		int n			= (int) in.nextInt();
		Coordinates[] coordinates = new Coordinates[n];

		for(int i = 0; i < n; i++) {
			Coordinates coordinate = new Coordinates();
			coordinate.x = in.nextInt();
			coordinate.y = in.nextInt();
			coordinate.gold = in.nextInt();
			coordinates[i] = coordinate;
		}
		
		in.close();
		
		if(n > 0) {
			double max = sol.maximizeGold(coordinates);
			String str = String.format("%.6f", max);			
			System.out.println(str);
		}
		else
			System.out.println(0.000000);			
	}
	
	// implementation of recurrence relation
	private double maximizeGold(Coordinates[] coordinates) {
		int n = coordinates.length;
		double[] max = new double[n];
		max[0] = coordinates[0].gold;
		
		for(int i = 1; i < n; i++) {
			double maxGold = Integer.MIN_VALUE;
			for(int j = 0; j <= i; j++) {
				if(j == 0) 
					maxGold = opt(coordinates, i, j);
				else
					maxGold = Math.max(maxGold,  max[i-j] + opt(coordinates, i, i-j));
			}
			max[i] = maxGold;
		}
		
		return max[n-1];
	}

	// returns the gold value when moving from 1 coordinate to another
	private double opt(Coordinates[] coordinates, int i, int j) {
		return coordinates[i].gold - 
				distance(coordinates[j].x, coordinates[j].y, coordinates[i].x, coordinates[i].y);
	}

	// calculates distance between 2 coordinates
	private double distance(double x1, double y1, double x2, double y2) {
	    return Math.sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1));
	}
}

// class to save the input
class Coordinates{
	double x;
	double y;
	double gold;		
}