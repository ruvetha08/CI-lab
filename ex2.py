import heapq

class Graph:
    def __init__(self):
        self.adj = {}
        self.heuristics = {}

    def add_node(self, node, h_value=0):
        self.adj[node] = self.adj.get(node, [])
        self.heuristics[node] = h_value
        print(f"Node '{node}' (h={h_value}) added.")

    def delete_node(self, node):
        if node in self.adj:
            del self.adj[node]
            del self.heuristics[node]
            for n in self.adj:
                self.adj[n] = [e for e in self.adj[n] if e[0] != node]
            print(f"Node '{node}' deleted.")
        else:
            print("Node not found.")

    def add_edge(self, n1, n2, cost):
        if n1 in self.adj and n2 in self.adj:
            self.adj[n1].append((n2, cost))
            self.adj[n2].append((n1, cost))
            print(f"Edge {n1}-{n2} (cost {cost}) added.")
        else:
            print("Error: Both nodes must exist first.")

    def delete_edge(self, n1, n2):
        if n1 in self.adj and n2 in self.adj:
            self.adj[n1] = [e for e in self.adj[n1] if e[0] != n2]
            self.adj[n2] = [e for e in self.adj[n2] if e[0] != n1]
            print("Edge deleted.")

    def display(self):
        print("\n--- Current Graph State ---")
        for node, neighbors in self.adj.items():
            print(f"Node {node} [h={self.heuristics[node]}] -> Neighbors: {neighbors}")

def a_star(graph, start, goal):

    open_list = [(graph.heuristics[start], 0, start, [start])]
    visited_g = {start: 0}

    print(f"\n--- Calculating A* from '{start}' to '{goal}' ---")

    while open_list:
        f, g, curr, path = heapq.heappop(open_list)

        print(f"Current: {curr}, g={g}, path={path}")

        if curr == goal:
            return path, g

        for neighbor, weight in graph.adj.get(curr, []):
            new_g = g + weight
            if neighbor not in visited_g or new_g < visited_g[neighbor]:
                visited_g[neighbor] = new_g
                new_f = new_g + graph.heuristics.get(neighbor, 0)
                print(f"  Exploring: {curr}->{neighbor}, new g={new_g}, h={graph.heuristics.get(neighbor, 0)}, f={new_f}")
                heapq.heappush(open_list, (new_f, new_g, neighbor, path + [neighbor]))

    return None, None

g = Graph()
print(" 1: Add Node (name, heuristic)\n 2: Delete Node\n 3: Add Edge (u, v, cost)\n 4: Delete Edge\n 5: Display Graph\n 6: Perform A* Search\n 7: Exit")

while True:
    choice = input("\nEnter menu choice (1-7): ").strip()

    if choice == '1':
        name = input("Node name: ")
        h = int(input("Heuristic h(n): "))
        g.add_node(name, h)
    elif choice == '2':
        g.delete_node(input("Node to delete: "))
    elif choice == '3':
        u = input("Node 1: ")
        v = input("Node 2: ")
        c = int(input("Edge cost: "))
        g.add_edge(u, v, c)
    elif choice == '4':
        u, v = input("Enter nodes (u v): ").split()
        g.delete_edge(u, v)
    elif choice == '5':
        g.display()
    elif choice == '6':
        s = input("Start node: ")
        target = input("Goal node: ")
        res_path, res_cost = a_star(g, s, target)
        if res_path:
            print(f"\nPath: {' -> '.join(res_path)} | Total Cost: {res_cost}")
        else:
            print("\nNo path found.")
    elif choice == '7':
        print("Exiting program.")
        break
    else:
        print("Invalid choice, try again.")
