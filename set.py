my_set = {1,2,3,3,3}
print(my_set)

java = {"유재석", "김태호", "조세호"}
python = set(["유재석", "하하"])

print(java.intersection(python))
print(java & python)

print(java.union(python))
print(java | python)

print(java - python)
print(java.difference(python))

python.add("김태호")
print(python)

java.remove("김태호")
print(java)