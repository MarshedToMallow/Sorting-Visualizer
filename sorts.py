import random

DEBUG = False

class Sortable:
    """Sortable - Manages the instructions produced by a Sort.
    """
    def __init__(self, data: list, colors: dict = {"Read":(255, 0, 0), "Write":(64, 64, 255), "Set":(255, 255, 255), "Swap":(255, 64, 255), "Compare":(255, 128, 255)}):
        self.data = data
        self.is_sorted: bool = False

        self.colors = colors
        self.colored: list = []

        self.comparison_count = 0
        self.write_count = 0
        self.swap_count = 0
        self.read_count = 0

        self.aux_write_count = 0
    
    def generate_random(data, *args, **kwargs):
        random.shuffle(data)
        return Sortable(data, *args, **kwargs)
    
    def read(self, index):
        self.colored = [(index, self.colors["Read"])]
        self.read_count += 1

        return self.data

    def reads(self, start_index, end_index): # Includes both end indices
        for index in range(start_index, end_index + 1):self.read(index)

        return self.data
    
    def write(self, index, value):
        self.colored = [(index, self.colors["Write"])]
        self.write_count += 1

        self.data[index] = value
        return self.data
    
    def swap(self, index_a, index_b):
        self.colored = [(index_a, self.colors["Swap"]), (index_b, self.colors["Swap"])]
        self.swap_count += 1

        self.data[index_a], self.data[index_b] = self.data[index_b], self.data[index_a]
        return self.data
    
    def set(self, new_sortable):

        self.colored = [("Set", self.colors["Set"])]
        self.write_count += len(self.data)

        self.data = new_sortable
        return self.data
    
    def compare(self, index_a, index_b):
        self.colored = [(index_a, self.colors["Compare"]), (index_b, self.colors["Compare"])]
        self.comparison_count += 1

        return self.data
    
    def sorted(self):
        self.is_sorted = True
    
    def not_sorted(self):
        self.is_sorted = False

    def draw(self):
        pass

class Sort:
    def __init__(self):
        pass

    def get_steps(self, input_list):
        pass

class BubbleSort(Sort):
    """Bubble Sort - Iterates over all elements, swapping them if the first element is larger than the second.
    """
    def __init__(self):
        super().__init__()
    
    def run(self, sortable: Sortable):

        while True:
            sortable.sorted()

            for index in range(len(sortable.data) - 1):
                yield sortable.read(index)
                yield sortable.read(index + 1)
                yield sortable.compare(index, index + 1)

                if sortable.data[index] > sortable.data[index + 1]:
                    yield sortable.swap(index, index + 1)
                    sortable.not_sorted()

            if sortable.is_sorted:break
        
        if DEBUG:print(sortable.data)

class InsertionSort(Sort):
    """Insertion Sort - Sorts by moving individual element to the correct position in the already sorted portion, starting with just the first element.
    """
    def __init__(self):
        super().__init__()
    
    def run(self, sortable: Sortable):

        index = 0
        while index < len(sortable.data) - 1:
            # Increment the index of the current element
            index += 1

            yield sortable.read(index)
            yield sortable.read(index + 1)
            yield sortable.compare(index, index + 1)

            # The order of the element is already correct
            if sortable.data[index - 1] <= sortable.data[index]:continue

            # Continue pushing the element until it reaches the correct spot
            for offset in range(index):
                b = index - offset
                a = b - 1

                yield sortable.read(a)
                yield sortable.read(b)
                yield sortable.compare(a, b)

                # The element has reached the correct position
                if sortable.data[a] <= sortable.data[b]:break

                yield sortable.swap(a, b)

        if DEBUG:print(sortable.data)

class SelectionSort(Sort):
    """Selection Sort - Sorts by moving the smallest element in the unsorted portion to the end of the sorted portion.
    """
    def __init__(self):
        super().__init__()
    
    def run(self, sortable: Sortable):

        for index in range(len(sortable.data) - 1):
            yield sortable.read(index)
            minimum = sortable.data[index], index

            # Find the minimum element in the unsorted section of the sortable
            for unsorted_index in range(index + 1, len(sortable.data)):
                yield sortable.read(unsorted_index)
                yield sortable.compare(minimum[1], unsorted_index)
                
                current = sortable.data[unsorted_index]
                if minimum[0] > current:minimum = current, unsorted_index

            # Place the minimum unsorted element at the end of the sorted section
            if index == minimum[1]:continue
            yield sortable.swap(index, minimum[1])
        
        if DEBUG:print(sortable.data)

class MergeSort(Sort):
    """Merge Sort - Sorts by merging adjacent sorted portions.
    This is done by selecting the smallest from either portion to put as the next element in the resulting portion.
    """
    def __init__(self):
        super().__init__()
    
    def run(self, sortable: Sortable, start_index = 0, end_index = None):
        
        if end_index is None:end_index: int = len(sortable.data)

        # Base Case
        if start_index + 1 == end_index:pass
        else:

            # Split into two halves, small indices and large indices
            length = end_index - start_index
            split_index = self.get_split(length) + start_index

            small_iter = self.run(sortable, start_index, split_index)
            for call in small_iter:yield call
            
            big_iter = self.run(sortable, split_index, end_index)
            for call in big_iter:yield call

            auxiliary = []
            small = sortable.data[start_index:split_index]
            big = sortable.data[split_index:end_index]

            small_index, big_index = 0, 0
            for _ in range(length):

                if small_index == len(small):
                    yield sortable.reads(split_index + big_index, split_index + len(big) - 1)
                    auxiliary += big[big_index:]
                    sortable.aux_write_count += len(big[big_index:])
                    break

                elif big_index == len(big):
                    yield sortable.reads(start_index + small_index, start_index + len(small) - 1)
                    auxiliary += small[small_index:]
                    sortable.aux_write_count += len(small[small_index:])
                    break

                elif small[small_index] <= big[big_index]:
                    yield sortable.read(start_index + small_index)
                    yield sortable.compare(start_index + small_index, split_index + big_index)
                    auxiliary.append(small[small_index])
                    sortable.aux_write_count += 1
                    small_index += 1

                else:
                    yield sortable.read(split_index + big_index)
                    yield sortable.compare(start_index + small_index, split_index + big_index)
                    auxiliary.append(big[big_index])
                    sortable.aux_write_count += 1
                    big_index += 1
            
            for offset, value in enumerate(auxiliary):
                yield sortable.write(start_index + offset, value)

    def get_split(self, sortable_length):
        index = 1
        while index < sortable_length:index <<= 1
        return index >> 1

