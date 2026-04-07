# Read student details
name = input("Enter student name: ")
dob = input("Enter Date of Birth (DD/MM/YYYY): ")
reg_no = input("Enter Register Number: ")
department = input("Enter Department: ")

# Read marks for 5 subjects
m1 = float(input("Enter marks for subject 1: "))
m2 = float(input("Enter marks for subject 2: "))
m3 = float(input("Enter marks for subject 3: "))
m4 = float(input("Enter marks for subject 4: "))
m5 = float(input("Enter marks for subject 5: "))

# Calculate total and percentage
total = m1 + m2 + m3 + m4 + m5
percentage = total / 5

# Display student details
print("\n----- STUDENT DETAILS -----")
print("Name:", name)
print("DOB:", dob)
print("Register Number:", reg_no)
print("Department:", department)

# Display marks
print("\nMarks:")
print("Subject 1:", m1)
print("Subject 2:", m2)
print("Subject 3:", m3)
print("Subject 4:", m4)
print("Subject 5:", m5)

print("\nTotal Marks:", total)
print("Percentage:", percentage)

# Display result
print("\n----- RESULT -----")
if percentage >= 90:
    print("Excellent Performance ")
elif percentage >= 75:
    print("Very Good ")
elif percentage >= 50:
    print("Pass ")
else:
    print("Fail ")