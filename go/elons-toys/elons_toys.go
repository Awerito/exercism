package elon

import "fmt"

// Car implements a remote controlled car.
type Car struct {
	speed, batteryDrain, battery, distance int
}

// Track implements a race track.
type Track struct {
	distance int
}

// CreateCar creates a new car with given specifications.
func CreateCar(speed, batteryDrain int) *Car {
	return &Car{speed, batteryDrain, 100, 0}
}

// CreateTrack creates a new track with given distance.
func CreateTrack(distance int) Track {
	return Track{distance}
}

// Drive drives the car one time.
func (car *Car) Drive() {
	batLeft := car.battery - car.batteryDrain
	if batLeft <= 0 {
		return
	}
	car.battery = batLeft
	car.distance += car.speed
	return
}

// CanFinish checks if a car is able to finish a certain track.
func (car *Car) CanFinish(track Track) bool {
	drives := int(car.battery/car.batteryDrain)*car.speed + car.distance
	return drives >= track.distance
}

// DisplayDistance displays the distance the car is driven.
func (car *Car) DisplayDistance() string {
	return fmt.Sprintf("Driven %v meters", car.distance)
}

// DisplayBattery displays the battery level.
func (car *Car) DisplayBattery() string {
	return fmt.Sprintf("Battery at %v%%", car.battery)
}
