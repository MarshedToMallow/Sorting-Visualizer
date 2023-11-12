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
        yield "Done"

class SelectionSort(Sort):
    """Selection Sort - Sorts by moving the smallest element in the unsorted portion to the end of the sorted portion.
    """
    def __init__(self):
        super().__init__()
    
    def get_steps(self, sortable):

        for index in range(len(sortable) - 1):
            yield f"Read {index}"
            minimum = sortable[index], index

            # Find the minimum element in the unsorted section of the sortable
            for unsorted_index in range(index + 1, len(sortable)):
                yield f"Read {unsorted_index}"
                yield f"Compare {minimum[1]} {unsorted_index}"
                
                current = sortable[unsorted_index]
                if minimum[0] > current:minimum = current, unsorted_index

            # Place the minimum unsorted element at the end of the sorted section
            if index == minimum[1]:continue
            yield f"Swap {index} {minimum[1]}"
            sortable[index], sortable[minimum[1]] = sortable[minimum[1]], sortable[index]
        
        yield "Done"
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
    # Sortable to be sorted
    sortable = list(range(6))
    random.shuffle(sortable)
    print(sortable)

    # Sort object
    print(SelectionSort.__doc__)
    sort = SelectionSort()

    # Sorting
    steps = sort.get_steps(sortable)
    print(len([i for i in steps]))