from app.core.db import SessionLocal
from app.models.user import User
from app.core.security import pwd_context
import uuid

db = SessionLocal()

user = User(
    id=uuid.uuid4(),
    name = "tester",
    email="test@example.com",
    hashed_password=pwd_context.hash("test123")
)

db.add(user)
db.commit()

print("User created:", user.email)

db.close()