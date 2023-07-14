import requests
import time
import api
import ids

# ----------------------------------------------------------------------------
# DOWNLOAD USERNAMES USING NO CONCURRENCY METHOD 

# def descargar_usuarios():
#     for i in range(0,150):
#         user = api.getOneUser(ids.ids[i])
#         print(user)

# start_time = time.time()
# descargar_usuarios()
# duration = time.time() - start_time
# print(f"Users downloaded in {duration} seconds, using a non concurrency method")
# ----------------------------------------------------------------------------




# ----------------------------------------------------------------------------
# DOWNLOAD USERNAMES USING ASYNCIO 
def download_all_sites(sites):
     with requests.Session() as session:
        for i in range(0,150):
            user = api.getOneUser_asyncio2(ids.ids[i],session)
            print(user)


if __name__ == "__main__":
    
    sites = ["https://jsonplaceholder.typicode.com/users/"]
    start_time = time.time()
    download_all_sites(sites)
    duration = time.time() - start_time
    print(f"Downloaded in {duration} seconds, using aosync concurrency method")
# ----------------------------------------------------------------------------