def graph2blif(graph, toporder, pilist, polist):
	toporder.reverse()
	rev = toporder

	# initial definitions
	fo = open("bp.blif", "w")
	fo.write(".model graph\n")
	fo.write(".inputs "+" ".join([str(x) for x in pilist])+"\n")
	fo.write(".outputs "+" ".join([str(x) for x in polist])+"\n")
	
	# recursive definition for truth tables
	for node in rev:
		inplist = []
		gate = -1
		for i in range(len(graph)):
			if graph[i][node]>=0 :
				inplist.append(i)
				gate = graph[i][node]
		if inplist:
			fo.write(".names "+" ".join([str(x) for x in inplist+[node]])+"\n")
			if gate == 2:
				mystring = [str(1) for j in inplist]
				mystring = "".join(mystring)
				mystring = mystring + " 1"
				fo.write(mystring+"\n") 		
			if gate == 4:
				for k in range(len(inplist)):
					mystring = ["-" for j in inplist]
					mystring[k] = str(1)
					mystring = "".join(mystring)
					mystring = mystring + " 1"
					fo.write(mystring+"\n") 		
			if gate == 5:
				mystring = [str(0) for j in inplist]
				mystring = "".join(mystring)
				mystring = mystring + " 1"
				fo.write(mystring+"\n")  	
			if gate == 3:
				for k in range(len(inplist)):
					mystring = ["-" for j in inplist]
					mystring[k] = str(0)
					mystring = "".join(mystring)
					mystring = mystring + " 1"
					fo.write(mystring+"\n") 					

	fo.write(".end")
	fo.close()