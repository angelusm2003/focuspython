About the solution

The solution is in the folder podcasts, you can clone it or download for my github
I use sql lite for the solution and some of the fields of the json provided

1. The search look up is implemented in the file main.py using the endpoint:

api.add_resource(PostName, '/podcast/<string:post_artistName>')

-you can try this in postman or directly in your console using the method GET:

http://localhost:5000/podcast/Steve in this example steve is the name of the artist we are looking for

-also you can look by id , the endpoint:

api.add_resource(PostResource, '/podcast/<int:post_id>')

-you can try this in postman or directly in your console using the method GET:

http://localhost:5000/podcast/1 in this example 1 is the id of the artist we are looking for

2. There is a service to create a new podcast, you can access using the method POST in postman through:

http://localhost:5000/podcast

or use curl in the terminal always specifing the fields like this:

curl http://localhost:5000/podcast \  
    -X POST \ 
    -H "Content-Type: application/json" \
    -d '{"artistName":"Eminen", "name":"es una prueba", "kind":"rap", "copyright":"no", "artistId":1,"artistUrl":"www.wwwwwwwww","artworkUrl100":"www.fff","url":"wwwww.fffffffss"}'

3. There is a service to update a podcast you can access using the method PATCH through:

http://localhost:5000/podcast

or use curl in the terminal always specifing the fields like this:

curl http://localhost:5000/podcast/1 \
    -X PATCH \
    -H "Content-Type: application/json" \
    -d '{"artistName":"JCn", "name":"m", "kind":"rap22222", "copyright":"yes", "artistId":2,"artistUrl":"w","artworkUrl100":"www.f","url":"wwwww.f"}'



4. There is a service to delete a podcast you can access using the method DELETE through:

http://localhost:5000/podcast/1 in this example 1 is the id of the artist we want to delete

5. There also a file readjson.py that create first and last20 json files from the url provided

Installation

Python version is 3.7

1.Download the folder podcasts
2. In the terminal of python install the dependencies needed for the project using pip:

$ pip install Flask \
    Flask-SQLAlchemy \
    Flask-RESTful \
    flask-marshmallow
3. You can use the database included in the project or create a new one executing this in the terminal:

from main import db
db.create_all()
exit()
4. You are ready to run the project in http://localhost:5000/podcast using a tool like postman or using the command curl in the terminal, taking in consideration the methods at the beginning.

Finally you can write me if you have any questions to my email. Thanks
