 # -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import processor
from datetime import datetime

def parse( url ):

	r = requests.get( url )
	if r.status_code == 404:
		processor.create_dictionary(url, r.status_code, [''], [''], '', '', '', '', [''], [''])

	r.encoding = 'UTF-8'
	soup = BeautifulSoup( r.text, "html.parser" )

	article = soup.find( id = 'main-content' )
	processor.decompose_scripts( article )
	article.find( class_ = 'reviewpic' ).decompose()

	date = article.find( class_ = 'published').get_text( strip = True )
	datetime_list = [datetime.date( datetime.strptime( date, "%d.%m.%Y" ) )]

	author = article.find( class_ = 'author' ).get_text( strip = True )
	title = article.find( 'h1' ).get_text( strip = True )
	text = processor.collect_text( article, 'class', 'entry-content' )
	images = processor.collect_images( article, '', '' )

	return processor.create_dictionary(url, r.status_code, [''], datetime_list, author, title, '', text, images, [''])

if __name__ == '__main__':

	parse("http://faktabaari.fi/fakta/petrus-pennanen-energiewende-oli-kaynnissa-jo-2002/", file('faktabaari.txt', 'w'))
