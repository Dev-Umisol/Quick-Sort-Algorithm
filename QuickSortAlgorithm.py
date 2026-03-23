def quick_sort(lst):
    """ 
    Sorts a list of integers using the quicksort algorithm 
    Args: lst: list of integers to sort
    Returns: a new sorted list from least to greatest
    """
    # base case for recursion
    if len(lst) <= 1:
        return lst
    
    pivot = lst[0] # <-- Take the first element
    
    # Partition into three sublists based on pivot
    pivot_less = [element for element in lst if element < pivot]
    pivot_equal = [element for element in lst if element == pivot]
    pivot_greater = [element for element in lst if element > pivot]
    
    # Recursively sort the less and greater sublists
    lesser_new_sort = quick_sort(pivot_less) 
    greater_new_sort = quick_sort(pivot_greater) 
    
    sorted_lst = lesser_new_sort + pivot_equal + greater_new_sort # concatenate all the sorted lists together
    
    return sorted_lst

# --> Example Usage <--
print(quick_sort([20, 3, 14, 1, 5]))
print(quick_sort([83, 4, 24, 2]))
print(quick_sort([4, 42, 16, 23, 15, 8]))
print(quick_sort([87, 11, 23, 18, 18, 23, 11, 56, 87, 56]))