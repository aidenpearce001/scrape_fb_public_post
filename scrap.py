# -*- coding: utf8 -*-
from bs4 import BeautifulSoup
import urllib.request
from bs4 import Comment
import re

url = 'https://www.facebook.com/phuongthao.le.142/posts/2043742905729911'
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page,"html.parser",from_encoding="utf-8")
f = open('new.txt','w',encoding="utf-8")
# f.write(str(soup.find_all('div')))
ls = []
for link in soup.find_all('div',class_ = 'hidden_elem'):
    # f.write(str(link.prettify()))
    # print(link.find_all('div'))
    # print(link.find_all('code'))
    for link1 in link.find_all('code'):
        comments = link1.find_all(string=lambda text: isinstance(text, Comment))
        for c in comments:
            result = re.findall(r'<p>.+?</p>',c)
            string = re.sub('<span.*?</span>','',str(result), flags=re.DOTALL)
            string = string.replace("</span>","")
            f.write(str(string))
            for match in re.findall(r"<[p]>(.+?)</[p]>",str(string)):
                print(match)
                # ls.append(match.string)
                f.write(str(match))

            # stripped = re.sub("<span>.*</span>", "", result)
            # print(result)
            # print(stripped)
            # print(c.split('<p>'))
            # f.write(str(result))
            print("===========")
            
        # print(link1.find_all('class'))

# print(ls)        
    # if 'mtm _5pco' in link.get('class'):
    #     print('yes')
    # print((link.get('class')))
    # f.write(str(link.get('class')))
    # print(link.get('href'))
    # if 'mtm _5pco' in str(link):
    #     print('1')
    # print(str(link))
    # print(link)
# s = soup.prettify()
# divs = soup.find('div', class_="mtm _5pcm")
# print(divs)
# for div in divs:
#     p = div.find('p')
#     print(p.get_text())
# print(soup.find_all('div',{'class':'mtm _5pco'})


# section = soup.find_all('div', {'data-testid': 'mtm _5pco'})
# print(section)
# for elem in section:
#     wrappers = elem.find_all('p')
#     print(wrappers)
# # text = soup.get_text()
# # print(text)
# # print(soup.prettify()) 


# f = open('file','w+',encoding="utf-8")
# f.write(soup.prettify())
# # print(page_content)
# regex = re.compile('^_5mfr')
# content_lis = soup.find_all('div', attrs={'class': regex})
# print(content_lis)