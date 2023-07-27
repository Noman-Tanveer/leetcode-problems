class Trie:
    def __init__(self):
        self.root={}

    def insert(self, word: str) -> None:
        cur = self.root
        for l in word:
            if l not in cur:
                cur[l] = {}
            cur = cur[l]
        cur['*'] = ""

    def search(self, word: str) -> bool:
        cur = self.root
        for l in word:
            if l not in cur:
                return False
            cur = cur[l]
        return '*' in cur

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for l in prefix:
            if l not in cur:
                return False
            cur = cur[l]
        return True
