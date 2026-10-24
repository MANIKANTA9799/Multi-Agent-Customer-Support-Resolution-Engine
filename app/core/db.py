from app.core.config import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
engine = create_engine(
    settings.database_url,
     pool_pre_ping=True
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False,bind = engine )
"""Concept: Connection Pooling and Session Management.
Why it exists: Opening a new connection to PostgreSQL is
 computationally expensive. If 1,000 users hit your API,
   and you open 1,000 independent connections, PostgreSQL
     will run out of memory and crash. We use a Connection 
     Pool (managed by SQLAlchemy) 
to keep a small number of connections alive and recycle them."""
