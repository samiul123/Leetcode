class Point {
    private final int[] point;
    private final double distanceFromOrigin;

    Point(int[] point, double distanceFromOrigin) {
        this.point = point;
        this.distanceFromOrigin = distanceFromOrigin;
    }

    public double getDistanceFromOrigin() {
        return distanceFromOrigin;
    }


    public int[] getPoint() {
        return point;
    }
}

class Solution {
    public int[][] kClosest(int[][] points, int k) {
        Queue<Point> heap = new PriorityQueue<>(Comparator.comparingDouble(Point::getDistanceFromOrigin));

        Arrays.stream(points).forEach(point -> {
            double distance = Math.sqrt(Math.pow(point[0], 2) + Math.pow(point[1], 2));
            heap.add(new Point(point, distance));
        });
        
        int[][] result = new int[k][2];
        for (int i = 0; i < k; i++) {
            result[i] = heap.poll().getPoint();
        }
        return result;
    }
}