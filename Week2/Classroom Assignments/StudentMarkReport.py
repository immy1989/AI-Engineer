marks = [78, 85, 62, 90, 55, 88]

highMark = max(marks)
lowMark = min(marks)
totalMark = sum(marks)
avgMark = totalMark/len(marks)

print(f"Highest Mark: {highMark}")
print(f"Lowest Mark: {lowMark}")
print(f"Average Mark: {avgMark}")

marks.append(95)
print(marks)
marks.pop(6)
print(marks)
marks.sort()
print(f"Sorted marks: {marks}")

for mark in marks:
    if mark > 75:
        print(f"Distinction Marks: {mark}")