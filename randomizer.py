complexity = input('enter number of loops to shuffle inputs: ')
counter = 0
counterlim = 5
entrylist = []
while counter < counterlim:
  entry = input('enter a number greater than 10: ')
	entrylist.append(entry)
	counter = counter + 1

maincounter = 0
while maincounter < complexity:
	modnumlist = []
	for item in entrylist:
		modnum = item % 9
		modnumlist.append(modnum)
			
	listlen = len(entrylist)
	loopcounter = 0
	newlist = []
	while loopcounter < listlen:
		entryitem = entrylist[loopcounter]
		moditem = modnumlist[loopcounter]

		entrystring = str(entryitem)
		modstring = str(moditem)

		newstring = []
		for item in entrystring:
			newstring.append(item)
		for item in modstring:
			newstring.append(item)

		finalstring = ''.join(newstring)
		finalstring = int(finalstring)
		newlist.append(finalstring)
		loopcounter = loopcounter + 1
	shufflelist = []
	shufflelist.append(newlist[0] + newlist[(len(newlist) - 1)])
	shufflecounter = 0
	while shufflecounter < (len(newlist) - 1):
		shuffleitem = newlist[shufflecounter] + newlist[shufflecounter + 1]
		shufflelist.append(shuffleitem)
		shufflecounter = shufflecounter + 1
	finalshuffle = []
	for element in shufflelist:
		newmod = element % 10
		if newmod == 0:
			newmod = 10
		shuffnumber = element/newmod
		shuffnumber = int(shuffnumber)
		finalshuffle.append(shuffnumber)
	shufflelist = finalshuffle

	print shufflelist
	entrylist = shufflelist
	maincounter = maincounter + 1
open("/Users/melquiades/Desktop/datafile.txt", "w").close()
with open("/Users/melquiades/Desktop/datafile.txt", "a") as writefile:
	for thing in entrylist:
		thing = str(thing)
		writefile.write(thing)
		writefile.write('\n')
