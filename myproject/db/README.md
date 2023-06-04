open virtual python session

python

run commands too see meta data

>>> User
>>> User.__tablename__
>>>User.__table__
>>> Base.metadata.create_all(engine)
2023-06-04 11:48:40,050 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2023-06-04 11:48:40,052 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("users")
2023-06-04 11:48:40,052 INFO sqlalchemy.engine.Engine [raw sql] ()
2023-06-04 11:48:40,058 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("users")
2023-06-04 11:48:40,058 INFO sqlalchemy.engine.Engine [raw sql] ()
2023-06-04 11:48:40,059 INFO sqlalchemy.engine.Engine 
CREATE TABLE users (
	id INTEGER NOT NULL, 
	username VARCHAR(25) NOT NULL, 
	email VARCHAR(80) NOT NULL, 
	date_created DATETIME, 
	PRIMARY KEY (id), 
	UNIQUE (username), 
	UNIQUE (email)
)



Will need to have access to 
DB Browser for SQLite



if everything works our db can be called and it will return the following data

(base) Nathans-Air:db nathanpillay$ python create_db.py 
<User username=JOnathan email=jona@jona.com>
2023-06-04 11:52:44,405 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2023-06-04 11:52:44,406 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("users")
2023-06-04 11:52:44,406 INFO sqlalchemy.engine.Engine [raw sql] ()
2023-06-04 11:52:44,407 INFO sqlalchemy.engine.Engine COMMIT


#sessionmaker
we use this to query our db and provide it with more info   

#bind
we have to create a bind
bind it to DB we have transactions on


(base) Nathans-Air:db nathanpillay$ python create_users.py 
<User username=JOnathan email=jona@jona.com>
2023-06-04 12:04:28,360 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2023-06-04 12:04:28,363 INFO sqlalchemy.engine.Engine INSERT INTO users (username, email, date_created) VALUES (?, ?, ?)
2023-06-04 12:04:28,364 INFO sqlalchemy.engine.Engine [generated in 0.00174s] ('jona', 'jona@company.com', '2023-06-04 10:04:28.362354')
2023-06-04 12:04:28,369 INFO sqlalchemy.engine.Engine COMMIT


#now we added users to the db

(base) Nathans-Air:db nathanpillay$ python create_users.py 
<User username=JOnathan email=jona@jona.com>
<User username=jerry email=jerry@company.com>
2023-06-04 12:13:55,026 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2023-06-04 12:13:55,028 INFO sqlalchemy.engine.Engine INSERT INTO users (username, email, date_created) VALUES (?, ?, ?)
2023-06-04 12:13:55,028 INFO sqlalchemy.engine.Engine [generated in 0.00023s] ('jerry', 'jerry@company.com', '2023-06-04 10:13:55.028124')
2023-06-04 12:13:55,031 INFO sqlalchemy.engine.Engine COMMIT
Added jerry
