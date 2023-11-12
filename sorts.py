import random
import copy

class Sortable:
    """Sortable - Manages the instructions produced by a Sort.
    """
    def __init__(self, sortable, colors = {"Read":(255, 0, 0), "Write":(64, 64, 255), "Set":(255, 255, 255), "Swap":(64, 64, 255), "Compare":(255, 255, 0)}):
        self.sortable = sortable
        self.colors = colors
        self.is_integer = all([type(i) is int for i in sortable])
    
    def run_steps(self, sort, debug = False):

        sortable = copy.deepcopy(self.sortable)

        for instruction in sort.get_steps(self.sortable):
            args = instruction.split(" ")
            count = instruction.count(" ")

            if args[0] == "Set":
                new_sortable = "".join(args[1:])[1:-1].split(",")
                new_sortable = [self.str_to_num(i) for i in new_sortable]
            elif count == 1:a = int(args[1][1:])
            elif count == 2:
                a = int(args[1][1:])
                b = args[2]
                if b[0] == "$":b = int(b[1:])
                else:b = self.str_to_num(b)

            # yield (instruction_type, affected_indices, color, sortable, is_sortable_changed)

            if args[0] == "Read":
                if debug:print(f"Sortable[{a}] ({sortable[a]})")
                yield ("Read", set((a,)), self.colors["Read"], sortable, False)

            elif args[0] == "Write":
                sortable[a] = b
                if debug:print(f"Sortable[{a}] <- {b}")
                yield ("Write", set((a,)), self.colors["Write"], sortable, True)

            elif args[0] == "Swap":
                sortable[a], sortable[b] = sortable[b], sortable[a]
                if debug:print(f"Sortable[{b}] ({sortable[b]}) <-> Sortable[{a}] ({sortable[a]})")
                yield ("Swap", set((a, b)), self.colors["Swap"], sortable, True)

            elif args[0] == "Set":
                sortable = new_sortable.copy()
                if debug:print(f"Sortable <- {new_sortable}")
                yield ("Set", None, self.colors["Set"], sortable, True)

            elif args[0] == "Compare":
                if debug:print(f"Sortable[{a}] ({sortable[a]}) vs Sortable[{b}] ({sortable[b]})")
                yield ("Compare", set((a, b)), self.colors["Compare"], sortable, False)

            elif args[0] == "Done":
                if debug:print(f"Done | {sortable}")
                yield ("Done", None, None, sortable, False)
        
        print(sortable)
    
    def str_to_num(self, string):
        return int(string) if self.is_integer else float(string)

class Sort:
    def __init__(self):
        pass

    def get_steps(self, input_list):
        pass

# ---Instructions---
# Read $a - Read the value at index a
# Write $a b - Write b to index a
# Swap $a $b - Swap the values at index a and index b
# Set a - Set the sortable to the new sortable a
# Compare $a $b - Compare the values at index a and index b
# Done - Sorting is done

DEBUG = False

class BubbleSort(Sort):
    """Bubble Sort - Iterates over all elements, swapping them if the first element is larger than the second.
    """
    def __init__(self):
        super().__init__()
    
    def get_steps(self, sortable):

        while True:
            is_sorted = True

            for index in range(len(sortable) - 1):
                yield f"Read ${index}"
                yield f"Read ${index + 1}"
                yield f"Compare ${index} ${index + 1}"

                if sortable[index] > sortable[index + 1]:
                    yield f"Swap ${index} ${index + 1}"
                    is_sorted = False
                    sortable[index], sortable[index + 1] = sortable[index + 1], sortable[index]

            if is_sorted:
                yield "Done"
                break
        
        if DEBUG:print(sortable)

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

            yield f"Read ${index}"
            yield f"Read ${index + 1}"
            yield f"Compare ${index} ${index + 1}"

            # The order of the element is already correct
            if sortable[index - 1] <= sortable[index]:continue

            # Continue pushing the element until it reaches the correct spot
            for offset in range(index):
                b = index - offset
                a = b - 1

                yield f"Read ${a}"
                yield f"Read ${b}"
                yield f"Compare ${a} ${b}"

                # The element has reached the correct position
                if sortable[a] <= sortable[b]:break

                yield f"Swap ${a} ${b}"
                sortable[a], sortable[b] = sortable[b], sortable[a]
        yield "Done"
        if DEBUG:print(sortable)

