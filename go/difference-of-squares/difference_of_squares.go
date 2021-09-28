package diffsquares

func SquareOfSum(n int) int {
	if n < 1 {
		return 0
	}
	return n * n * (n + 1) * (n + 1) / 4
}

func SumOfSquares(n int) int {
	if n < 1 {
		return 0
	}
	return n * (2*n + 1) * (n + 1) / 6
}

func Difference(n int) int {
	if n < 1 {
		return 0
	}
	return SquareOfSum(n) - SumOfSquares(n)
}
