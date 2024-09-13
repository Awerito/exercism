package letter

// FreqMap records the frequency of each rune in a given text.
type FreqMap map[rune]int

// Frequency counts the frequency of each rune in a given text and returns this
// data as a FreqMap.
func Frequency(s string) FreqMap {
	m := FreqMap{}
	for _, r := range s {
		m[r]++
	}
	return m
}

func ConcurrentFrequency(strs []string) FreqMap {
	output := make(chan FreqMap)
	defer close(output)

	for _, str := range strs {
		go func(s string) {
			output <- Frequency(s)
		}(str)
	}

	sumFreq := FreqMap{}
	for _ = range strs {
		freqmap := <-output
		for letter, freq := range freqmap {
			sumFreq[letter] += freq
		}
	}

	return sumFreq
}
