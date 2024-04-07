# Use: paste a block of text that has timestamps in the form of 
# (min:sec) and this script will make a total of the time.
# This is particularly useful to me for determining watch time
# left for Professor Messer's cert videos

import re

def extract_time_stamps(file_path):
    # Regular expression pattern to match text in the form (x:y)
    pattern = r'\((\d+:\d+)\)'

    with open(file_path, 'r') as file:
        text = file.read()

    # Use findall to extract all matches of the pattern
    time_stamps = re.findall(pattern, text)
    return time_stamps


file_path = 'input.txt' 
time_stamps = extract_time_stamps(file_path)

def split_strings_to_array(strings):
    result = []
    for string in strings:
        x, y = map(int, string.split(':'))
        result.append([x, y])
    return result

split_time_stamps = split_strings_to_array(time_stamps)

hours = 0
minutes = 0
seconds = 0

for min, sec in split_time_stamps:
    seconds += sec
    minutes += min

    if seconds >= 60:
        minutes += 1
        seconds -= 60
    
    if minutes >= 60:
        hours += 1
        minutes -= 60

print("Total time:", hours, "hours", minutes, "minutes", seconds, "seconds")

