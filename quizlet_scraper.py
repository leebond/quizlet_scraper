# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 15:16:10 2018

@author: Guanhua
"""

from bs4 import BeautifulSoup
import urllib3
import csv

def parse_url(myurl):
    url = myurl
    http = urllib3.PoolManager()
    response = http.request('GET', url)
    soup = BeautifulSoup(response.data, features="lxml")
    
    # find list of all span elements containing the words and definitions
    wordspan = soup.find_all('span', {'class' : 'TermText notranslate lang-en'})
    #print(wordspan[-2])
    #print(wordspan[-1])
    
    # create list of lines corresponding to element texts 
    content = [span.get_text(separator=u" ") for span in wordspan]
    #print(content)
    
    return content

def content_dict(content):
    content_dict = {}
    for i in range(len(content)):
        if i % 2 == 0:
            content_dict[content[i]] = content[i+1]
    return content_dict

if __name__ == '__main__':
    urls = ["https://quizlet.com/154676205/networking-chapter-1-flash-cards/",\
            "https://quizlet.com/8441391/634-multi-final-flash-cards/",\
            "https://quizlet.com/14155256/cd-ch3-flash-cards/",\
            "https://quizlet.com/154929352/networking-chapter-3-flash-cards/",\
            "https://quizlet.com/228063800/is-312-chapter-2-flash-cards/",\
            "https://quizlet.com/154920713/networking-chapter-2-flash-cards/"]
    all_content = []
    for url in urls:
        all_content += parse_url(url)
    
    content = content_dict(all_content)
    
    with open('CS625_quizlet_chap123.csv','w', newline='') as out:
        for key, val in content.items(): 
            mywriter = csv.writer(out, delimiter = ',')
            mywriter.writerow([key,val])    