import random

class Sort:
    def __init__(self):
        pass

    def get_steps(self, input_list):
        pass

class Bogosort(Sort):
    """Bogosort - Sorts by shuffling the sortable until it is sorted.
    """
    def __init__(self):
        super().__init__()
    
    def get_steps(self, sortable):

        # Loops until sorted
        while True:

            # Checking each adjacent pair of values is in the correct order
            sort = True
            for i in range(len(sortable) - 1):
                yield f"Read {i}"
                yield f"Read {i + 1}"
                yield f"Compare {i} {i + 1}"
                # If a pair of values is not in the correct order, sortable is not sorted
                if sortable[i] > sortable[i + 1]:
                    sort = False
                    break

            # Sortable is successfully sorted    
            if sort:
                yield "Done"
                break

            # If it isn't sorted, randomize it
            random.shuffle(sortable)
            yield f"Set {sortable}"

if __name__ == "__main__":
    print(Bogosort.__doc__)
    """
    sort = Bogosort()
    for i in sort.get_steps([i for i in range(1, 10)] + [0]):
        print(i)
    """