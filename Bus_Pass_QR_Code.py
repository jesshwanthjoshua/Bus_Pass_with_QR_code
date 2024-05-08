import qrcode

print("QR Code for Bus Pass")
student_details = {}
student_regno = input("Student Reg. No: ")
student_details['Student Reg. No'] = student_regno
student_name = input("Name of the Student: ")
student_details['Name'] = student_name
college_name = input("Name of the College: ")
student_details['College Name'] = college_name
town_bus_stop = input("Student Bus Stop: ")
student_details['Town Bus Stop'] = town_bus_stop
college_bus_stop = input("College Bus Stop: ")
student_details['College Bus Stop'] = college_bus_stop

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=5,
    border=1,
)
for k,v in student_details.items():
    v = student_details[k]
    a = k +" : "+ v
    print(a)
    qr.add_data(a+" \n")

qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
img.save("Bus_Pass.png")
 
