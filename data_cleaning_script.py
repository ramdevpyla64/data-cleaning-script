import json
def clean_data(data):
    data["users"]= [user for user in data["users"] if user["name"].strip()]
    for user in data["users"]:
        user["friends"]=list(set(user["friends"]))
    data["users"]=[user for user in data["users"] if user["friends"] or user["liked_pages"]]
    unique={}
    for page in data['pages']:
        unique[page['id']]=page
    data['pages']=list(unique.values())
    return data
data =json.load(open("data.json"))
data =clean_data(data)
json.dump(data,open("cleaned_data1","w"),indent=4)
print("data cleaned successfully")
