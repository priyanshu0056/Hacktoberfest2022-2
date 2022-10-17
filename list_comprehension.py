# list of characters creation using list comprehension
build_char_list = [ char for char in "comprehension" ]
print(build_char_list)

# Define a tuple of multi-million companies
companies_tuple = ("Facebook","Google", "Twitter", "IBM","Apple", "HP", "DELL")

# use list comprehension to create a list from tuple 
companies_list = [ site for site in companies_tuple ]
print(companies_list)
