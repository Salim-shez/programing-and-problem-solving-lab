#Write a Python program to perform union, intersection and difference operations on Set A and Set B.
a = list(map(int,input("Set A: ").split()))
A = set(a)
b = list(map(int,input("Set B: ").split()))
B = set(b)

# Write your code here to perform different operations-B
union=A.union(B)
inter=A.intersection(B)
diff=A-B
print("Union: ",union)
print("Intersection: ",inter)
print("Difference: ",diff)
