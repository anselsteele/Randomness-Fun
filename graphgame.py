from Tkinter import *
import math
import random
complexity = input('Enter complexity,from 1 to 169: ')

master = Tk()
cvs = Canvas(master,width = 700,height = 700)
cvs.pack()
xcorner1 = 30
xcorner2 = 70
ycorner1 = 30
ycorner2 = 70
xcounter = 0
ycounter = 0

pointlist = []
pointx1 = xcorner1
pointx2 = xcorner2
pointy1 = ycorner1
pointy2 = ycorner2

while ycounter <= 12:
  xcounter = 0
	while xcounter <= 12:
		adder = 50 * xcounter
		pointx1 = xcorner1 + adder
		pointx2 = xcorner2 + adder
		xcounter = xcounter + 1
		if xcounter == 12:
			adder = 50 * ycounter
			pointy1 = ycorner1 + adder
			pointy2 = ycorner2 + adder
			ycounter = ycounter + 1
		datapoint = (pointx1,pointy1,pointx2,pointy2)
		pointlist.append(datapoint)
random.shuffle(pointlist)

counter = 0
while counter < complexity:
	datapoint = pointlist[counter]
	xcorner1 = datapoint[0]
	ycorner1 = datapoint[1]
	xcorner2 = datapoint[2]
	ycorner2 = datapoint[3]
	cvs.create_rectangle(xcorner1,ycorner1,xcorner2,ycorner2,fill = 'green')
	print counter
	counter = counter + 1

master.mainloop()
