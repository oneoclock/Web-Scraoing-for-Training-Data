import requests ; from bs4 import BeautifulSoup
import re
f = open('negativetrainset.review', 'a')
inc=1

for inc in range(1,190):
	print "page %d" %inc
	#print url
	url="https://www.amazon.com/Game-Thrones-Song-Fire-Book/product-reviews/B0001DBI1Q/ref=cm_cr_getr_d_paging_btm_%d?ie=UTF8&reviewerType=all_reviews&pageNumber=%d&filterByStar=critical"%(inc,inc)
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

#https://www.amazon.com/Amazons-Choice-E5-575-33BM-15-6-Inch-Generation/product-reviews/B01K1IO3QW/ref=cm_cr_dp_d_hist_5?ie=UTF8&filterByStar=five_star&reviewerType=avp_only_reviews#reviews-filter-bar

#https://www.amazon.com/Amazons-Choice-E5-575-33BM-15-6-Inch-Generation/product-reviews/B01K1IO3QW/ref=cm_cr_arp_d_paging_btm_2?ie=UTF8&filterByStar=five_star&reviewerType=avp_only_reviews&pageNumber=2#reviews-filter-bar

#https://www.amazon.com/Amazons-Choice-E5-575-33BM-15-6-Inch-Generation/product-reviews/B01K1IO3QW/ref=cm_cr_getr_d_paging_btm_4?ie=UTF8&filterByStar=five_star&reviewerType=avp_only_reviews&pageNumber=4#reviews-filter-bar

#https://www.amazon.com/Amazons-Choice-E5-575-33BM-15-6-Inch-Generation/product-reviews/B01K1IO3QW/ref=cm_cr_getr_d_paging_btm_1?ie=UTF8&filterByStar=five_star&reviewerType=avp_only_reviews&pageNumber=1#reviews-filter-bar

#https://www.amazon.com/Amazons-Choice-E5-575-33BM-15-6-Inch-Generation/product-reviews/B01K1IO3QW/ref=cm_cr_arp_d_paging_btm_1?ie=UTF8&filterByStar=five_star&reviewerType=avp_only_reviews&pageNumber=1#reviews-filter-bar
