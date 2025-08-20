class MyRange:
    def __init__(self, start, end, step=1):
        self.start = start
        self.end = end
        self.step = step

    def __iter__(self):
        current = self.start
        while current < self.end:
            yield current     # genera el valor bajo demanda
            current += self.step

# Uso
for x in MyRange(0, 5):
    print(x)

