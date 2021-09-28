// Package twofer function
package twofer

import "fmt"

// ShareWith gives the message "One for <name>, one for me."
// "One for you, one for me." if name is an empty string
func ShareWith(name string) string {
	if name == "" {
		name = "you"
	}
	return fmt.Sprintf("One for %s, one for me.", name)
}
