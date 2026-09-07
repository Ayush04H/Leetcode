class Solution {
    public int maxPower(String s) {
        int c = 1;
        int m = 0;
        for(int i = 1;i<s.length();i++){
            if(s.charAt(i)==s.charAt(i-1)){
                c+=1;
            }
            else{
                m = Math.max(m,c);
                c = 1;
            }
        }
        return Math.max(m,c);
    }
}