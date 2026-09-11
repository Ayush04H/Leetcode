class Solution {
    public int largestAltitude(int[] gain) {
        int max = 0;
        int[] maxi = new int[gain.length+1];
        maxi[0]=0;
        for(int i = 1;i < gain.length+1 ;i++){
            maxi[i] = maxi[i-1] + gain[i-1];
            if(maxi[i] > max){
                max = maxi[i];
            }
        }
        return max;
        
    }
}