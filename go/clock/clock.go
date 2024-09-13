package clock

import (
	"fmt"
)

const timeInADay = 24 * 60

type Clock struct{ minute int }

func New(hour, minute int) Clock {
	minutes := (hour*60 + minute) % timeInADay
	if minutes < 0 {
		minutes += timeInADay
	}

	return Clock{minutes}
}

func (c Clock) String() string {
	return fmt.Sprintf("%02d:%02d", c.minute/60, c.minute%60)
}

func (c Clock) Add(minute int) Clock {
	return New(0, c.minute+minute)
}

func (c Clock) Subtract(minute int) Clock {
	return New(0, c.minute-minute)
}
