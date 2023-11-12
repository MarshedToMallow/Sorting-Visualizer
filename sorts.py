import random

class Sort:
    def __init__(self):
        pass

    def get_steps(self, input_list):
        pass

class InsertionSort(Sort):
    """Insertion Sort - Sorts by moving individual element to the correct position in the already sorted portion, starting with just the first element.
    """
    def __init__(self):
        super().__init__()
    
    def get_steps(self, sortable):

        index = 0
        while index < len(sortable) - 1:
            # Increment the index of the current element
            index += 1

            yield f"Read {index}"
            yield f"Read {index + 1}"
            yield f"Compare {index} {index + 1}"

            # The order of the element is already correct
            if sortable[index - 1] <= sortable[index]:continue

            # Continue pushing the element until it reaches the correct spot
            for offset in range(index):
                b = index - offset
                a = b - 1

                yield f"Read {a}"
                yield f"Read {b}"
                yield f"Compare {a} {b}"

                # The element has reached the correct position
                if sortable[a] <= sortable[b]:break

                yield f"Swap {a} {b}"
                sortable[a], sortable[b] = sortable[b], sortable[a]
        print(sortable)

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
    """
    print(Bogosort.__doc__)
    sort = Bogosort()
    for i in sort.get_steps([i for i in range(1, 10)] + [0]):
        print(i)
    """

    print(InsertionSort.__doc__)
    sort = InsertionSort()
    sortable = list(range(4))
    random.shuffle(sortable)
    print(sortable)
    steps = sort.get_steps(sortable)
    print(len([i for i in steps]))