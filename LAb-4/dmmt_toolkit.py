# ASSIGNMENT-4 

# ________________ TASK 1: BINARY SEARCH TREE _____________________________
class BSTNode:
    def __init__(self, key):
        self.key   = key
        self.left  = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None   

    # --- Insert ---
    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return BSTNode(key)      
        if key < node.key:
            node.left  = self._insert(node.left, key)   
        elif key > node.key:
            node.right = self._insert(node.right, key)  
        return node

    # --- Search ---
    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None:
            return False            
        if key == node.key:
            return True
        if key < node.key:
            return self._search(node.left, key)
        return self._search(node.right, key)

    # --- Delete ---
    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return None

        if key < node.key:
            node.left  = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            # Found  node to delete — handle 3 cases:

            # Case 1: leaf node — just remove it
            if node.left is None and node.right is None:
                return None

            # Case 2: one child — replace node with that child
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left

            # Case 3: two children
            successor = node.right
            while successor.left is not None:
                successor = successor.left
            node.key   = successor.key
            node.right = self._delete(node.right, successor.key)

        return node

    # --- Inorder Traversal  ---
    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node is not None:
            self._inorder(node.left, result)
            result.append(node.key)
            self._inorder(node.right, result)


# ________________________  GRAPH + BFS + DFS___________________________________

class Graph:
    def __init__(self):
        self.adj = {}

    def add_edge(self, u, v, weight):
        if u not in self.adj:
            self.adj[u] = []
        if v not in self.adj:
            self.adj[v] = []
        self.adj[u].append((v, weight))

    def print_adjacency_list(self):
        print("  Adjacency List:")
        for node in self.adj:
            line = "    " + node + " -> "
            parts = []
            for neighbour, weight in self.adj[node]:
                parts.append(neighbour + "(" + str(weight) + ")")
            if parts:
                line += ", ".join(parts)
            print(line)

    def bfs(self, start):
        visited = []       
        queue   = [start] 
        visited.append(start)
        order = []

        while len(queue) > 0:
            node = queue.pop(0)    
            order.append(node)

            for neighbour, weight in self.adj.get(node, []):
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)

        return order

    def dfs(self, start):
        visited = []
        order   = []
        self._dfs(start, visited, order)
        return order

    def _dfs(self, node, visited, order):
        visited.append(node)
        order.append(node)
        for neighbour, weight in self.adj.get(node, []):
            if neighbour not in visited:
                self._dfs(neighbour, visited, order)


# ______________________ HASH TABLE (SEPARATE CHAINING) ____________________________

class HashTable:
    def __init__(self, size):
        self.size    = size
        self.buckets = []
        for i in range(size):
            self.buckets.append([])

    def _hash(self, key):
        return key % self.size    

    def insert(self, key, value):
        index = self._hash(key)
        for pair in self.buckets[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.buckets[index].append([key, value])

    def get(self, key):
        index = self._hash(key)
        for pair in self.buckets[index]:
            if pair[0] == key:
                return pair[1]
        return None 

    def delete(self, key):
        index = self._hash(key)
        for i in range(len(self.buckets[index])):
            if self.buckets[index][i][0] == key:
                self.buckets[index].pop(i)
                return True
        return False   

    def print_table(self):
        print("  Hash Table Buckets:")
        for i in range(self.size):
            if len(self.buckets[i]) == 0:
                print("    [" + str(i) + "]: empty")
            else:
                chain = ""
                for pair in self.buckets[i]:
                    chain += "(" + str(pair[0]) + ", " + str(pair[1]) + ") -> "
                chain += "None"
                print("    [" + str(i) + "]: " + chain)


# __________________  TEST CASES     _______________________________

def test_bst():
    print("=" * 55)
    print("  TASK 1: Binary Search Tree")
    print("=" * 55)

    bst = BST()
    for key in [50, 30, 70, 20, 40, 60, 80]:
        bst.insert(key)

    print("\n  Inserted: [50, 30, 70, 20, 40, 60, 80]")
    print("  Inorder  :", bst.inorder())

    print("\n  Search 20 ->", bst.search(20))
    print("  Search 90 ->", bst.search(90))

    bst.insert(65)
    print("\n  Inserted 65  (now node 60 has one child: 65)")
    print("  Inorder  :", bst.inorder())

    print("\n  Delete 20  (Case 1: leaf node)")
    bst.delete(20)
    print("  Inorder  :", bst.inorder())

    print("\n  Delete 60  (Case 2: one child — child is 65)")
    bst.delete(60)
    print("  Inorder  :", bst.inorder())

    print("\n  Delete 30  (Case 3: two children — 20 was removed, children are 40 on left, 65 side on right)")
    bst.delete(30)
    print("  Inorder  :", bst.inorder())


def test_graph():
    print("\n" + "=" * 55)
    print("  TASK 2: Graph BFS and DFS")
    print("=" * 55)

    g = Graph()
    g.add_edge('A', 'B', 2)
    g.add_edge('A', 'C', 4)
    g.add_edge('B', 'D', 7)
    g.add_edge('B', 'E', 3)
    g.add_edge('C', 'E', 1)
    g.add_edge('C', 'F', 8)
    g.add_edge('D', 'F', 5)
    g.add_edge('E', 'D', 2)
    g.add_edge('E', 'F', 6)
    print()
    g.print_adjacency_list()
    print("\n  BFS from A:", " -> ".join(g.bfs('A')))
    print("  DFS from A:", " -> ".join(g.dfs('A')))

def test_hash_table():
    print("\n" + "=" * 55)
    print("  TASK 3: Hash Table with Separate Chaining")
    print("=" * 55)

    ht = HashTable(size=5)
    print("\n  Table size = 5   |   hash(key) = key % 5")
    print("  Inserting keys: [10, 15, 20, 7, 12]")

    ht.insert(10, 'ten')
    print("    insert(10, 'ten')     -> bucket [" + str(10 % 5) + "]")
    ht.insert(15, 'fifteen')
    print("    insert(15, 'fifteen') -> bucket [" + str(15 % 5) + "]")
    ht.insert(20, 'twenty')
    print("    insert(20, 'twenty')  -> bucket [" + str(20 % 5) + "]")
    ht.insert(7, 'seven')
    print("    insert(7,  'seven')   -> bucket [" + str(7  % 5) + "]")
    ht.insert(12, 'twelve')
    print("    insert(12, 'twelve')  -> bucket [" + str(12 % 5) + "]")

    print()
    ht.print_table()

    print("\n  get(10) ->", ht.get(10))
    print("  get(15) ->", ht.get(15))
    print("  get(7)  ->", ht.get(7))

    print("\n  Delete key 20 from bucket [0] (same bucket as 10 and 15):")
    ht.delete(20)
    ht.print_table()

#__________ MAIN ________________________-
if __name__ == "__main__":
    print("\n  Data Management Mini Toolkit (DMMT)")
    print("  Data Structures | Unit 4 Assignment")
    print()
    test_bst()
    test_graph()
    test_hash_table()
    print()