package luhn

import (
	"regexp"
	"strings"
)

func Valid(cardNumber string) bool {
	parsedCardNumber := strings.ReplaceAll(cardNumber, " ", "")
	if matched, _ := regexp.MatchString(`\D`, parsedCardNumber); matched {
		return false
	}

	length := len([]byte(parsedCardNumber))
	if length < 2 {
		return false
	}
	sum := int(parsedCardNumber[length-1] - '0')

	parity := length % 2
	for i, number := range parsedCardNumber[:length-1] {
		digit := int(number - '0')
		if i%2 == parity {
			digit *= 2
		}
		if digit > 9 {
			digit -= 9
		}
		sum += digit
	}
	return sum%10 == 0
}
