"""
    => Data type: Lists
    => Encapsulate with square braces []
    => Contain deplicate items
    => Items in a set have a defined order
    => Items can be referred to by index
    => Items can be changed, and added/removed
"""
my_list = ["January", "February", "March", "January"]
print(my_list[1])
my_list.append("April")
print(my_list)
my_list.remove("January")
print(my_list)
