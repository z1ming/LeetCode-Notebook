class Solution {
    public List<Integer> countSteppingNumbers(int low, int high) {
        Queue<Integer> temp = new LinkedList<>();
        List<Integer> result = new ArrayList<Integer>();
        addElementBFS(temp,result,low,high);
        return result;
    }

    //因为宽度优先搜索，所以一层层加入进去本身就有顺序无需排序
    public static void addElementBFS(Queue<Integer> temp,List<Integer> res,int low,int high){
        if(low == 0){//如果low==0就在结果加0
            res.add(0);
        }

        for(int i=1;i<=9;i++){//1到9符合题意
            temp.add(i);
        }
        
        while(temp != null){
            int t= temp.poll();//取列表头元素
            int end = t;//单位数末位为本身
            if(t>=10){
                end = t%10;//非单位数末位求余
            }
            if(t > high){//元素超过范围退出
                break;
            }
            if(t>=low && t<=high){
                res.add(t);//如果步进数再范围内就添加
            }
            if(end != 0){//避免10会产生结果99
                temp.add(t*10 + (end-1));
            }
            if(end != 9){//避免9会产生结果100
                temp.add(t*10 + (end+1));
            }
        }
    }
}
//菜狗解析，有意见指出，有问题call我
