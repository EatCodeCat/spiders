from  mongodao.yellohubmodel import VideosModel
from collections import Counter
model = VideosModel()

c = model.find()

tag_list = []

for item in c:
    tag_list += item['tag_list']

print(Counter(tag_list))
