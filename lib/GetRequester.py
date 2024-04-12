import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):

        response = requests.get(self.url)
        return response.content
        

    def load_json(self):

        response_body = self.get_response_body()
        json_data = json.loads(response_body)  # Convert response body to Python dictionary
        return json_data

        # response = requests.get(self.url)
        # return response.json()
        

get_requester = GetRequester("https://github.com/immanuelcherui1/python-p4-getting-remote-data-lab.git")

# get_requester = GetRequester('https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json')
# print(get_requester.load_json())
