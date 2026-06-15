items = [('apple', 5), ('banana', 2), ('cherry', 8), ('date', 3)]
items.sort(key=lambda x:x[1])
print(items)
most=max(items,key=lambda i:i[1])
print(most)