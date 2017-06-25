from  mongodao.yellohubmodel import VideosModel
from collections import Counter
import jieba
import jieba.analyse
model = VideosModel()

jieba.set_dictionary('dict.txt.big.txt')

c = model.find()

tag_list = []
title_list = []

for item in c:
    title_list.append(item['title'])
    seg_list = jieba.cut(item['title'])
    tag_list += seg_list
    print(", ".join(seg_list))
    #item['tag_list'] = [it for it in item['tag_list'] if it != '性爱']
    #model.replace_one(item, **{'_id':item['_id']})


#tags =jieba.analyse.extract_tags(''.join(title_list), topK=50,withWeight=True)
Counter(tag_list)
print(Counter(tag_list))