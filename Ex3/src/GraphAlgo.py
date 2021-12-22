# from Ex3.src.GraphAlgoInterface import GraphAlgoInterface
# from Ex3.src.GraphInterface import GraphInterface
# import json
# from os import path
# import DiGraph
# """
# this is like 'MyDWGraphAlgo' we did in Ex2 in java
# this class - GraphAlgo implement GraphAlgoInterface,
# like -  MyDWGraphAlgo implement DirectedWeightedGraphAlgorithms
#
# """
#
#
# class GraphAlgo(GraphAlgoInterface):
#     _graph: GraphInterface
#
#     def __init__(self, graph: GraphInterface = None):
#         self._graph = graph
#
#     def get_graph(self) -> GraphInterface:
#         return self._graph
#
#     def load_from_json(self, file_name: str) -> bool:
#         if path.exists(file_name): # didnt understand this line
#             graph: GraphInterface = DiGraph()
#         try:
#             with open(file_name, 'r') as json_file:
#                 dict = json.load(json_file)
#                 for node in dict["Nodes"]:
#                     if "pos" in node: # this if statement is for the case we dont get the 'pos' in json file. like in file 'T0'
#                         xyz = node["pos"].split(",")
#                         pos = float(xyz[0]), float(xyz[1]), float(xyz[2])
#                         graph.add_node(node["id"], pos)
#                     else:
#                         graph.add_node(node["id"])
#                 for e in dict["Edges"]:
#                     # Notice that it is true that in input json file we get it in different order.
#                     # we get src,w,dest. but in our given func that we need to do we get as input in this order
#                     # src,dest,w.
#                     graph.add_edge(e["src"], e["dest"], e["w"])
#                 self._graph = graph
#             return True
#         except IOError as e:
#             print(e)
#         return False
#
#     def save_to_json(self, file_name: str) -> bool:
#         if self.get_graph() is not None:
#             try:
#                 with open(file_name, 'w') as f:
#                     json.dump(self.get_graph(), indent=4, fp=f, default=lambda a: a.__dict__())
#                     return True
#             except IOError as e:
#                 print(e)
#         return False
#
#     def shortest_path(self, id1: int, id2: int) -> (float, list):
#         pass
#
#     def plot_graph(self) -> None:
#         pass
#
#     def TSP(self, node_lst: List[int]) -> (List[int], float):
#         pass
#
#     def centerPoint(self) -> (int, float):
#         pass
