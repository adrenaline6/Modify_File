import urllib3
from bs4 import BeautifulSoup

# thay the url
url = 'http://qldt.actvn.edu.vn/CMCSoft.IU.Web.info/Login.aspx'
http = urllib3.PoolManager()
r = http.request('GET', url, preload_content=False)
body = r.data.decode()
soup = BeautifulSoup(body, 'html.parser')
# thay the tag 'input'
result = soup.find_all('input')
print(type(result))
print(result[0])