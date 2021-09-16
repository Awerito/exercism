// Package for weather forecasting management
package weather

var (
	// Saves the current condition given by the user
	CurrentCondition string
	// Saves the current location given by the user
	CurrentLocation string
)

// Log the weather condition for the given location
func Log(city, condition string) string {
	CurrentLocation, CurrentCondition = city, condition
	return CurrentLocation + " - current weather condition: " + CurrentCondition
}
