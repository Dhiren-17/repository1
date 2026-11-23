"""Examples of indexing and slicing in Python."""

items = [10, 20, 30, 40, 50]

# Indexing selects one item; indexes start at 0.
print(items[0])   # 10
print(items[-1])  # 50 (last item)

# Slicing uses sequence[start:stop:step]; stop is excluded.
print(items[1:4])   # [20, 30, 40]
print(items[:3])    # [10, 20, 30]
print(items[2:])    # [30, 40, 50]
print(items[::2])   # [10, 30, 50]
print(items[::-1])  # [50, 40, 30, 20, 10]

text = "Python"
print(text[1])    # y
print(text[1:4])  # yth
