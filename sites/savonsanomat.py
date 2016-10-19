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

	article = soup.find( role = 'main' )
	processor.decompose_all( article.find_all( 'script' ) )
	processor.decompose( article.find( class_ = 'article-author__image' ) )

	categories = [processor.collect_text( article.find( class_ = 'article__section' ) )]

	datetime_string = article.find( class_ = 'article__published').get_text( strip = True )
	datetime_object = datetime.strptime( datetime_string, '%d.%m.%Y %H:%M')
	datetime_list = [datetime_object]

	author = processor.collect_text( article.find( class_ = 'article__author' ) )
	title = processor.collect_text( article.find( class_ = 'article__title' ) )
	text = processor.collect_text( article.find( class_ = 'article__body' ) )
	images = processor.collect_images_by_parent( article.find_all( class_ = 'article__images' ), '' )
	captions = processor.collect_image_captions( article.find_all( 'figcaption' ) )

	return processor.create_dictionary(url, r.status_code, categories, datetime_list, author, title, '', text, images, captions)

if __name__ == '__main__':
	parse("http://www.savonsanomat.fi/uutiset/kotimaa/itsenaisyyspaivan-korkein-kunniamerkki-arkkipiispa-makiselle/1944316", file('savon.txt', 'w'))
