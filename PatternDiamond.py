s = "abcde"
f = "f"
reverse1 = s[::-1]
q = s + f + reverse1
print(q)
print(q.replace("f", " "))
print(q.replace("efe", "   "))
print(q.replace("defed", "     "))
print(q.replace("cdefedc", "       "))
print(q.replace("bcdefedcb", "         "))
print(q.replace("cdefedc", "       "))
print(q.replace("defed", "     "))
print(q.replace("efe", "   "))
print(q.replace("f", " "))
print(q)
