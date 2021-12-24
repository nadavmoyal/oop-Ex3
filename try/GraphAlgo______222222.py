import json
from os import path
from GraphAlgoInterface import GraphAlgoInterface
from GraphInterface import GraphInterface
from DiGraph import DiGraph
from Node import Node
from typing import List
import heapq as hq
from collections import deque

"""
this is like 'MyDWGraphAlgo' we did in Ex2 in java
this class - GraphAlgo implement GraphAlgoInterface,
like -  MyDWGraphAlgo implement DirectedWeightedGraphAlgorithms

"""


class GraphAlgo(GraphAlgoInterface):
    _graph: GraphInterface

    def __init__(self, graph: GraphInterface = None):
        self._graph = graph

    def get_graph(self) -> GraphInterface:
        return self._graph

    def load_from_json(self, file_name: str) -> bool:
        if path.exists(file_name):  # didnt understand this line
            graph: GraphInterface = DiGraph()
        try:
            with open(file_name, 'r') as json_file:
                dict = json.load(json_file)
                for node in dict["Nodes"]:
                    if "pos" in node:  # this if statement is for the case we dont get the 'pos' in json file. like in file 'T0'
                        xyz = node["pos"].split(",")
                        pos = float(xyz[0]), float(xyz[1]), float(xyz[2])
                        graph.add_node(node["id"], pos)
                    else:
                        graph.add_node(node["id"])
                for e in dict["Edges"]:
                    # Notice that it is true that in input json file we get it in different order.
                    # we get src,w,dest. but in our given func that we need to do we get as input in this order
                    # src,dest,w.
                    graph.add_edge(e["src"], e["dest"], e["w"])
                self._graph = graph
            return True
        except IOError as e:
            print(e)
        return False

    def save_to_json(self, file_name: str) -> bool:
        if self.get_graph() is not None:
            try:
                with open(file_name, 'w') as f:
                    json.dump(self.get_graph(), indent=4, fp=f, default=lambda a: a.__dict__())
                    return True
            except IOError as e:
                print(e)
        return False

    def plot_graph(self) -> None:
        pass

        # ===================

    def dijkstra(self, src: Node, dest: Node) -> dict:
        # create empty minimum heap
        # the elements in the heap should be a tuple that hold two elements
        # the first is the distance from the src node to the current node, the second is the node himself
        heap: hq = []
        src.set_dist(0)
        src.set_visited(True)
        hq.heappush(heap, (0, src))
        # create new dictionary of the path, every key holds up his parent node
        # the parent of the src is None
        # di_path = {src: None}
        di_path = []

        while len(heap) > 0:
            # pooping out the minimum element from the heap
            node: Node = hq.heappop(heap)[1]  # !!!!!! notice that in here we do '[1]' because our first node in our min heap is our src
            if node.get_key() == dest.get_key():
                break
            if not node.get_visited():
                # if the node wasn't visited yet set the visit to true
                node.set_visited(True)
            edgesToNeighbor = self.get_graph().all_out_edges_of_node(node.get_key())
            # looping over all the edges the going out of the node
            for e in edgesToNeighbor:
                neighborNode: Node = self.get_graph().get_all_v().get(e)
                if not neighborNode.get_visited():
                    # if the node wasn't visited yet calculate the distance from the src node to this node
                    # and check if the distance is lower then the previous distance
                    # (assuming the distances initialized to infinity (in this case -1 is infinity))
                    dist = node.get_dist() + edgesToNeighbor.get(e)
                    if neighborNode.get_dist() == -1 or dist < neighborNode.get_dist():
                        # updating the distance, adding the node to the heap and updating the parent of the node
                        neighborNode.set_dist(dist)
                        hq.heappush(heap, (dist, neighborNode))
                        di_path.insert(0,node.get_key())
        return di_path

    def _reconstruct_path(self, src: int, dest: int, full_path: dict) -> list:
        if full_path.get(dest) is None:
            return []
        shortest_path = [dest]
        parent = full_path.get(dest)
        # reconstructing the path using the path dictionary into a list starting from the dest key
        while parent != src:
            # wile we didn't get to the src node that his parent is None
            # insert the parent to the list and go to the next parent
            shortest_path.insert(0, parent)
            parent = full_path.get(parent)
        shortest_path.insert(0, src)
        return shortest_path

    # ==============================================================

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        n1: Node = self.get_graph().get_all_v().get(id1)
        n2: Node = self.get_graph().get_all_v().get(id2)
        if n1 is None or n2 is None:
            return float('inf'), []
        self._reset_values()
        # calculate the shortest path from id1 to id2
        shortest_path = self._reconstruct_path(id1, id2, self.dijkstra(n1, n2))
        # print(self.get_graph().get_all_v().get(id2).get_dist())
        return n2.get_dist(), shortest_path

    def _reset_values(self):
        nodes: dict = self.get_graph().get_all_v()
        # reset all node values of visited to false and distance to -1
        for n in nodes:
            nodes.get(n).set_visited(False)
            nodes.get(n).set_dist(float('inf'))

    def _reset_visit(self):
        nodes: dict = self.get_graph().get_all_v()
        # reset all node values of visited to false and distance to -1
        for n in nodes:
            nodes.get(n).set_visited(False)
            # nodes.get(n).set_dist(float('inf'))

    """
    in order to do the TSP with used DFS
    """
    def TSP(self, node_id: int) -> (List[int], float):
        self._reset_visit()
        stack = deque()
        dfs_path = [node_id]
        stack.append(node_id)  # add the first node to the stack
        node: Node = self.get_graph().get_all_v().get(node_id)
        node.set_visited(True)
        while len(stack) != 0:
            curr = stack.pop()
            for neighbor in self.get_graph().all_out_edges_of_node(curr).keys():
                nei_node: Node = self.get_graph().get_all_v().get(neighbor)
                if not nei_node.get_visited():
                    stack.append(neighbor)
                    nei_node.set_visited(True)
                    dfs_path.append(neighbor)
        return dfs_path



if __name__ == '__main__':
    _graphAlgo = GraphAlgo()
    _graph = DiGraph()

    #
    _graph.add_node(0, (2, 3))
    _graph.add_node(1, (3, 3))
    _graph.add_node(2, (5, 3))
    _graph.add_node(3, (5, 2))
    _graph.add_node(4, (2, 9))
    # _graph.add_node(5, (6, 9))
    # _graph.add_node(6, (9, 9))
    # _graph.add_node(7, (8, 9))
    _graph.add_edge(0, 1, 1)
    _graph.add_edge(0, 2, 10)
    _graph.add_edge(1, 2, 1)


    _graphAlgo.__init__(_graph)

    print(_graphAlgo.shortest_path(0,2))

    print(_graphAlgo.TSP(0))