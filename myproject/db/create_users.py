from main import User, Session, engine

users = [
    {
        "username": "jerry",
        "email": "jerry@company.com"
    },
    {
        "username": "jack",
        "email": "jack@company.com"
    },
    {
        "username": "ben",
        "email": "ben@company.com"
    },
    {
        "username": "twigo",
        "email": "twigo@company.com"
    },
    {
        "username": "skopa",
        "email": "skopa@company.com"
    },
    {
        "username": "weezy",
        "email": "weezy@company.com"
    },
    {
        "username": "fbaby",
        "email": "fbaby@company.com"
    },
]

local_session=Session(bind=engine)

#new_user = User(username="jona", email="jona@company.com")

#local_session.add(new_user)
 
#local_session.commit()

for u in users:
    new_user = User(username=u["username"], email=u["email"])
    print(new_user)

    local_session.add(new_user)

    local_session.commit()

    print(f"Added {u['username']}")