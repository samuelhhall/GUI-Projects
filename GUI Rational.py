#! C:\Python37\python.exe
from tkinter import *
from math import *


master = Tk()

Label(master, text="High Point").grid(row=0, sticky=W)
Label(master, text="Low Point").grid(row=1, sticky=W)
Label(master, text="Hydraulic Length").grid(row=2, sticky=W)
Label(master, text="Total Area").grid(row=3, sticky=W)
Label(master, text="Run Off Coefficient").grid(row=4, sticky=W)
Label(master, text="Storm Year").grid(row=5, sticky=W)
Label(master, text="Results").grid(row=6, column=1)
Label(master, text="Your total time of concentration is ").grid(row=7, column=0)
Label(master, text="Your pipe size is ").grid(row=8, column=0, sticky=W)
Label(master, text="Your rainfall intensity is  ").grid(row=9, column=0, sticky=W)
Label(master, text="Your peak discharge is ").grid(row=10, column=0, sticky=W)

num1 = Entry(master)
num2 = Entry(master)
num3 = Entry(master)
num5 = Entry(master)
num4 = Entry(master)
num0 = Entry(master)

num1.grid(row=0, column=1)
num2.grid(row=1, column=1)
num3.grid(row=2, column=1)
num5.grid(row=3, column=1)
num4.grid(row=4, column=1)
num0.grid(row=5, column=1)


# Q = int(float(e4.get())*I2*int(e3.get()))
# x = int(e0.get())*int(e1.get())


