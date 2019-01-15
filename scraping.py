from html.parser import HTMLParser
import difflib
import requests
import sched, time


r = requests.get('https://giraffewarrior.github.io/scrapingtest/')
y = r.text
f = open("scrapeddata.html", "w+")
f.write(y)
f.close()
time.sleep(2)
r1 = requests.get('https://giraffewarrior.github.io/scrapingtest/')
y1 = r1.text
f1 = open("scrdata2.html", "w+")
f1.write(y1)
f1.close
#f = open("samplehtml.html")
 
 
# for line in f.readlines():
#         print(line)
#         time.sleep(2)

f2 = open("textdata.txt", "w+")
f3 = open("textdata2.txt", "w+")
class MyHTMLParser(HTMLParser):
    def handle_data(self, data):
        if (data.isspace()):
         return
        f2.write(data)
        
class MyHTMLParser2(HTMLParser):
    def handle_data(self, data2):
        if (data2.isspace()):
         return
        f3.write(data2)

f4 = open("scrapeddata.html")
parser = MyHTMLParser()
if f4.mode == "r":
    contents = f4.read() # read the entire file
    parser.feed(contents)

f5 = open("scrdata2.html")
parser2 = MyHTMLParser2()
if f5.mode == "r":
    contents2 = f5.read() # read the entire file
    parser2.feed(contents2)


