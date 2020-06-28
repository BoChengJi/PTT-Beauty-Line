import requests
import urllib
from bs4 import BeautifulSoup
#r = requests.Session()
def get_page(ptturl,url): #突破滿18
	payload ={
		"from":ptturl+url,
		"yes":"yes"
	}
	r1 = requests.post("https://www.ptt.cc/ask/over18",payload ,allow_redirects = False)
	#print(r1.text)
	return r1.cookies
def get_allurl(ptturl,url): #上一頁
	r2 = r2 = requests.get(ptturl+url,cookies = get_page(ptturl,url))
	soup = BeautifulSoup(r2.text, "html.parser")
	sel = soup.select('div.btn-group a')
	print(sel[3]["href"])
	return sel[3]["href"]
def get_url(ptturl,url,urllink): #取得當頁所有連結
	r2 = requests.get(ptturl+url,cookies = get_page(ptturl,url))
	soup = BeautifulSoup(r2.text, "html.parser")
	
	
	sel = soup.find_all('div',class_="title")
	print(sel)
	for s in sel:
		a = s.find('a')
		if a is not None:
			print(a["href"])
			print(a.text[1:3])
			if(a.text[1:3]=='正妹'):
				urllink.append(a["href"])
	return urllink
def download_img(ptturl,url): #取得內文連結並下載
	r2 = requests.get(ptturl+url,cookies = get_page(ptturl,url))
	#print(r2.text)
	soup = BeautifulSoup(r2.text, "html.parser")
	sel = soup.select('div.richcontent a')
	#print(sel)
			
	sel = soup.find_all('div',class_='richcontent')
	for s in sel:
		a = s.find('a')
		if a is not None:
			print(a["href"])
			html = requests.get('https:'+a["href"]+'.jpg')
			print('https:'+a["href"]+'.jpg')
			#https://imgur.com/A2jFwhj
			with open('image/'+a["href"][-6:]+'.jpg','wb') as f:
				f.write(html.content)
				f.close()
def test():
	ptturl='https://www.ptt.cc/'
	url = 'bbs/Beauty/index.html'
	urllink=[]
	urllink = get_url(ptturl,url,urllink)
def main():
	ptturl='https://www.ptt.cc/'
	url = 'bbs/Beauty/index.html'
	urllink=[]
	urllink = get_url(ptturl,url,urllink)
	print(urllink)
	for urls in urllink:
		download_img(ptturl,urls)
		print('download')
	for i in range(10):
		urllink = get_url(ptturl,get_allurl(ptturl,url),urllink)
		print(urllink)
		for urls in urllink:
			print('download')
			download_img(ptturl,urls)
if __name__ == '__main__':
	main()
	#test()