import statistics

def median_of_list(lst):
    # Sorting the list in ascending order
    lst = sorted(lst)
    print("Sorted list: ", lst)
    # Calculating and returning the median of the list
    return statistics.median(lst)

list1 = [1, 3, 8, 4, 5]
list2 = [7, 9, 10, 11, 12, 2]
# Combining the two lists into one
list_three = list1 + list2
# Calculating and printing the median of the combined list
print(median_of_list(list_three))
