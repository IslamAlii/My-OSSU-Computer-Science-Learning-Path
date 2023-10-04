def chop(lst):
    """Removes the first and last elements of the list."""
    if len(lst) >= 2:
        del lst[0]  # Remove the first element
        del lst[-1]  # Remove the last element
    else:
        # Handle the case where the list has fewer than 2 elements
        lst.clear()  # Clear the list

def middle(lst):
    """Returns a new list containing all but the first and last elements."""
    if len(lst) >= 2:
        return lst[1:-1]  # Slice the list to exclude the first and last elements
    else:
        # Handle the case where the list has fewer than 2 elements
        return []

# Example usage:
my_list = [1, 2, 3, 4, 5]
chop(my_list)
print(my_list)  # This will print: [2, 3, 4]

my_list = [1, 2, 3, 4, 5]
new_list = middle(my_list)
print(new_list)  # This will print: [2, 3, 4]
