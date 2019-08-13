import redis

conn = redis.Redis('localhost')

userdata = {"Name": "value", "Company": "COmpanyname", "Address": "ADD", "Location": "Location"}

conn.hmset("pythonDict", userdata)

conn.hgetall("pythonDict")

[{'Company': 'CryptoAimdy PVT LTD', 'Address': 'Hyderabad', 'Location': 'HiTech City', 'Name': 'CryptoAimdy'},

 {'Company': 'Microsoft', 'Address': 'Hyderabad', 'Location': 'Gachibowli', 'Name': 'Ashfaque'}]