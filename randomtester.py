import math

zerocount = 0
onecount = 0
twocount = 0
threecount = 0
fourcount = 0
fivecount = 0 
sixcount = 0
sevencount = 0
eightcount = 0
ninecount = 0

f1 = open('/Users/melquiades/Desktop/datafile.txt', 'r')
numblist = f1.read()

for item in numblist:
  try:
		item = int(item)
	except ValueError:
		item = 10
	if item == 0:
		zerocount = zerocount + 1
	if item == 1:
		onecount = onecount + 1
	if item == 2:
		twocount = twocount + 1
	if item == 3:
		threecount = threecount + 1
	if item == 4:
		fourcount = fourcount + 1
	if item == 5:
		fivecount = fivecount + 1
	if item == 6:
		sixcount = sixcount + 1
	if item == 7:
		sevencount = sevencount + 1
	if item == 8:
		eightcount = eightcount + 1
	if item == 9:
		ninecount = ninecount + 1

print 'zerocount: %d'%(zerocount)
print 'onecount: %d'%(onecount)
print 'twocount: %d'%(twocount)
print 'threecount: %d'%(threecount)
print 'fourcount: %d'%(fourcount)
print 'fivecount: %d'%(fivecount)
print 'sixcount: %d'%(sixcount)
print 'sevencount: %d'%(sevencount)
print 'eightcount: %d'%(eightcount)
print 'ninecount: %d'%(ninecount)

countlist = []
countlist.append(zerocount)
countlist.append(onecount)
countlist.append(twocount)
countlist.append(threecount)
countlist.append(fourcount)
countlist.append(fivecount)
countlist.append(sixcount)
countlist.append(sevencount)
countlist.append(eightcount)
countlist.append(ninecount)

average = 0
for item in countlist:
	average = average + item
total = average
average = average/10

devlist = []
for item in countlist:
	deviance = (item - average) ** 2
	devlist.append(deviance)
stdev = 0
for item in devlist:
	stdev = stdev + item

stdev = stdev/10
stdev = math.sqrt(stdev)


print 'standard deviation: %d' %(stdev)

randfactor= stdev/average
randfactor = randfactor * 100
randomness = 100 - randfactor

print 'digits analyzed: %d' %(total)
print 'randomness percentage: %d' %(randomness)
