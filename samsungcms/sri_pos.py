import json
from sri_client import SRIClient  # Assuming SRIClient is imported from another module

class ApiException401(Exception):
    def __init__(self, status_code, response):
        self.status_code = status_code
        self.response = response
        super().__init__(f"API error {status_code}: {response.content}")

class SMAPI(object):
    quippets_uri = "/queries/"

    def __init__(self):
        self.client = SRIClient()

    def _return_json(self, http_response):
        """Return JSON from HTTP response, or raise an error."""
        r = http_response
        if r.status_code == 200:
            return r.json
        elif r.status_code == 401:
            raise ApiException401(r.status_code, r)
        elif r.status_code == 404:
            raise django.http.Http404("Page not found")
        elif r.status_code != 500:
            error_data = dict(error=r.json) if isinstance(r.json, dict) else json.loads(r.json) if r.json else {}
            raise ApiException(r.status_code, error_data)
        else:
            raise Exception("API error {0}: {1}".format(r.status_code, r.content))

    def call_json_method(self, method_name, *args, **kwargs):
        """Call a method from the JSON file and return the JSON object."""
        try:
            with open('data.json') as f:  # Assuming data.json is the JSON file containing the data
                data = json.load(f)
            method = getattr(self, method_name)
            return method(data, *args, **kwargs)
        except FileNotFoundError:
            raise Exception("JSON data file not found.")
        except AttributeError:
            raise Exception(f"Method '{method_name}' not found.")

    def get_website_data(self, data):
        """Demo function to get website data from JSON."""
        return data.get('website_data', {})

    def get_social_links(self, data):
        """Demo function to get social links from JSON."""
        return data.get('social_links', [])

    def get_locations(self, data):
        """Demo function to get locations from JSON."""
        return data.get('locations', [])
    
    def get_stores_data(self, data):
        pass

# Example usage:
# api = PWAPI()
# website_data = api.call_json_method('get_website_data')
# social_links = api.call_json_method('get_social_links')
# locations = api.call_json_method('get_locations')