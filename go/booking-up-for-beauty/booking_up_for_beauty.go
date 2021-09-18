package booking

import "time"

const (
	scheduleTimeFormat    = "1/2/2006 15:04:05"
	hasPassedTimeFormat   = "January 2, 2006 15:04:05"
	isAfternoonTimeFormat = "Monday, January 2, 2006 15:04:05"
	anniversaryTimeFormat = "2006-01-02"
)

// Schedule returns a time.Time from a string containing a date
func Schedule(date string) time.Time {
	dateTime, err := time.Parse(scheduleTimeFormat, date)
	if err != nil {
		panic("Error formating time")
	}
	return dateTime
}

// HasPassed returns whether a date has passed
func HasPassed(date string) bool {
	dateTime, err := time.Parse(hasPassedTimeFormat, date)
	if err != nil {
		panic("Error formating time")
	}
	return dateTime.Before(time.Now())
}

// IsAfternoonAppointment returns whether a time is in the afternoon
func IsAfternoonAppointment(date string) bool {
	dateTime, err := time.Parse(isAfternoonTimeFormat, date)
	if err != nil {
		panic("Error formating time")
	}
	hour := dateTime.Hour()
	return hour >= 12 && hour < 18
}

// Description returns a formatted string of the appointment time
func Description(date string) string {
	dateTime := Schedule(date)
	return dateTime.Format(
		"You have an appointment on Monday, January 2, 2006, at 15:04.",
	)
}

// AnniversaryDate returns a Time with this year's anniversary
func AnniversaryDate() time.Time {
	dateTime, err := time.Parse(anniversaryTimeFormat, "2021-09-15")
	if err != nil {
		panic("Error formating time")
	}
	return dateTime
}
