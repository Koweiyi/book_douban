'''
Created on 2020年6月16日

@author: 44786
'''
import requests
import json
import pprint


class DouBan():
    '''爬取豆瓣电视数据'''
    def __init__(self):
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0"}
        self.url = "https://movie.douban.com/j/search_subjects?type=tv&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start={}"
                    
    
    def get_url(self,pag, url):
        '''发送请求获取数据'''
        response = requests.get(url.format(pag), headers = self.headers)
        return response.content.decode()
    def parser_url(self, url):
        print(url)
        response = requests.get(url, headers = self.headers)
        return response.content.decode()

    def run(self):
        #发送请求获取响应
        for url in self.url:
            print("*"*50)
            num = 0
            while True:
                url = self.url.format(num)
                json_str = self.parser_url(url)
                
                #print(type(json_str))

                #提取数据
                #python类型的数据
                rep_dict = json.loads(json_str)

                #列表
                rep_list = rep_dict["subjects"]
                if len(rep_list) < 20:

                    print("豆瓣热门电视剧推荐信息收集完成")

                break

                #保存数据，只能写入str类型
                with open("douban.txt", "a", encoding="utf-8") as f:
                    for content in rep_list:
                        json.dump(content, f, ensure_ascii=False)    #ensure_ascii=Fales显示中文内容
                        #f.write(json.dumps(content, ensure_ascii=False))
                        f.write("\n")

                num += 20


if __name__ == '__main__':
    douban = DouBan()
    douban.run()
