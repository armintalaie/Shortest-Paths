class Dijkstra:

    def __init__(self, n):
        self.V = n
        self.vertices = {i: [] for i in range(1, self.V + 1)}
        self.not_covered = [i for i in range(1, self.V + 1)]
        self.distance = {i: float("inf") for i in range(1, self.V + 1)}

    def find_next(self):
        min_dist, index = -1, -1

        for i in self.not_covered:
            if min_dist == -1 or min_dist > self.distance[i]:
                min_dist = self.distance[i]
                index = i

        return index

    def reset_variables(self):
        self.not_covered = [i for i in range(1, self.V + 1)]
        self.distance = {i: float("inf") for i in range(1, self.V + 1)}

    def find_shortest_path(self, start, end):
        #print(self.distance)

        if len(self.not_covered) == self.V:
            self.reset_variables()
            self.distance[start] = 0
        self.not_covered.remove(start)

        for adj in self.vertices[start]:
            new_dist = adj[0] + self.distance[start]
            if new_dist < self.distance[adj[1]]:
                self.distance[adj[1]] = new_dist

        if len(self.not_covered) == 0:
            if self.distance == float("inf"):
                print("no path to destination found")
            else:
                print("shortest path duration: " + str(self.distance[end]))
        else:
            return self.find_shortest_path(self.find_next(), end)


# getting input

graph = Dijkstra(int(input("Enter number of vertices\n")))

print("please enter each line as an edge, with (starting node) (weight) (finishing node)\n"
      "for example: 1 4 5 is an edge of weight 4 that goes from 1 to 5\n enter done when finished")
while 1:
    inp = input()
    if inp == "done":
        break
    temp = inp.split()
    graph.vertices[int(temp[0])].append([int(temp[1]), int(temp[2])])

print("please enter starting node and destination node")
inp = input().split()
graph.find_shortest_path(int(inp[0]), int(inp[1]))
