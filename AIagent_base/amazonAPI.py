import keepa

api = keepa.Keepa("YOUR_KEEPA_API_KEY")

asin = "B0CDSP8G6Q"
response = api.query(asin)

print("Title:", response[0]['title'])
print("Current price:", response[0]['buyBoxPrice'])
print("Lowest price:", response[0]['csv'][0])