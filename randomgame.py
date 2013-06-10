from Tkinter import *
import curses
import random

master = Tk()

cvsheight = 700
cvswidth = 700
mobnumber = input('Enter Number of AIs: ')
color = 'light blue'
cvs = Canvas(master,width = cvswidth,height = cvsheight)
cvs.pack()

rawstring = 'creature'
counter = 1
taglist = []
while counter <= mobnumber:
	random1 = random.randint(0,cvswidth)
	random2 = random.randint(0,cvsheight)

	coord1 = random1
	coord2 = random2
	coord3 = random1 + 10
	coord4 = random2 + 10

	tagger = rawstring
	strcounter = str(counter)
	tagger += strcounter

	cvs.create_rectangle(coord1,coord2,coord3,coord4,fill = 'red',tag = tagger)
	taglist.append(tagger)
	counter = counter + 1

newcolor = 'blue'
while True:
	cvs.create_rectangle(10,20,30,40,fill = newcolor)
	#newcolor = newcolor + 1
	for item in taglist:
		random1 = random.randint(0,1)
		random2 = random.randint(0,1)

		random3 = random.randint(1,3)
		random4 = random.randint(1,3)

		itemcoords = cvs.coords(item)

		coordsx = itemcoords[0]
		coordsy = itemcoords[1]

		if coordsx < 0:
			random1 = 1
		if coordsx > cvswidth:
			random1 = 0
		if coordsy < 0:
			random2 = 1
		if coordsy > cvsheight:
			random2 = 0

		for element in taglist:
			elecoords = cvs.coords(element)
			xele = elecoords[0]
			yele = elecoords[1]
			if coordsx - xele < 5 and coordsx - xele > 0:
				random1 = 0
			if coordsx - xele > -5 and coordsx - xele < 0:
				random1 = 1
			if coordsy - yele < 5 and coordsy - yele > 0:
				random2 = 0
			if coordsy - yele > -5 and coordsy -yele > 0:
				random2 = 1
		


		if random1 == 0:
			movex = -1
		else:
			movex = 1
		if random2 == 0:
			movey = -1
		else:
			movey = 1

		movex = movex * random3
		movey = movey * random4

		cvs.move(item,movex,movey)
		cvs.update()
master.mainloop()
