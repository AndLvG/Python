 from urllib.parse import urlparse, parse_qs
url = input()
kod = input()
o = urlparse(url)
query = parse_qs(o.query)
print(*query[kod])
