from attendance.student import Student
from attendance.attendance import Attendance

if __name__ == "__main__":
    students = [Student("Rohan", "Omkar"), Student("Bapu", "Omkar"), Student("Dilip", "Omkar"),
                Student("Shubham", "Omkar")]
    # creating attendance object
    take_attendance = True
    while take_attendance:
        aobj1 = Attendance(input("Today's date: "), students)
        aobj1.mark_attendace()
        Attendance.attendance_by_date.append(aobj1)
        try:
            if int(input("Do you want to take attendance for any other date then press 1 else 0: ")) == 1:
                take_attendance = True
            else:
                take_attendance = False

        except:
            take_attendance = False
