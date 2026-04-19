class Solution {
    public boolean isPalindrome(int x) {
        int rem=0,sum=x;
        while(x>0){
            rem=(rem * 10) + (x%10);
            x/=10;;


        }
        return rem == sum;
        
    }
}
