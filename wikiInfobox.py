from pandas.io.html import read_html


page = 'https://en.wikipedia.org/wiki/Nestle'

# get infoboxes
infoboxes = read_html(page, index_col=0, attrs={"class":"infobox"})
infobox_df = infoboxes[0]

# get tables
wikitables = read_html(page, index_col=0, attrs={"class":"wikitable"})
wikitables_df = wikitables[0]

founded = infobox_df.loc["Founded"]
industry = infobox_df.loc["Industry"]
num_employees = infobox_df.loc["Number of employees"]
