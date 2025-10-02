import cloudscraper
class CloudFlareSolver:
    @staticmethod
    def request(method, url, **kwargs):
        scraper = cloudscraper.create_scraper()
        return scraper.request(method, url, **kwargs)

    @staticmethod
    def get(url, **kwargs):
        return CloudFlareSolver.request("GET", url, **kwargs)

    @staticmethod
    def post(url, **kwargs):
        return CloudFlareSolver.request("POST", url, **kwargs)

    @staticmethod
    def put(url, **kwargs):
        return CloudFlareSolver.request("PUT", url, **kwargs)

    @staticmethod
    def delete(url, **kwargs):
        return CloudFlareSolver.request("DELETE", url, **kwargs)

    @staticmethod
    def head(url, **kwargs):
        return CloudFlareSolver.request("HEAD", url, **kwargs)

    @staticmethod
    def options(url, **kwargs):
        return CloudFlareSolver.request("OPTIONS", url, **kwargs)

    @staticmethod
    def patch(url, **kwargs):
        return CloudFlareSolver.request("PATCH", url, **kwargs)
        