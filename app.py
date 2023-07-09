from flask import Flask, request
import cloudscraper
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
        return {'source':source}, 200
    except Exception as ex:
        return {'error': str(ex)}, 400

@app.route('/uc')
def uc():

    url = request.args.get('url')

    try:
        driver = uc.Chrome() 
        driver.get(url)
        return {'source':driver.page_source}, 200

    except Exception as ex:
        return {'error': str(ex)}, 400

if __name__ == '__main__':
    app.run()
