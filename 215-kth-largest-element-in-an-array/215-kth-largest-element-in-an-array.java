class Solution {
    public int findKthLargest(int[] nums, int k) {
        Queue<Integer> heap = new PriorityQueue<>(Comparator.comparingInt(Integer::intValue).reversed());
        
        Arrays.stream(nums).forEach(num -> heap.add(num));
        
        int kThLargest = heap.poll();
        for (int i = 1; i < k; i++) {
            kThLargest = heap.poll();
        }
        
        return kThLargest;
    }
}