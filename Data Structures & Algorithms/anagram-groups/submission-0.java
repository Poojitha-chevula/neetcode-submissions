class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String,List<String>> mpp=new HashMap<>();
        for(String s:strs){
            char[] c=s.toCharArray();
            Arrays.sort(c);
            String k=new String(c);
            if(!mpp.containsKey(k)){
                mpp.put(k,new ArrayList<>());
            }
            mpp.get(k).add(s);
        }
        return new ArrayList<>(mpp.values());
    }
}
