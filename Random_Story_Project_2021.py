#!/usr/bin/env python3

import random

when = ['A few years ago', 'Back in 1990', 'Last night', 'A long, long time ago']
who = ['a boy', 'a wizard', 'a girl', 'a witch']
name = ['Liam', 'Mary', 'Hank', 'Shawn']
residence = ['Barcelona', 'Germany', 'Ireland', 'Canada']
went = ['nether', 'college', 'mcdonalds', 'gamestop']
happened = ['made a lot of friends', 'bought a new game', 'solved a puzzle', 'failed their exam']

print( random.choice(when) + ', ' + random.choice(who) + ' that lived in ' + random.choice(residence) + ', went to the ' + random.choice(went) + ' and ' + random.choice(happened))
