import json
from sourceLists import buyerList, competitorList, newEntrantList, otherUrlList, substituteList, supplierList
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


def get_company_info(url):
    # ask user to tell us who that url is for
    co_name = input(f'Please enter a name for {url}: ')

    # check for wiki
    page_name = wiki.check_for_wiki(co_name)
    if not page_name:
        # set these in cases wiki not found
        founded = ""
        num_emp = ""
        name = co_name
    else:
        name = page_name.title
        # if wiki exists get some info about the company
        # TODO: CLEAN THESE BABIES UP
        # print("fullurl: ", page_name.fullurl)
        founded = infobox.get_founded(page_name.fullurl)
        # print(founded)
        num_emp = infobox.get_emp(page_name.fullurl)

    company_json = {
        "type": "company",
        "name": name,
        "url": url,
        "attributes": {
            "founded": founded,
            "numberEmployees": num_emp,
        }
    }
    return company_json


if __name__ == '__main__':
    # create the company objects
    # TODO: add a check to see if the nodes file already includes this company so we don't loop through the whole
    #  list when we iterate
    # buyers
    for buyer in buyerList.buyer_list:
        json_buyer = get_company_info(buyer)
        with open('twitter-nodes-company.jl', 'a') as f:
            f.write(json.dumps(json_buyer) + '\n')
    # competitors
    for competitor in competitorList.competitor_list:
        json_competitor = get_company_info(competitor)
        with open('twitter-nodes-company.jl', 'a') as f:
            f.write(json.dumps(json_competitor) + '\n')
    # potential new entrants
    for ne in newEntrantList.new_entrants_list:
        json_ne = get_company_info(ne)
        with open('twitter-nodes-company.jl', 'a') as f:
            f.write(json.dumps(json_ne) + '\n')
    # other companies
    for other in otherUrlList.other_url_list:
        json_other = get_company_info(other)
        with open('twitter-nodes-company.jl', 'a') as f:
            f.write(json.dumps(json_other) + '\n')
    # substitutes
    for sub in substituteList.substitute_list:
        json_sub = get_company_info(sub)
        with open('twitter-nodes-company.jl', 'a') as f:
            f.write(json.dumps(json_sub) + '\n')
    # suppliers
    for supplier in supplierList.supplier_list:
        json_supplier = get_company_info(supplier)
        with open('twitter-nodes-company.jl', 'a') as f:
            f.write(json.dumps(json_supplier) + '\n')

