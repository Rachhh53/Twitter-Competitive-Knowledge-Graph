new_entrant_list_urls = [
    "https://slack.com/",
    "https://discord.com/",
    "https://truthsocial.com/",
    "https://joinmastodon.org/",
    "https://www.care2.com/",
    "https://ello.co/",
    "https://the-dots.com/",
    "https://www.plurk.com/portal/",
    "https://www.soup.io/",
    "https://wt.social/",
    "https://www.clubhouse.com/",
    "https://www.kooapp.com/",
    "https://aminoapps.com/",
    "https://getaether.net/",
    "https://www.peeks.com/",
    "https://www.twitch.tv/",
    "https://app.net/",
    "https://www.caffeine.tv/",
    "https://www.shopify.com/",
    "https://tinder.com/",
    "https://withkoji.com/",
    "https://genies.com/",
    "https://rally.io/",
    "https://ooooo.com/",
    "https://pearpop.com/",
    "https://www.launchhouse.com/",
    "https://www.lumanu.com/",
    "https://faveforfans.com/",
    "https://www.kuaishou.com/en",
    "https://www.skype.com/en/",
    "https://www.microsoft.com/en-us/microsoft-teams/group-chat-software",
    "https://www.aboutamazon.com/",
    "https://abc.xyz/",
    "https://www.hulu.com/",
    "https://www.netflix.com/"
]


# create new_entrant list objects
def get_new_entrant_list_objs():
    new_entrant_list_objs = []
    for new_entrant in new_entrant_list_urls:
        name = input(f'What is the name you would like to assign {new_entrant}?: ')
        b = {
            "name": name,
            "url": new_entrant
        }
        new_entrant_list_objs.append(b)
    print("New Entrant List: ", new_entrant_list_objs)
    return new_entrant_list_objs


# # create new entrant list in memory
# created_new_entrant_list_objects = get_new_entrant_list_objs()

new_entrant_objs = [
    {'name': 'Slack', 'url': 'https://slack.com/'},
    {'name': 'Discord', 'url': 'https://discord.com/'},
    {'name': 'Truth Social', 'url': 'https://truthsocial.com/'},
    {'name': 'Mastodon social', 'url': 'https://joinmastodon.org/'},
    {'name': 'Care2', 'url': 'https://www.care2.com/'},
    {'name': 'Ello (social network)', 'url': 'https://ello.co/'},
    {'name': 'The Dots', 'url': 'https://the-dots.com/'},
    {'name': 'Plurk', 'url': 'https://www.plurk.com/portal/'},
    {'name': 'Soup.io', 'url': 'https://www.soup.io/'},
    {'name': 'WT Social', 'url': 'https://wt.social/'},
    {'name': 'Clubhouse (app)', 'url': 'https://www.clubhouse.com/'},
    {'name': 'Kooapp', 'url': 'https://www.kooapp.com/'},
    {'name': 'Amino (app)', 'url': 'https://aminoapps.com/'},
    {'name': 'Aether', 'url': 'https://getaether.net/'},
    {'name': 'Peek (software)', 'url': 'https://www.peeks.com/'},
    {'name': 'twitch.tv', 'url': 'https://www.twitch.tv/'},
    {'name': 'App.net', 'url': 'https://app.net/'},
    {'name': 'Caffeine (service)', 'url': 'https://www.caffeine.tv/'},
    {'name': 'Shopify', 'url': 'https://www.shopify.com/'},
    {'name': 'Tinder (app)', 'url': 'https://tinder.com/'},
    {'name': 'Koji', 'url': 'https://withkoji.com/'},
    {'name': 'Genies, Inc', 'url': 'https://genies.com/'},
    {'name': 'Rally', 'url': 'https://rally.io/'},
    {'name': 'ooooo', 'url': 'https://ooooo.com/'},
    {'name': 'Pearpop', 'url': 'https://pearpop.com/'},
    {'name': 'Launch House', 'url': 'https://www.launchhouse.com/'},
    {'name': 'Lumanu', 'url': 'https://www.lumanu.com/'},
    {'name': 'Fave', 'url': 'https://faveforfans.com/'},
    {'name': 'Kuaishou', 'url': 'https://www.kuaishou.com/en'},
    {'name': 'Skype', 'url': 'https://www.skype.com/en/'},
    {'name': 'Microsoft Teams', 'url': 'https://www.microsoft.com/en-us/microsoft-teams/group-chat-software'},
    {'name': 'Amazon (company)', 'url': 'https://www.aboutamazon.com/'},
    {'name': 'Alphabet company', 'url': 'https://abc.xyz/'},
    {'name': 'Hulu', 'url': 'https://www.hulu.com/'},
    {'name': 'Netflix', 'url': 'https://www.netflix.com/'}
]
