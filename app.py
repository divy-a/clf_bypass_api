from flask import Flask, request
import cloudscraper
import cfscrape
import undetected_chromedriver as uc 
import traceback

app = Flask(__name__)


@app.route('/')
def index():
    return 'INDEX'


@app.route('/cloud_scrapper')
def cloud_scrapper():

    url = request.args.get('url')

    try:
        scraper = cloudscraper.create_scraper()
        source = scraper.get(url).text
        return source, 200
    except Exception as ex:
        return {'error': ex, 'traceback': traceback.format_exc()}, 400


@app.route('/cfscrape')
def cfscrape():

    url = request.args.get('url')

    try:
        scraper = cfscrape.create_scraper()
        scraped_data = scraper.get(url)
        return scraped_data.text, 200

    except Exception as ex:
        return {'error': ex, 'traceback': traceback.format_exc()}, 400

@app.route('/uc')
def uc():

    url = request.args.get('url')

    try:
        driver = uc.Chrome() 
        driver.get('https://opensea.io/rankings/trending')
        return driver.page_source, 200

    except Exception as ex:
        return {'error': ex, 'traceback': traceback.format_exc()}, 400

if __name__ == '__main__':
    app.run()
