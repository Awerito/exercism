package logs

import (
	"fmt"
	"regexp"
	"strings"
)

// Message extracts the message from the provided log line.
func Message(line string) string {
	regex := regexp.MustCompile(`.*?:\s+(.*)`)
	msg := regex.ReplaceAllString(line, "$1")
	return strings.TrimSpace(msg)
}

// MessageLen counts the amount of characters (runes) in the message of the log line.
func MessageLen(line string) int {
	return len([]rune(Message(line)))
}

// LogLevel extracts the log level string from the provided log line.
func LogLevel(line string) string {
	regex := regexp.MustCompile(`\[(.*?)\].*`)
	msg := regex.ReplaceAllString(line, "$1")
	msg = strings.TrimSpace(msg)
	return strings.ToLower(msg)
}

// Reformat reformats the log line in the format `message (logLevel)`.
func Reformat(line string) string {
	return fmt.Sprintf("%s (%s)", Message(line), LogLevel(line))
}
