full_name = input("What is your name? ")
credit_1 = int(input("Enter the credit for Python : "))
credit_2 = int(input("Enter the credit for C# : "))
credit_3 = int(input("Enter the credit for Networking : "))
point_1 = float(input("Enter the point for Python: "))
point_2 = float(input("Enter the point for C# : "))
point_3 = float(input("Enter the point for Networking : "))

credits = [credit_1, credit_2, credit_3]
points = [point_1, point_2, point_3]
def calculate_gpa(credits, points):
    sum = 0
    sum_credits = 0
    for i in range(len(points)):
        sum += credits[i] * points[i]
        sum_credits += credits[i]
    gpa = sum / sum_credits
    return gpa
gpa = calculate_gpa(credits, points)
def show_student_gpa(name, gpa):
    print("Student:", name)
    print("GPA:", gpa)
    try:
        file = open('data/points.txt', 'w')
        file.write("Name student: " + name + "\n"  " GPA: " + str(gpa))
        file.close()
    except:
        print("An error file open.")
show_student_gpa(full_name, gpa)
