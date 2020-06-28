import requests

def lineNotifyMessage(token, msg):
    headers = {
        "Authorization": "Bearer " + token, 
        
    }

    payload = {'message': msg}
    r = requests.post("https://notify-api.line.me/api/notify", headers = headers, params = payload)
    return r.status_code
token = ''#LINEBOT帳號
number = 1
# 修改為你要傳送的訊息內容
message = ''
# 修改為你的權杖內容
while (number < 2):
	message = input('輸入需要傳送的話\n')
	lineNotifyMessage(token, message)