import base64
import zlib

f = open('./items_demo.json',encoding='utf-8')
json = f.read()
f.close()

compressed = zlib.compress(str.encode(json))
encoded = base64.b64encode(compressed)
replaced = encoded.replace(b'+',b'-').replace(b'/',b'_')

f = open('./items_code_demo.txt', 'wb')
f.write(replaced)
f.close()