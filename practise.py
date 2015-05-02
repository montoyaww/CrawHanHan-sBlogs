# -*- encoding: utf-8 -*-
import urllib2
WebPage ='http://blog.sina.com.cn/s/articlelist_1191258123_0_1.html'
def get_test(url): 
	HtmlPage = urllib2.urlopen(url)
	page = HtmlPage.read()
	return page

def get_next_target(page):
	start_title = page.find('<a title')
	start_link = page.find('href', start_title)
	if start_link == -1:
		return None, 0
	start_quote = page.find('"', start_link)
	end_quote = page.find('"', start_quote + 1)
	url = page[start_quote + 1:end_quote]
	return url, end_quote

def go_next_page(page):
	start_point = page.find('SG_pgnext')
	start_link = page.find('href', start_point)
	start_quote = page.find('"', start_link)
	end_quote = page.find('"', start_quote + 1)
	url = page[start_quote + 1: end_quote]
	return url
	
def print_all_links(url):
	page = get_test(url)
	while True:
		print_links(page)
		if page.find('SG_pgnext') != -1:
			url = go_next_page(page)
			page = get_test(url)
		else:
			break
			
	
def print_links(page):
	while True:
		url, endpos = get_next_target(page)
		if url:
			print url
			f.write(url + '\n')
			page = page[endpos:]
		else:
			break
f = open('t.txt', 'wb')		
print_all_links(WebPage)
f.close()
