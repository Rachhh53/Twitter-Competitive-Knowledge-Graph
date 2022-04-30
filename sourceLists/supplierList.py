supplier_list_url = [
    "https://www.akamai.com/",
    "https://www.logmein.com/",
    "https://www.liveperson.com/",
    "https://synacor.com/",
    "https://www.smithmicro.com/",
    "https://qumu.com/",
    "https://www.worlds.com/",
    "https://www.voip-pal.com/",
    "https://www.ibm.com/us-en/",
]


# create supplier list objects
def get_supplier_list_objs():
    supplier_list_objs = []
    for supplier in supplier_list_url:
        name = input(f'What is the name you would like to assign {supplier}?: ')
        b = {
            "name": name,
            "url": supplier
        }
        supplier_list_objs.append(b)
    print("substitute List: ", supplier_list_objs)
    return supplier_list_objs


# # create other list in memory
# created_supplier_list_objects = get_supplier_list_objs()

supplier_objs = [
    {'name': 'Akamai', 'url': 'https://www.akamai.com/'},
    {'name': 'Logmein', 'url': 'https://www.logmein.com/'},
    {'name': 'Live Person', 'url': 'https://www.liveperson.com/'},
    {'name': 'Synacor', 'url': 'https://synacor.com/'},
    {'name': 'Smith Micro', 'url': 'https://www.smithmicro.com/'},
    {'name': 'Qumu', 'url': 'https://qumu.com/'},
    {'name': 'Worlds Incorporated', 'url': 'https://www.worlds.com/'},
    {'name': 'Voip-Pal', 'url': 'https://www.voip-pal.com/'},
    {'name': 'IBM', 'url': 'https://www.ibm.com/us-en/'}
]