class InPlaceMergeSort(Sort):
    """In-Place Merge Sort - Sorts by merging adjacent sorted portions without auxiliary memory.
    This is done by selecting the smallest from either portion to put as the next element in the resulting portion.
    """
    def __init__(self):
        super().__init__()
    
    def run(self, sortable: Sortable, start_index: int = 0, end_index: int = -1):
        
        if end_index == -1:end_index: int = len(sortable.data) - 1
        length = end_index - start_index + 1

        if length == 1:pass

        elif length == 2:
            yield sortable.read(start_index)
            yield sortable.read(end_index)
            yield sortable.compare(start_index, end_index)

            if sortable.data[start_index] > sortable.data[end_index]:
                yield sortable.swap(start_index, end_index)

        else:
            split_index: int = (length >> 1) + start_index

            for call in self.run(sortable, start_index, split_index - 1):
                yield call
            
            for call in self.run(sortable, split_index, end_index):
                yield call
            
            left_index = start_index
            right_index = split_index

            read_right = True

            for _ in range(start_index, end_index + 1):

                yield sortable.read(left_index)
                left = sortable.data[left_index]

                if read_right:
                    yield sortable.read(right_index)
                    right = sortable.data[right_index]
                    read_right = False
                
                sortable.compare(left_index, right_index)
                if right < left:
                    for dx in range(right_index - left_index):
                        yield sortable.swap(right_index - dx, right_index - dx - 1)
                    read_right = True
                    right_index += 1
                
                left_index += 1

                if left_index == right_index or right_index > end_index:break

class Quicksort(Sort):
    """Quicksort - Selects a random element and puts all elements on one side if they're smaller and the other side if they're larger.
    This is repeated recursively on the unsorted portions."""
    def __init__(self):
        super().__init__()
    
    def run(self, sortable: Sortable, start_index: int = 0, end_index: int = None):
        if end_index is None:end_index: int = len(sortable.data) - 1

        if start_index >= end_index:pass
        else:
            pivot_index = random.randint(start_index, end_index)
            yield sortable.read(pivot_index)
            pivot = sortable.data[pivot_index]

            if end_index != pivot_index:
                yield sortable.read(end_index)
                yield sortable.swap(pivot_index, end_index)

            item_from_left = start_index
            item_from_right = end_index - 1

            found_left = False
            found_right = False
            while item_from_left <= item_from_right:

                if not found_left:
                    yield sortable.read(item_from_left)
                    yield sortable.compare(item_from_left, pivot_index)
                    if sortable.data[item_from_left] > pivot:found_left = True
                    else:item_from_left += 1

                if not found_right:
                    yield sortable.read(item_from_right)
                    yield sortable.compare(item_from_right, pivot_index)
                    if sortable.data[item_from_right] < pivot:found_right = True
                    else:item_from_right -= 1

                if found_left and found_right:
                    yield sortable.swap(item_from_left, item_from_right)
                    found_left = False
                    found_right = False
                    item_from_left += 1
                    item_from_right -= 1
            
            if item_from_left != end_index:
                yield sortable.swap(item_from_left, end_index)

            for i in self.run(sortable, start_index, item_from_left - 1):
                yield i
                
            for i in self.run(sortable, item_from_left + 1, end_index):
                yield i

class Bogosort(Sort):
    """Bogosort - Sorts by shuffling the sortable until it is sorted.
    """
    def __init__(self):
        super().__init__()
    
    def run(self, sortable: Sortable):

        # Loops until sorted
        while True:

            # Checking each adjacent pair of values is in the correct order
            sortable.sorted()
            for i in range(len(sortable.data) - 1):
                yield sortable.read(i)
                yield sortable.read(i + 1)
                yield sortable.compare(i, i + 1)

                # If a pair of values is not in the correct order, sortable is not sorted
                if sortable.data[i] > sortable.data[i + 1]:
                    sortable.not_sorted()
                    break

            # Sortable is successfully sorted    
            if sortable.is_sorted:break

            # If it isn't sorted, randomize it
            temp = sortable.data.copy()
            random.shuffle(temp)
            yield sortable.set(temp)
            
        if DEBUG:print(sortable)

if __name__ == "__main__":
    # Sortable to be sorted
    s = list(range(16))
    random.shuffle(s)
    sortable = Sortable(s)
    print(sortable.data)

    # Sort object
    sort = Quicksort()

    # Sorting
    print("Starting sort of", len(s), "elements")
    step_count = 0
    for i in sort.run(sortable):
        step_count += 1
        #print(i, sortable.colored)
    print(sortable.data)
    print("Steps:", step_count)