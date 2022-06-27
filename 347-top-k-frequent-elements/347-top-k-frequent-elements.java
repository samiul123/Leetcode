class NumberFrequency {
    private int number;
    private int frequency;

    public NumberFrequency(int number, int frequency) {
        this.number = number;
        this.frequency = frequency;
    }
    
    public int getNumber() {
        return this.number;
    }
    
    public int getFrequency() {
        return this.frequency;
    }

    
    @Override
    public String toString() {
        return number + " " + frequency + "\n";
    }
}

class Solution {
    public void maxHeapify(NumberFrequency[] nums, int index, int heapSize) {
        int leftChildIndex = 2 * index + 1;
        int rightChildIndex = 2 * index + 2;
        int largestValIndex = index;

        if (leftChildIndex < heapSize && leftChildIndex < nums.length && nums[largestValIndex].getFrequency() < nums[leftChildIndex].getFrequency()) {
            largestValIndex = leftChildIndex;
        }
        if (rightChildIndex < heapSize && rightChildIndex < nums.length && nums[largestValIndex].getFrequency() < nums[rightChildIndex].getFrequency()) {
            largestValIndex = rightChildIndex;
        }

        if (largestValIndex != index) {
            NumberFrequency temp = nums[largestValIndex];
            nums[largestValIndex] = nums[index];
            nums[index] = temp;

            maxHeapify(nums, largestValIndex, heapSize);
        }

    }

    public void buildHeap(NumberFrequency[] nums, int heapSize) {
        for (int i = (int) Math.floor(nums.length / 2) - 1; i >= 0; i--) {
            maxHeapify(nums, i, heapSize);
        }
    }

    public NumberFrequency extractMax(NumberFrequency[] frequencies, int heapSize) {
        // if (heapSize < 1) {
        //     return null;
        // }
        NumberFrequency numberWithMaxFrequency = frequencies[0];
        frequencies[0] = frequencies[heapSize-1];
        maxHeapify(frequencies, 0, heapSize);
        return numberWithMaxFrequency;
    }

    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> frequencyMap = new HashMap<>();
        Arrays.stream(nums).forEach(num -> frequencyMap.put(num, frequencyMap.getOrDefault(num, 0)+1));

        NumberFrequency[] frequencies = new NumberFrequency[frequencyMap.size()];

        final int[] i = {0};
        frequencyMap.forEach((num, frequency) -> {
            NumberFrequency numberFrequency = new NumberFrequency(num, frequency);
            frequencies[i[0]] = numberFrequency;
            i[0] += 1;
        });

        buildHeap(frequencies, frequencies.length);

        // Arrays.stream(frequencies).forEach(System.out::println);
        // System.out.println();
        int[] result = new int[k];
        for (int j = 0; j < k; j++) {
            result[j] = extractMax(frequencies, frequencies.length-j).getNumber();
            // Arrays.stream(frequencies).forEach(System.out::println);
            // System.out.println();
        }
        return result;
    }
}