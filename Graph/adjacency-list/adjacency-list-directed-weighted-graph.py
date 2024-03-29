

class Vertex:
        def __init__(self, name):
           self.name = name


class DirectedWeightedGraph:

        def __init__(self):
            self._graph = {}
            self._vertexObjects = set()


        def display(self):
           for vertex in self._graph:
                print( vertex, " - > " , self._graph[vertex] )
           print()


        def numVertices(self):
            return len(self._graph)


        def numEdges(self):  
            e = 0
            for adjList in self._graph.values():
               e += len(adjList)
            return e    
            
               
        def vertices(self):
            return list(self._graph)
            

        def edges(self):  
           edgesList = []
           for u in self._graph:
               for v,w in self._graph[u]:  
                  edgesList.append((u,v,w))
           return edgesList


        def insertVertex(self,name):

            if name in self._graph:
                print("Vertex with this name already present in the graph")
            else:
                self._graph[name] = set()
                self._vertexObjects.add( Vertex(name) )


        def removeVertex(self,name):
            if name not in self._graph:
               print("Vertex not present in the graph")
               return 

            self._graph.pop(name)
                   
            for u in self._graph:
               for i,t in enumerate( self._graph[u] ):
                  if t[0] == name:
                    self._graph[u].pop(i)

            for vertex in self._vertexObjects:
               if name == vertex.name:
                   v = vertex
                   break
            self._vertexObjects.remove(v)
            

        def insertEdge(self, s1, s2,w):
            if s1 not in self._graph:
                print("Start vertex not present in the graph, first insert the start vertex")
            elif s2 not in self._graph:
                print("End vertex not present in the graph, first insert the end vertex")
            elif s1 == s2:
                print("Not a valid edge")
            elif s2 in ( t[0] for t in self._graph[s1] ):
    	        print("Edge already present in the graph") 
            else:  
                self._graph[s1].add((s2,w))   
        

        def removeEdge(self, s1,s2):
             for u in self._graph:
               for t in self._graph[u] :
                  if u==s1 and t[0] == s2:
                    self._graph[u].remove(t)
                    return
             print("Edge not present in the graph")


        def isAdjacent(self, s1, s2):
            if s1 not in self._graph:
               print("Start vertex not present in the graph")
               return False
            if s2 not in self._graph:
               print("End vertex not present in the graph")
               return False
            return s2 in ( t[0] for t in self._graph[s1] )
      
        
        def outdegree(self, s):
            if s not in self._graph:
                print("Vertex not present in the graph")
                return
            return len(self._graph[s]) 
             

        def indegree(self, s):
            if s not in self._graph:
                print("Vertex not present in the graph")
                return

            ind = 0
            for u in self._graph:
              for t in self._graph[u]:
                 if t[0] == s:
                   ind += 1
                   
            return ind

        def _getVertex(self,s):
            for vertex in self._vertexObjects:
                if s == vertex.name:
                   return vertex
            return None


if __name__ == '__main__':

  g = DirectedWeightedGraph() 

  g.insertVertex("AA")
  g.insertVertex("BB")
  g.insertVertex("CC")
  g.insertVertex("DD")
  g.insertVertex("EE")
  g.insertEdge("AA","BB",3)
  g.insertEdge("AA","CC",5)
  g.insertEdge("CC","DD",4)
  g.insertEdge("DD","AA",2)
  g.insertEdge("CC","AA",7)
  g.insertEdge("BB","EE",9)

  while True:
      print("1.Display Adjacency list, vertices and edges")
      print("2.Insert a vertex")
      print("3.Remove a vertex")
      print("4.Insert an edge")
      print("5.Delete an edge")
      print("6.Display indegree and outdegree of a vertex")
      print("7.Check if there is an edge between two vertices")
      print("8.Quit")
        
      option = int(input("Enter your choice : " ))

      if option == 1:
          g.display()
          print("Number of vertices : ", g.numVertices() )
          print("Number of edges : ", g.numEdges() )
          print("List of Vertices : ", g.vertices() )
          print("List of Edges : ", g.edges() )
      elif option == 2:
          s = input("Enter the name of vertex : ")
          g.insertVertex(s)
      elif option == 3:
          s = input("Enter the name of vertex : ")
          g.removeVertex(s)
      elif option == 4:
          s1 = input("Enter the name of start vertex : ")
          s2 = input("Enter the name of end vertex : ")
          w = input("Enter the weight : ")
          g.insertEdge(s1,s2,w)
      elif option == 5:
          s1 = input("Enter the name of start vertex : ")
          s2 = input("Enter the name of end vertex : ")
          g.removeEdge(s1,s2)
      elif option == 6:
          s = input("Enter vertex name : ")
          i = g.indegree(s)
          if i is not None:
             print("Indegree of", s , "is", i)
          o = g.outdegree(s)
          if o is not None:
             print("Outdegree of", s , "is", o)
      elif option == 7:
          s1 = input("Enter the name of first vertex : ")
          s2 = input("Enter the name of second vertex : ")
          if g.isAdjacent(s1, s2):
              print("There is an edge from ", s1 , " to " , s2)
          else:
              print("There is no edge from " , s1 , " to " , s2)
      elif option == 8:
          break
      else:
          print("Wrong option")
   
      print()


   
