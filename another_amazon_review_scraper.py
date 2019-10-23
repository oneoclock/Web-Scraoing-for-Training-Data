import requests ; from bs4 import BeautifulSoup
import re
f = open('testtrain.review', 'a')
inc=1
for inc in range(1,190):
	print "page %d" %inc
	url="https://www.amazon.com/Magic-Secret-Rhonda-Byrne/product-reviews/1451673442/ref=cm_cr_arp_d_paging_btm_%d?ie=UTF8&reviewerType=all_reviews&pageNumber=%d"%(inc,inc)
	link=requests.get(url).text
	soup = BeautifulSoup(link, "html.parser")

	for item in soup.find_all("div",{"class":"a-row review-data"}):
		f.write('<review>\n')
		f.write('<review_text>\n')
		line = re.sub('[<>&]','', item.text.encode('utf-8').strip())
		f.write(line)
		f.write('\n')
		f.write('</review_text>\n')
		f.write('</review>\n')
