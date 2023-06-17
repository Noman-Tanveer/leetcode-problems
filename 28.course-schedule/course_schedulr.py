from typing import List
class Solution:
    def makeAdjacencyList(self, n, edges):
        adjList = [[] for _ in range(n)]
        for c1, c2 in edges:
            adjList[c2].append(c1)
        return adjList

    def topological_sort(self, n, prereqs):
        adj = self.makeAdjacencyList(n, prereqs)

        degrees = [0] * n
        for c1, c2 in prereqs:
            degrees[c1] += 1

        queue = []
        for i in range(n):
            if degrees[i] == 0:
                queue.append(i)

        count = 0
        topo_sorted = []
        while queue:
            v = queue.pop(0)
            topo_sorted.append(v)
            count += 1
            for des in adj[v]:
                degrees[des] -= 1
                if degrees[des] == 0:
                    queue.append(des)
        if count != n:
            return None
        else:
            return topo_sorted

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        return True if self.topological_sort(numCourses, prerequisites) else False
