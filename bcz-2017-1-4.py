
# -*- coding:utf-8 -*-
'''
Created on  
2016年11月3日   下午7:37:05
@author: yzw
保存的csv文件，可能乱码，需要用txt打开之后，保存，乱码消失。
'''
import requests 
from bs4 import BeautifulSoup
from word_id_get import c as c
from word_id_get import a as numi
import pandas as pd

#=======================###
word_list=list()
mean_cn_list=list()
sentence_list=list()
accent_list=list()
sentence_trans_list=list()
unit_list =list()
#=======================###
login="http://www.baicizhan.com/login"
UA = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0"  
header = { "User-Agent" : UA,
           "Referer": "http://www.baicizhan.com/login"
           
           }
note_session = requests.Session()
f = note_session.get(login,headers=header)
soup = BeautifulSoup(f.content,"html.parser")
postData = { 
            'authenticity_token':'5o79vrUx0jMKnHXqhwHAzK35T0Rn9lCl/GV1L8wH4jM=',
            'email':'1529806383@qq.com',
            'raw_pwd':'wsyzwn123',
            'remember_me':0
             }
note_session.post(login,
                  data = postData,
                  headers = header)
for j in sorted(numi):                  
    for x in numi[j]:
        unit_list.append(j)
        postData1 = {
                        'topic_ids[]':x,
                        'authenticity_token':'EslQgouxtgcD4SiaPmbqAV22DmwcKU+qrGHb2Cmh/2U=',
                        'current_user_email':'1529806383@qq.com',
                        'client_version':'ec67393eab3850b6099772de30c474813ed11615',
                        'cur_word_level_id':58,
                        'last_do_at':'2016-11-06'
                     }
        f = note_session.post('http://www.baicizhan.com/words/get_words_by_ids',
                              data = postData1,
                              headers =header)  
            
        #s = eval("u'%s'" % f.content)
        #a= s.encode('utf_8')
        
        a =f.content  
        a =a.split('}')
        a = a[0]
        a = a.strip('[')
        #c =a.rfind("audio_file")
        c =a.rfind(',"sentence_phrase"')
        a =a[:c]
        a =a.replace('.zpk"','"}')
        a =a.replace('null','"null"')
        a =a.replace('\r\n','')
        a.strip('')  
        
        #=====================================#
        a = eval("dict(%s)" %a)
        
        #=====================================#
        word =a['word']
        word_list.append(word)
        #Unicode-chn
        accent =a['accent']
        
        #accent =eval('u"%s"' % accent)
        #accent =accent.encode('utf-8')
        accent_list.append(accent)
        
        #==================Unicode-chn
        try:
            mean_cn =a['mean_cn']
            mean_cn =mean_cn.replace('\r\n','')
            #mean_cn =eval("u'%s'"% mean_cn)
            #mean_cn =mean_cn.encode('gbk')
        except Exception as e:
            mean_cn =''
        mean_cn_list.append(mean_cn)
        #==========================#
        sentence =a['sentence']
        sentence_list.append(sentence)
        #===========================#
        etyma =a['etyma']
        similar =a['similar_words']
        #Unicode-chn
        sentence_trans =a['sentence_trans']
        #sentence_trans =eval("u'%s'" % sentence_trans)
        #sentence_trans =sentence_trans.encode('gbk')
        sentence_trans_list.append(sentence_trans)
        print sentence_trans
        #======================================#
        #print word,accent,etyma,mean_cn,sentence,sentence_trans 
    #Modlues/Units两个地方同时修改
    output = pd.DataFrame(columns=['units','words','accent','mean_cn','sentence','sentence_tra'])
    output['words'] = word_list
    output['accent'] = accent_list
    output['mean_cn'] = mean_cn_list
    output['sentence'] = sentence_list
    output['sentence_tra'] =sentence_trans_list
    output['units']=unit_list
    output.to_csv(u'初中上海牛津九年级上.csv',encoding='utf-8',index=False)
    #=========================================#
    '''output_accent = pd.DataFrame(columns=['accent'])
    output_accent['accent'] = accent_list

    output_accent.to_csv(u'accent.csv',encoding='utf-8',index=False)'''
    
        
        