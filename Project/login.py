from tkinter import *

main_screen = Tk()
main_screen.geometry("1024x480")
main_screen.title("Login")
main_screen.configure(bg="Light Blue")






label1 = Label(main_screen, text="Tenant Login", bg="Teal", height="2",width="64" , font=("Calibri", 24)).pack()

btnlogin = Button(text="Login", height="3", width="30", bg="Teal").place(x=700,y=400)

label2 = Label(main_screen, text="Name", font=("Calibri"), bg="Light Blue").place(x=790,y=300)
t_name = Entry(main_screen, width="30").place(x=720,y=320)

label3 = Label(main_screen, text="Serial No.",font=("Calibri"), bg="Light Blue").place(x=784,y=340)
t_snum = Entry(main_screen, width="30").place(x=720,y=359)

main_screen.mainloop()    