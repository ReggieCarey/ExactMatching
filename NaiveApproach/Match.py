class Match:

    def __init__(self):
        pass

    @staticmethod
    def match(t: str, p: str) -> list:
        c = 0
        n = len(t)
        m = len(p)
        results = list()
        for i in range(n - m + 1):
            NOMATCH = False
            for j in range(m):
                c += 1
                if p[j] != t[i + j]:
                    NOMATCH = True
                    break
            if not NOMATCH:
                results.append(i)
        print()
        print("Complexity =", c)
        print("n =", n)
        print("m =", m)
        print("nm - m^2 + m =", n*m-m**2+m)
        return results

# QUESTION:
# Does this algorithm always perform n*m - m^2 + m operations?  No the calculation represents an upper bound on the
# execution complexity.

# QUESTION:
# Assume we just want to find the first match, do you ever need nm-m^2+m operations?  Yes, in the degenerate case where
# the pattern almost matches the text.  In that case the runtime complexity level is reached.
