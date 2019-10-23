# Web-Scraoing-for-Training-Data
Scrapers for some websites to collect review dataset.

The amazon scarpers can be used by simply replacing the number after 'btm_' and 'pageNumber=' to %d

For Example a link:

https://www.amazon.com/Life-We-Bury-Allen-Eskens/product-reviews/1616149981/ref=cm_cr_arp_d_paging_   btm_2   ?ie=UTF8&filterByStar=five_star&reviewerType=avp_only_reviews&   pageNumber=2   #reviews-filter-bar"%(inc,inc)

can be edited as:

https://www.amazon.com/Life-We-Bury-Allen-Eskens/product-reviews/1616149981/ref=cm_cr_arp_d_paging_btm_%d?ie=UTF8&filterByStar=five_star&reviewerType=avp_only_reviews&pageNumber=%d#reviews-filter-bar"%(inc,inc)

Code for read more reviews can be used for websites that contain a 'read more' option for every review.
