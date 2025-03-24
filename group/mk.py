def add(a, b):
    """Return the sum of two integers."""
    return a + b

def text_add(s1, s2):
    """Return the concatenation of two strings."""
    return s1 + s2

if __name__ == "__main__":
    # Testing integer addition
    print("Integer Addition (5 + 3):", add(5, 3))
    
    # Testing textual addition
    print("Textual Addition ('abs' + 'ent'):", text_add("abs", "ent"))
