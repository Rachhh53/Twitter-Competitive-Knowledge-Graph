import json
from sourceLists import buyerList
import wikipedia as wiki


# takes a string type and a company
def create_json(type, url):
    match type:
        case 'buyer':
            co_name = input(f'Please enter a name for {url}: ')

            # check for wiki
            page_name = wiki.check_for_wiki(co_name)
            if not page_name.exists():
                print('Page {} does not have a wiki.'.format(co_name))
            else:
                create_json('article', wiki.wiki_link())

            buyer_json = {
                "type": "company",
                "name": co_name,
                "url": url,
                "attributes": {
                    "founded": "",
                    "numberEmployees": "",
                }
            }
            return buyer_json


if __name__ == '__main__':
    for buyer in buyerList.buyer_list:
        json_buyer = create_json('buyer', buyer)
        with open('twitter-nodes-company.jl', 'a') as f:
            f.write(json.dumps(json_buyer) + '\n')
