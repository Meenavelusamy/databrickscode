def check_grade(marks):
    # Determine the performance category based on the marks
    if marks >= 90:
        return "Outstanding"
    elif marks >= 75:
        return "Excellent"
    elif marks >= 50:
        return "Pass"
    else:
        return "Fail"
student_marks = 82
result = check_grade(student_marks)
print(f"Marks: {student_marks} --> Category: {result}")

company1='inceptez'
company2="inceptez"
company3="""inceptez"""
print(company1,company2,company3)

name='inceptez'
print(name[0]) #print i
print(name[1])
print(name[2])
print(name[3])
#print n
active_flag=True
print(active_flag)
print(type(active_flag))
active_flag=False
print(active_flag)
print(type(active_flag))