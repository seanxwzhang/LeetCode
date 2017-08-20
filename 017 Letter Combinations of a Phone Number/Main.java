//Given a digit string, return all possible letter combinations that the number could represent.
//
//        A mapping of digit to letters (just like on the telephone buttons) is given below.
//
//
//
//        Input:Digit string "23"
//        Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
//        Note:
//        Although the above answer is in lexicographical order, your answer could be in any order you want.
import java.util.*;


public class Main {
    public static class Solution {

        private HashMap<Character, String> CreateMap() {
            HashMap<Character, String> map = new HashMap<>();
            map.put('1', "");
            map.put('2', "abc");
            map.put('3', "def");
            map.put('4', "ghi");
            map.put('5', "jkl");
            map.put('6', "mno");
            map.put('7', "pqrs");
            map.put('8', "tuv");
            map.put('9', "wxyz");
            map.put('0', "");
            return map;
        }

        private final HashMap<Character, String> mapping = CreateMap();


        public List<String> letterCombinations(String digits) {
            List<String> results = new ArrayList<>();
            if (digits.length() != 0 && digits.indexOf('0') == -1 && digits.indexOf('1') == -1) {
                String[] cc = this.mapping.get(digits.charAt(0)).split("");
                for (int i = 0; i < cc.length; i++) {
                    String s = cc[i];
                    List<String> subRes = letterCombinations(digits.substring(1));
                    subRes.replaceAll(o -> s + o);
                    results.addAll(subRes);
                    if (subRes.size() == 0) {
                        results.add(s);
                    }
                }
            }
            return results;
        }
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        List<String> r = s.letterCombinations("23");
        System.out.println(Arrays.toString(r.toArray()));
    }
}