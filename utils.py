# Useful functions for python

def concatenate_string(str_a, str_b):
  return str_a + str_b;

def value_in_string(string, value):
  exists = False;
  if value in string:
    exists = True
  return exists
