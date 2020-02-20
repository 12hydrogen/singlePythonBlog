from time import time
import hashlib

now = time()
sha = hashlib.sha256()
sha.update(bytes(str(now), 'utf-8'))

with open('key', 'wb') as key:
	key.write(bytes(sha.hexdigest(), 'utf-8'))

	