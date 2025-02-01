class Solution{
public int[] plusOne(int[] digits) {
    for(int i=digits.length-1;i>=0;i--){ //Traverse from right (n-1) to left of the number - 0 based indexing - decrement till i>=0 
    if (digits[i]+1<10) { //case1: if less than 10 increment and return the array
//case2: if greater than 10 make that element 0 and iterate over the array and resolve carry over for the next element
        digits[i]++;
        return digits; //in case of 1 2 3 to 1 2 4
    }
    else{
        digits[i] = 0;//in case of carry over digits[i]=0 (i,e) in case of 9
        }//due to i-- then we go to the previous element this is the next iteration and for loop will go on
    }
    digits=new int[digits.length+1];//new array of size n+1
    digits[0]=1;
    return digits;
    }
}
