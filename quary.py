import urllib3
from bs4 import BeautifulSoup

def get_html_from_naver_search(keyword):
    burl = 'https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%ED%8C%8C%EC%9D%B4%EC%8D%AC&oquery=%EC%BD%94%EB%A1%9C%EB%82%98&tqi=hglE%2FsprvmZssA1kLRhssssss6G-474544'
    surl = burl + keyword
    req = urllib3.PoolManager()
    return req.request('GET', surl).data

result = get_html_from_naver_search('파이썬')
parsed = BeautifulSoup(result, 'html.parser')

print(parsed.title)
print(parsed.p)
print(parsed.find('a'))