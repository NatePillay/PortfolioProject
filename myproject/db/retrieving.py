from main import User, Session, engine

#create local session class

local_session=Session(bind=engine)


#returns all objects
users=local_session.query(User).all()
#users=local_session.query(User).all()[:3] returns 3 results


#loop through query set and return users
for user in users:
    print(user.username)
    

#query to return one object based on ID or specific attribute it has
#jona=local_session.query(User).filter(User.username=="jona").first()   will only return 1 object