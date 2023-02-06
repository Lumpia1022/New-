from tkinter import *

main_screen = Tk()
main_screen.geometry("1024x480")
main_screen.title("Registration")
main_screen.configure(bg="Light Blue")


label1 = Label(main_screen, text="Registration For New Tenants", height="2",width="64" , bg="Teal", font=("Calibri", 24)).pack()

btnreg = Button(text="Register", height="3", width="30", bg="Teal").place(x=700,y=400)

label2 = Label(main_screen, text="First Name", font=("Calibri"), bg="Light Blue").place(x=1,y=125)
t_name = Entry(main_screen, width="30").place(x=100,y=125)

label3 = Label(main_screen, text="Middle Name", font=("Calibri"), bg="Light Blue").place(x=1,y=200)
t_mname = Entry(main_screen, width="30").place(x=100,y=200)

label4 = Label(main_screen, text="Last Name", font=("Calibri"), bg="Light Blue").place(x=1,y=275)
t_lname = Entry(main_screen, width="30").place(x=100,y=275)

label5 = Label(main_screen, text="Floor", font=("Calibri"), bg="Light Blue").place(x=1,y=350)
t_floor = Entry(main_screen, width="30").place(x=100,y=350)


main_screen.mainloop()