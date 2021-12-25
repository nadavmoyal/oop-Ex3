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

## Second part - GUI visualization:

|          class                  | Details                             | 
| --------------------------------|:--------------------------------------:| 
|`NewPanel`,`NewFrame`|A classes that contains all the functions and calculations in order to display the graph and algorithms clearly on the screen.| 

## matplotlib visualization -check2 from the main:
<img width="310" alt="‏‏check2" src="https://user-images.githubusercontent.com/79272744/147392864-23f80209-6eb6-4f9e-8668-f4384f450b45.PNG">



## Diagram of the project: 
(It is recommended to zoom in.)
### Node
![Node](https://user-images.githubusercontent.com/79272744/147393070-8d4fba45-49c7-41fd-a8b5-8601de9855b0.png)
### GraphInterface
![GrapgInterface](https://user-images.githubusercontent.com/79272744/147393074-aac1a11f-83aa-4618-8382-21ce8674a01d.png)
### GraphAlgoInterface
![GraphAlgoInterface](https://user-images.githubusercontent.com/79272744/147393090-9a048523-9496-4787-bcd0-211c767ff22a.png)






### RunTime  ==== NEED TO CHANGE=====:
1000V , 10000E :
building graph - 1.76 sec
,isconnected - 0.3 sec
,remove - 0.26 sec
,shortpathdist - 0.31 sec 

10000V , 100000E :
building graph - 4.44 sec
,shortpathdist - 0.31 sec

100000V, 1000000E :
building graph - 19 sec
,shortpathdist - 0.35 sec
