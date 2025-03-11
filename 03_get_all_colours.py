import csv
import random

def round_ans(val):
    """
    Rounds numbers to nearest integer
    :param val: number to be rounded.
    :return: Rounded number (an integer)
    """
    var_rounded = (val * 2 + 2) // 2
    raw_unrounded = "{:.0f}".format(var_rounded)
    return int(raw_unrounded)

# retrieve colours from csv anf put them in a list
file = open("colour_quest/00_colour_list_hex_v3.csv", "r")
all_colours = list(csv.reader(file, delimiter=","))
file.close()


# remove the first row
all_colours.pop(0)

round_colours = []
colour_scores = []

# loop until we have four colours with different scores
while len(round_colours) < 4:
    potential_colour = random.choice(all_colours)

    # get the score and check its not a duplicate
    if potential_colour[1] not in colour_scores:
        round_colours.append(potential_colour)
        colour_scores.append(potential_colour[1])

print(round_colours)
print(colour_scores)

#  find target scores

# change score to integers
int_scores = [int(x) for x in colour_scores]
print("Scores Unsorted", int_scores)
int_scores.sort()
print("Sorted Scores", int_scores)

median = (int_scores[1] + int_scores[2]) / 2
print(f"unrounded median: {median}")
print(f"median: {median:.0f}")