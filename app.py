from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    """Return homepage."""
    search = request.args.get('search')
    payload = {
    	"q": search,
    	"key": "5KADMY4UP11V"
    }
    req = requests.get("https://api.tenor.com/v1/search?", params=payload)
    data = req.json()
    results = data["results"][0:10]
    return render_template(
        "index.html",
        results=results
        )

if __name__ == '__main__':
    app.run(debug=True)
    # 
    # TODO: Extract query term from url
    # TODO: Render the 'index.html' template, passing the gifs as a named parameter
    # TODO: Make 'params' dict with query term and API key
    # TODO: Get the first 10 results from the search results
    # TODO: Make an API call to Tenor using the 'requests' library