class SelectionSort(Sort):
    """Selection Sort - Sorts by moving the smallest element in the unsorted portion to the end of the sorted portion.
    """
    def __init__(self):
        super().__init__()
    
    def get_steps(self, sortable):

        for index in range(len(sortable) - 1):
            yield f"Read ${index}"
            minimum = sortable[index], index

            # Find the minimum element in the unsorted section of the sortable
            for unsorted_index in range(index + 1, len(sortable)):
                yield f"Read ${unsorted_index}"
                yield f"Compare ${minimum[1]} ${unsorted_index}"
                
                current = sortable[unsorted_index]
                if minimum[0] > current:minimum = current, unsorted_index

            # Place the minimum unsorted element at the end of the sorted section
            if index == minimum[1]:continue
            yield f"Swap ${index} ${minimum[1]}"
            sortable[index], sortable[minimum[1]] = sortable[minimum[1]], sortable[index]
        
        yield "Done"
        if DEBUG:print(sortable)

class MergeSort(Sort):
    """Merge Sort - Sorts by merging adjacent sorted portions.
    This is done by selecting the smallest from either portion to put as the next element in the resulting portion.
    """
    def __init__(self):
        super().__init__()
    
    def get_steps(self, sortable):
        instructions, sortable = self.merge(sortable, 0)
        for instruction in instructions:
            yield instruction
        yield "Done"
        #print(sortable)

    def merge(self, sortable, offset):
        if len(sortable) == 1:
            #print(sortable)
            return [[f"Read ${offset}"], sortable]
        else:
            split_index = self.get_split(len(sortable))

            instructions_a, a = self.merge(sortable[:split_index], 0)
            instructions_b, b = self.merge(sortable[split_index:], split_index)

            instructions = instructions_a + instructions_b

            offset_a, offset_b = offset, len(a) + offset
            index_a, index_b = 0, 0
            auxiliary = []

            for i in range(len(a) + len(b)):

                # a or b have been exhausted

                if index_a == len(a):
                    for j in range(index_b, len(b)):
                        instructions.append(f"Write ${j + offset_b} {b[j]}")
                        auxiliary.append(b[j])
                    #print(auxiliary)
                    return [instructions, auxiliary]

                elif index_b == len(b):
                    for j in range(index_a, len(a)):
                        instructions.append(f"Write ${j + offset_a} {a[j]}")
                        auxiliary.append(a[j])
                    #print(auxiliary)
                    return [instructions, auxiliary]
                
                # Pick the smaller of the smallest value in a and b
                
                instructions += [
                    f"Read ${index_a + offset_a}",
                    f"Read ${index_b + offset_b}",
                    f"Compare ${index_a + offset_a} ${index_b + offset_b}"
                ]

                if a[index_a] <= b[index_b]:
                    instructions.append(f"Write ${i + offset} {a[index_a]}")
                    auxiliary.append(a[index_a])
                    index_a += 1

                else:
                    instructions.append(f"Write ${i + offset} {b[index_b]}")
                    auxiliary.append(b[index_b])
                    index_b += 1

    def get_split(self, sortable_length):
        index = 1
        while index < sortable_length:
            index <<= 1
        return index >> 1

class Quicksort(Sort):
    """Quicksort - Selects a random element and puts all elements on one side if they're larger and the other side if they're smaller.
    This is repeated recursively on the unsorted portions."""
    def __init__(self):
        super().__init__()
    
    def get_steps(self, sortable):
        pass

    def get_pivot(self, sortable_length):
        return random.randint(0, sortable_length - 1)

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
                yield f"Read ${i}"
                yield f"Read ${i + 1}"
                yield f"Compare ${i} ${i + 1}"

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
        if DEBUG:print(sortable)

if __name__ == "__main__":
    # Sortable to be sorted
    s = list(range(512))
    random.shuffle(s)
    sortable = Sortable(s)
    print(sortable.sortable)

    # Sort object
    #print(BubbleSort.__doc__)
    sort = MergeSort()

    # Sorting
    sorting = sortable.run_steps(sort)
    steps = []
    for i in sorting:
        steps.append(i)
    print("Steps:", len(steps))
    print("Modifying Steps:", len([i for i in steps if i[-1]]))