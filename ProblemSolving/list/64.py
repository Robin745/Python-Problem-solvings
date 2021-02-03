
def my_zip(*iterables):
        # zip('ABCD', 'xy') --> Ax By
    sentinel = object()
    iterators = [iter(it) for it in iterables]
    while iterators:
        result = []
        for it in iterators:
            elem = next(it, sentinel)
            if elem is sentinel:
                return
            result.append(elem)
        yield tuple(result)

nums = [1, 2, 3]
colors = ['red', 'white', 'black']
for (a,b) in my_zip(nums, colors):
    print(a, b)