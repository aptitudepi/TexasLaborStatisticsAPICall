import json,requests
num = 309
strofnum = str(num)
for x in range(3668-309): 
        if (x < 1000):
                url = r"https://texaslaboranalysis.com/api/GetSupplySchoolDetail(Fice='000" + strofnum + "')"
                response = requests.get(url).json()        # API call to URL in line 8
                with open(f'out/000{num}.json', 'w') as f: # Dump Resulting JSON from HTTP GET API request
                                                           # # 3-digit ID numbers require 3 preceding zeroes. Python complains about preceding zeros, so I used string concatenation.
                        json.dump(response, f)
                num+=1
        else:
                url = r"https://texaslaboranalysis.com/api/GetSupplySchoolDetail(Fice='00" + strofnum + "')"
                response = requests.get(url).json()        # API call to URL in line 14
                with open(f'out/00{num}.json', 'w') as f:  # Dump resulting JSON from HTTP Get API Request
                                                           # # 4-digit ID numbers require 2 preceding zeroes. Python complains about preceding zeros, so I used string concatenation.
                        json.dump(response, f)
                num+=1
