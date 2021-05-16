import requests
import json

url = "https://cb-api.ozonru.me" # Cсылку нужно поменять на боевую среду
method = "/v1/product/info/description" # Сюда вбиваем нужный метод
print(url + method)
head = {
  "Client-Id": "836", # сюда клиент id
  "Api-Key": "0296d4f2-70a1-4c09-b507-904fd05567b9" # Сюда Api-Key
}

# Сюда пишем параметры запроса
body = {
  "offer_id": "1",
  "product_id": "0"
}
body = json.dumps(body) # Нужно передавать в озон именно так, потому что string он как json не понимает
response = requests.post(url + method, headers=head, data=body)

print(response.text) # ответ сервера Озон