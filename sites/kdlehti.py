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

	article = soup.find( 'article' )
	processor.decompose_all( article.find_all( 'script' ) )
	processor.decompose_all( article.find( 'header' ).find_all( 'img' ) )
	processor.decompose_all( article.find_all( 'blockquote' ) )

	categories = [processor.collect_text( article.find( class_ = 'cat' ) )]

	datetime_string = article.find( class_ = 'date' ).get_text( strip = True ).replace( 'klo ', ' ')
	datetime_object = datetime.strptime( datetime_string, '%d.%m.%Y %H:%M' )
	datetime_list = [datetime_object]

	author = processor.collect_text( article.find( class_ = 'author' ) )
	title = processor.collect_text( article.find( class_ = 'article-title' ) )

	ingress_tag = article.find( class_ = 'ingress' )
	ingress = processor.collect_text( ingress_tag )
	ingress_tag.decompose()

	text = processor.collect_text( article.find( class_ = 'content' ) )
	images = processor.collect_images( article.find_all( 'img' ), 'http:' )

	captions = [None]
	for img_frame in article.find_all( class_ = 'featured-image' ):
		captions.append( processor.collect_text( img_frame ) )
	captions.pop(0)

	return processor.create_dictionary(url, r.status_code, categories, datetime_list, author, title, ingress, text, images, captions)

if __name__ == '__main__':
	parse("http://www.kdlehti.fi/2015/03/15/paivi-rasanen-internetin-terrorismisisaltoon-puututtava-tehokkaammin/", file('kdlehti.txt', 'w'))
