
#3.7
from tkinter import *
from math import *




master = Tk()

Label(master, text="High Point").grid(row=0)
Label(master, text="Low Point").grid(row=1)
Label(master, text="Hydraulic Length").grid(row=2)
Label(master, text="Total Area").grid(row=3)
Label(master, text="Run Off Coefficent").grid(row=4)
Label(master, text="Storm Year").grid(row=5)

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
            print("Your total time of concentration is {}.".format(tc))
            print("Your pipe size is {}.".format(PD))
            rainfall_intensity_2_years_greater_than_300()
            peak_discharge_2_years_greater_than_300()
        elif int(float(num0.get())) == 2 and int(float(num3.get())) < 300:
            print("Your total time of concentration is {}.".format(tc2))
            rainfall_intensity_2_years_less_than_300()
            peak_discharge_2_years_less_than_300()


    #Q = int(float(e4.get())*I2*int(e3.get()))
    #x = int(e0.get())*int(e1.get())




Button(master, text='Show', command=add).grid(row=7, column=1, sticky=W, pady=4)

master.mainloop()
