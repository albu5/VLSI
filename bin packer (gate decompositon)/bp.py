# Author: Sagun Pai (Famguy)
# Codename: Hello from the outside!
# Timestamp: 29th Oct 2015, 4:24 AM
# Location: Room no 325, Hostel 9, IIT Bombay, Powai

# given input dag_graph, we shall use the bin backing approach to get LUTs of specific size (5 in this case)
LUTsize = 5
dag_graph = [[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
 [-1, -1, -1, -1, -1, -1, -1, -1, 4, -1, -1],
 [-1, -1, -1, -1, -1, -1, -1, -1, -1, 4, -1],
 [-1, -1, -1, -1, -1, -1, -1, -1, 4, 4, -1],
 [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 4],
 [-1, -1, -1, -1, -1, -1, -1, -1, 4, -1, 4],
 [-1, -1, -1, -1, -1, -1, -1, -1, -1, 4, 4],
 [-1, -1, -1, -1, -1, -1, -1, -1, 4, 4, 4],
 [-1, 4, -1, 4, -1, 4, -1, 4, -1, -1, -1],
 [-1, -1, 4, 4, -1, -1, 4, 4, -1, -1, -1],
 [-1, -1, -1, -1, 4, 4, 4, 4, -1, -1, -1]]

# dag for encoder



