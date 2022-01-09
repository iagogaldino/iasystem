import google_images_download_del

response = google_images_download_del.googleimagesdownload()

search_queries = ["Coca cola lata 350"]


def downloadimages(query):

    arguments = {
        "keywords": query,
        "format": "png",
        "limit": 1,
        "print_urls": True,
        "size": "medium",
        "aspect_ratio": "panoramic",
        "prefix": query,
    }
    try:
        return response.download(arguments)

    except FileNotFoundError:
        arguments = {
            "keywords": query,
            "format": "png",
            "limit": 1,
            "print_urls": True,
            "size": "medium",
        }

        try:
            return response.download(arguments)
        except:
            pass


def runDownload():
    for query in search_queries:
        downloadimages(query)
        print()


# downloadimages("coca cola")
