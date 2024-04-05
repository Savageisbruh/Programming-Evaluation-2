# Asking user for course grade
Course1 = int(input("Enter the marks of the first course: "))
Course2 = int(input("Enter the marks of the second course: "))
Crouse3 = int(input("Enter the marks of the third course: "))
Crouse4 = int(input("Enter the marks of the fourth course: "))

# Calculating the average
Average = (Course1 + Course2 + Crouse3 + Crouse4) / 4

letter_grade = ""

# Determining the letter grade
if Average >= 95:
  letter_grade = "A+"
elif Average >= 87:
  letter_grade = "A"
elif Average >= 80:
  letter_grade = "A-"
elif Average >= 77:
   letter_grade = "B+"
elif Average >= 72:
  leter_grade = "B"
elif Average >= 70:
  letter_grade = "B-"
elif Average >= 67:
  letter_grade = "C+"
elif Average >= 63:
  letter_grade = "C"
elif Average >= 60:
  letter_grade = "C-"
elif Average >= 57:
  letter_grade = "D+"
elif Average >= 54:
  letter_grade = "D"
elif Average >= 50:
  letter_grade = "D-"
elif Average >= 0:
  letter_grade = "F"

# Printing the average and letter grade
print("The average is " + str(Average) + "%" " This is considered " ,letter_grade)

