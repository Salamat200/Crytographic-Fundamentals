# Modular addition
def m_add(a, b):
    return (a + b) % 26

# Modular subtraction
def m_sub(a, b):
    return (a - b) % 26

# from Question 1
print("25 + 15 mod 26 =", m_add(25, 15))
print("8 - 20 mod 26 =", m_sub(8, 20))
