import requests

url = "https://indianrailways.p.rapidapi.com/index.php"

headers = {
    'x-rapidapi-host': "indianrailways.p.rapidapi.com",
    'x-rapidapi-key': "d7ef839508msh0da954446361c44p1036cajsn9f3229eab5b7"
}


def pnrstatus(querystring):
    if type(querystring) not in [int, float]:
        return TypeError("The PNR number should be non negative real number")
    elif querystring < 0:
        return TypeError("The PNR number cannot be less than 0")
    else:
        print("Loading...")
        response = requests.request("GET", url, headers=headers, params=str(querystring))
        if response.status_code == 200 or response.status_code == 201:
            if response.text == "{\"pnr\":\"\",\"error\":\"invalid pnr number\"}":
                print("Failed: " + response.text)
            else:
                print("Passed:" + response.text)
        else:
            print("Failed " + str(response.status_code) + " " + response.text)
        return response.status_code




if __name__ == "__main__": #Doesn't run while import
    print(pnrstatus(123456))