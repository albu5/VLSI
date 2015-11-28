# Author: Sagun Pai (Famguy)
# Codename: Hello from the outside!
# Timestamp: 29th Oct 2015, 4:24 AM
# Location: Room no 325, Hostel 9, IIT Bombay, Powai
from pprint import pprint
from copy import deepcopy

# given input dag_graph, we shall use the bin backing approach to get LUTs of specific size (5 in this case)
LUTsize = 5
d1ag_graph = [[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 4, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 4, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 4, 4, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 4, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 4, -1, 4, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 4, 4, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 4, 4, 4, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 4], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 4, -1, -1, 4], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 4, -1, 4], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 4, 4, -1, 4], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 4, 4], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 4, -1, 4, 4], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 4, 4, 4], [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 4, 4, 4, 4], [-1, 4, -1, 4, -1, 4, -1, 4, -1, 4, -1, 4, -1, 4, -1, 4, -1, -1, -1, -1], [-1, -1, 4, 4, -1, -1, 4, 4, -1, -1, 4, 4, -1, -1, 4, 4, -1, -1, -1, -1], [-1, -1, -1, -1, 4, 4, 4, 4, -1, -1, -1, -1, 4, 4, 4, 4, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, 4, 4, 4, 4, 4, 4, 4, 4, -1, -1, -1, -1]]

# 10
dag_graph = [[-1,2,2,2,2,2,2,2,2,2,2],
[2,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
[2,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
[2,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
[2,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
[2,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
[2,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
[2,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
[2,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
[2,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
[2,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]]


# 9
dag_graph2 = [[-1,2,2,2,2,2,2,2,2,2],
[2,-1,-1,-1,-1,-1,-1,-1,-1,-1],
[2,-1,-1,-1,-1,-1,-1,-1,-1,-1],
[2,-1,-1,-1,-1,-1,-1,-1,-1,-1],
[2,-1,-1,-1,-1,-1,-1,-1,-1,-1],
[2,-1,-1,-1,-1,-1,-1,-1,-1,-1],
[2,-1,-1,-1,-1,-1,-1,-1,-1,-1],
[2,-1,-1,-1,-1,-1,-1,-1,-1,-1],
[2,-1,-1,-1,-1,-1,-1,-1,-1,-1],
[2,-1,-1,-1,-1,-1,-1,-1,-1,-1]]


# dag for encoder

_GATE = {'0':0, '1':1, 'and':2, 'nand':3, 'or':4, 'nor':5, 'xor':6, 'xnor':7}

def onlygates(l):
	return [x for x in l if x not in [-1,0,1]]

def extenddag(dag,adds):
	dag_ret = deepcopy(dag)
	for k in dag_ret:
		k.append(adds)
	dag_ret.append([adds for s in range(len(k))])
	return dag_ret

original_size = len(dag_graph)

for ind, i in enumerate(dag_graph):
	j = onlygates(i)
	numand = j.count(_GATE['and'])
	# numor = j.count(_GATE['or'])
	if numand > 6:
		newnod = original_size - 1
		nnumand = int(numand/4) # consecutive and gates
		rnumand = numand%4		# extra inputs in first one
		gatesadded = nnumand
		for inop,nop in enumerate(range(gatesadded)):
			dag_graph = extenddag(dag_graph,-1)
			if inop == 0:
				dag_graph[ind][nop+original_size] = _GATE['and']
				dag_graph[nop+original_size][ind] = _GATE['and']
		
		for il in range(original_size,original_size+gatesadded+1):
			try:
				dag_graph[il][il+1] = _GATE['and']
				dag_graph[il+1][il] = _GATE['and']
				print il
			except Exception, e:
				pass


		indexes = [k for k,x in enumerate(i) if x == _GATE['and']]
		for nog in range(rnumand):
			indexes.pop(0)
		for inoh,noh in enumerate(range(nnumand)):
			newnod = newnod + 1
			try:
				inp1 = indexes.pop(0)
				dag_graph[newnod-original_size-inoh][inp1] = -1
				dag_graph[newnod][inp1] = _GATE['and']
				dag_graph[inp1][newnod-original_size-inoh] = -1
				dag_graph[inp1][newnod] = _GATE['and']
			except Exception, e:
				pass
			try:
				inp1 = indexes.pop(0)
				dag_graph[newnod-original_size-inoh][inp1] = -1
				dag_graph[newnod][inp1] = _GATE['and']
				dag_graph[inp1][newnod-original_size-inoh] = -1
				dag_graph[inp1][newnod] = _GATE['and']
			except Exception, e:
				pass
			try:
				inp1 = indexes.pop(0)
				dag_graph[newnod-original_size-inoh][inp1] = -1
				dag_graph[newnod][inp1] = _GATE['and']
				dag_graph[inp1][newnod-original_size-inoh] = -1
				dag_graph[inp1][newnod] = _GATE['and']
			except Exception, e:
				pass
			try:
				inp1 = indexes.pop(0)
				dag_graph[newnod-original_size-inoh][inp1] = -1
				dag_graph[newnod][inp1] = _GATE['and']
				dag_graph[inp1][newnod-original_size-inoh] = -1
				dag_graph[inp1][newnod] = _GATE['and']
			except Exception, e:
				pass

pprint(dag_graph)








