# ASSIGNMENT -1 #########

######## STACK ADT ########## 

class StackADT:
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return "Stack is empty"

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return "Stack is empty"

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)


########  FACTORIAL ###############


def factorial(n):
    if n < 0:
        return "Invalid input"
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)


########### FIBONACCI NAIVE ###########


fib_calls_naive = 0

def fib_naive(n):
    global fib_calls_naive
    fib_calls_naive += 1

    if n <= 1:
        return n

    return fib_naive(n-1) + fib_naive(n-2)


#########  FIBONACCI MEMOIZATION  ############

fib_calls_memo = 0
memo = {}

def fib_memo(n):
    global fib_calls_memo
    fib_calls_memo += 1

    if n in memo:
        return memo[n]

    if n <= 1:
        memo[n] = n
        return n

    memo[n] = fib_memo(n-1) + fib_memo(n-2)
    return memo[n]


######## TOWER OF HANOI ############


moves_stack = StackADT()

def hanoi(n, source, helper, destination):

    if n == 1:
        move = f"Move disk 1 from {source} to {destination}"
        print(move)
        moves_stack.push(move)
        return

    hanoi(n-1, source, destination,helper)

    move = f"Move disk {n} from {source} to {destination}"
    print(move)
    moves_stack.push(move)

    hanoi(n-1, helper, source, destination)


#########  RECURSIVE BINARY SEARCH #########


def binary_search(arr, key, low, high):

    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == key:
        return mid

    elif arr[mid] > key:
        return binary_search(arr, key, low, mid-1)

    else:
        return binary_search(arr, key, mid+1, high)


###########  MENU DRIVEN MAIN PROGRAM ######### 

def main():

    while True:

        print("\n====== AERT TOOLKIT MENU ======")
        print("1. Calculate Factorial")
        print("2. Fibonacci (Naive)")
        print("3. Fibonacci (Memoization)")
        print("4. Tower of Hanoi")
        print("5. Recursive Binary Search")
        print("6. Exit")

        choice = int(input("Enter your choice: "))

        # FACTORIAL
        if choice == 1:
            n = int(input("Enter a number: "))
            print("Factorial =", factorial(n))


        # FIBONACCI NAIVE
        elif choice == 2:
            n = int(input("Enter n: "))

            global fib_calls_naive
            fib_calls_naive = 0

            result = fib_naive(n)

            print("Fibonacci =", result)
            print("Number of recursive calls =", fib_calls_naive)


        # FIBONACCI MEMO
        elif choice == 3:
            n = int(input("Enter n: "))

            global fib_calls_memo
            fib_calls_memo = 0
            memo.clear()

            result = fib_memo(n)

            print("Fibonacci =", result)
            print("Number of recursive calls =", fib_calls_memo)


        # TOWER OF HANOI
        elif choice == 4:
            n = int(input("Enter number of disks: "))

            moves_stack.stack.clear()

            hanoi(n, 'A', 'B', 'C')

            print("Total moves stored in stack:", moves_stack.size())


        # BINARY SEARCH
        elif choice == 5:

            arr = list(map(int, input("Enter sorted numbers separated by space: ").split()))
            key = int(input("Enter element to search: "))

            index = binary_search(arr, key, 0, len(arr)-1)

            if index == -1:
                print("Element not found")
            else:
                print("Element found at index:", index)


        # EXIT
        elif choice == 6:
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Try again.")


# PROGRAM START
if __name__ == "__main__":
    main()