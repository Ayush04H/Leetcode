class Solution {
    public boolean checkZeroOnes(String s) {
        int zc = 0 , oc = 0;
        int zm = 0 ,om = 0;
        for(int i = 0;i < s.length();i++){
            if(s.charAt(i)=='1'){
                oc+=1;
            }
            else{
                om = Math.max(oc,om);
                oc = 0 ;
            }
        }
        int maxo = Math.max(oc,om);

        for(int i = 0;i< s.length();i++){
            if(s.charAt(i)=='0'){
                zc+=1;
            }
            else{
                zm = Math.max(zc,zm);
                zc = 0 ;
            }
        }
        int maxz = Math.max(zc,zm);
        return maxo>maxz;
    }
}