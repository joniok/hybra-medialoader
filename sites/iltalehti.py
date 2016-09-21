import requests

from bs4 import BeautifulSoup
import bs4

def parse( url , out ):

	r = requests.get( url )
	r.encoding = 'UTF-8'
	soup = BeautifulSoup( r.text, "html.parser" )

	teksti = soup.find_all( 'isense' )

	for e in teksti[0]:
		if isinstance( e, bs4.element.Tag):
			if not e.get('id') and e.string and not e.get('type'): ## hack, fixme
				out.write( e.string.encode('utf8') + ' ' )

if __name__ == '__main__':

	parse("http://www.iltalehti.fi/uutiset/2014120218885176_uu.shtml", file('iltalehti.txt', 'w'))
