def count_names(names):
    counts = {}
    for name in names:
        if name in counts:
            counts[name] += 1
        else:
            counts[name] = 1
    return counts


class HashMap:
    def __init__(self):
        self.slots = [None, None]
        self.size = 0

    def _index(self, key):
        total = 0
        for char in key:
            total += ord(char)
        return total % len(self.slots)

    def _find_slot(self, key):
        index = self._index(key)
        checked = 0
        while checked < len(self.slots):
            pair = self.slots[index]
            if pair is None or pair[0] == key:
                return index
            index = (index + 1) % len(self.slots)
            checked += 1
        raise RuntimeError("HashMap is full")

    def put(self, key, value):
        index = self._find_slot(key)
        if self.slots[index] is None:
            self.size += 1
        self.slots[index] = (key, value)
        if self.size * 4 > len(self.slots) * 3:
            self._resize()

    def get(self, key, default=None):
        index = self._find_slot(key)
        pair = self.slots[index]
        if pair is None:
            return default
        return pair[1]

    def _resize(self):
        old_slots = self.slots
        self.slots = [None] * (2 * len(old_slots))
        self.size = 0
        for pair in old_slots:
            if pair is not None:
                self.put(pair[0], pair[1])


class DuplicateSolution:
    def containsDuplicate(self, nums):
        seen = {}
        for number in nums:
            if number in seen:
                return True
            seen[number] = True
        return False


class AnagramSolution:
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        counts = {}
        for char in s:
            counts[char] = counts.get(char, 0) + 1
        for char in t:
            if counts.get(char, 0) == 0:
                return False
            counts[char] -= 1
        return True


if __name__ == "__main__":
    names = ["Alice", "Brad", "Alice", "Collin", "Brad", "Alice"]
    counts = count_names(names)
    print("Name counts:", counts)
    repeated_names = [name for name in counts if counts[name] > 1]
    print("Repeated names:", repeated_names)
    print("Number of repeated names:", len(repeated_names))

    cities = HashMap()
    for name, city in [("Alice", "NYC"), ("Brad", "Chicago"),
                       ("Collin", "Seattle")]:
        cities.put(name, city)
        print("Slots:", cities.slots)
    print("Collin:", cities.get("Collin"))
    print("Bob:", cities.get("Bob", "Unknown"))
    cities.put("Brad", "Boston")
    print("Brad:", cities.get("Brad"))
    cities.put("Bob", "Miami")
    print("After resize:", cities.slots)

    print("Contains duplicate:",
          DuplicateSolution().containsDuplicate([1, 2, 3, 1]))
    print("Valid anagram:", AnagramSolution().isAnagram("aab", "aba"))
