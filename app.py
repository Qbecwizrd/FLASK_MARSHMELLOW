from flask import Flask, request


app=Flask(__name__)

stores =[
    {
        "name":"MyStore",
        "Items":[
            {
                "name":"Chair",
                "price":194.55
            }
        ]
    }
]

@app.get("/store")
def get_stores():
    return {"stores": stores},200


@app.post("/store")
def create_store():
    request_data=request.get_json()
    new_store={
        "name":request_data["name"],"items":[]
    }
    stores.append(new_store)
    return new_store,201

##what if the store name should be specified

@app.post("/store/<string:name>")
def create_item(name):
    new_data=request.get_json()
    for store in stores:
        if store["name"]==name:
            new_item={"name":new_data["name"],"price":new_data["price"]}
            store["items"].append(new_item)
            return new_item
    return {"message":"store not found"},404

@app.get("/store/<string:name>/item")
def get_item_in_store(name):
    new_data=request.get_json()
    for store in stores:
        if store["name"]==name:
            return {"items":store["items"]}
    return {"message":"store not found"},404