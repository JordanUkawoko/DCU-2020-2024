#!/usr/bin/env python3

import datetime
import calendar


def findDay(date):
    born = datetime.datetime.strptime(date, '%d %m %Y').weekday()
    return (calendar.day_name[born])


lines = {"Monday": "and Monday's child is fair of face.",
         "Tuesday": "and Tuesday's child is full of grace.",
         "Wednesday": "and Wednesday's child is full of woe.",
         "Thursday": "and Thursday's child has far to go.",
         "Friday": "and Friday's child is loving and giving.",
         "Saturday": "and Saturdays child works hard for a living.",
         "Sunday": "and Sunday's child is fair and wise and good in every way."

         }


date = '18 6 2003'
day = findDay(date)
print("You were born on a " + day + " " + lines[day])



