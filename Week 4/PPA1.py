# Note this prefix code is to verify that you are not using any for loops in this exercise. This won't affect any other functionality of the program.
with open(__file__) as f:
    content = f.read().split("# <nofor>")[2]
if "for " in content:
    print("You should not use for loop or the word for anywhere in this exercise")

# Sample inputs (# note: The values given in the prefix code will be changed by the autograder according to the testcase while running them.)
marks = [80, 75, 90, 75, 60]
subjects = ("math", "science", "english", "history")
new_marks = (95, 88)
search_subject = "science"
extra_subjects = {"art", "math", "music"}

# <nofor>
# <eoi>

# Use list, tuple, and set operations only.
# Use built-in functions like len, sum, min, max, and sorted where useful.
# Convert to a set when you need unique values.
# Convert to a list when you need to concatenate with a list.

number_of_marks = len(marks) # int: number of values in marks
highest_mark = max(marks) # int: highest value in marks
lowest_mark = min(marks) # int: lowest value in marks
total_marks = sum(marks) # int: sum of all values in marks
unique_marks_sorted = sorted(set(marks)) # list: unique marks in ascending order
first_two_subjects = subjects[:2] # tuple: first two subjects
last_subject = subjects[-1] # str: last subject in subjects
is_search_subject_present = search_subject in subjects # bool: check whether search_subject is in subjects
all_marks = marks + list(new_marks) # list: marks followed by values from new_marks
all_subjects_sorted = sorted(set(subjects) | extra_subjects) # list: all unique subjects in ascending 