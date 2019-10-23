import requests ; from bs4 import BeautifulSoup

soup = BeautifulSoup(requests.get("http://www.mouthshut.com/product-reviews/Ruby-Hall-Clinic-Sassoon-Road-Pune-reviews-925043003").text, "html.parser")
inc=0
for inc in range(0,20):
	print "____________________________________________________________________________________________________________________________"
	if inc < 9:
	 review="a#ctl00_ctl00_ContentPlaceHolderFooter_ContentPlaceHolderBody_rptreviews_ctl0%d_lnkTitle"%inc
	else:
	 review="a#ctl00_ctl00_ContentPlaceHolderFooter_ContentPlaceHolderBody_rptreviews_ctl%d_lnkTitle"%inc
	for title in soup.select(review):
	 
	 broth = BeautifulSoup(requests.get(title.get('href')).text, "html.parser")
  	 for item in broth.select("div.user-review p"):
		
        	print(item.text)
#"a#ctl00_ctl00_ContentPlaceHolderFooter_ContentPlaceHolderBody_rptreviews_ctl01_lireviewdetails"
#ctl00_ctl00_ContentPlaceHolderFooter_ContentPlaceHolderBody_rptreviews_ctl01_lireviewdetails

#ctl00_ctl00_ContentPlaceHolderFooter_ContentPlaceHolderBody_rptreviews_ctl00_lnkTitle
#ctl00_ctl00_ContentPlaceHolderFooter_ContentPlaceHolderBody_rptreviews_ctl01_lnkTitle

#http://www.mouthshut.com/product-reviews/Ruby-Hall-Clinic-Sassoon-Road-Pune-reviews-925043003

#http://www.mouthshut.com/product-reviews/Lakeside-Chalet-Mumbai-reviews-925017044


