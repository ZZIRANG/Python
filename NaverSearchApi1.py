# 네이버 검색 Open API 예제 - 블로그 검색
import os
import sys
import urllib.request
client_id = "MlfQ3QT7btAqNAW99JwT"
client_secret = "LU_AF7uCIP"
encText = urllib.parse.quote("김치")
url = "https://openapi.naver.com/v1/search/blog?query=" + encText 

request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id", client_id)
request.add_header("X-Naver-Client-Secret", client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200) :
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)