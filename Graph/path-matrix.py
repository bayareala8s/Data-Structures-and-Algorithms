

class Vertex:
        def __init__(self, name):
           self.name = name

          
class DirectedGraph:

        def __init__(self,size=20):
           self._adj = [  [0 for column in range(size)]  for row in range(size) ]
           self._n = 0
           self._vertexList = []
           

        def display(self):
            for i in range(self._n):
                for j in range(self._n):
                   print( self._adj[i][j], end =' ')
                print()


        def numVertices(self):
            return self._n


        def numEdges(self):
            e = 0
            for i in range(self._n):
                for j in range(self._n):
                    if self._adj[i][j]!=0:
                        e+=1
            return e


        def vertices(self):
            return [vertex.name for vertex in self._vertexList]


        def edges(self):
            edges = []
            for i in range(self._n):
                for j in range(self._n):
                   if self._adj[i][j] != 0:
                      edges.append( (self._vertexList[i].name, self._vertexList[j].name) )
            return edges


        def _getIndex(self,s):
            index = 0
            for name in (vertex.name for vertex in self._vertexList):
                if s == name:
                   return index
                index += 1
            return None


        def insertVertex(self,name):
            if name in (vertex.name for vertex in self._vertexList): ######## 
                print("Vertex with this name already present in the graph")
                return                
            self._vertexList.append( Vertex(name) )  
            self._n += 1


        def removeVertex(self,name):
             u = self._getIndex(name)
             if u is None:
                print("Vertex not present in the graph")
                return
        
             self._adj.pop(u)

             for i in range(self._n):
                  self._adj[i].pop(u)
                  
             self._vertexList.pop(u)
             self._n -= 1
               
    
        def insertEdge(self, s1, s2):
            u = self._getIndex(s1)
            v = self._getIndex(s2)
            if u is None:
                print("Start vertex not present in the graph, first insert the start vertex")
            elif v is None:
                print("End vertex not present in the graph, first insert the end vertex")
            elif u == v:
                print("Not a valid edge") 
            elif self._adj[u][v] != 0 :
                print("Edge already present in the graph") 
            else:  
                self._adj[u][v] = 1
                
        
        def removeEdge(self, s1,s2):
             u = self._getIndex(s1)
             v = self._getIndex(s2)
             if u is None:
                print("Start vertex not present in the graph")
             elif v is None:
                print("End vertex not present in the graph")
             elif self._adj[u][v] == 0:
                print("Edge not present in the graph")
             else:        
                self._adj[u][v] = 0


        def isAdjacent(self, s1, s2):
            u = self._getIndex(s1)
            v = self._getIndex(s2)
            if u is None:
                print("Start vertex not present in the graph")
                return False
            elif v is None:
                print("End vertex not present in the graph")
                return False
            return False if self._adj[u][v] == 0 else True   

      
        def outdegree(self, s):
            u = self._getIndex(s)
            if u is None:
               print("Vertex not present in the graph")
               return
        
            outd = 0
            for v in range(self._n):
                if self._adj[u][v] != 0 :
                   outd+=1
            return outd
             

        def indegree(self, s):
            u = self._getIndex(s)
            if u is None:
               print("Vertex not present in the graph")
               return
        
            ind = 0

            for v in range(self._n):
                if self._adj[v][u] != 0 :
                    ind+=1
            return ind

        def findPathMatrix(self):
                             
            x = [ [None for column in range(self._n)]  for row in range(self._n) ]
            
            adjp = [ [None for column in range(self._n)]  for row in range(self._n) ]
            temp = [ [None for column in range(self._n)]  for row in range(self._n) ]
                           
            for i in range(self._n):
                 for j in range(self._n):
                        x[i][j] = adjp[i][j] = self._adj[i][j]
           
            for p in range(2, self._n+1):   

               for i in range(self._n):
                   for j in range(self._n):
                      temp[i][j] = 0
                      for k in range(self._n):
                            temp[i][j] = temp[i][j] + adjp[i][k] *  self._adj[k][j]
                             
               for i in range(self._n):
                   for j in range(self._n):
                       adjp[i][j] = temp[i][j]
                  
               for i in range(self._n):
                   for j in range(self._n):
                        x[i][j] = x[i][j] + adjp[i][j]
                
           
            #Display x
            for i in range(self._n):
               for j in range(self._n):
                   print(x[i][j],end=" ")
               print()
                
            print()      
      
            
            for i in range(self._n):
                for j in range(self._n):
                   if x[i][j] != 0:
                       x[i][j] = 1
                   
            #Display Path Matrix
            for i in range(self._n):
               for j in range(self._n):
                   print(x[i][j],end=" ")
               print()
          

if __name__ == '__main__':

  g1 = DirectedGraph() 
  
  g1.insertVertex("Zero")
  g1.insertVertex("One")
  g1.insertVertex("Two")
  g1.insertVertex("Three")

  g1.insertEdge("Zero","One")
  g1.insertEdge("Zero","Three")
  g1.insertEdge("One","Two")
  g1.insertEdge("One","Three")
  g1.insertEdge("Three","Two")
  g1.findPathMatrix()
  
  print()
                 
  g2 = DirectedGraph()
  
  g2.insertVertex("Zero")
  g2.insertVertex("One")
  g2.insertVertex("Two")
  g2.insertVertex("Three")
                  
  g2.insertEdge("Zero","One")
  g2.insertEdge("Zero","Three")
  g2.insertEdge("One","Two")
  g2.insertEdge("One","Three")
  g2.insertEdge("Two","Zero")
  g2.insertEdge("Three","Two")
  g2.findPathMatrix()

  print()


   
