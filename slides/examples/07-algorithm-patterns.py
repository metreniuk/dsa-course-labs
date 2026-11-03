import ast


class ExpressionNode:
    def __init__(self, label, left=None, right=None):
        self.label = label
        self.left = left
        self.right = right


def single_number(nums):
    result = 0
    for value in nums:
        result ^= value
    return result


def subsets(nums):
    result = []
    path = []

    def visit(index):
        if index == len(nums):
            result.append(path.copy())
            return

        visit(index + 1)

        path.append(nums[index])
        visit(index + 1)
        path.pop()

    visit(0)
    return result


def factorial_recursive(n):
    if n == 0:
        return 1
    return n * factorial_recursive(n - 1)


def factorial_dp(n):
    fact = [1] * (n + 1)
    for i in range(1, n + 1):
        fact[i] = i * fact[i - 1]
    return fact[n]


def climb_stairs_memo(n):
    memo = {0: 1, 1: 1}

    def ways(steps):
        if steps in memo:
            return memo[steps]

        memo[steps] = ways(steps - 1) + ways(steps - 2)
        return memo[steps]

    return ways(n)


def climb_stairs(n):
    ways = [0] * (n + 1)
    ways[0] = 1
    if n >= 1:
        ways[1] = 1

    for step in range(2, n + 1):
        ways[step] = ways[step - 1] + ways[step - 2]

    return ways[n]


def dijkstra(graph, start):
    distance = {city: float("inf") for city in graph}
    previous = {city: None for city in graph}
    settled = set()
    distance[start] = 0

    while True:
        current = None
        for city in graph:
            if city in settled:
                continue
            if current is None or distance[city] < distance[current]:
                current = city

        if current is None or distance[current] == float("inf"):
            break

        settled.add(current)
        for neighbor, cost in graph[current]:
            if neighbor in settled:
                continue
            candidate = distance[current] + cost
            if candidate < distance[neighbor]:
                distance[neighbor] = candidate
                previous[neighbor] = current

    return distance, previous


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True

    def _find_node(self, text):
        node = self.root
        for char in text:
            if char not in node.children:
                return None
            node = node.children[char]
        return node

    def search(self, word):
        node = self._find_node(word)
        return node is not None and node.is_word

    def startsWith(self, prefix):
        return self._find_node(prefix) is not None


class TinyBloomFilter:
    def __init__(self):
        self.bits = 0

    def add_positions(self, positions):
        for position in positions:
            self.bits |= 1 << position

    def might_contain_positions(self, positions):
        for position in positions:
            if (self.bits & (1 << position)) == 0:
                return False
        return True


def main():
    print('Expression tree')
    multiply = ExpressionNode("*", ExpressionNode("3"), ExpressionNode("4"))
    root = ExpressionNode("+", ExpressionNode("2"), multiply)
    print(root.label, root.left.label, root.right.label)

    print('Python AST')
    source = "result = 2 + 3 * 4"
    tree = ast.parse(source)
    assignment = tree.body[0]
    print(ast.dump(assignment.value, indent=2))

    print('Bit flags')
    flags = 0
    read_flag = 1 << 0
    write_flag = 1 << 1
    flags |= read_flag
    flags |= write_flag
    print((flags & write_flag) != 0)
    flags ^= write_flag
    print((flags & write_flag) != 0)

    print('Single Number')
    print(single_number([4, 1, 2, 1, 2]))

    print('Subsets')
    print(subsets([1, 2, 3]))

    print('Factorial: recursion and tabulation')
    print(factorial_recursive(5), factorial_dp(5))

    print('Memoization')
    print(climb_stairs_memo(5))

    print('Tabulation')
    print(climb_stairs(5))

    print('Dijkstra city routes')
    graph = {
        "A": [("B", 1), ("C", 10), ("D", 4)],
        "B": [("A", 1), ("C", 1), ("D", 6)],
        "C": [("A", 10), ("B", 1), ("D", 1)],
        "D": [("A", 4), ("B", 6), ("C", 1)],
    }
    distance, previous = dijkstra(graph, "A")
    print(distance)
    route = []
    city = "D"
    while city is not None:
        route.append(city)
        city = previous[city]
    route.reverse()
    print(route)

    print('Trie')
    trie = Trie()
    trie.insert("car")
    trie.insert("cat")
    trie.insert("dog")
    print(trie.search("car"))
    print(trie.search("ca"))
    print(trie.startsWith("ca"))
    trie.insert("ca")
    print(trie.search("ca"))

    print('Bloom filter')
    positions = {
        "cat": [1, 4],
        "dog": [2, 4],
        "owl": [3, 6],
        "cow": [1, 2],
    }
    bloom = TinyBloomFilter()
    exact_keys = {"cat", "dog"}
    bloom.add_positions(positions["cat"])
    bloom.add_positions(positions["dog"])
    for key in ["cat", "owl", "cow"]:
        possible = bloom.might_contain_positions(positions[key])
        print(key, possible)
        if possible:
            print("Exact lookup:", key in exact_keys)


if __name__ == "__main__":
    main()
