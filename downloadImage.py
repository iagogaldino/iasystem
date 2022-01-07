from google_images_download import google_images_download

response = google_images_download.googleimagesdownload()

search_queries = ["Coca cola lata 350"]


def downloadimages(query):

    arguments = {
        "keywords": query,
        "format": "png",
        "limit": 4,
        "print_urls": True,
        "size": "medium",
        "aspect_ratio": "panoramic",
    }
    try:
        response.download(arguments)

    except FileNotFoundError:
        arguments = {
            "keywords": query,
            "format": "png",
            "limit": 4,
            "print_urls": True,
            "size": "medium",
        }

        try:
            response.download(arguments)
        except:
            pass


def runDownload():
    for query in search_queries:
        downloadimages(query)
        print()
