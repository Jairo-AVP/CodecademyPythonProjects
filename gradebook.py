"""
Gradebook
You are a student and you are trying to organize your subjects and grades using Python. Let’s explore what we’ve learned about lists to 
organize your subjects and scores.
"""

last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Your code below: 

### Create some lists
subjects = ["physics", "calculus", "poetry", "history"]
grades = [98, 97, 85, 88]

gradebook = [["physics", 98], ["calculus", 97], ["poetry", 85], ["history", 88]]

### Add more subjects
gradebook.append(["computer science", 100])
gradebook.append(["visual arts", 93])

### Modify the gradebook
gradebook[-1][-1] += 5
gradebook[2].remove(85)
# print(gradebook)
gradebook[2].append("Pass")

# print(gradebook)
print()

### Joing both lists
full_gradebook = last_semester_gradebook + gradebook
print("- Current Gradebook", gradebook)
print()
print("- Full Gradebook", full_gradebook)