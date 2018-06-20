
movies = ["The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91,
          ["Graham Chapman", ["Michael Palin", "John Cleese", ["Terry Gilliam", "Eric Idle"], "Terry Jones"]]]

# print(movies)

# for each_item in movies:
#     if isinstance(each_item, list):
#         for nested_item in each_item:
#             if isinstance(nested_item, list):
#                 for item in nested_item:
#                     print(item)
#             else:
#                 print(nested_item)
#     else:
#         print(each_item)

def print_lol(the_list):
    if isinstance(the_list, list):
        for list_item in the_list:
            print_lol(list_item)
    else:
        print(the_list)


print_lol(movies)



