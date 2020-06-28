import requests, os
 
"""
發送 Line Notify 訊息
"""
def lineNotify(token, msg, picURI):
    url = "https://notify-api.line.me/api/notify"
    headers = {
        "Authorization": "Bearer " + token
    }
   
    payload = {'message': msg}
    files = {'imageFile': open(picURI, 'rb')}
    r = requests.post(url, headers = headers, params = payload, files = files)
    return r.status_code
 
 

if __name__ == '__main__':
	token = ''#LINEBOT 帳號
	msg = "系統發送"
	allFileList = os.listdir('image/')
	for file in allFileList:
		print(file)
		lineNotify(token, msg, 'image/'+file)