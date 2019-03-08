import sys


class ZAlgorithm:
    def __init__(self, p, t=None):
        self.p = p
        self.t = t
        self.count = 0

    def Z_fast(self):
        """
        For a text T, let us define a simple function Z_naive that captures the  internal structure of the text.
        Specifically, for every position i \in (0,n] in T, we define Z_naive[i] to be the length of the longest
        prefix of T[i..n] that matches exactly a prefix of T[0..n]. We also define Z_naive[0] = 0.  Here's an
        example:

            Text:   A T T C A C T A T T C G G C T A T
            Z[i]:   0 0 0 0 1 0 0 4 0 0 0 0 0 0 0 2 0

        :return: Z the computed values

        TODO:  There is a bug in this code.  It should have an cost O(n) but I find the algorithm ends up having
        a cost O(n+x) where x is some value x >= 0.
        """
        T = self.p if self.t is None else self.p + "$" + self.t
        n = len(T)
        self.count = 0
        plen = len(self.p)
        matches = list()

        def EQ(a, b):
            self.count += 1
            return a == b

        Z = [0] * n
        maxZ = 0
        j = 0
        for i in range(1, n):
            if maxZ < i:
                Z[i] = 0
                l = Z[i]
                while i + l < n and EQ(T[i + l], T[l]):
                    Z[i] += 1
                    l += 1
                maxZ = i + Z[i]
                j = i
            else:
                k = i - j
                if Z[k] + i < maxZ:  # CASE 1
                    Z[i] = Z[k]
                elif Z[k] + i > maxZ:  # CASE 2
                    Z[i] = maxZ - i
                else:  # CASE 3   z[k] + i = maxZ
                    Z[i] = maxZ - i
                    l = Z[i]
                    while i + l < n and EQ(T[i + l], T[l]):
                        Z[i] += 1
                        l += 1
                    maxZ = i + Z[i]
                    j = i
            if Z[i] == plen:
                matches.append(i - plen - 1)

        return Z, matches

    # Question: check the algorithm and correct any off by 1 errors
    # Question: Why is this algorithm efficient?

    def Z_naive(self):
        """
        For a text T, let us define a simple function Z_naive that captures the  internal structure of the text.
        Specifically, for every position i \in (0,n] in T, we define Z_naive[i] to be the length of the longest
        prefix of T[i..n] that matches exactly a prefix of T[0..n]. We also define Z_naive[0] = 0.  Here's an
        example:

            Text:   A T T C A C T A T T C G G C T A T
            Z_naive[i]:   0 0 0 0 1 0 0 4 0 0 0 0 0 0 0 2 0

        :return: Z_naive the computed values
        """
        T = self.p if self.t is None else self.p + "$" + self.t
        n = len(T)
        self.count = 0

        Z = [0 for _ in range(n)]
        pos = 1
        while pos < n:
            while pos + Z[pos] < n and T[pos + Z[pos]] == T[Z[pos]]:
                Z[pos] += 1
            pos += 1
        # print("NAIVE complexity", self.count, "- len of T", n)
        # print(" ".join(T))
        # print(" ".join(str(i) for i in Z))
        # sys.stdout.flush()
        return Z


def doZAlgorithm(alg, goal):
    print()
    z, m = alg.Z_fast()
    if alg.t is None:
        print(f"text '{alg.p}', n = {len(alg.p)}")
    else:
        print(f"pattern '{alg.p}', m = {len(alg.p)}")
        print(f"text '{alg.t}', n = {len(alg.t)}")

    T = alg.p if alg.t is None else alg.p + "$" + alg.t
    n = len(T)

    print(f"Runtime complexity = O({alg.count}).  len(T) = {n}")
    print("TEXT:   " + " ".join((" " * (len(str(i)) - 1)) + f"{t}" for t, i in zip(T, z)))
    print("ACTUAL: " + " ".join(str(i) for i in z))
    sys.stdout.flush()
    try:
        assert z == goal
    except AssertionError:
        for _ in range(1000000):
            pass
        print("ASSERT: " + " ".join(str(i) for i in goal), file=sys.stderr)
    if m:
        print("Matches found at locations", m)


try:
    p = "ATAT"
    t = "GATATATGCATATACTT"
    alg = ZAlgorithm(p, t)
    goal = alg.Z_naive()
    doZAlgorithm(alg, goal)

    # t = "ATTCACTATTCGGCTAT"
    # alg = ZAlgorithm(t)
    # goal = alg.Z_naive()  # [0, 0, 0, 0, 1, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 2, 0]
    # doZAlgorithm(alg, goal)
    #
    # t = "ATTCACTATTCGGCTATATTCACTAATTCACTATTCGGCTATATTCACTA"
    # alg = ZAlgorithm(t)
    # goal = alg.Z_naive()  # [0, 0, 0, 0, 1, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 2, 0, 8, 0, 0, 0, 1, 0, 0, 1, 25, 0, 0, 0, 1,
    # # 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 2, 0, 8, 0, 0, 0, 1, 0, 0, 1]
    # doZAlgorithm(alg, goal)
    #
    # t = "ASDFDSAFAFSDSAASFFSDSADFFASDDSFFSSADSDFFSSAFSDSASFGFDAAFFDAASFDSADFDSFSDSSASADFDSFDFSDFDFDAASD"
    # alg = ZAlgorithm(t)
    # goal = alg.Z_naive()  # [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 3, 0, 0, 0, 0,
    # # 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 2, 0, 0, 0, 0, 1, 0, 0, 0,
    # # 0, 0, 0, 0, 0, 0, 2, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 3, 0, 0]
    # doZAlgorithm(alg, goal)
    #
    # t = "ABABABABAB"
    # alg = ZAlgorithm(t)
    # goal = alg.Z_naive()  # [0, 0, 8, 0, 6, 0, 4, 0, 2, 0]
    # doZAlgorithm(alg, goal)
    #
    # t = "AAAAAAAAAA"
    # alg = ZAlgorithm(t)
    # goal = alg.Z_naive()  # [0, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    # doZAlgorithm(alg, goal)
    #
    # t = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
    # alg = ZAlgorithm(t)
    # goal = alg.Z_naive()  # [0, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38,
    # # 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10,
    # # 9, 8, 7, 6, 5, 4, 3, 2, 1]
    # doZAlgorithm(alg, goal)
    #
    # t = "TAAAAAAAAA"
    # alg = ZAlgorithm(t)
    # goal = alg.Z_naive()  # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # doZAlgorithm(alg, goal)
    #
    # p = "abc"
    # t = "xabcabzabc"
    # alg = ZAlgorithm(p, t)
    # goal = alg.Z_naive()  # [0, 0, 0, 0, 0, 3, 0, 0, 2, 0, 0, 3, 0, 0]
    # doZAlgorithm(alg, goal)
    #
    # t = "aabxaabxcaabxaabxay"
    # alg = ZAlgorithm(t)
    # goal = alg.Z_naive()  # [0, 1, 0, 0, 4, 1, 0, 0, 0, 8, 1, 0, 0, 5, 1, 0, 0, 1, 0]
    # doZAlgorithm(alg, goal)

except AssertionError as e:
    sys.stdout.flush()
    # induce a delay
    for i in range(1000000):
        pass
    raise e
except IndexError as e:
    sys.stdout.flush()
    # induce a delay
    for i in range(1000000):
        pass
    raise e
