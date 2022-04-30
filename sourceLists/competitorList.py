competitor_list_urls = [
    "https://www.wechat.com/",
    "https://www.facebook.com/",
    "https://www.pinterest.com/",
    "https://www.snapchat.com/",
    "https://www.bytedance.com/en/",
    "https://vk.com/?lang=en",
    "https://www.linkedin.com/",
    "https://www.reddit.com/",
    "https://www.tumblr.com/",
    "https://www.instagram.com/",
    "https://www.tiktok.com/en/",
    "https://www.whatsapp.com/",
    "https://www.weibo.com/",
    "https://parler.com/",
    "https://myspace.com/",
    "https://foursquare.com/",
    "https://qzone.qq.com/"
]


# create competitor list objects
def get_competitor_list_objs():
    competitor_list_objs = []
    for competitor in competitor_list_urls:
        name = input(f'What is the name you would like to assign {competitor}?: ')
        b = {
            "name": name,
            "url": competitor
        }
        competitor_list_objs.append(b)
    print("Competitor List: ", competitor_list_objs)
    return competitor_list_objs


# # create competitor list in memory
# created_competitor_list_objects = get_competitor_list_objs()

competitor_list_objs = [
    {'name': 'WeChat', 'url': 'https://www.wechat.com/'},
    {'name': 'Facebook', 'url': 'https://www.facebook.com/'},
    {'name': 'Pinterest', 'url': 'https://www.pinterest.com/'},
    {'name': 'Snapchat', 'url': 'https://www.snapchat.com/'},
    {'name': 'ByteDance', 'url': 'https://www.bytedance.com/en/'},
    {'name': 'VK', 'url': 'https://vk.com/?lang=en'},
    {'name': 'LinkedIn', 'url': 'https://www.linkedin.com/'},
    {'name': 'Reddit', 'url': 'https://www.reddit.com/'},
    {'name': 'Tumblr', 'url': 'https://www.tumblr.com/'},
    {'name': 'Instagram', 'url': 'https://www.instagram.com/'},
    {'name': 'tiktok', 'url': 'https://www.tiktok.com/en/'},
    {'name': 'Whatsapp', 'url': 'https://www.whatsapp.com/'},
    {'name': 'Weibo', 'url': 'https://www.weibo.com/'},
    {'name': 'Parler', 'url': 'https://parler.com/'},
    {'name': 'myspace', 'url': 'https://myspace.com/'},
    {'name': 'Foursquare (social media)', 'url': 'https://foursquare.com/'},
    {'name': 'Qzone', 'url': 'https://qzone.qq.com/'}
]