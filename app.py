from flask import Flask, request
import cloudscraper
import traceback

app = Flask(__name__)


@app.route('/')
def index():
    return 'INDEX'


@app.route('/scrape')
def search():

    url = request.args.get('url')

    try:
        scraper = cloudscraper.create_scraper()
        source = scraper.get(url).text
        return source, 200
    except Exception as ex:
        return {'error': ex, 'traceback': traceback.format_exc()}, 400


if __name__ == '__main__':
    app.run()
