from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from config.config import DB_URL

# Create the database engine
engine = create_engine(DB_URL, echo=True)  # Set `echo=True` for SQL query logging (optional)

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a scoped session for thread-safe operations
Session = scoped_session(SessionLocal)

# Dependency for FastAPI (or other frameworks) to use in routes
def get_db():
    """
    Dependency function to get a database session.
    Yields a session, and ensures it is closed after use.
    """
    db = Session()
    try:
        yield db
    finally:
        db.close()
