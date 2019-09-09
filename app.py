from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    """Return homepage."""
    # TODO: Extract query term from url
    search = request.args.get('search')
    # TODO: Make 'params' dict with query term and API key
    payload = {
    	"q": search,
    	"key": "5KADMY4UP11V"
    }
    # TODO: Make an API call to Tenor using the 'requests' library
    r = requests.get("https://api.tenor.com/v1/search?", params=payload)
    data = r.json()
    print(data)
    # TODO: Get the first 10 results from the search results

    # TODO: Render the 'index.html' template, passing the gifs as a named parameter

    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)