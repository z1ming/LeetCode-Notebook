给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。

示例 1:

输入: "(()"
输出: 2
解释: 最长有效括号子串为 "()"
示例 2:

输入: ")()())"
输出: 4
解释: 最长有效括号子串为 "()()"
// 方法一 暴力
// time:O(N^2)
// space:O(N)
class Solution {
    public boolean isValid(String s){
        Stack<Character> stack = new Stack<Character>();
        for (int i =0;i<s.length();i++){
            if (s.charAt(i)=='('){
                stack.push('(');
            }else if (!stack.empty() && stack.peek() == '('){
                stack.pop();
            }
            else{
                return false;
            }

    }
    return stack.empty();
    }
    public int longestValidParentheses(String s) {
        int maxlen = 0;
        for (int i = 0;i<s.length();i++){
            for (int j = i + 2;j<=s.length();j+=2){
                if (isValid(s.substring(i,j))){
                    maxlen =  Math.max(maxlen,j-i);
                }
            }
        }
        return maxlen;
    }
    }
// 方法二  栈
class Solution {
    public int longestValidParentheses(String s) {
        int maxans = 0;
        Stack<Integer> stack = new Stack<>();
        stack.push(-1);
        for (int i = 0;i < s.length();i++){
            if (s.charAt(i)== '('){
                stack.push(i);
            }else{
                stack.pop();
                if (stack.empty()){
                    stack.push(i);
                }else{
                    maxans = Math.max(maxans,i-stack.peek());
                }
            }
        }
        return maxans;
    }
}

// 方法三  不需要额外空间
class Solution {
    public int longestValidParentheses(String s) {
        int left = 0,right = 0,maxlength = 0;
        for (int i = 0;i < s.length();i++){
            if (s.charAt(i) == '('){
                left++;
            }else{
                right++;
            }
            if (left == right){
                maxlength = Math.max(maxlength,2*right);
            }else if(right > left){
                left = right = 0;
            }
        }
        left = right = 0;
        for (int i = s.length() - 1;i >= 0; i--){
            if (s.charAt(i) == '('){
                left ++;
            }else{
                right++;
            }
            if(left == right){
                maxlength = Math.max(maxlength,2*left);
            }else if (left >= right){
                left = right = 0;
            }
        }
        return maxlength;
    }
}