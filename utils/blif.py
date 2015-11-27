x = []



def graph2blif(graph, toporder, pilist, polist):
	rev = toporder.reverse()
	fo = open("blif.txt", "w")
	fo.write(".model graph\n")
	fo.write(".inputs "+" ".join([str(x) for x in pilist])+"\n")
	fo.write(".outputs "+" ".join([str(x) for x in polist])+"\n")
	



	for node in rev:



