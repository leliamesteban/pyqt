import ipfsapi
import io

api = ipfsapi.connect('127.0.0.1', 5001)
res = api.add('test.txt')
print(api.cat(res['Hash']))

with io.open('sample.txt', 'w', encoding='utf-8') as f:
    numbytes = f.write('f.write returns the number of bytes written to the file')
api.add('sample.txt')
