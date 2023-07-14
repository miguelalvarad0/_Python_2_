import requests
import time
import api
import ids
import concurrent.futures
import threading

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
# def download_all_sites(sites):
#      with requests.Session() as session:
#         for i in range(0,150):
#             user = api.getOneUser_asyncio2(ids.ids[i],session)
#             print(user)


# if __name__ == "__main__":
    
#     sites = ["https://jsonplaceholder.typicode.com/users/"]
#     start_time = time.time()
#     download_all_sites(sites)
#     duration = time.time() - start_time
#     print(f"Downloaded in {duration} seconds, using aosync concurrency method")
# ----------------------------------------------------------------------------



# ----------------------------------------------------------------------------
# DOWNLOAD USERNAMES USING THREAD

thread_local = threading.local()


def get_session():
    if not hasattr(thread_local, "session"):
        thread_local.session = requests.Session()
    return thread_local.session


def download_site(sites):
    session = get_session()
    with session.get(sites) as response:
        for i in range(0,150):
            user = api.getOneUser_thread(ids.ids[i],response)
            print(user)


def download_all_sites(sites):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(download_site, sites)
        


if __name__ == "__main__":
    sites = [
        "https://jsonplaceholder.typicode.com/users/",
    ]
    start_time = time.time()
    download_all_sites(sites)
    duration = time.time() - start_time
    print(f"Downloaded in {duration} seconds, using thread concurency method")
# -------------------------------------------------------------------------------------