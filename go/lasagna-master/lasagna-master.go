package lasagna

// PreparationTime takes the layers and estimates the preparation time
func PreparationTime(layers []string, timePerLayer int) int {
	layersLength := len(layers)
	if timePerLayer == 0 {
		return 2 * layersLength
	}
	return timePerLayer * layersLength
}

// Quantities estimates the amount of ingredient you need for the given layers
func Quantities(layers []string) (int, float64) {
	var noodles, sauce int
	for _, ingredient := range layers {
		if ingredient == "sauce" {
			sauce++
		}
		if ingredient == "noodles" {
			noodles++
		}
	}
	return noodles * 50, float64(sauce) * 0.2
}

// AddSecretIngredient adds the newIngredients to oldIngredients if the aren't
// in oldIngredients
func AddSecretIngredient(newIngredients, oldIngredients []string) []string {
	return append(
		oldIngredients,
		newIngredients[len(newIngredients)-1],
	)
}

// ScaleRecipe scales the recipe quantities by the given portions
func ScaleRecipe(quantities []float64, portions int) []float64 {
	var scales []float64
	quantity := float64(portions) / 2.0
	for _, val := range quantities {
		scales = append(scales, val*quantity)
	}
	return scales
}
