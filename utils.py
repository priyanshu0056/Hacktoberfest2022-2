# Useful functions for python

def concatenate_string(str_a, str_b):
  return str_a + str_b;

def value_in_string(string, value):
  exists = False;
  if value in string:
    exists = True
  return exists

def quicksort(array):
    if len(array) <= 1:
        return array
    else:
        return quicksort([x for x in array[1:] if x < array[0]])
        + [array[0]]
        + quicksort([x for x in array[1:] if x >= array[0]])
