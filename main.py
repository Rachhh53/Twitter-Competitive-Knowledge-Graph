import json
from sourceLists import buyerList, competitorList, newEntrantList, otherUrlList, substituteList, supplierList
import wikipedia as wiki
import wikiInfobox as infobox


# takes a company url
def get_company_info(company):
    # ask user to tell us who that url is for
    # co_name = input(f'Please enter a name for {url}: ')
    print(company)
    co_name = company['name']

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
        industry = infobox.get_industry(page_name.fullurl)
        # don't create these nodes or relationships if industry is null
        if industry:
            make_industry(industry, name)

    company_json = {
        "type": "company",
        "name": name,
        "url": company['url'],
        "attributes": {
            "founded": founded,
            "numberEmployees": num_emp,
        }
    }
    return company_json, name


# create edge object
# class edge list example has duplicate keys...not sure that's valid json?
def get_edge_company(co1, co2, relation):
    edge = {
        "company1": co1,
        "relation": relation,
        "company2": co2
    }
    return edge


# create edge object
def get_edge_service(co, serv, relation):
    edge = {
        "company": co,
        "relation": relation,
        "service": serv
    }
    return edge


# create service object
def get_service_info(ser):
    service = {
        "type": "service",
        "name": ser,
        "description": ""
    }
    return service


# create industry object
def make_industry(industry, name):
    # make industry object
    ind = {
        "type": "industry",
        "name": industry,
        "attributes": {
            "NAICScode": "",
            "NAICStitle": "",
            "description": ""
        }
    }
    # write industry object
    with open('twitter-nodes-other.jl', 'a') as file:
        file.write(json.dumps(ind) + '\n')

    # create edge
    rel = {
        "company": name,
        "relation": "is_in",
        "industry": industry
    }
    with open('twitter-edges.jl', 'a') as f:
        f.write(json.dumps(rel) + '\n')


if __name__ == '__main__':
    # Ask the user what's up
    while True:
        try:
            menu = int(input(f'Press 1 for to enter names for companies,\n Press 2 to create nodes and edges, '
                             f'\n Press any other number to exit: '))
        except ValueError:
            print('Sorry, I didn\'t understand that. Please try again')
            continue
        else:
            break

    # Run this to create objects from lists of urls. Copy/paste them into variables
    if menu == 1:
        b = buyerList.get_buyer_list_objs()
        c = competitorList.get_competitor_list_objs()
        n = newEntrantList.get_new_entrant_list_objs()
        o = otherUrlList.get_other_list_objs()
        sub = substituteList.get_substitute_list_objs()
        sup = supplierList.get_supplier_list_objs()

    # create the company objects, edge objects and json lines files
    elif menu == 2:
        # Set up for my company
        my_co = "Twitter"
        # TODO: add a check to see if the nodes file already includes this company so we don't loop through the whole
        #  list when we iterate
        # create advertising node
        ads_json = get_service_info('advertising')
        with open('twitter-nodes-other.jl', 'a') as f:
            f.write(json.dumps(ads_json) + '\n')
        # create advertising edge
        ads_edge = get_edge_service(my_co, 'advertising', 'sells')
        with open('twitter-edges.jl', 'a') as f:
            f.write(json.dumps(ads_edge) + '\n')

        # buyers
        print('Staring buyers')
        for buyer in buyerList.buyer_list_objs:
            # create company obj
            json_buyer, name = get_company_info(buyer)
            with open('twitter-nodes-company.jl', 'a') as f:
                f.write(json.dumps(json_buyer) + '\n')
            # create service node
            # rel = input(f'What service does {name} buy from Twitter?: ')
            # json_service = get_service_info(rel)
            # with open('twitter-nodes-other.jl', 'a') as f:
            #     f.write(json.dumps(json_service) + '\n')
            # create buyer relationship (edge)

            # we don't have any other services right now
            rel = 'advertising'
            buyer_edge = get_edge_service(name, rel, 'buys')
            with open('twitter-edges.jl', 'a') as f:
                f.write(json.dumps(buyer_edge) + '\n')

        # competitors
        print('Staring competitors')
        for competitor in competitorList.competitor_list_objs:
            json_competitor, name = get_company_info(competitor)
            with open('twitter-nodes-company.jl', 'a') as f:
                f.write(json.dumps(json_competitor) + '\n')
            # create edge object
            competitor_edge = get_edge_company(my_co, name, 'competes_with')
            with open('twitter-edges.jl', 'a') as f:
                f.write(json.dumps(competitor_edge) + '\n')

        # potential new entrants
        print('Staring new entrants')
        for ne in newEntrantList.new_entrant_objs:
            json_ne, name = get_company_info(ne)
            with open('twitter-nodes-company.jl', 'a') as f:
                f.write(json.dumps(json_ne) + '\n')
            # create edge object
            ne_edge = get_edge_company(my_co, name, 'has_potential_entrant')
            with open('twitter-edges.jl', 'a') as f:
                f.write(json.dumps(ne_edge) + '\n')

        # Twitter itself
        print(f'Let us not forget {my_co}')
        for other in otherUrlList.other_objs:
            json_other, name = get_company_info(other)
            with open('twitter-nodes-company.jl', 'a') as f:
                f.write(json.dumps(json_other) + '\n')

        # substitutes
        print('Staring substitutes')
        for sub in substituteList.substitute_objs:
            json_sub, name = get_company_info(sub)
            with open('twitter-nodes-company.jl', 'a') as f:
                f.write(json.dumps(json_sub) + '\n')
            # create edge object
            sub_edge = get_edge_company(my_co, name, 'has_substitute')
            with open('twitter-edges.jl', 'a') as f:
                f.write(json.dumps(sub_edge) + '\n')

        # suppliers
        print('Staring suppliers')
        for supplier in supplierList.supplier_objs:
            json_supplier, name = get_company_info(supplier)
            with open('twitter-nodes-company.jl', 'a') as f:
                f.write(json.dumps(json_supplier) + '\n')

        # articles
        print('Starting articles')
        print('Wikipedia articles')
        wiki_articles = wiki.wiki_scrape(my_co)
        for index, row in wiki_articles.iterrows():
            a = {
                "type": "article",
                "name": row['page'],
                "url": row['link'],
                "table": "",
                "keywords": row['categories'],
                "author": "Wikipedia",
                "text": row['text']
            }
            edge = {
                "company": my_co,
                "relation": "has_article",
                "article": row['page']
            }
            with open('twitter-nodes-other.jl', 'a') as f:
                f.write(json.dumps(a) + '\n')
            with open('twitter-edges.jl', 'a') as f:
                f.write(json.dumps(edge) + '\n')

    # leave this place!
    else:
        print("Goodbye")
