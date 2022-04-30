buyer_list_urls = [
    "https://www.nestle.com/",
    "https://www.verizon.com/",
    "https://thewaltdisneycompany.com/",
    "https://www.kraftheinzcompany.com/",
    "https://www.unilever.com/",
    "https://www.kelloggcompany.com/en_US/home.html",
    "https://www.gsk.com/en-gb/home/",
    "https://www.thepennyhoarder.com/",
    "https://corporate.comcast.com/",
    "https://www.cvs.com/",
    "https://www.firebellymarketing.com/",
    "https://www.socialdriver.com/",
    "https://chatterkick.com/",
    "https://thriveagency.com/",
    "https://www.shootyou.com/",
    "https://edesigninteractive.com/",
    "https://www.lyfemarketing.com/",
    "https://seoplus.com/",
    "https://www.visualfizz.com/",
    "https://metrictheory.com/",
    "https://www.oyova.com/",
    "https://www.bastionelevate.com/",
    "https://codedesign.org/",
    "https://www.chamber.media/",
    "https://sachsmarketinggroup.com/",
    "https://wearecoal.co.uk/",
    "https://www.brandetize.com/",
    "https://www.ourownbrand.co/",
]


# create buyer list objects
def get_buyer_list_objs():
    buyer_list_objs = []
    for buyer in buyer_list_urls:
        name = input(f'What is the name you would like to assign {buyer}?: ')
        b = {
            "name": name,
            "url": buyer
        }
        buyer_list_objs.append(b)
    print("Buyer List: ", buyer_list_objs)
    return buyer_list_objs


# # create buyer list in memory
# created_buyer_list_objects = get_buyer_list_objs()

buyer_list_objs = [
    {'name': 'Nestle', 'url': 'https://www.nestle.com/'},
    {'name': 'Verizon', 'url': 'https://www.verizon.com/'},
    {'name': 'Disney', 'url': 'https://thewaltdisneycompany.com/'},
    {'name': 'Kraft Heinz', 'url': 'https://www.kraftheinzcompany.com/'},
    {'name': 'Unilever', 'url': 'https://www.unilever.com/'},
    {'name': "Kellogg's", 'url': 'https://www.kelloggcompany.com/en_US/home.html'},
    {'name': 'GlaxoSmithKline', 'url': 'https://www.gsk.com/en-gb/home/'},
    {'name': 'The Penny Hoarder', 'url': 'https://www.thepennyhoarder.com/'},
    {'name': 'Comcast', 'url': 'https://corporate.comcast.com/'},
    {'name': 'CVS Pharmacy', 'url': 'https://www.cvs.com/'},
    {'name': 'Firebelly Marketing', 'url': 'https://www.firebellymarketing.com/'},
    {'name': 'Social Driver', 'url': 'https://www.socialdriver.com/'},
    {'name': 'Chatter Kick', 'url': 'https://chatterkick.com/'},
    {'name': 'Thrive Agency', 'url': 'https://thriveagency.com/'},
    {'name': 'Shoot You', 'url': 'https://www.shootyou.com/'},
    {'name': 'eDesign Interactive', 'url': 'https://edesigninteractive.com/'},
    {'name': 'Lyfe Marketing', 'url': 'https://www.lyfemarketing.com/'},
    {'name': 'Seoplus', 'url': 'https://seoplus.com/'},
    {'name': 'Visual Fizz', 'url': 'https://www.visualfizz.com/'},
    {'name': 'Metric Theory', 'url': 'https://metrictheory.com/'},
    {'name': 'Oyova', 'url': 'https://www.oyova.com/'},
    {'name': 'Bastion Elevate', 'url': 'https://www.bastionelevate.com/'},
    {'name': 'Codedesign', 'url': 'https://codedesign.org/'},
    {'name': 'Chamber Media', 'url': 'https://www.chamber.media/'},
    {'name': 'Sachs Marketing Group', 'url': 'https://sachsmarketinggroup.com/'},
    {'name': 'Coal Marketing', 'url': 'https://wearecoal.co.uk/'},
    {'name': 'Brandetize', 'url': 'https://www.brandetize.com/'},
    {'name': 'Our Own Brand', 'url': 'https://www.ourownbrand.co/'}
]
