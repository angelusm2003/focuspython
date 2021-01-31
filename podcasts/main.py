from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api, Resource

#database setup
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///podcast.db'
db = SQLAlchemy(app)
ma = Marshmallow(app)
api = Api(app)

#database model
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    artistName = db.Column(db.String(100))
    name = db.Column(db.String(100))
    kind = db.Column(db.String(50))
    copyright = db.Column(db.String(200))
    artistId = db.Column(db.Integer)
    artistUrl = db.Column(db.String(200))
    artworkUrl100 = db.Column(db.String(200))
    url = db.Column(db.String(200))
    

    def __repr__(self):
        return '<Post %s>' % self.artistName


class PostSchema(ma.Schema):
    class Meta:
        fields = ("id","artistName", "name", "kind", "copyright", "artistId", "artistUrl", "artworkUrl100", "url")
                


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
    def get(self):
        posts=Post.query.all().group_by(request.json['name'])
        print(posts)
        return post_schema.dump(posts)    


#endpoints
api.add_resource(PostListResource, '/podcast')
api.add_resource(PostResource, '/podcast/<int:post_id>')
api.add_resource(PostName, '/podcast/<string:post_artistName>')
api.add_resource(PostGroupName, '/podcastgroup/<string:post_name>')

if __name__ == '__main__':
    app.run(debug=True)
