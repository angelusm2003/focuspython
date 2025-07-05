# 🎧 Podcast API (Flask + SQLite)

## 📂 About the Solution

The solution is located in the `podcasts` folder. You can clone or download it from my GitHub repository.

- The project uses **SQLite** as the database.
- It works with a subset of the fields from the provided JSON.

---

## 🔍 Search Functionality

Search by **artist name**:

- Endpoint defined in `main.py`:
  
```
api.add_resource(PostName, '/podcast/<string:post_artistName>')
```
  
Example (GET request):

```
http://localhost:5000/podcast/Steve
```
    
This will search for podcasts where the artist name is Steve.

Search by ID:

Endpoint defined in main.py:

```
api.add_resource(PostResource, '/podcast/<int:post_id>')
```

Example (GET request):

```
http://localhost:5000/podcast/1
```

This will search for the podcast with ID 1.

➕ Create a New Podcast

Method: POST

URL:

```
http://localhost:5000/podcast
```

Using curl:

```
    curl http://localhost:5000/podcast \
        -X POST \
        -H "Content-Type: application/json" \
        -d '{"artistName":"Eminen", "name":"es una prueba", "kind":"rap", "copyright":"no", "artistId":1,"artistUrl":"www.wwwwwwwww","artworkUrl100":"www.fff","url":"wwwww.fffffffss"}'
```

✏️ Update a Podcast

Method: PATCH

URL:

```
http://localhost:5000/podcast/1
```

Using curl:

```
    curl http://localhost:5000/podcast/1 \
        -X PATCH \
        -H "Content-Type: application/json" \
        -d '{"artistName":"JCn", "name":"m", "kind":"rap22222", "copyright":"yes", "artistId":2,"artistUrl":"w","artworkUrl100":"www.f","url":"wwwww.f"}'
```

❌ Delete a Podcast

Method: DELETE

Example URL:

```
http://localhost:5000/podcast/1
```

This deletes the podcast with ID 1.

🗃️ JSON Helper Script

The file readjson.py generates the first20.json and last20.json files from the source URL provided.
⚙️ Installation

```
Python version: 3.7+
```

Steps

-Download the podcasts folder.

-Install dependencies using pip:

```
pip install Flask Flask-SQLAlchemy Flask-RESTful flask-marshmallow
```

Use the included database or create a new one:

```
from main import db
db.create_all()
exit()
```

Run the project:

Open in browser or Postman:

```
http://localhost:5000/podcast
```

Or use curl from your terminal (see examples above).

📬 Contact

Feel free to reach out to me by email if you have any questions.
Thanks for checking out the project!
