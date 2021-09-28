package raindrops

import "strconv"

// Factors map of factors and string
var Factors = map[int]string{
	3: "Pling",
	5: "Plang",
	7: "Plong",
}

// Convert construct a string out of factors of the given number
// and returns it.
func Convert(number int) (factors string) {
	// range the Factors map couse inconsistency
	for _, factor := range []int{3, 5, 7} {
		if number%factor == 0 {
			factors += Factors[factor]
		}
	}

	if factors == "" {
		factors = strconv.Itoa(number)
	}
	return
}
