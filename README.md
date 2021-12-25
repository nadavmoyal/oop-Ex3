![alt text](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRUC7G6cLvCjY5-Sq4vRcieUJc_O4KjwMl8NQEKDTrAElDHc2178puykOjpVgY8XRASD_M&usqp=CAU)

# Ex3
>Made by Yehonatan Barel and Nadav Moyal.
>
>GitHub pages: 
>
>https://github.com/nadavmoyal
>
>https://github.com/yehonatanbarel    

## Introduction:
This project is an assignment in an object-oriented course at Ariel University. The project consists of two parts: The first part is an implenentation of directed weighted graph in python and consist 3 classes, 2 interfaces and 2 test. 
The second part of the project is to plot the graph using `matplotlib` visualize it.

## Operating Instructions =====WE NEED TO CHE OW WE NEED TO SUBMIT IT===== :
1. Download the jar file.
2. Put the Json files in the same folder.
3. In the command line, write the following command:
"java -jar Ex2.jar "NameOfJsonFile.json" "

# Description of the classes:


## Class Node implements NodeData:
##### This class represents the set of operations applicable on a node (vertex) in a (directional) weighted graph.

|          Methods                | Details                             | 
| --------------------------------|:--------------------------------------:| 
|`get_key()`|Returns the key (id) associated with this node.|
|`get_dist()`| get the dist of a given node.|
|`get_dist()`| allow to set the dist of a given node.|
|`get_visited`| tell us if the node have been visited or not.|
|`set_visited`| allow us to the node visited mode (True \ False).|
|`get_pos()`|Returns the location of this node, if none return None.| 
|`set_pos(x,y,z)`|Allows changing this node's location.|
|`get_x`| get the X location of the node.|
|`get_y`| get the Y location of the node.|


## Class DiGraph implements GraphInterface:
##### This class represents the set of operations applicable on a directional edge (src,dest) in a (directional) weighted graph.
                                 
|          Methods                | Details                             | 
| --------------------------------|:--------------------------------------:| 
|`v_size()`| Returns the number of vertices in this graph.| 
|`e_size()`| Returns the number of edges in this graph|
|`get_all_v()`|return a dictionary of all the nodes in the Graph, each node is represented using a pair (node_id, node_data).| 
|`all_in_edges_of_node()`| return a dictionary of all the nodes connected to (into) node_id ,each node is represented using a pair (other_node_id, weight)| 
|`all_out_edges_of_node()`|return a dictionary of all the nodes connected from node_id , each node is represented using a pair (other_node_id, weight).| 
|`get_mc()`| Returns the current version of this graph, on every change in the graph state - the MC should be increased .|   
|`add_node()`| Adds a node to the graph.|
|`remove_node()`| Removes a node from the graph.|
|`remove_edge()`| Removes an edge from the graph.|

## Class  GraphAlgo implements GraphAlgoInterface:
##### This class represents a Directional Weighted Graph.
 
|          Methods                | Details                             | 
| --------------------------------|:--------------------------------------:| 
|`get_graph()`| return the directed graph on which the algorithm works on.| 
|`load_from_json()`|Loads a graph from a json file.|
|`save_to_json()`|Saves the graph in JSON format to a file.| 
|`shortest_path()`|Returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm.| 
|`TSP()`|Finds the shortest path that visits all the nodes in the list.| 
|`centerPoint()`|Finds the node that has the shortest distance to it's farthest node.|   
|`plot_graph()`| Plots the graph.|

## We did tests on each class


## matplotlib visualization:
| A1 | A2 | check2 from the main |  
|:---------:|:---------:|:---------:| 
|![A1](https://user-images.githubusercontent.com/79272744/147393215-5ea779af-e80b-4d52-ba75-bf679b49b0c3.png)|![A2](https://user-images.githubusercontent.com/79272744/147393213-8c57b7e4-214f-4919-8ab9-b6605d4a14e5.png)|![check2](https://user-images.githubusercontent.com/79272744/147393275-5adb067d-66ae-463b-a80e-c43ef9d335c2.png)
|


## Diagram of the project: 
| Node | GraphInterface | GraphAlgoInterface |  
|:---------:|:---------:|:---------:| 
| ![Node](https://user-images.githubusercontent.com/79272744/147393118-d5cd11db-c9a1-4ad9-a087-90c87bea0994.png)| ![GrapgInterface](https://user-images.githubusercontent.com/79272744/147393123-e0e9fe75-4b39-4d93-b36b-30e42862d03b.png)|![GraphAlgoInterface](https://user-images.githubusercontent.com/79272744/147393124-2df8a214-35c3-4c3d-9fb0-a71906e09685.png)|








## Run Time: 
| 1000V, 9000E | 10000V, 90000E | 100000V, 2000000E |  
|:---------:|:---------:|:---------:| 
|![1_000](https://user-images.githubusercontent.com/79272744/147395246-b4c37d2a-7737-4db6-a6d3-ea573094ec38.png)| ![10_000](https://user-images.githubusercontent.com/79272744/147395250-b8d1fd52-4cee-4c49-9f89-97bdff483134.png)| ![100_000](https://user-images.githubusercontent.com/79272744/147395252-166fb6be-bbb6-4f85-a398-be461cccdbfc.png)|


