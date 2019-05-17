"""
Using username_generator from
https://github.com/awesmubarak/username_generator_cli

Creating random usernames with 1 to 15
characters and using underscores randomly

Created by Kevin Sattakun
"""

import csv
import random

import username_generator

screennames = []
count = 0
minimum_char = 1
maximum_char = 15

for x in range(800000):
    bool_underscore = bool(random.getrandbits(1))
    name = username_generator.get_uname(minimum_char, maximum_char, bool_underscore)
    screennames.append(name)

with open('screennames.txt', "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    for screenname in screennames:
        writer.writerow([screenname])
