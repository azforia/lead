import sys

trades = sys.argv[1].split()
links = []
for i in range(len(trades)):    
    links.append("https://www.pinpoint7.net/BitcoinERA/?campaigns=Trade" + trades[i] + "&api_key=ROxUP76L7CNfJ8K&landings=BitcoinERA&product=")

print(links)