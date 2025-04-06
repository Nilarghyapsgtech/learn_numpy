from sqlalchemy import NullPool, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import oracledb
import urllib.parse
from pydantic import AnyUrl



DATABASE_URL='sqlite:///./todos2.db'




if "oracle+oracledb" in DATABASE_URL:
    url=AnyUrl(DATABASE_URL)
    params=dict(url.query_params())
    pool=oracledb.create_pool(
        user=url.username,
        password=urllib.parse.unquote(url.password),
        dsn=url.host,                                       # Extracts the Database Server Name (DSN) (could be an IP or domain).
        min=10,                                             # Minimum number of connections in the pool
        max=30,                                             # Maximum number of connections in the pool
        wallet_location=params.get("wallet_location",None),
        wallet_password=params.get("wallet_password",None),
        increments=5,
        cclass="Topology-Viewer",                            # Connection class name for Connection Pooling.
        server_type="pooled"
        
        )

    

engine=create_engine(DATABASE_URL,connect_args={'check_same_thread':False},poolclass=NullPool,creator=pool.acquire,pool_pre_ping=True)



SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine,expire_on_commit=False)

Base=declarative_base()
Base.metadata.create_all(bind=engine)

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()