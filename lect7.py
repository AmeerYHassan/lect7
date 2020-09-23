import flask
import os

app = flask.Flask(__name__)
artists = ["Molchat Doma", "Car Seat Headrest", "Ic3peak", "The Weeknd", "The Smiths"]
artist_pictures = ["molchat_doma.jpg", "car_seat_headrest.jpg", "ic3peak.jpg", "the_weeknd.jpg", "the_smiths.jpg"]
@app.route('/')
def index():
    return flask.render_template(
        "index.html",
        artistsLen = len(artists),
        favArtists = artists,
        pictures_len = len(artist_pictures),
        pictures = artist_pictures
    )

app.run(
    port = int(os.getenv('PORT', 8080)),
    host = os.getenv('IP', '0.0.0.0'),
    debug=True
)
