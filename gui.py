from tkinter import *
import cv2
r=Tk()
r.config(bg='Lightcyan3')
r.geometry('1000x500+0+0')
def a1():
    r.destroy()
    import livedetection
    cv2.waitKey(0)
    cv2.destroyAllWindows()
def a2():
    r.destroy()
    import takeimages
    cv2.waitKey(0)
    cv2.destroyAllWindows()
def a3():
    r.destroy()
    import imagetest
    cv2.waitKey(0)
    cv2.destroyAllWindows()
def a4():
    r.destroy()
    import create_your_own_training_model

l=Label(text="Face Recognition System",bg='Lightcyan3',fg='gray10',font=('segoe print',20,'bold'))
l.pack()
b=Button(text="Start",command=a1,bg='Lightcyan3',fg='gray10',font=('segoe print',10,'bold'),width=10)
b.place(x=580,y=370)
c=Button(text="Take Images",command=a2,bg='Lightcyan3',fg='gray10',font=('segoe print',10,'bold'),width=10)
c.place(x=305,y=370)
d=Button(text="Start Image Test",command=a3,bg='Lightcyan3',fg='gray10',font=('segoe print',10,'bold'),width=20)
d.place(x=405,y=370)
e=Button(text="Update Data Set",command=a4,bg='Lightcyan3',fg='gray10',font=('segoe print',10,'bold'),width=20)
e.place(x=405,y=450)
r.mainloop()
