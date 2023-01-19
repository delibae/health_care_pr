import requests

def send_data(url):
    files = {
        'file':open('./path/to/image.jpg', 'rb')
    }
    res = requests.post(url,files=files)
    return res.text

url = "http://192.168.xxx.xxx:8021/predict"
print(send_post(url))