from bs4 import BeautifulSoup
import requests

data = {
    "Referer": "https://www.mouser.com/ProductDetail/AVX/SCMS22F255MRBA0?qs=sGAEpiMZZMsCu9HefNWqpmIe8hz%2fozG9sdkguRTb0grxIiD2shqm1A%3d%3d",
    "User-Agent": "Mozilla/5.0 (Linux; Android 8.0.0; Pixel 2 XL Build/OPD1.170816.004) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Mobile Safari/537.36"
}
result = requests.get("https://www.mouser.com/ProductDetail/Maxwell-Technologies/PCAP0050-P230-S01?qs=sGAEpiMZZMsCu9HefNWqpmIe8hz%2fozG9OAZkcuosDr%252bBjldqqja7%252bg%3d%3d", params=data)
print(result.status_code)
print(result.text)