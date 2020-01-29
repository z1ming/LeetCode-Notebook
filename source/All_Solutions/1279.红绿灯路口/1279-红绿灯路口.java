class TrafficLight {
    private AtomicBoolean occupied = new AtomicBoolean(false);

    private volatile boolean roadAAllowed = true;
    private AtomicInteger roadACardCount = new AtomicInteger(0);

    private volatile boolean roadBAllowed = false;
    private AtomicInteger roadBCardCount = new AtomicInteger(0);
    
    public TrafficLight() {   
    }
    
    public void carArrived(
        int carId,           // ID of the car
        int roadId,          // ID of the road the car travels on. Can be 1 (road A) or 2 (road B)
        int direction,       // Direction of the car
        Runnable turnGreen,  // Use turnGreen.run() to turn light to green on current road
        Runnable crossCar    // Use crossCar.run() to make car cross the intersection 
    ) {
        if (roadId == 1 && tryOccupyRoadA(turnGreen)) {
            this.roadACardCount.incrementAndGet();
            crossCar.run();
            releaseRoadAIfNecessary();
        } else if (roadId == 2 && tryOccupyRoadB(turnGreen)) {
            this.roadBCardCount.incrementAndGet();
            crossCar.run();
            releaseRoadBIfNecessary();
        }
    }

    private boolean tryOccupyRoadA(Runnable turnGreen) {
        while (!this.roadAAllowed) {
            if (this.occupied.compareAndSet(false, true)) {
                turnGreen.run();
                this.roadAAllowed = true;
                this.roadBAllowed = false;
            } else {
                LockSupport.parkNanos(1L);
            }
        }

        return true;
    }

    private boolean tryOccupyRoadB(Runnable turnGreen) {
        while (!this.roadBAllowed) {
            if (this.occupied.compareAndSet(false, true)) {
                turnGreen.run();
                this.roadAAllowed = false;
                this.roadBAllowed = true;
            } else {
                LockSupport.parkNanos(1L);
            }
        }

        return true;
    }

    private void releaseRoadAIfNecessary() {
        if (this.roadACardCount.decrementAndGet() == 0) {
            this.occupied.set(false);
        }
    } 

    private void releaseRoadBIfNecessary() {
       if (this.roadBCardCount.decrementAndGet() == 0) {
            this.occupied.set(false);
        } 
    }
}