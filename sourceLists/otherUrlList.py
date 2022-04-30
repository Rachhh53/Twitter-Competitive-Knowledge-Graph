other_url_list = [
    'https://twitter.com'
]


# create other list objects
def get_other_list_objs():
    other_list_objs = []
    for other in other_url_list:
        name = input(f'What is the name you would like to assign {other}?: ')
        b = {
            "name": name,
            "url": other
        }
        other_list_objs.append(b)
    print("Other List: ", other_list_objs)
    return other_list_objs


# # create other list in memory
# created_other_list_objects = get_other_list_objs()

other_objs = [
    {'name': 'Twitter', 'url': 'https://twitter.com'}
]