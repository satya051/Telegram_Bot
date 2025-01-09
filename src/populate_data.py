from db.session import Session
from db.models import User, Task, TaskStatus
from datetime import datetime

def poppulate_data():
    """
    Populate the database with initial data for testing.
    """
    db = Session()

    try:
        # Step 1: Create Admin User
        admin = User(username="admin_user", is_admin=True)
        db.add(admin)

        # Step 2: Create Regular Users
        user1 = User(username="user_one", is_admin=False)
        user2 = User(username="user_two", is_admin=False)
        db.add_all([user1, user2])

        # Commit Users
        db.commit()

        # Step 3: Create Tasks
        task1 = Task(
            task_description="Review the project requirements",
            assigned_user_id=user1.user_id,
            status=TaskStatus.PENDING,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
        )

        task2 = Task(
            task_description="Complete the initial design draft",
            assigned_user_id=user2.user_id,
            status=TaskStatus.IN_PROGRESS,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
        )

        task3 = Task(
            task_description="Prepare final project report",
            assigned_user_id=user1.user_id,
            status=TaskStatus.PENDING,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
        )

        # Add Tasks
        db.add_all([task1, task2, task3])

        # Commit Tasks
        db.commit()

        print("Data populated successfully.")

    except Exception as e:
        print(f"Error populating data: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    populate_data()
