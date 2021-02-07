from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from flask_marshmallow import Marshmallow
from flask_restful import Api, Resource
import json,urllib.request

#json file
datasource = urllib.request.urlopen("https://rss.itunes.apple.com/api/v1/us/podcasts/top-podcasts/all/100/explicit.json").read()

#database setup
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///podcast.db'
db = SQLAlchemy(app)
ma = Marshmallow(app)
api = Api(app)

#database model
class Post(db.Model):
    artistName = db.Column(db.String(100))
    id = db.Column(db.Integer, primary_key=True)
    releaseDate =db.Column(db.DateTime) 
    name = db.Column(db.String(100))
    kind = db.Column(db.String(50))
    copyright = db.Column(db.String(100))
    artistId = db.Column(db.Integer)
    contentAdvisoryRating = db.Column(db.String(25))
    artistUrl = db.Column(db.String(100))
    artworkUrl100 = db.Column(db.String(100))
    genreId = db.Column(db.Integer)
    namegen = db.Column(db.String(50))
    urlgen = db.Column(db.String(100))
    genreId2 = db.Column(db.Integer)
    namegen2 = db.Column(db.String(50))
    urlgen2 = db.Column(db.String(100))
    genreId3 = db.Column(db.Integer)
    namegen3 = db.Column(db.String(50))
    urlgen3 = db.Column(db.String(100))
    genreId4 = db.Column(db.Integer)
    namegen4 = db.Column(db.String(50))
    urlgen4 = db.Column(db.String(100))
    genreId5 = db.Column(db.Integer)
    namegen5 = db.Column(db.String(50))
    urlgen5= db.Column(db.String(100))
    url = db.Column(db.String(100))
 

    def __repr__(self):
        return '<Post %s>' % self.id

#"genreid1", "namegen1", "urlgen1"
#"contentAdvisoryRating"
# "genreId1"        

class PostSchema(ma.Schema):
    class Meta:
        fields = ("artistName", "id", "releaseDate", "name", "kind", "copyright", "artistId", "contentAdvisoryRating",
                  "artistUrl","artworkUrl100", "genreId", "namegen", "urlgen", "genreId2", "namegen2", "urlgen2", "genreId3", 
                  "namegen3", "urlgen3","genreId4", "namegen4", "urlgen4", "genreId5", "namegen5", "urlgen5","url")
                


post_schema = PostSchema()
posts_schema = PostSchema(many=True)

#definition of apis

#select all
class PostListResource(Resource):
    def get(self):
        posts = Post.query.all()
        return posts_schema.dump(posts)

#create
    def post(self):
        new_post = Post(
            artistName=request.json['artistName'],
            name=request.json['name'],
            kind=request.json['kind'],
            copyright=request.json['copyright'],
            artistId=request.json['artistId'],
            artistUrl=request.json['artistUrl'],
            artworkUrl100=request.json['artworkUrl100'],
            url=request.json['url']
        )
        db.session.add(new_post)
        db.session.commit()
        return post_schema.dump(new_post)

#search for id
class PostResource(Resource):
    def get(self, post_id):
        post = Post.query.get_or_404(post_id)
        return post_schema.dump(post)
    
#update for id
    def patch(self, post_id):
        post = Post.query.get_or_404(post_id)

        if 'artistName' in request.json:
            post.artistName = request.json['artistName']
        if 'name' in request.json:
            post.name = request.json['name']
            
        if 'kind' in request.json:
            post.kind = request.json['kind']
        if 'copyright' in request.json:
            post.copyright = request.json['copyright']  
            
        if 'artistId' in request.json:
            post.artistId = request.json['artistId']
        if 'artistUrl' in request.json:
            post.artistUrl = request.json['artistUrl']
            
        if 'artworkUrl100' in request.json:
            post.artworkUrl100 = request.json['artworkUrl100']
        if 'url' in request.json:
            post.url = request.json['url']    
            
        db.session.commit()
        return post_schema.dump(post)

#delete by id
    def delete(self, post_id):
        post = Post.query.get_or_404(post_id)
        db.session.delete(post)
        db.session.commit()
        return '', 204

#search for name
class PostName(Resource):
    def get(self, post_artistName):
        post = Post.query.filter_by(artistName=post_artistName).first()
        return post_schema.dump(post)   

class PostGroupName(Resource):
    def get(self,post_artistName):
      
        posts=Post.query(post_artistName).group_by(post_artistName).all()
        
        return posts_schema.dump(posts)   

class PostTop20(Resource):
    def get(self):       
        
        #first 20 records are saved in a new json file with name first.json
        output = json.loads(datasource)
        var=[]
        var=output['feed']['results'][0:20]
        with open("first.json", "w") as p: 
            json.dump(var,p) 
        pass

class PostReplaceTop20(Resource):
    def get(self):   
        #datasource2 = urllib.request.urlopen("https://rss.itunes.apple.com/api/v1/us/podcasts/top-podcasts/all/100/explicit.json").read()
        #first 20 records are replaced for the button 20 in a new json file with name last20.json
        output = json.loads(datasource)
        last20=output['feed']['results'][-20:]+output['feed']['results'][20:81]+output['feed']['results'][-20:]
        with open("last20.json", "w") as p: 
            json.dump(last20,p)   
        pass

#endpoints
api.add_resource(PostListResource, '/podcast')
api.add_resource(PostResource, '/podcast/<int:post_id>')
api.add_resource(PostName, '/podcast/<string:post_artistName>')
api.add_resource(PostGroupName, '/podcastgroup/<string:post_artistName>')
api.add_resource(PostTop20, '/podcastop20')
api.add_resource(PostReplaceTop20, '/podcastlast20')

if __name__ == '__main__':
    app.run(debug=True)
