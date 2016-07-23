#!/usr/bin/env python3

# example of multidimensional list

my_course = [["Buny",90,87,95],["Duck", 78,96,89],["Rubb", 83,85,92]]

for student_data in my_course:
    total_grade=0
    for grade_index in range(1,len(student_data)) :
        total_grade = total_grade + student_data[grade_index]
    print("The average for ", student_data[0], "is ", total_grade/3.0)
