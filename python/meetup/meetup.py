from calendar import Calendar, day_name
from datetime import date


class MeetupDayException(Exception):
    pass


def meetup(year, month, week, day_of_week):

    day_index = list(day_name).index(day_of_week)
    month_days = [
        month_week[day_index]
        for month_week in Calendar().monthdayscalendar(year, month)
        if month_week[day_index] != 0
    ]

    if week == 'last':
        day = month_days[-1]
    elif week == 'teenth':
        day = next(day for day in month_days if day > 12)
    else:
        try:
            nth_week = ["1st", "2nd", "3rd", "4th", "5th"]
            day = month_days[nth_week.index(week)]
        except IndexError:
            raise MeetupDayException("%d/%d do not have %s week!" % (month, year, week))

    return date(year, month, day)