def add():
    if int(num0.get()) == 2:
        # s1 slope for the pipe
        s = (int(float(num1.get())) - int(float(num2.get()))) / int(float(num3.get()))

        # velocity

        V = 16.1345 * s ** .5

        # time of concentration

        tc = (float(.7039*(300**.3917)*(float(num4.get())**-1.1309)*((int(float(num1.get()))-int(float(num2.get()))))/int(float(num3.get()))**-.1985)+(int(float(num3.get()))-300)/(
            120)) / 60
        tc2 = (float(.7039*(int(float(num3.get()))**.3917)*(float(num4.get())**-1.1309)*((int(float(num1.get()))-int(float(num2.get())))/float(num3.get()))**-.1985))

        # rainfall intinsity

        I2 = (float(2.815 * (tc + .282) ** -.899))
        i2 = (float(2.815 * (tc2 + .282) ** -.899))

        # peak discharge

        Q = float(num4.get())*I2*float(num5.get())

        q = float(num4.get())*i2*float(num5.get())

        # pipe size < 300

        pd = 12 * ((q) / (3.14 * V)) ** .5

        # pipe size > 300

        PD = 12 * ((Q) / (3.14 * V)) ** .5

        # The following data is for a 2 year storm

        def peak_discharge_2_years_greater_than_300():

            print("Your peak discharge is {}.".format(Q))

        def peak_discharge_2_years_less_than_300():
            print("Your peak discharge is {}.".format(q))

        def rainfall_intensity_2_years_less_than_300():
            print("Your rainfall intensity is {}.".format(i2))

        def rainfall_intensity_2_years_greater_than_300():
            print("Your rainfall intensity is {}.".format(I2))

        if int(float(num0.get())) == 2 and int(float(num3.get())) > 300:
            Label(master, text=round(tc,2)).grid(row=7, column=1)
            Label(master, text=round(PD,2)).grid(row=8, column=1)
            Label(master, text=round(I2,2)).grid(row=9, column=1)
            Label(master, text=round(Q,2)).grid(row=10, column=1)

        elif int(float(num0.get())) == 2 and int(float(num3.get())) < 300:
            Label(master, text=round(tc2,2)).grid(row=7, column=1)
            Label(master, text=round(pd,2)).grid(row=8, column=1)
            Label(master, text=round(i2,2)).grid(row=9, column=1)
            Label(master, text=round(q,2)).grid(row=10, column=1)


    if int(num0.get()) == 5:
        # s1 slope for the pipe
        s = (int(float(num1.get())) - int(float(num2.get()))) / int(float(num3.get()))

        # velocity

        V = 16.1345 * s ** .5

        # time of concentration

        tc = (float(.7039 * (300 ** .3917) * (float(num4.get()) ** -1.1309) * (
        (int(float(num1.get())) - int(float(num2.get())))) / int(float(num3.get())) ** -.1985) + (
                          int(float(num3.get())) - 300) / (
                  120)) / 60
        tc2 = (float(.7039 * (int(float(num3.get())) ** .3917) * (float(num4.get()) ** -1.1309) * (
                    (int(float(num1.get())) - int(float(num2.get()))) / float(num3.get())) ** -.1985))

        # rainfall intinsity

        I5 = (float(3.536 * (tc + .330) ** -.851))
        i5 = (float(3.536 * (tc2 + .330) ** -.851))

        # peak discharge

        Q = float(num4.get()) * I5 * float(num5.get())

        q = float(num4.get()) * i5 * float(num5.get())

        # pipe size < 300

        pd = 12 * ((q) / (3.14 * V)) ** .5

        # pipe size > 300

        PD = 12 * ((Q) / (3.14 * V)) ** .5

        # The following data is for a 2 year storm

        if int(float(num0.get())) == 5 and int(float(num3.get())) > 300:
            Label(master, text=round(tc, 2)).grid(row=7, column=1)
            Label(master, text=round(PD, 2)).grid(row=8, column=1)
            Label(master, text=round(I5, 2)).grid(row=9, column=1)
            Label(master, text=round(Q, 2)).grid(row=10, column=1)

        elif int(float(num0.get())) == 5 and int(float(num3.get())) < 300:
            Label(master, text=round(tc2, 2)).grid(row=7, column=1)
            Label(master, text=round(pd, 2)).grid(row=8, column=1)
            Label(master, text=round(i5, 2)).grid(row=9, column=1)
            Label(master, text=round(q, 2)).grid(row=10, column=1)

    if int(num0.get()) == 10:
        # s1 slope for the pipe
        s = (int(float(num1.get())) - int(float(num2.get()))) / int(float(num3.get()))

        # velocity

        V = 16.1345 * s ** .5

        # time of concentration

        tc = (float(.7039 * (300 ** .3917) * (float(num4.get()) ** -1.1309) * (
            (int(float(num1.get())) - int(float(num2.get())))) / int(float(num3.get())) ** -.1985) + (
                      int(float(num3.get())) - 300) / (
                  120)) / 60
        tc2 = (float(.7039 * (int(float(num3.get())) ** .3917) * (float(num4.get()) ** -1.1309) * (
                (int(float(num1.get())) - int(float(num2.get()))) / float(num3.get())) ** -.1985))

        # rainfall intinsity

        I10 = (float(4.016 * (tc + .347) ** -.826))
        i10 = (float(4.016 * (tc2 + .347) ** -.826))

        # peak discharge

        Q = float(num4.get()) * I10 * float(num5.get())

        q = float(num4.get()) * i10 * float(num5.get())

        # pipe size < 300

        pd = 12 * ((q) / (3.14 * V)) ** .5

        # pipe size > 300

        PD = 12 * ((Q) / (3.14 * V)) ** .5

        # The following data is for a 2 year storm

        if int(float(num0.get())) == 10 and int(float(num3.get())) > 300:
            Label(master, text=round(tc, 2)).grid(row=7, column=1)
            Label(master, text=round(PD, 2)).grid(row=8, column=1)
            Label(master, text=round(I10, 2)).grid(row=9, column=1)
            Label(master, text=round(Q, 2)).grid(row=10, column=1)

        elif int(float(num0.get())) == 10 and int(float(num3.get())) < 300:
            Label(master, text=round(tc2, 2)).grid(row=7, column=1)
            Label(master, text=round(pd, 2)).grid(row=8, column=1)
            Label(master, text=round(i10, 2)).grid(row=9, column=1)
            Label(master, text=round(q, 2)).grid(row=10, column=1)




Button(master, text='Show', command=add).grid(row=11, column=1, sticky=W, pady=4)

master.mainloop()
