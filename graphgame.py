from Tkinter import *
import math
import random
import copy
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
		datapoint = [pointx1,pointy1,pointx2,pointy2]
		pointlist.append(datapoint)
random.shuffle(pointlist)

counter = 0
meanlist = []
while counter < complexity:
	datapoint = pointlist[counter]
	xcorner1 = datapoint[0]
	ycorner1 = datapoint[1]
	xcorner2 = datapoint[2]
	ycorner2 = datapoint[3]

	xmean = (xcorner1 + xcorner2) * 0.5
	ymean = (ycorner1 + ycorner2) * 0.5

	minipoint = [xmean,ymean]
	meanlist.append(minipoint)

	cvs.create_rectangle(xcorner1,ycorner1,xcorner2,ycorner2,fill = 'green')
	counter = counter + 1

counter = 0
random.shuffle(meanlist)
nodelist = []
for item in meanlist:
	done = False
	while done == False:
		nodes = random.randint(2,len(meanlist))
		if nodes % 2 == 0:
			done = True
			nodelist.append(nodes)

while counter < len(meanlist):
	print meanlist
	point1 = meanlist[counter]
	point1a = point1[0]
	point1b = point1[1]
	nodes = nodelist[counter]
	nodecounter = 0
	dummylist = copy.deepcopy(meanlist) 
	while nodecounter < nodes:

		dummylen = len(dummylist) - 1
		if dummylen > 1:
			newrand = random.randint(0,dummylen)
			sample = dummylist[newrand]
			point2a = sample[0]
			point2b = sample[1]
			del dummylist[newrand]
			cvs.create_line(point1a,point1b,point2a,point2b,fill = 'red',width = 1.5)
		nodecounter = nodecounter + 1

	counter = counter + 1

master.mainloop()
