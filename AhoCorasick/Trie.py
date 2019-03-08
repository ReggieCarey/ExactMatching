"""
3.7 Dealing with multiple patterns – Aho-Corasick algorithm
-----------------------------------------------------------
So far we have managed to solve the exact matching problem efficiently when we only need to search one pattern
against a text. What happens, however, if we want to match multiple patterns against a same text? Can we do better
than matching each character to the text separately? This situation occurs quite commonly, e.g., when mapping all
the reads generated in a sequencing experiment against a genome.

Let us assume we have z patterns, each of length m, and we want to match them against a text of length n. The
trivial algorithm leads to a runtime of O(z(n + m)), which can be prohibitive for large values of z (e.g., millions
of sequences matched to a genome).

A first intuition behind the Aho-Corasick algorithm is the idea that we should exploit similarities between the
patterns as much as possible, the same way we've exploited self-similarity within the patterns in KMP and
Boyer-Moore. The datastructure we'll use is called a keyword tree – just a fancy word to say we'll construct a tree
structure that merges together patterns which have common prefixes (see below for patterns abcq, abcr, bcde, cd).
Each edge in this tree is labeled with one single character, and every path from the root to a leaf spells the
sequence of one of the patterns.
"""


class Trie:
    def __init__(self, parentLink=None):
        self.parentLink = parentLink
        self.failLink = None
        self.outputLink = None
        self.final = False
        self.children = dict()

    def add_patterns(self, patterns: list):
        for pattern in patterns:
            self.add_pattern(pattern)

    def add_pattern(self, pattern: str):
        node = root = self
        for ch in pattern:
            print(ch)
            if ch in node.children:
                node = node.children[ch]
            else:
                newNode = Trie(node)
                newNode.failLink = root
                node.children[ch] = newNode
                node = newNode
        node.final = True

    def traverse(self, indent):
        child_keys = list(self.children.keys())
        s = f"""parent = {self.parentLink}
{' '*indent}fail   = {self.failLink}
{' '*indent}output = {self.outputLink}
{' '*indent}final  = {self.final}
{' '*indent}children = {child_keys}
"""
        # print(s)
        for k in child_keys:
            s += f"""
{' '*indent}{k} : {self.children[k].traverse(indent+4)}
"""
        # print(s)
        return s

    # def __str__(self):
    #     return self.traverse(0)


ac = Trie()
ac.add_patterns(["ASDF"])
print(ac.traverse(0))
