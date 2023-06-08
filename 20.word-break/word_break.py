
def find_match(corpus, words):
    def check_true(current, words, mem):

        if current in mem:
            return mem[current]

        for word in words:
            if current.startswith(word):
                current = current[len(word):]
                mem[current]=check_true(current, words, mem)
                return mem[current]
            if not current:
                return True

        mem[current] = False
        return False
    mem = {}
    return check_true(corpus, words, mem)








if __name__ == "__main__":
    find_match("whataboutus", ["about", "what", "us"])