import json
from os import path

import numpy as np
from matplotlib.patches import ConnectionPatch

from GraphAlgoInterface import GraphAlgoInterface
from GraphInterface import GraphInterface
from DiGraph import DiGraph
from Node import Node
from typing import List, Tuple
import heapq as hq
from collections import deque
import matplotlib.pyplot as plt
import random

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

    """
    Note that already here we handle cases where there is a vertex in the JSON file without POS
    """

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

            ## ***************** TAKE CARE OF NONE POS **************************
            if self.check_if_all_none() == 0:  # if all of them are none so do random 0-10 to all
                self.init_none_random(0, 10, 0, 10)
            elif self.check_if_all_none() == 1:
                pass
            else:
                minX, maxX, minY, maxY = self.minMax()
                self.init_none_random(minX, maxX, minY, maxY)
            ## ***************** TAKE CARE OF NONE POS **************************

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
        fig, ax = plt.subplots()
        all_v = self.get_graph().get_all_v().keys()
        for node in all_v:
            node: Node = self.get_graph().get_all_v().get(node)
            x, y, z = node.get_pos()
            curr_point = np.array([x, y])
            xyA = curr_point
            ax.annotate(node.get_key(), (x, y),
                        color='blue',
                        fontsize=13)  # draw id
            for e in self.get_graph().all_out_edges_of_node(node.get_key()).keys():
                nei_node: Node = self.get_graph().get_all_v().get(e)
                x, y, z = nei_node.get_pos()
                curr_point = np.array([x, y])
                xyB = curr_point
                con = ConnectionPatch(xyA, xyB, "data", "data",
                                      arrowstyle="-|>", shrinkA=6, shrinkB=6,
                                      mutation_scale=14, fc="black", color="black")
                ax.plot([xyA[0], xyB[0]], [xyA[1], xyB[1]], "o", color='red', markersize=8, linewidth=10)
                ax.add_artist(con)
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.title("Graph Plot")
        plt.show()


        """
        this dijkstra algo to find short path between two given nodes
        """

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
        di_path = {}

        while len(heap) > 0:
            # pooping out the minimum element from the heap

            node: Node = hq.heappop(heap)[1]
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
                        di_path[neighborNode.get_key()] = node.get_key()
        return di_path


    """
    notice that dijkstra will give us all the parent path so we need to reverse that in order to see the actual path
    """

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


    """
    this func will give us the weight of the shortest path and also will show us the path itself
    """

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

    """
    in our 'Node' classwe gave the possibility to each node to have 'value' and 'visit' that we can set up to them.
    this 2 func will help us in order to find the shortest path and TSP 
    """

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
    this is DFS algo and this will be used in TSP func
    """

    def dfs(self, node_id: int) -> (List[int], float):
        self._reset_visit()
        node_id = int(node_id)
        stack = deque()
        dist = 0
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
                    # print(f"=========={self.get_graph().all_out_edges_of_node(curr)}")
                    # dist = dist+self.get_graph().all_out_edges_of_node(curr).get(neighbor)
        for i in range(len(dfs_path) - 1):
            dist = dist + self.get_graph().all_out_edges_of_node(dfs_path[i]).get(dfs_path[i + 1])
        return dfs_path, dist

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        return self.dfs(node_lst[0])

    """
    this func will gave us the range of our nodes pos 
    minX - maxX
    minY - maxY 
    """

    def minMax(self) -> Tuple[float, float, float, float]:
        x = []
        y = []
        for i in self._graph.get_all_v().keys():
            node: Node = self.get_graph().get_all_v().get(i)
            x.append(node.get_x())
            y.append(node.get_y())
        minX = min(x)
        maxX = max(x)
        minY = min(y)
        maxY = max(y)

        return minX, maxX, minY, maxY

    """
    this func will check if all of our node dont have pos.
    if its True - if all of our node wont have pos so we will put random pos between 0-10 (NOTICE: this is in float not int)
    but if its False - that's mean that some node does have pos in them so we will init random pos 
    on the Nodes that have 'None' in their pos between the range we found in the 'minMax' func we did for it
    we have 3 situation: 
    (1) - all of the node have pos
    (2) - some does and some doesnt
    (3) - all of the node doesnt have pos
    we will take care of this situation when we load our json graph with load func 
    explanation of the output - 
    return 0 - it mean that all of our given node have 'None' as pos 
    return 1 - all of our node have a real pos (not 'None')
    return -1 - some have 'None' and some doesnt 
    """

    def check_if_all_none(self) -> int:
        isNone = 0
        for i in self._graph.get_all_v().keys():
            node: Node = self.get_graph().get_all_v().get(i)
            if node.get_pos() is None:
                isNone += 1
        if isNone == self.get_graph().v_size():
            return 0
        elif isNone == 0:
            return 1
        else:
            return -1

    """
    init the none node pos random float between 0-10
    """

    def init_none_random(self, minX: int, maxX: int, minY: int, maxY: int):
        for i in self._graph.get_all_v().keys():
            node: Node = self.get_graph().get_all_v().get(i)
            if node.get_pos() is None:
                x = random.uniform(minX, maxX)
                y = random.uniform(minY, maxY)
                z = 0
                node.set_pos((x, y, z))


if __name__ == '__main__':
    _graphAlgo = GraphAlgo()
    _graph = DiGraph()

    _graphAlgo.load_from_json('T0.json')

    print(_graphAlgo.get_graph())
    _graphAlgo.plot_graph()
