class Solution {
    public int[] smallestRange(List<List<Integer>> nums) {
        //小根堆，堆顶为各列表最小当前元素 二维坐标
        Queue<int[]> minQueue = new PriorityQueue<>(Comparator.comparingInt(arr -> nums.get(arr[0]).get(arr[1])));
        //大根堆，堆顶为各列表最大当前元素 二维坐标
        Queue<int[]> maxQueue = new PriorityQueue<>((arr1, arr2) -> nums.get(arr2[0]).get(arr2[1]) - nums.get(arr1[0]).get(arr1[1]));
        int[] ans = new int[]{Integer.MIN_VALUE, Integer.MAX_VALUE};
        for (int i = 0; i < nums.size(); i++) {
            //初始化各列表第一个元素，小根堆&大根堆添加同一个对象，方便后面remove
            int[] arr = new int[]{i, 0};
            minQueue.offer(arr);
            maxQueue.offer(arr);
        }
        while (minQueue.size() == nums.size()) {
            //推出小根堆顶元素，小根堆size-1
            int[] minArr = minQueue.poll();
            //小根堆顶元素与大根堆顶元素区间，每个列表至少有一个数包含在其中
            int[] maxArr = maxQueue.peek();
            //注意此处相减值溢出，需要转成long
            if ((long) nums.get(maxArr[0]).get(maxArr[1]) - (long) nums.get(minArr[0]).get(minArr[1]) < (long) ans[1] - (long) ans[0]) {
                ans[0] = nums.get(minArr[0]).get(minArr[1]);
                ans[1] = nums.get(maxArr[0]).get(maxArr[1]);
            }
            //丢弃小根堆顶元素，取其所在列表下一元素重新构建堆
            if (minArr[1] < nums.get(minArr[0]).size() - 1) {
                int[] newArr = new int[] {minArr[0], minArr[1] + 1};
                minQueue.offer(newArr);
                //因为添加相同对象，可以直接remove
                maxQueue.remove(minArr);
                maxQueue.offer(newArr);
            }
        }
        return ans;
    }
}

