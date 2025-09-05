# Backend

## Migrations

1. **Activate your Python virtual environment** (if not already active):

   ```console
   # Windows
   .venv\Scripts\activate
   # Unix/macOS
   source .venv/bin/activate
   ```

2. **Navigate to the backend directory containing `alembic.ini`:**

   ```console
   cd backend
   ```

3. **Create a new migration revision:**

   ```console
   alembic revision --autogenerate -m "Refactor same models"
   ```

   *Commit the generated files in the alembic directory to your git repository.*

4. **Apply the migration to your database:**

   ```console
   alembic upgrade head
   ```

