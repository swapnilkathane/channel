import requests
from bs4 import BeautifulSoup as  bs
import _json
#Dist=input("Enter the district to get live number of corona cases")

response=requests.get("https://api.covid19india.org/state_district_wise.json")
r=response.json()
#rint(type(r))
for i,j in r.items():
    #print(i,j)
    for k,l in j.items():
        if i=="Maharashtra" :
            #print(k,l)
            for m,n in l.items():
                #print(m,n)
                for o,p in n.items():
                    for Dist in
                    if o=="confirmed":

                        print(m,p)


