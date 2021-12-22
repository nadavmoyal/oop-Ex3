from Ex3.src.GraphInterface import GraphInterface
"""
# ======= contructor from Ex2 that we did for reminder =====
# public class DW_Graph implements DirectedWeightedGraph {
#     public HashMap< Integer, NodeData > Nodes;
#     public HashMap<Integer ,HashMap<Integer,EdgeData>> Edges;
#     private int ModeCount;
#     private int NumberOfNodes;
#     private int NumberOfEdges;
# ======= contructor from Ex2 that we did for reminder =====
"""
# this is the constructor that will have every thing that a graph will hold in it
from Ex3.src.Node import Node


class DiGraph(GraphInterface):
    # from the json file we can see that the nodes is a dict with 2 KEY - pos,id
    # "Nodes": [
    #     {
    #         "pos": "35.18753053591606,32.10378225882353,0.0",
    #         "id": 0
    #     },
    # and in here we will hold it like we did in Ex2 in java.
    # it will be a dict that the key is the node id and the value is another dict (nested dict) that will hold all
    # of his neighbors like this, KEY: 'other_nodes_id', VALUE: 'weight'
    # (this is according to the GraphInterface). that will make easy on us when we want in func
    _nodes: dict
    _edgesOut: dict # in Ex2 in java we had hashmap of edge theat hold KEY: node_id , VALUE: nested hashmap with all of his neighbor. so now in here we will have 2 dict (hashMap) for it, for in\out neighbors
    _edgesInside: dict  # this also will be dict of dict like '_edgeOut' but this time it will be holding all the edges that comes *IN* from key node. this is for the use of the func 'all_in_edges_of_node'
    _mc: int  # this will be the mode count that check the the number of changes in the graph
    _numOfEdges: int
    _numOfNodes: int  # i added it

    # _edges: dict # the edges in the json file is a dict that look like that "Edges": [{"src": 0,"w": 1.4004465106761335,"dest": 1},,.....

    # i didnt add '_inEdge' didnt understand what it is

    def __init__(self):
        self._nodes: dict = {}
        self._edgesOut: dict = {}  # dict of dict
        self._edgesInside: dict = {}  # dict of dict
        self._numOfEdges: int = 0
        self._numOfNodes: int = 0
        self._mc: int = 0
        # self._inEdge: dict = {}

    def v_size(self) -> int:  # 'v' is for vertex - node
        return self._numOfNodes

    def e_size(self) -> int:
        return self._numOfEdges

    def get_mc(self) -> int:
        return self._mc

    # ****** DID SOME CHANGE ****** DO WE WANT TO ADD THE TRY CATCH ****
    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if id1 not in self._nodes or id2 not in self._nodes or id1 == id2:
            return False
        elif  id2 in self._edgesOut[id1]: # if in our 'edgesOut' we already have this int KEY that mean that the edge is already exist,note that this edge is from id1->id2.
            # self._edgesOut[id1]-> get to the value of KEY [id1]
            return False
        else:
            # this just mean that in our edges dict (in\out) we will add our new egde
            # self._edgesOut[id1][id2] = {id2: weight}
            # self._edgesOut[id1] -> get inside our dict with KEY: id1
            # [id2] -> (we get inner dict) now we tell it to put in KEY [id2]
            # id2: weight} -> our new value from the input
            # self._edgesOut[id1].update({id2: weight})
            # self._edgesInside[id2].update({id1: weight})

            self._edgesOut[id1].update({id2: weight})
            self._edgesInside[id2].update({id1: weight})
            self._numOfEdges += 1
            self._mc += 1
            return True

    # every time we add a node we will also add  it to our edges (in\out)
    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if node_id in self._nodes:  # if the node already exist
            return False
        # **** need double check ****
        self._nodes[node_id] = pos
        # self._nodes[node_id] = Node(node_id, pos)
        # **** need double check ****

        self._edgesOut[node_id] = {}  # because he doesnt have a neighbor yet
        self._edgesInside[node_id] = {}  # because he doesnt have a neighbor yet
        self._numOfNodes+=1
        self._mc += 1

        # i didnt add '_inEdge'
        return True

    # ****** DID SOME CHANGE ****** WHY THE FOR LOOP ****
    def remove_node(self, node_id: int) -> bool:
        if node_id not in self._nodes:  # if the node that want to be remove doesn't exist
            return False
        del self._nodes[node_id]
        del self._edgesOut[node_id]  # this will delete all of the edges that comes out from the deleted node
        del self._edgesInside[node_id]  # this will delete all of the edges that comes out from the deleted node
        self._mc += 1
        self._numOfNodes -= 1
        return True
        # ******** he add 2 for loop that i didnt understand why???

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if node_id1 not in self._nodes or node_id2 not in self._nodes:
            return False
        # if self.all_out_edges_of_node(node_id1).get(node_id2) is None:
        if node_id2 not in self.all_out_edges_of_node(node_id1):
            return False
        del (self._edgesOut[node_id1][node_id2])
        del (self._edgesInside[node_id2][node_id1])
        self._numOfEdges -= 1
        self._mc += 1
        return True

    # ========== THIS FUNC WASNT AT START ======
    def get_all_v(self) -> dict:
        return self._nodes

    def all_in_edges_of_node(self, id1: int) -> dict:
        # this will first check if the node input is in our graph
        if id1 not in self._nodes.keys():
            return {}
        # if it doesit will return the inner dict for the KEY:'id1' in '_edgesInside' outer dict
        return self._edgesInside.get(
            id1)  # return all of the nodes neighbors (dict of dict, like we did in Ex2 in java)

    def all_out_edges_of_node(self, id1: int) -> dict:
        # this will first check if the node input is in our graph
        if id1 not in self._nodes.keys():  # if there is no node with this id in the graph, return empty dict {}
            return {}
        # if it doesnt will return the inner dict for the KEY:'id1' in '_edgesOut' outer dict
        return self._edgesOut.get(id1)  # return all of the nodes neighbors (dict of dict, like we did in Ex2 in java)

    def __repr__(self):
        return self._nodes.__repr__()