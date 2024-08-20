items = ["apple", "banana", "orange", "apple", "mango", "mango"]
uniqueItem = set()
for item in items:
    if item in uniqueItem:
        print("Duplicate item is",item)
    uniqueItem.add(item)
