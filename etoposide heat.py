#! /usr/bin/env python3
file = open("data.txt",'r')
line = 0

array = open("array.txt",'w')
etoposide = {}

for row in file:
	rowlist = row.split('\t')
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


	etoplength = (etopend-etopstart)
	origincoord = etopstart-(6000-(etoplength/2))

	xetopstart = (etopstart-origincoord)/20
	xetopend = (etopend-origincoord)/20
	xg1start = (g1start-origincoord)/20
	if xg1start < 0:
		xg1start = 0
	xg1end = (g1end-origincoord)/20
	if xg1end > 600:
		xg1end = 600
	xg2start = (g2start-origincoord)/20
	if xg2start < 0:
		xg2start = 0
	xg2end = (g2end-origincoord)/20
	if xg2end > 600:
		xg2end = 600
	xre1start = (re1start-origincoord)/20
	if xre1start < 0:
		xre1start = 0
	xre1end = (re1end-origincoord)/20
	if xre1end > 600:
		xre1end = 600


	import tkinter

	tk = tkinter.Tk()
	tk.title('demo')
	canvas = tkinter.Canvas(tk)
	canvas.pack()



	canvas.create_line(5, 50, 605, 50, width=4, fill='gray60')  #"genome"
	canvas.create_text(5, 54, text=int(origincoord), anchor='nw', font=(('Verdana', 'sans'), 10, 'italic'), fill='black')

	canvas.create_line(xetopstart+5, 25, xetopend+5, 25, width=6, fill='purple') #etop
	canvas.create_text(xetopstart+5, 23, text='Etoposide', anchor='sw', font=(('Verdana', 'sans'), 10, 'italic'), fill='black')

	if g1huh == True:
		canvas.create_line(xg1start+5, 50, xg1end+5, 50, width=6, fill='green') #gene1
		canvas.create_text(xg1start+5, 48, text=g1, anchor='sw', font=(('Verdana', 'sans'), 10, 'italic'), fill='black')
	
	if g2huh == True:
		canvas.create_line(xg2start+5, 50, xg2end+5, 50, width=6, fill='green') #gene2
		canvas.create_text(xg2start+5, 48, text=g2, anchor='sw', font=(('Verdana', 'sans'), 10, 'italic'), fill='black')

	if re1huh == True:
		canvas.create_line(xre1start+5, 75, xre1end+50, 75, width=6, fill='red') #topo?
		canvas.create_text(xre1start+5, 73, text='RE1 (Sig.=' + str(re1sig) + ')', anchor='sw', font=(('Verdana', 'sans'), 10, 'italic'), fill='black')


	canvas.create_line(5, 100, 605, 100, width=2, fill='gray90')  #scale
	canvas.create_line(5, 100, 5, 95, width=2, fill='gray90')  #scale
	canvas.create_line(55, 100, 55, 95, width=2, fill='gray90')  #scale
	canvas.create_line(105, 100, 105, 95, width=2, fill='gray90')  #scale
	canvas.create_line(155, 100, 155, 95, width=2, fill='gray90')  #scale
	canvas.create_line(205, 100, 205, 95, width=2, fill='gray90')  #scale
	canvas.create_line(255, 100, 255, 95, width=2, fill='gray90')  #scale
	canvas.create_line(305, 100, 305, 95, width=2, fill='gray90')  #scale
	canvas.create_line(355, 100, 355, 95, width=2, fill='gray90')  #scale
	canvas.create_line(405, 100, 405, 95, width=2, fill='gray90')  #scale
	canvas.create_line(455, 100, 455, 95, width=2, fill='gray90')  #scale
	canvas.create_line(505, 100, 505, 95, width=2, fill='gray90')  #scale
	canvas.create_line(555, 100, 555, 95, width=2, fill='gray90')  #scale
	canvas.create_line(605, 100, 605, 95, width=2, fill='gray90')  #scale

	canvas.create_text(5, 115, text=chromosome, anchor='sw', font=(('Verdana', 'sans'), 10, 'italic'), fill='black')
	canvas.create_text(5, 125, text='Etoposide peak: ' +str(etopname), anchor='sw', font=(('Verdana', 'sans'), 10, 'italic'), fill='black')
	canvas.create_text(5, 135, text='Description: ' + str(description), anchor='sw', font=(('Verdana', 'sans'), 10, 'italic'), fill='black')

				#canvas.create_rectangle(20, 10, 120, 80, fill =colors[0])
				#canvas.create_polygon(150, 180, 175, 115, 190, 160, 215, 125, 240, 180, fill=colors[3])
				#canvas.create_polygon(150, 180, 175, 115, fill=colors[4])
	canvas.postscript(file=str(num) + '_' + chromosome + '_' + etopname + '_' + g1 + '.eps', width=610, height=145, colormode='color')
	tk.destroy
