package isogram

import "strings"

func IsIsogram(text string) bool {
	var saves = []rune("")
	parsedText := strings.ToLower(text)
	parsedText = strings.ReplaceAll(parsedText, "-", "")
	parsedText = strings.ReplaceAll(parsedText, " ", "")

	for _, char := range []rune(parsedText) {
		for _, cache := range saves {
			if char == cache {
				return false
			}
		}
		saves = append(saves, char)
	}
	return true
}
