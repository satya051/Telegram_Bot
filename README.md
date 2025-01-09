
# Task Assignment Telegram Bot

A scalable and efficient Telegram bot designed for managing tasks within groups, coupled with a REST API for seamless integration with other systems. The bot provides task creation, assignment, and status tracking features.

---

## Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [Installation](#installation)
4. [Environment Setup](#environment-setup)
5. [Project Structure](#project-structure)
6. [API Details](#api-details)
7. [Deployment](#deployment)
8. [Testing](#testing)
9. [Contributing](#contributing)
10. [License](#license)

---

## Overview

This Telegram bot helps teams organize and assign tasks within a group, while also providing a comprehensive REST API to manage tasks programmatically. It supports multiple commands for both administrators and users, and uses JWT authentication for secure API access.

---

## Features

- **Admin Commands:**
  - `/add_task @username task description`: Assign a task to a user.
  - `/view_all_tasks`: View all tasks and their current status.

- **User Commands:**
  - `/my_tasks`: View all assigned tasks for the logged-in user.
  - `/change_status task_id status`: Update the status of a task.

- **REST API:**
  - Fetch tasks by user or by status.
  - Secure access with JWT tokens.

---

## Installation

To get started with the bot, follow the installation steps below.

### Prerequisites

- Python 3.11 or higher
- PostgreSQL (for database storage)
- Docker (for containerized deployment)

### Setting up the Bot

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/telegram-task-bot.git
   cd telegram-task-bot
   ```

2. Create a Python virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Environment Setup

Before running the bot, you need to configure the environment variables.

1. Copy the example environment file:
   ```bash
   cp .env.example .env
   ```

2. Update the `.env` file with your credentials:
   ```
   DATABASE_URL=postgresql://user:password@localhost:5432/task_bot
   TELEGRAM_BOT_TOKEN=your_bot_token
   JWT_SECRET_KEY=your_jwt_secret_key
   ```

---

## Project Structure

Here’s an overview of how the project is organized:

```
telegram-task-bot/
├── app/                 # Core application logic
│   ├── api/             # API routes and handlers
│   ├── auth/            # Authentication and security
│   ├── bot/             # Telegram bot command handlers
│   ├── db/              # Database models and migrations
│   └── services/        # Business logic
├── tests/               # Unit and integration tests
├── Dockerfile           # Container setup
└── requirements.txt     # Python dependencies
```

---

## API Details

### Authentication

All API endpoints require JWT authentication. Include the token in the `Authorization` header:
```
Authorization: Bearer <JWT_TOKEN>
```

### Endpoints

- **Get Tasks by User:**
  - URL: `/api/tasks/{user_id}`
  - Method: `GET`
  - Response:
    ```json
    {
      "tasks": [
        {
          "id": 1,
          "description": "Complete report",
          "status": "in_progress"
        }
      ]
    }
    ```

- **Get Tasks by Status:**
  - URL: `/api/tasks/status/{status}`
  - Method: `GET`
  - Response:
    ```json
    {
      "tasks": [
        {
          "id": 1,
          "description": "Complete documentation",
          "assigned_to": 123456
        }
      ]
    }
    ```

---

## Deployment

### Docker Deployment

Build the Docker image and run the bot in a containerized environment.

1. Build the Docker image:
   ```bash
   docker build -t task-bot .
   ```

2. Run the Docker container:
   ```bash
   docker run -p 8080:8080 --env-file .env task-bot
   ```

### Cloud Deployment

You can deploy this bot on platforms such as:
- **Google Cloud Run**
- **AWS ECS**
- **Azure App Service**

Follow the respective platform's documentation to deploy the Docker container.

---

## Testing

To ensure everything works as expected, run the unit and integration tests.

1. Install pytest:
   ```bash
   pip install pytest
   ```

2. Run the tests:
   ```bash
   pytest tests/
   ```

---

## Contributing

We welcome contributions to improve the bot! Here's how you can help:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes with meaningful messages.
4. Push your branch to your fork.
5. Open a Pull Request with a description of your changes.

---

## License

This project is licensed under the MIT License.

---

### Key Changes and Additions
- **Environment Setup**: Streamlined the environment setup steps.
- **Project Structure**: Described the folder structure in a simplified manner.
- **Clearer Commands**: Renamed some bot commands for clarity.
- **Deployment Instructions**: Reorganized to include both Docker and cloud-based deployment options.
