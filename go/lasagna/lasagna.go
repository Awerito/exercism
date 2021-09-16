package lasagna

func OvenTime() int {
    return 40
}

func RemainingOvenTime(time int) int {
    return OvenTime() - time
}

func PreparationTime(layers int) int {
    return 2 * layers
}

func ElapsedTime(layers int, time int) int {
    return PreparationTime(layers) + time
}
