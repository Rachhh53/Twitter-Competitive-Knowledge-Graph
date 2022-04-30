import json
from sourceLists import buyerList


# takes a string type and a company
def create_json(type, url):
    match type:
        case 'buyer':
            co_name = input(f'Please enter a name for {url}: ')
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
