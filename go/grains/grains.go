package grains

import "errors"

const TotalGrains uint64 = 2<<63 - 1

// Square calculate the amount of grains in the n-th chessboard square
// by calculating the 2 ^ (n - 1) on a right shift bit operation
func Square(number int) (uint64, error) {
	if number < 1 || number > 64 {
		return 0, errors.New("Invalid input")
	}
	if number == 1 {
		return 1, nil
	}
	return 2 << (number - 2), nil
}

// Total gives the total amount of grains in the chessboard by the s = 2^64 - 1
// https://en.wikipedia.org/wiki/Wheat_and_chessboard_problem#Solutions
func Total() uint64 {
	return TotalGrains
}
