# Sorting Algorithm Visualizer

My own implementation of a sorting algorithm visualizer for various sorting algorithms.

# Implementation Progress

## Algorithms

- [x] [Bubble Sort](https://en.wikipedia.org/wiki/Bubble_sort)
- [x] [Selection Sort](https://en.wikipedia.org/wiki/Selection_sort)
- [x] [Insertion Sort](https://en.wikipedia.org/wiki/Insertion_sort)
- [x] [Merge Sort](https://en.wikipedia.org/wiki/Merge_sort)
- [ ] [Heapsort](https://en.wikipedia.org/wiki/Heapsort)
- [ ] [Introsort](https://en.wikipedia.org/wiki/Introsort)
- [ ] [Timsort](https://en.wikipedia.org/wiki/Timsort)
- [x] [Quicksort](https://en.wikipedia.org/wiki/Quicksort)
- [ ] [Radix Sort (LSD)](https://en.wikipedia.org/wiki/Radix_sort#Least_significant_digit)
- [x] [Bogosort](https://en.wikipedia.org/wiki/Bogosort)

### Variants

- [ ] [Insertion Sort (Binary Search)](https://en.wikipedia.org/wiki/Insertion_sort#Variants)
- [ ] Insertion Sort (Custom - Center Search)
- [ ] Insertion Sort (Custom - End and Center Search)
- [ ] Quicksort (Custom - Average Pivot)
- [ ] Quicksort (Custom - Triple Pivot)
- [ ] [Shellsort](https://en.wikipedia.org/wiki/Shellsort)*
- [ ] [Comb Sort](https://en.wikipedia.org/wiki/Comb_sort)*
- [ ] [Cocktail Shaker Sort](https://en.wikipedia.org/wiki/Cocktail_shaker_sort)*
- [ ] [Radix Sort (LSD Hybrid - Insertion Sort on small bins)](https://en.wikipedia.org/wiki/Sorting_algorithm#Radix_sort)
- [ ] [Bogobogosort](https://www.dangermouse.net/esoteric/bogobogosort.html)**

\* Variant of Bubble Sort

\*\* Variant of Bogosort

## Visualizer

- [x] Basic Visualizer
- [x] Colored Changes
- [ ] Operation Stats

## Code

- [ ] Full Comments and Docstrings
- [ ] Code Cleanup

# Custom Sorting Algorithms

## Insertion Sort (Custom - Center Search)

Rather than searching from the end, the search begins in the middle of the sorted portion.  It then moves in the relevant direction based on the comparison between the middle element and the element being inserted.

## Insertion Sort (Custom - End and Center Search)

Includes both Center Search and a search from both the small and large ends of the sorted portion.

## Quicksort (Custom - Average Pivot)

Rather than choosing an entirely random element, all elements are averaged and the pivot is chosen as the element closest to the average.

## Quicksort (Custom - Triple Pivot)

Rather than a single random pivot, three random elements are picked and the element between the other two is then selected as the pivot.
The intention is to get an element which is likely closer to the median.