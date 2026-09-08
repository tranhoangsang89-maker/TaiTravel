import urllib.request, re

try:
    req = urllib.request.Request('https://commons.wikimedia.org/w/index.php?search=Xanh+SM&title=Special:MediaSearch&go=Go&type=image', headers={'User-Agent': 'Mozilla/5.0'})
    html = urllib.request.urlopen(req).read().decode('utf-8')
    urls = re.findall(r'https://upload\.wikimedia\.org/wikipedia/commons/thumb/[^\"]+?\.jpg/[^\"]+?\.jpg', html)
    print("Xanh SM:")
    for u in urls[:5]: print(u)
except Exception as e:
    print("Error:", e)
