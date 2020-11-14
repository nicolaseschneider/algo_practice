Imagine we live in the future and all cars have full self-driving capabilities. A standard has been adopted so that every car has a uniform API for interacting with 3rd party software. You are tasked with designing the software for an automated parking lot that will take advantage of the standard car API in order to allow cars to enter, park and exit the parking lot autonomously. Essentially, the passengers will exit the car at the parking-lot entrance and the car will park by itself. When the passengers return the car will automatically exit the lot to a loading area to pick up the passengers.


# drive a -> b 
# park
# distance from key

ParkingSpace
    id -> uuid
    latitude -> float
    longitude -> float
    occupied -> bool

Parked_Car
    id -> uuid
    car_id -> uuid
    parkingSpaceId -> uuid ref: ParkingSpace
    parked -> bool default: true
    createdAt -> datetime -when car was parked
    updatedAt -> datetime -when car left
    
SELECT id FROM parking_space WHERE occupied = False

drive car to parkingSpace
Create parked car record
parkingspace occupied = True
