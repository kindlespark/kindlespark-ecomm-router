from fastapi import FastAPI
from router import Router

app = FastAPI()
router_list = []

@app.get("/")
async def router_shop():
    print(f"inside router_shop")
    return {"message": "Welcome to the Router Shop"}

@app.get("/routers")
async def get_routers():
    print(f"Get all router list")
    return {"available _routers": router_list}

@app.post("/new-router")
def add_new_router(router: Router):
    router_list.append(router.dict())
    return router_list

@app.get("/router/{id}")
def get_router_by_id(id: int):
    for router in router_list:
        if router['id'] == id:
            return router
        
@app.delete("/router/{id}")
def delete_router_by_id(id: int):
    for router in router_list:
        if router['id'] == id:
            router_id = router_list.index(router)
            router_list.pop(router_id)
            return router_list

# if __name__ == "__main__":
#     print(f"startup |")