# Node Connections

node_zero_links = [1]
node_one_links = [0, 2, 3]
node_two_links = [1, 3]
node_three_links = [1, 2]
nodes_list = [node_zero_links, node_one_links, node_two_links, node_three_links]

nodes_matrix = []
for i in range(4):
    temporary_list = []
    for j in range(4):
        #  print(f"j: {j} -- List X: {nodes_list[x]}")
        if j in nodes_list[i]:  # j value takes the same index in temporary_list
            temporary_list.append(1)
        else:
            temporary_list.append(0)
    nodes_matrix.append(temporary_list)

print(nodes_matrix)
