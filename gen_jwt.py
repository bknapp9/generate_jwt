import requests

# Read in local private.key files - also can read from a DB
with open('jajam.key') as f:
    profileKey = f.read()

payload = {'domain': 'jajam',
           'privateKey': profileKey,
           'profileKey': 'BFCK102-N064KZJ-QSA6ADF-31M84M8'}
headers = {'Content-Type': 'application/json',
           'Authorization': 'Bearer TKVGSY3-2KRMR6F-NPF0QPD-S69WPB0'}

r = requests.post('https://app.ayrshare.com/api/profiles/generateJWT',
                  json=payload,
                  headers=headers)

print(r.json())
