def get_letter_grade(score):
    if score >= 90: return "A"
    elif score >= 80 and score < 90: return "B"
    elif score >= 70 and score < 80: return "C"
    elif score >= 60 and score < 70: return "D"
    else: return "F"
		        
def get_class_average(students):
    class_avg = 0.0
    class_avg += get_average(students)
    return average(class_avg)

def average(l):
    return sum(l) / len(l)

lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}

alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}

tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

students = [lloyd, alice, tyler]

# Add your function below!
def average(grades):
    return (sum(grades))/len(grades)

def get_average(students):
    return (average(students['homework']) * .10 + average(students['quizzes']) * .30 + average(students['tests']) * .60)

def get_class_average(students):
    total = 0.0
    for name in students:
        total += get_average(name)
    return float(total) / len(students)

print get_letter_grade(get_class_average(students)) 
print str(get_class_average(students))
