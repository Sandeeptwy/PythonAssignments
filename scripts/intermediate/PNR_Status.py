import requests

url = "https://indianrailways.p.rapidapi.com/index.php"


headers = {
    'x-rapidapi-host': "indianrailways.p.rapidapi.com",
    'x-rapidapi-key': "d7ef839508msh0da954446361c44p1036cajsn9f3229eab5b7"
}


def pnrstatus(querystring):
    print("Loading... \n")
    response = requests.request("GET", url, headers=headers, params=querystring)
    print("response: " + response.text)