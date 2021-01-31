import json,urllib.request
data = urllib.request.urlopen("https://rss.itunes.apple.com/api/v1/us/podcasts/top-podcasts/all/100/explicit.json").read()


#first 20 records are saved in a the sample json file

output = json.loads(data)
var=[]
var=output['feed']['results'][0:20]
with open("first.json", "w") as p: 
    json.dump(var,p) 
   
#last 20 records are saved in a the sample json file
    
last20=output['feed']['results'][-20:]
with open("last20.json", "w") as p: 
    json.dump(last20,p)     