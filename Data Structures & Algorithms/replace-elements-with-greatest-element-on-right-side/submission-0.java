class Solution {
    public int[] replaceElements(int[] arr) {
        for(int i=0;i<arr.length;i++){
            int m=-1;
            for(int j=i+1;j<arr.length;j++){
                m=Math.max(m,arr[j]);
            }
            arr[i]=m;
        }
        return arr;
    }
}