'''
Created on 2020年6月16日

@author: 44786
'''
import requests
import json
import pprint
import pymysql
import pymysql.cursors
from bs4 import BeautifulSoup
import re
class DouBan():
    '''爬取豆瓣电视数据'''
    def __init__(self):
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0"}
        self.url = ["https://movie.douban.com/j/search_subjects?type=tv&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start={}",
                    "https://movie.douban.com/j/search_subjects?type=tv&tag=%E7%BE%8E%E5%89%A7&sort=recommend&page_limit=20&page_start={}",
                    "https://movie.douban.com/j/search_subjects?type=tv&tag=%E8%8B%B1%E5%89%A7&sort=recommend&page_limit=20&page_start={}",
                    "https://movie.douban.com/j/search_subjects?type=tv&tag=%E9%9F%A9%E5%89%A7&sort=recommend&page_limit=20&page_start={}",
                    "https://movie.douban.com/j/search_subjects?type=tv&tag=%E6%97%A5%E5%89%A7&sort=recommend&page_limit=20&page_start={}",
                    "https://movie.douban.com/j/search_subjects?type=tv&tag=%E5%9B%BD%E4%BA%A7%E5%89%A7&sort=recommend&page_limit=20&page_start={}",
                    "https://movie.douban.com/j/search_subjects?type=tv&tag=%E6%B8%AF%E5%89%A7&sort=recommend&page_limit=20&page_start={}",
                    "https://movie.douban.com/j/search_subjects?type=tv&tag=%E6%97%A5%E6%9C%AC%E5%8A%A8%E7%94%BB&sort=recommend&page_limit=20&page_start={}",
                    "https://movie.douban.com/j/search_subjects?type=tv&tag=%E7%BB%BC%E8%89%BA&sort=recommend&page_limit=20&page_start={}",
                    "https://movie.douban.com/j/search_subjects?type=tv&tag=%E7%BA%AA%E5%BD%95%E7%89%87&sort=recommend&page_limit=20&page_start={}"
                   ]
        self.tagsum = ["热门",
                       "美剧",
                       "英剧",
                       "韩剧",
                       "日剧",
                       "国产剧",
                       "港剧",
                       "日本动画",
                       "综艺",
                       "纪录片",
            ]
#         self.connect = pymysql.connect(
#             host="www.91iedu.com",
#             port=3391,
#             db="team06",
#             user="team06",
#             passwd="team06",
#             charset="utf8mb4",
#             use_unicode=True
#             )
#         self.cursor = self.connect.cursor()            
    def connectDB(self):

                    db=pymysql.connect(
                        host="www.91iedu.com",
                        port=3391,
                        db="team06",
                        user="team06",
                        passwd="team06",
                        charset="utf8mb4",
                        use_unicode=True
                        )
                    return db
                    cursorDB=db.cursor()
                    return cursorDB
    
                   
                
    def get_url(self,pag, url):
        '''发送请求获取数据'''
        response = requests.get(url.format(pag), headers = self.headers)
        return response.content.decode()
    def parser_url(self, url):
        
        response = requests.get(url, headers = self.headers)
        return response.content.decode()
    def run(self):
        #发送请求获取响应
        
            true = 0
            for url in self.url:
                print("*"*50)
                num = 0
                
                temp=str(url)
                while True:
                    
                    url = temp.format(num)
                    json_str = self.parser_url(url)
                    
                    #print(type(json_str))
        
                    #提取数据
                    #python类型的数据
                    rep_dict = json.loads(json_str)
                    
                    
                    #列表
                    rep_list = rep_dict["subjects"]
                    print('当前标签：'+self.tagsum[true]+'读取量:'+str(num))
                    print(rep_list)
                    if len(rep_list) < 20:
        
                        print("豆瓣热门电视剧推荐信息收集完成")
                        
                        break
                    
                    
                    
                    #连接数据库 mysql
                    
                    
        #                 def creatTable(self,createTableName):
        #                     createTableSql="CREATE TABLE IF NOT EXISTS "+ createTableName+"(id VARCHAR(40),title VARCHAR(100),url  VARCHAR(256),author VARCHAR(10))" 
        #                     DB_create=self.connectDB()
        #                     cursor_create=DB_create.cursor()
        #                     cursor_create.execute(createTableSql)
        #                     DB_create.close()
        #                     print ('creat table '+createTableName+' successfully' )     
        #                     return createTableName 
                    def inserttable(self,insertTable,inserttag,insertTitle,inserturl,insertauthor):
                        insertContentSql="INSERT INTO "+insertTable+"(tag,title,url,author)VALUES(%s,%s,%s,%s)"
        #         insertContentSql="INSERT INTO "+insertTable+"(time,title,text,clicks)VALUES("+insertTime+" , "+insertTitle+" , "+insertText+" , "+insertClicks+")"
        
        
                        DB_insert=self.connectDB()
                        cursor_insert=DB_insert.cursor()        
                        cursor_insert.execute(insertContentSql,(inserttag,insertTitle,inserturl,insertauthor))
                        DB_insert.commit()
                        DB_insert.close()
                        print ('inert contents to  '+insertTable+' successfully'  )
                      
                    table='sxy_douban_mivie'
                    for i in range(len(rep_dict['subjects'])):
                        
#                         self.cursor.execute('''select * from sxy_douban_mivie where title = %s''',(rep_dict['subjects'][i]['title'],))
#                         film = self.cursor.fetchone()
#                         if film ==None:
                            try:
                                tag=self.tagsum[true]
                                
                                title=rep_dict['subjects'][i]['title']
                                url=rep_dict['subjects'][i]['url']
                                json_str2 = self.parser_url(url)
                                soup = BeautifulSoup(json_str2, 'lxml')
                                string= soup.find_all(class_ = 'attrs')  # get a list.
                                au = str(string[0]);
                                news = re.sub(u"\\<.*?\\>|\\{.*?}|\\[.*?]", "", au)
                                string= soup.find_all(class_ = 'rating_per')  # get a list.
                                star5=str(string[0])
                                star4=str(string[1])
                                star3=str(string[2])
                                star2=str(string[3])
                                star1=str(string[4])
                                string= soup.find_all(attrs={'property':'v:genre'})  # get a list.
                                au = str(string)
                                lei = re.sub(u"\\<.*?\\>|\\{.*?}", "", au)
                                lei = lei[1:-1]
                                string= soup.find_all(attrs={'property':'v:initialReleaseDate'})  # get a list.
                                au = str(string)
                                lei = re.sub(u"\\<.*?\\>|\\{.*?}", "", au)
                                time = lei[1:-1]
                                print(lei)
                                author=news
                                #inserttable(self,table,tag,title,url,author)
                            except:
                                continue
                         
                    num += 20
                true +=1    
                
                    
if __name__ == '__main__':
    douban = DouBan()
    douban.run()
