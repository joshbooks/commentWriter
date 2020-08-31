#!/usr/bin/python3
from bs4 import BeautifulSoup
import mechanize
import re


def make_soup(response_body):
    return BeautifulSoup(response_body, features='html5lib')

def make_browser():
    br = mechanize.Browser()
    br.set_handle_robots(False)
    br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
    return br

br = make_browser()



request1 = br.open("https://www.theredheadbaker.com/instant-pot-short-ribs-red-wine/")
assert br.viewing_html()


print(br.title())
soup = make_soup(request1.read())
for form in soup.find_all('form', id='commentform'):
    print(form.__dict__)

br.select_form(id='commentform')
br['author'] = 'Carl Dunway'
br['comment'] = 'OMG, So Good! The vegetables were tasty enough for even our pickiest eater'
br['email'] = 'carl.dunway@gmail.com'

form_response = br.submit()
print(form_response.read())
