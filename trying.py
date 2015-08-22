#! /usr/bin/env python3
file = open("data.txt",'r')
line = 0

points = []
pip = 0  
while pip < 601:
    points.append(pip)
    pip = pip + 1
    
print(points)

dictetoposide = {}.fromkeys(points,0)
dictre1 = {}.fromkeys(points,0)
dictgene = {}.fromkeys(points,0)

print(dictgene)

#this section takes a "comma-seperated" text file exported from excel 
#and pulls out all of the fields from one row or line of the file
#assigning each of them to a variable
#it has some "if then" clauses for cases where a field may have been left blank 
for row in file:
	rowlist = row.split('\t')
	if rowlist[0] == '':
		break
	num = int(rowlist[0])
	chromosome = rowlist[1]
	etopstart = int(rowlist[2])
	etopend = int(rowlist[3])
	etopname = rowlist[4]
	g1 = rowlist[5]
	g1huh = True
	if g1 == 'NO GENE':
		g1huh = False
		g1start = 0
		g1end = 0
	else:
		g1start = int(rowlist[6])
		g1end = int(rowlist[7])
	g2 = rowlist[8]
	g2huh = True	
	if g2 == 'NO GENE':
		g2huh = False
		g2start = 0
		g2end = 0
	else:
		g2start = int(rowlist[9])
		g2end = int(rowlist[10])
	re1sig = rowlist[11]
	re1huh = True
	if re1sig == 'NO':
		re1huh = False
		re1start = 0
		re1end = 0
	else:
		re1start = int(rowlist[12])
		re1end = int(rowlist[13])
	description = rowlist[14]

#this part does some confusing math to determine how to anchor the
#elements in the drawing. essentially I needed the center of the "Etoposide" element to be
#at the center of the drawing and everything else to be relative to that

	etoplength = (etopend-etopstart)
	origincoord = etopstart-(6000-(etoplength/2))
	print(origincoord)
	
#this section just scales the numbers from the excel file into something appropriate for
#drawing a smallish image basically dividing everything by 20

	xetopstart = (etopstart-origincoord)/20
	if xetopstart < 0:
		xetopstart = 0
	if xetopstart > 600:
		xetopstart = 600
		
	xetopend = (etopend-origincoord)/20
	if xetopend < 0:
		xetopend = 0
	if xetopend > 600:
		xetopend = 600
		
	xg1start = (g1start-origincoord)/20
	if xg1start < 0:
		xg1start = 0
	if xg1start > 600:
		xg1start = 600
		
	xg1end = (g1end-origincoord)/20
	if xg1end < 0:
		xg1end = 0
	if xg1end > 600:
		xg1end = 600
		
	xg2start = (g2start-origincoord)/20
	if xg2start < 0:
		xg2start = 0
	if xg2start > 600:
		xg2start = 600
		
	xg2end = (g2end-origincoord)/20
	if xg2end < 0:
		xg2end = 0
	if xg2end > 600:
		xg2end = 600
		
	xre1start = (re1start-origincoord)/20
	if xre1start < 0:
		xre1start = 0
	if xre1start > 600:
		xre1start = 600
		
	xre1end = (re1end-origincoord)/20
	if xre1end < 0:
		xre1end = 0
	if xre1end > 600:
		xre1end = 600
		
	print(xetopstart) 
	print(xetopend)
	print(xg1start)
	print(xg1end)
	print(xg2start)
	print(xg2end)
	print(xre1start)
	print(xre1end) 		
#iteration of the position dictionaries
	
	blip = int(xetopstart)
	while blip < xetopend:
		a = dictetoposide[blip]
		a = a + 1
		dictetoposide[blip] = a
		blip = blip + 1
	
	blip = int(xg1start)
	while blip < xg1end:
		a = dictgene[blip]
		a = a + 1
		dictgene[blip] = a
		blip = blip + 1
		
	blip = int(xg2start)
	while blip < xg2end:
		a = dictgene[blip]
		a = a + 1
		dictgene[blip] = a
		blip = blip + 1
	
	blip = int(xre1start)
	while blip < xre1end:
		a = dictre1[blip]
		a = a + 1
		dictre1[blip] = a
		blip = blip + 1

print(dictetoposide)
print(dictgene)
print(dictre1)