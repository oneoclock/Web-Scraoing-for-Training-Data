import requests ; from bs4 import BeautifulSoup
import re
f = open('abc.txt', 'a')
inc=1

for inc in range(1,266):
    print(inc)
    url="https://www.amazon.com/Life-We-Bury-Allen-Eskens/product-reviews/1616149981/ref=cm_cr_arp_d_paging_btm_%d?ie=UTF8&filterByStar=five_star&reviewerType=avp_only_reviews&pageNumber=%d#reviews-filter-bar"%(inc,inc)
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
