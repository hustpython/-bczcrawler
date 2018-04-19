# -*- coding:utf-8 -*-
'''
Created on  
2016年11月4日   下午8:42:02
@author: yzw
'''

# -*- coding:utf-8 -*-
'''
Created on  
2016年11月3日   下午7:37:05
@author: yzw
'''
# -*- coding:utf-8 -*-
'''
Created on  
2016年11月3日   下午10:39:07
@author: yzw
'''
# -*- coding:utf-8 -*-
'''
Created on  
2016年11月3日   下午7:37:05
@author: yzw
'''
import requests 
from bs4 import BeautifulSoup
from word_id_get import a as numi

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
a =[4376
    ,19993
    ,7995
    ,5732
    ,7993
    ,19991
    ,5420
    ,19994
    ,7153
    ,19364
    ,18640]
for i in a:
    postData1 = {
                    'topic_ids[]':6604,
                    'authenticity_token':'EslQgouxtgcD4SiaPmbqAV22DmwcKU+qrGHb2Cmh/2U=',
                    'current_user_email':'1529806383@qq.com',
                    'client_version':'ec67393eab3850b6099772de30c474813ed11615',
                    'cur_word_level_id':32,
                    'last_do_at':'2016-11-04'
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
    a =a.replace('\n','')
    a.strip('')  
    #=====================================#
    a = eval('dict(%s)' %a)
    word =a['word']
    #Unicode-chn
    accent =a['accent']
    accent =eval("u'%s'" % accent)
    accent =accent.encode('utf_8')
    #Unicode-chn
    mean_cn =a['mean_cn']
    #mean_cn =eval("u'%s'" % mean_cn)
    #mean_cn =mean_cn.encode('utf_8')
    
    sentence =a['sentence']
    etyma =a['etyma']
    similar =a['similar_words']
    #Unicode-chn
    sentence_trans =a['sentence_trans']
    sentence_trans =eval("u'%s'" % sentence_trans)
    sentence_trans =sentence_trans.encode('utf_8')
    #======================================#
    #print word,accent,etyma,mean_cn,sentence,sentence_trans
    print word,accent,sentence,sentence_trans

