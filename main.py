import json
from sourceLists import buyerList
import wikipedia as wiki
import wikiInfobox as infobox


# # takes a string type and a company
# def create_json(type, url):
#     match type:
#         case 'buyer':
#             # set these in cases wiki not found
#             founded = ""
#             num_emp = ""
#
#             # ask user to tell us who that url is for
#             co_name = input(f'Please enter a name for {url}: ')
#
#             # check for wiki
#             page_name = wiki.check_for_wiki(co_name)
#             if not page_name.exists():
#                 print('Page {} does not have a wiki.'.format(co_name))
#             else:
#                 # if wiki exists get some info about the company
#                 founded = infobox.get_founded(page_name.fullurl)
#                 num_emp = infobox.get_emp(page_name.fullurl)
#
#                 # # create a reference to the wiki in article node
#                 # create_json('article', page_name.fullurl)
#
#             buyer_json = {
#                 "type": "company",
#                 "name": co_name,
#                 "url": url,
#                 "attributes": {
#                     "founded": founded,
#                     "numberEmployees": num_emp,
#                 }
#             }
#             return buyer_json
#         case 'article':
#             article_json = {
#                 "type": "article",
#                 "name": "",
#                 "url": url,
#                 "table": "",
#                 "keywords": [],
#                 "author": "",
#                 "text": ""
#             }
#         case _:
#             print("Missing from case statement in create_json()")


def get_buyer_info(url):
    # set these in cases wiki not found
    founded = ""
    num_emp = ""

    # ask user to tell us who that url is for
    co_name = input(f'Please enter a name for {url}: ')

    # check for wiki
    page_name = wiki.check_for_wiki(co_name)
    if not page_name.exists():
        print('Page {} does not have a wiki.'.format(co_name))
    else:
        # if wiki exists get some info about the company
        # TODO: CLEAN THESE BABIES UP
        # print("fullurl: ", page_name.fullurl)
        founded = infobox.get_founded(page_name.fullurl)
        # print(founded)
        num_emp = infobox.get_emp(page_name.fullurl)

    buyer_json = {
        "type": "company",
        "name": page_name.title,
        "url": url,
        "attributes": {
            "founded": founded,
            "numberEmployees": num_emp,
        }
    }
    return buyer_json


if __name__ == '__main__':
    for buyer in buyerList.buyer_list:
        json_buyer = get_buyer_info(buyer)
        with open('twitter-nodes-company.jl', 'a') as f:
            f.write(json.dumps(json_buyer) + '\n')
