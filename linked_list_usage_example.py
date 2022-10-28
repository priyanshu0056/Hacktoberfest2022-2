# Linked-List Usage example
import linked_list

s = linked_list() # Create a Linked-List

# Add values to linked-list
s.add_first(4)
s.add_next(3)
s.add_first(7)
s.add_next(2)
s.add_next(1)
s.add_next(9)

s.print_list() # Default list print
s.print_list(separator = " - ") # List print with custom separator
