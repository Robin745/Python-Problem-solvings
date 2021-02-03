def multiplies(items):
    multiplies = 1
    for item in items:
        multiplies *= item
    return multiplies

print(multiplies([1,2,3]))