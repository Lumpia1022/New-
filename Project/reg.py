from tkinter import *
import tkinter as tk

main_screen = Tk()
main_screen.geometry("1024x480")
main_screen.title("Registration")
main_screen.resizable(False, False)
main_screen.configure(bg="Light Blue")


#done ko na is mag ayos ng spacings sa ibang labels, inayoss ko ng onti yung button, then placements ng onti -Dondon Pogi


label2 = Label(main_screen, text="First Name", font=("Verdana"), bg="Light Blue").place(x=1,y=125)
t_name = Entry(main_screen, width="30")
t_name.place(x=113,y=125, height="25")


#ADJUST YUNGG SPACING NG MIDDLE NAME AT YUNG ENTRY BOX  -Dondon Pogi
label3 = Label(main_screen, text="Middle Name", font=("Verdana"), bg="Light Blue").place(x=1,y=200)
t_mname = Entry(main_screen, width="30")
t_mname.place(x=113,y=200, height="25")

label4 = Label(main_screen, text="Last Name", font=("Verdana"), bg="Light Blue").place(x=1,y=275)
t_lname = Entry(main_screen, width="30")
t_lname.place(x=113,y=275, height="25")

label5 = Label(main_screen, text="Floor", font=("Verdana"), bg="Light Blue").place(x=1,y=350)
t_floor = Entry(main_screen, width="30").place(x=113,y=350, height="25")


#wag mo muna tangfgalin tatapusin ko pa yan -IAN
#List = ("1st Floor", "2nd Floor", "3rd Floor", "4th Floor")
#cv = StringVar()

#goods na to ahahahha IAN
def display():
    fname = t_name.get()
    mnane = t_mname.get()
    lname = t_lname.get()

    greet = "Welcome " + fname + "\n" + lname
    l1 = Label(main_screen, text=greet,bg="Light Blue", font=("Verdana", 17, 'bold')).place(x=700, y=200)

label1 = Label(main_screen, text="Registration For New Tenants", height="2",width="64" , bg="Teal", font=("Verdana", 24, 'bold')).pack()
btnreg = Button(text="Register", height="2", width="20", bg="Teal", font=("Verdana", 15, 'bold'), command=display).place(x=700,y=400)


main_screen.mainloop()