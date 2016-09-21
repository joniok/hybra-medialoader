import requests

from bs4 import BeautifulSoup

# Lapin kansa on nykyään maksullinen lehti

def parse( url , out ):

	r = requests.get( url )
	r.encoding = 'UTF-8'
	soup = BeautifulSoup( r.text, "html.parser" )

	teksti = soup.find_all( class_ = 'news-excerpt' )

	for string in teksti[0].stripped_strings:
	        out.write( string.encode('utf8') + ' ' )

if __name__ == '__main__':
	parse("http://www.lapinkansa.fi/Lappi/1194944697007/artikkeli/kaunis+tykky+voi+olla+kavala+puille.html", file('lapinkansa.txt', 'w'))
