import requests

url = "https://icanhazdadjoke.com/"

payload={}
headers = {
  'Accept': 'application/json',
}

response = requests.request("GET", url, headers=headers, data=payload)

responseJson = response.json()

print(responseJson)
print('Wow that was funny huh')
