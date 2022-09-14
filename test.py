import requests

BASE = "http://127.0.0.1:5000/"

"""
data = [{"likes": 15, "name": "Decorators in Python", "views": 150000}, 
		{"likes": 10, "name": "How to make REST API", "views": 100000}, 
		{"likes": 200, "name": "How to ace your DS & Algorithms assessment", "views": 2000000}]

for i in range(len(data)):
	response = requests.put(BASE + "video/" + str(i), data[i])
	print(response.json())
"""

response = requests.patch(BASE + "video/2", {})
print(response.json())