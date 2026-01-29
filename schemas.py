from pydantic import BaseModel

class Todobase(BaseModel):
    title: str
    description: str | None = None
    completed: bool = False


class Todocreate(Todobase):
    pass

class Todo(Todobase):
    id: int
    class Config:
        orm_mode = True

# 1️⃣ Data comes from the browser as JSON
# 2️⃣ JSON enters the FastAPI endpoint
# 3️⃣ FastAPI sends that JSON to TodoCreate
# 4️⃣ TodoCreate checks:

# Is title present?

# Is it a string?

# Is completed a boolean?

# ✔ If valid → continue
# ❌ If not valid → FastAPI sends an error response


# Clean, correct explanation (same meaning)

# 1️⃣ Data comes from the database as a SQLAlchemy object
# 2️⃣ FastAPI sends that object to the Todo schema
# 3️⃣ orm_mode = True allows the schema to read the ORM object
# 4️⃣ The schema checks the shape of the data (id, title, description, completed)
# 5️⃣ FastAPI converts it into JSON
# 6️⃣ The JSON is sent back to the browser as the response