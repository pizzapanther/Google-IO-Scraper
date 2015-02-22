# Google-IO-Scraper
Tool to help find Google IO Codes in images

## Directions for finding a Google IO Code in images
1. Run the scraper

        cd gio
        scrapy crawl image1 -o images1.json
1. Process the JSON images

        ./process_json.py images1.json
1. Open `index.html` and browse images. Look for codes!

## Keyboard Navigation
Next Page: press `n`

Previous Page: press `b`
