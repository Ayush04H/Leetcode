class Solution {
    public boolean isPalindrome(String s) {
        int i = 0 , j = s.length()-1;
        while(i<j){
            char left = s.charAt(i);
            if(!Character.isLetterOrDigit(left)){
                i+=1;
                continue;
            }
            char right = s.charAt(j);
            if(!Character.isLetterOrDigit(right)){
                j-=1;
                continue;
            }

            if(Character.toLowerCase(left) !=Character.toLowerCase(right) ){
                return false;
            }
            i+=1;
            j-=1;

        }
        return true;
    }
    
}