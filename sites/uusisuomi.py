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

	text = soup.find_all( class_='field field-name-body field-type-text-with-summary field-label-hidden' )
	for script in text[0].find_all( 'script' ):
		script.decompose()
	text = text[0].get_text(' ', strip = True)
	text = processor.process(text)

	return processor.create_dictionary(url, r.status_code, [''], [''], '', '', '', text, [''], [''])

if __name__ == '__main__':
	parse("http://www.uusisuomi.fi/kotimaa/79148-ex-ministeri-kummastelee-jotkut-pitavat-lahes-rikollisena", file('uusisuomi.txt', 'w'))
