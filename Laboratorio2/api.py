import requests as req


def getOneUser(id):
    url = "https://jsonplaceholder.typicode.com/users/"
    response = req.get(url)
    return response.json()[id]['name']



def getOneUser_asyncio2(id,session):
    url = "https://jsonplaceholder.typicode.com/users/"
    response = session.get(url)
    return response.json()[id]['name']
          

          