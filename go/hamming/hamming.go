package hamming

import "errors"

// Distance calculate the similarities between two DNA strands.
// Return error on different length
func Distance(a, b string) (int, error) {
	strandA, strandB := []rune(a), []rune(b)
	if len([]byte(a)) != len([]byte(b)) {
		return 0, errors.New("strands are not the same length")
	}
	hammingDistance := 0
	for i := range strandA {
		if strandA[i] != strandB[i] {
			hammingDistance++
		}
	}
	return hammingDistance, nil
}
