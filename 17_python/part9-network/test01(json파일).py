# json 데이터 파싱
import json

with open("json.txt", "r", encoding="utf-8") as f:
    data = json.loads(f.read())

# print(type(data))
# print(data)
# print(data["channel"])
# print(data["channel"]["item"])

for item in data["channel"]["item"]:        # json.txt 파일 안에 channel 안에 item 을 반복도는데, item의 author 와 title 만 꺼내오기
    print(item["author"], item["title"])
