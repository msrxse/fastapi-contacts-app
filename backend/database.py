import sqlalchemy as _sql
import sqlalchemy.ext.declarative as _declarative
import sqlalchemy.orm as _orm

''' NOTE: 
    [database-name] = fastapi_contacts_app_database
    [user] = myuser
    [password] = password
'''

# DATABASE_URL = "postgresql://[user]:[password]@localhost/[database-name]"
DATABASE_URL = "postgresql://myuser:password@localhost/fastapi_contacts_app_database"

engine = _sql.create_engine(DATABASE_URL)

# autocomit=False,
SessionLocal = _orm.sessionmaker(autoflush=False, bind=engine) 

Base = _declarative.declarative_base()
