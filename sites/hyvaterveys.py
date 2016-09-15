import requests

from bs4 import BeautifulSoup

def parse( url , out ):

	r = requests.get( url )
	r.encoding = 'UTF-8'
	soup = BeautifulSoup( r.text, "lxml" )

	for p in soup.find_all( class_='field-items' ):
		for string in p.stripped_strings:
	        	out.write( string.encode('utf8') + ' ' )

if __name__ == '__main__':

	parse("http://www.hyvaterveys.fi/artikkeli/blogit/paljain_jaloin_pariisissa/eriavien_mielipiteiden_merkityksesta", file('hyvaterveys.txt', 'w'))
