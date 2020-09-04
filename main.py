# Author: Krish Choudhary ksc5496@psu.edu
course1grade = input("Enter your course 1 letter grade: ")
course1credit = input("Enter your course 1 credit: ")
course1credit = int(course1credit)
if course1grade == "A":
  gradepoint1 = 4.0
  print("Grade point for course 1 is: 4.0")
elif course1grade == "A-":
  gradepoint1 = 3.67
  print("Grade point for course 1 is: 3.67")
elif course1grade == "B+":
  gradepoint1 = 3.33
  print("Grade point for course 1 is: 3.33")
elif course1grade == "B":
  gradepoint1 = 3.0
  print("Grade point for course 1 is: 3.0")
elif course1grade == "B-":
  gradepoint1 = 2.67
  print("Grade point for course 1 is: 2.67")
elif course1grade == "C+":
  gradepoint1 = 2.33
  print("Grade point for course 1 is: 2.33")
elif course1grade == "C":
  gradepoint1 = 2.0
  print("Grade point for course 1 is: 2.0")
elif course1grade == "D":
  gradepoint1 = 1.0
  print("Grade point for course 1 is: 1.0")
else:
  gradepoint1 = 0.0
  print("Grade point for course 1 is: 0.0")

course2grade = input("Enter your course 2 letter grade: ")
course2credit = input("Enter your course 2 credit: ")
course2credit = int(course2credit)
if course2grade == "A":
  gradepoint2 = 4.0
  print("Grade point for course 2 is: 4.0")
elif course2grade == "A-":
  gradepoint2 = 3.67
  print("Grade point for course 2 is: 3.67")
elif course2grade == "B+":
  gradepoint2 = 3.33
  print("Grade point for course 2 is: 3.33")
elif course2grade == "B":
  gradepoint2 = 3.0
  print("Grade point for course 2 is: 3.0")
elif course2grade == "B-":
  gradepoint2 = 2.67
  print("Grade point for course 2 is: 2.67")
elif course2grade == "C+":
  gradepoint2 = 2.33
  print("Grade point for course 2 is: 2.33")
elif course2grade == "C":
  gradepoint2 = 2.0
  print("Grade point for course 2 is: 2.0")
elif course2grade == "D":
  gradepoint2 = 1.0
  print("Grade point for course 2 is: 1.0")
else:
  gradepoint2 = 0.0
  print("Grade point for course 2 is: 0.0")

course3grade = input("Enter your course 3 letter grade: ")
course3credit = input("Enter your course 3 credit: ")
course3credit = int(course3credit)
if course3grade == "A":
  gradepoint3 = 4.0
  print("Grade point for course 3 is: 4.0")
elif course3grade == "A-":
  gradepoint3 = 3.67
  print("Grade point for course 3 is: 3.67")
elif course3grade == "B+":
  gradepoint3 = 3.33
  print("Grade point for course 3 is: 3.33")
elif course3grade == "B":
  gradepoint3 = 3.0
  print("Grade point for course 3 is: 3.0")
elif course3grade == "B-":
  gradepoint3 = 2.67
  print("Grade point for course 3 is: 2.67")
elif course3grade == "C+":
  gradepoint3 = 2.33
  print("Grade point for course 3 is: 2.33")
elif course3grade == "C":
  gradepoint3 = 2.0
  print("Grade point for course 3 is: 2.0")
elif course3grade == "D":
  gradepoint3 = 1.0
  print("Grade point for course 3 is: 1.0")
else:
  gradepoint3 = 0.0
  print("Grade point for course 3 is: 0.0")

gpa = (gradepoint1 * course1credit + gradepoint2 * course2credit + gradepoint3 * course3credit) / (course1credit + course2credit + course3credit) 
gpa = float(gpa)
print("Your GPA is: " + str(gpa))

