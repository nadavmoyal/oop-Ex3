from GraphInterface import GraphInterface
from Node import Node
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



class DiGraph(GraphInterface):

    _nodes: dict
    _edgesOut: dict
    _edgesInside: dict
    _mc: int
    _numOfEdges: int
    _numOfNodes: int


    def __init__(self):
        self._nodes: dict = {}
        self._edgesOut: dict = {}  # dict of dict
        self._edgesInside: dict = {}  # dict of dict
        self._numOfEdges: int = 0
        self._numOfNodes: int = 0
        self._mc: int = 0

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
        # self._nodes[node_id] = pos
        self._nodes[node_id] = Node(node_id, pos)
        # **** need double check ****

        self._edgesOut[node_id] = {}  # because he doesnt have a neighbor yet
        self._edgesInside[node_id] = {}  # because he doesnt have a neighbor yet
        self._numOfNodes+=1
        self._mc += 1

        return True

    # ****** DID SOME CHANGE ****** WHY THE FOR LOOP ****
    def remove_node(self, node_id: int) -> bool:
        if node_id not in self._nodes:  # if the node that want to be remove doesn't exist
            return False
        # from numOfEdge we need to del all of the edge we del when we del node id1
        numOfEdgeOutFromNode_id = len(self.all_out_edges_of_node(node_id))
        numOfEdgeInsideFromNode_id = len(self.all_in_edges_of_node(node_id))
        del self._nodes[node_id]
        del self._edgesOut[node_id]  # this will delete all of the edges that comes out from the deleted node
        del self._edgesInside[node_id]  # this will delete all of the edges that comes out from the deleted node
        self._mc += 1
        self._numOfNodes -= 1
        self._numOfEdges -= (numOfEdgeOutFromNode_id + numOfEdgeInsideFromNode_id)
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