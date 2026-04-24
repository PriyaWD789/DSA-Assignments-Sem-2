#    ASSIGNMENT- 2 
# =========================
# 1. Dynamic Array
# =========================
class DynamicArray:
    def __init__(self, cap=2):
        self.cap = cap
        self.size = 0
        self.arr = [None] * cap

    def resize(self):
        new_cap = self.cap * 2
        new_arr = [None] * new_cap
        for i in range(self.size):
            new_arr[i] = self.arr[i]
        self.arr = new_arr
        self.cap = new_cap
        print(f"Resized to {self.cap}")

    def append(self, x):
        if self.size == self.cap:
            self.resize()
        self.arr[self.size] = x
        self.size += 1

    def pop(self):
        if self.size == 0:
            raise IndexError("Empty array")
        val = self.arr[self.size - 1]
        self.size -= 1
        return val

    def show(self):
        print([self.arr[i] for i in range(self.size)],
              f"(size={self.size}, cap={self.cap})")


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

# =========================
#  Singly Linked List
# =========================
class SinglyLL:
    def __init__(self):
        self.head = None

    def insert_begin(self, x):
        n = Node(x)
        n.next = self.head
        self.head = n

    def insert_end(self, x):
        n = Node(x)
        if not self.head:
            self.head = n
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = n

    def delete(self, x):
        if not self.head:
            return
        if self.head.val == x:
            self.head = self.head.next
            return
        cur = self.head
        while cur.next:
            if cur.next.val == x:
                cur.next = cur.next.next
                return
            cur = cur.next

    def show(self):
        cur = self.head
        while cur:
            print(cur.val, end=" -> ")
            cur = cur.next
        print("None")


# =========================
#  Doubly Linked List
# =========================
class DoublyLL:
    def __init__(self):
        self.head = None

    def insert_end(self, x):
        n = Node(x)
        if not self.head:
            self.head = n
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = n
        n.prev = cur

    def insert_after(self, target, x):
        cur = self.head
        while cur:
            if cur.val == target:
                n = Node(x)
                n.next = cur.next
                n.prev = cur
                if cur.next:
                    cur.next.prev = n
                cur.next = n
                return
            cur = cur.next

    def delete_pos(self, pos):
        cur = self.head
        i = 0
        while cur and i < pos:
            cur = cur.next
            i += 1
        if not cur:
            return
        if cur.prev:
            cur.prev.next = cur.next
        else:
            self.head = cur.next
        if cur.next:
            cur.next.prev = cur.prev

    def show(self):
        cur = self.head
        while cur:
            print(cur.val, end=" <-> ")
            cur = cur.next
        print("None")


# =========================
# Stack (using SLL)
# =========================
class Stack:
    def __init__(self):
        self.head = None

    def push(self, x):
        n = Node(x)
        n.next = self.head
        self.head = n

    def pop(self):
        if not self.head:
            raise IndexError("Stack empty")
        val = self.head.val
        self.head = self.head.next
        return val

    def peek(self):
        return self.head.val if self.head else None


# =========================
#  Queue (using SLL)
# =========================
class Queue:
    def __init__(self):
        self.head = self.tail = None

    def enqueue(self, x):
        n = Node(x)
        if not self.tail:
            self.head = self.tail = n
            return
        self.tail.next = n
        self.tail = n

    def dequeue(self):
        if not self.head:
            raise IndexError("Queue empty")
        val = self.head.val
        self.head = self.head.next
        if not self.head:
            self.tail = None
        return val

    def front(self):
        return self.head.val if self.head else None


# =========================
# 4. Parentheses Checker
# =========================
def is_balanced(expr):
    s = Stack()
    pairs = {')': '(', '}': '{', ']': '['}

    for ch in expr:
        if ch in "({[":
            s.push(ch)
        elif ch in ")}]":
            if not s.head or s.pop() != pairs[ch]:
                return False

    return s.head is None


# ==========================================
# TEST CASES (REQUIRED)
# ==========================================
if __name__ == "__main__":

    print("\n--- Dynamic Array ---")
    da = DynamicArray(2)
    for i in range(1, 11):
        da.append(i)
        da.show()

    print("Pop:", da.pop())
    print("Pop:", da.pop())
    print("Pop:", da.pop())
    da.show()

    print("\n--- Singly Linked List ---")
    sll = SinglyLL()
    sll.insert_begin(10)
    sll.insert_begin(20)
    sll.insert_begin(30)
    sll.insert_end(40)
    sll.insert_end(50)
    sll.insert_end(60)
    sll.show()
    sll.delete(20)
    sll.show()

    print("\n--- Doubly Linked List ---")
    dll = DoublyLL()
    for x in [10, 20, 30, 40, 50]:
        dll.insert_end(x)
    dll.show()
    dll.insert_after(20, 25)
    dll.show()
    dll.delete_pos(1)
    dll.show()
    dll.delete_pos(4)
    dll.show()

    print("\n--- Stack ---")
    st = Stack()
    st.push(10); st.push(20); st.push(30)
    print("Pop:", st.pop())
    print("Peek:", st.peek())

    print("\n--- Queue ---")
    q = Queue()
    q.enqueue(10); q.enqueue(20); q.enqueue(30)
    print("Dequeue:", q.dequeue())
    print("Front:", q.front())

    print("\n--- Parentheses ---")
    tests = ["([])", "([)]", "(((", "", "{[()]}"]
    for t in tests:
        print(t, "->", is_balanced(t))