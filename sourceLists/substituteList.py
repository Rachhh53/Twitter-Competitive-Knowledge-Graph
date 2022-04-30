substitute_list_url = [
    "https://www.quora.com/",
    "https://www.youtube.com/",
    "https://www.microsoft.com/en-us/",
    "https://about.facebook.com/meta/",
    "https://thewaltdisneycompany.com/",
    "https://www.expediagroup.com/home/default.aspx",
    "https://www.ebay.com/",
    "https://ir.yandex/",
    "https://www.gannett.com/",
    "https://scripps.com/",
    "https://www.nytco.com/",
    "https://www.liveperson.com/",
    "https://www.prodivnet.com/",
    "https://medium.com/",
    "https://mtch.com/",
    "https://www.spotify.com/us/",
    "https://www.costargroup.com/",
    "https://telegram.org/",
    "https://www.aboutamazon.com/",
]


# create substitute list objects
def get_substitute_list_objs():
    substitute_list_objs = []
    for substitute in substitute_list_url:
        name = input(f'What is the name you would like to assign {substitute}?: ')
        b = {
            "name": name,
            "url": substitute
        }
        substitute_list_objs.append(b)
    print("substitute List: ", substitute_list_objs)
    return substitute_list_objs


# # create other list in memory
# created_substitute_list_objects = get_substitute_list_objs()

substitute_objs = [
    {'name': 'Quora', 'url': 'https://www.quora.com/'},
    {'name': 'YouTube', 'url': 'https://www.youtube.com/'},
    {'name': 'Microsoft', 'url': 'https://www.microsoft.com/en-us/'},
    {'name': 'Meta Platforms', 'url': 'https://about.facebook.com/meta/'},
    {'name': 'Disney', 'url': 'https://thewaltdisneycompany.com/'},
    {'name': 'Expedia', 'url': 'https://www.expediagroup.com/home/default.aspx'},
    {'name': 'eBay', 'url': 'https://www.ebay.com/'},
    {'name': 'Yandex', 'url': 'https://ir.yandex/'},
    {'name': 'Gannett', 'url': 'https://www.gannett.com/'},
    {'name': 'E.W. Scripps Company', 'url': 'https://scripps.com/'},
    {'name': 'The New York Times', 'url': 'https://www.nytco.com/'},
    {'name': 'LivePerson', 'url': 'https://www.liveperson.com/'},
    {'name': 'Professional Diversity Network', 'url': 'https://www.prodivnet.com/'},
    {'name': 'Medium (website)', 'url': 'https://medium.com/'},
    {'name': 'Match.com', 'url': 'https://mtch.com/'},
    {'name': 'Spotify', 'url': 'https://www.spotify.com/us/'},
    {'name': 'CoStar Group', 'url': 'https://www.costargroup.com/'},
    {'name': 'Telegram (software)', 'url': 'https://telegram.org/'},
    {'name': 'Amazon', 'url': 'https://www.aboutamazon.com/'}
]