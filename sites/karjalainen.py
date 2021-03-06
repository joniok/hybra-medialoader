# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import processor
from datetime import datetime

def parse( url ):

	r = requests.get( url )
	if r.status_code == 404:
		return processor.create_dictionary('', url, r.status_code, [u''], [u''], u'', u'', u'', u'', [u''], [u''])

	r.encoding = 'UTF-8'
	soup = BeautifulSoup( r.text, "html.parser" )

	article = soup.find( id = 'sp-component' )
	if article == None:
		return processor.create_dictionary('', url, r.status_code, [u''], [u''], u'', u'', u'', u'', [u''], [u''])

	processor.decompose_all( article.find_all( 'script' ) )

	meta = article.find( class_ = 'category_date' )

	categories = processor.collect_categories( meta.find_all( 'a' ) )
	datetime_list = processor.collect_datetime( meta )
	author = processor.collect_text( article.find( class_ = 'author_credits' ) )
	title = processor.collect_text( article.find( 'h1' ) )
	text = processor.collect_text( article.find( class_ = 'itemIntroText' ) )
	images = processor.collect_images_by_parent( article.find_all( class_ = 'itemImage' ), 'https://www.karjalainen.fi' )
	captions = processor.collect_image_captions( article.find_all( class_ = 'itemImageCaption' ) )

	return processor.create_dictionary('Karjalainen', url, r.status_code, categories, datetime_list, author, title, u'', text, images, captions)

if __name__ == '__main__':
	parse("http://www.karjalainen.fi/uutiset/uutis-alueet/kotimaa/item/71016-arhinmaen-perheeseen-syntymassa-lapsi-puheenjohtaja-ei-osallistu-vaalitilaisuuksiin", file('karjalainen.txt', 'w'))
