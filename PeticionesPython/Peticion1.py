import hashlib
import time

# Your API key and private key
PUBLIC_KEY = "1bf075d536f284d8d6c923c4b425be90"
PRIVATE_KEY = "94c1286e33750006ed249aac0b114366a3a41694"

# Generate a timestamp
timestamp = str(time.time())

# Combine the timestamp, private key, and API key
hash_string = timestamp + PRIVATE_KEY + PUBLIC_KEY

# Generate an MD5 hash of the resulting string
hash = hashlib.md5(hash_string.encode()).hexdigest()

# Include the hash and API key in your request URL
url = f"https://gateway.marvel.com/v1/public/characters?apikey={PUBLIC_KEY}&hash={hash}&ts={timestamp}"
url2 = f"https://gateway.marvel.com:443/v1/public/characters?nameStartsWith=I&orderBy=name&limit=5&apikey={PUBLIC_KEY}&hash={hash}&ts={timestamp}"
url3 = f"https://gateway.marvel.com:443/v1/public/series?apikey={PUBLIC_KEY}&hash={hash}&ts={timestamp}"
#https://gateway.marvel.com:443/v1/public/series?apikey=1bf075d536f284d8d6c923c4b425be90
#https://gateway.marvel.com:443/v1/public/characters?nameStartsWith=I&orderBy=name&limit=5&apikey=1bf075d536f284d8d6c923c4b425be90
print(url)
print(url2)
print(url3)

