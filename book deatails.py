import requests
import re

url = "https://books.toscrape.com/catalogue/under-the-tuscan-sun_504/index.html"
response = requests.get(url)
text = response.text
image_find = re.compile(r'\s*<div class="item active">\s*<img src="(.*?)" alt="(.*?)">.*', re.S | re.DOTALL)
x = image_find.findall(text)
text_find = re.compile(r'\s*<th>(.*?)\s*<td>(.*?)\s*<', re.S | re.DOTALL)
y = text_find.findall(text)
for he in x:
    he = str(he)
    xi = re.sub(r'\/>\s*.+', " ", he)
    xi = xi.replace("(", "")
    xi = xi.replace("'", "")
    xi = xi.replace('"', "")
    dic1 = {xi[0:62]: xi[62:103]}
    for x, value in dic1.items():
        print("This photo is", x, "\nThe book name:", value)
print(" Book details is:: ")
for hi in y:
    hi1 = str(hi[0])
    hi0 = hi1.replace('</th>', " ")
    dic = {hi0: hi[1]}
    for xi, yi in dic.items():
        print(" ", xi, "   ", yi)
