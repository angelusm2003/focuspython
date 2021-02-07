import sqlite3
import json,urllib.request
import datetime

def checkKey(row, key): 
    #print(row)
    #print(key)
    if key in row.keys(): 
        return row[key]
    else: 
        return None
  
dat = urllib.request.urlopen("https://rss.itunes.apple.com/api/v1/us/podcasts/top-podcasts/all/100/explicit.json").read()
output = json.loads(dat)

genreId=[None, None, None, None, None]
namegen=[None, None, None, None, None]
urlgen=[None, None, None, None, None]

dataframe= list()

for row in output['feed']['results']:
  date = datetime.datetime.strptime(row['releaseDate'], '%Y-%m-%d')
  contentadvi=checkKey(row,'contentAdvisoryRating')
  copyri=checkKey(row,'copyright')
  artistId=checkKey(row,'artistId')
  artistU=checkKey(row,'artistUrl')
  i=0
  for gen in row['genres']:
    genreId[i]=gen['genreId']
    namegen[i]=gen['name']
    urlgen[i]=gen['url']
    i=i+1
   
  data = (str(row['artistName']), int(row['id']), date, str(row['name']), str(row['kind']), copyri, artistId, contentadvi,
          artistU, str(row['artworkUrl100']),
          genreId[0], namegen[0],urlgen[0], 
          genreId[1], namegen[1],urlgen[1],
          genreId[2], namegen[2],urlgen[2],
          genreId[3], namegen[3],urlgen[3],
          genreId[4], namegen[4],urlgen[4],
          str(row['url'])
          )

  dataframe.append(data)

try:
 db = sqlite3.connect('podcast.db')
 cursor = db.cursor()
 cursor.execute('''create table post (artistName varchar(100),
                                      id int, 
                                      releaseDate datetime,
                                      name varchar(100),
                                      kind varchar(50), 
                                      copyright varchar(100),
                                      artistId int,
                                      contentAdvisoryRating varchar(25),
                                      artistUrl varchar(100),
                                      artworkUrl100 varchar(100),
                                      genreId int,
                                      namegen varchar(50), 
                                      urlgen varchar(100),
                                      genreId2 int,
                                      namegen2 varchar(50), 
                                      urlgen2 varchar(100),
                                      genreId3 int,
                                      namegen3 varchar(50), 
                                      urlgen3 varchar(100),
                                      genreId4 int,
                                      namegen4 varchar(50), 
                                      urlgen4 varchar(100),
                                      genreId5 int,
                                      namegen5 varchar(50), 
                                      urlgen5 varchar(100),
                                      url varchar(100))''')
except Exception as E:
 print('Error :', E)
else:
 print('table created')
 

try:
 cursor.executemany('insert into post values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', dataframe)
except Exception as E:
 print('Error', E)
else:
 db.commit()
 print('data inserted')
 
