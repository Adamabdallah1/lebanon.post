import requests

LB_POST_HEADERS = {
    "country": "lb",
    "apikey": "pub_2533162b45f4c0a11f07b5ff4f72d54244c30"
}

respone = requests.get("https://newsdata.io/api/1/news", params=LB_POST_HEADERS)
data_json = respone.json()
posts = data_json['results']
print(posts)