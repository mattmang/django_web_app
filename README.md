Assignment: Django Web Application for User Authentication and CRUD Operations with MySQL

Objective:  
In this assignment, you are required to build a Django web application that allows users to log in, log out, and perform CRUD (Create, Read, Update, Delete) operations on a task model. The application will use **MySQL** as the database backend to store user and task information.

---

Instructions:

1. Set up Django with MySQL:
   - Install and configure MySQL on your machine or use a remote MySQL database.
   - Install the required Python packages, including `mysqlclient` or `PyMySQL`.
   - Create a new database in MySQL to store your application data (e.g., `django_crud`).

2. **Django Project Setup**:
   - Create a new Django project named `user_auth_crud`.
   - Create a new app within the project called `tasks`.

3. **User Authentication**:
   - Set up Django's built-in authentication system to allow users to log in and log out.
   - Create a simple login page where users can log in and a logged-out page that confirms successful logout.
   - Use Django's built-in templates for login and logout (you can find these in `django.contrib.auth`).

4. Model Creation (Task Model):
   - Create a model called `Task` with the following fields:
     - `title`: CharField, maximum length 100.
     - `description`: TextField.
     - `created_at`: DateTimeField, auto-set to the time of creation.
     - `user`: ForeignKey to the built-in `User` model, which links each task to a specific user.
   
   - After creating the model, run migrations to create the appropriate tables in MySQL.

5. CRUD Views:
   Implement the following CRUD operations for the `Task` model:

   - **Create**: Create a view where the logged-in user can add a new task.
   - **Read**: Create a view to display a list of tasks for the logged-in user.
   - **Update**: Create a view to update an existing task.
   - **Delete**: Create a view to delete a task.

6. Forms:
   - Create a form for the `Task` model to handle task creation and updating.
   - Ensure that the form includes the fields `title` and `description`.

7. URLs:
   - Define URL patterns for the above CRUD operations in your app’s `urls.py`.
   - Ensure each view has its corresponding URL.

8. Templates:
   - Create HTML teplates for the following pages:
     - Task list page (shows all tasks for the logged-in user).
     - Task creation form.
     - Task update form.
     - Task delete confirmation page.
   - Ensure the templates are clear, user-friendly, and include navigation to allow easy access to all functionality.

9. Database Setup in `settings.py`:
   - In `settings.py`, configure the database to use MySQL instead of SQLite.
   - Ensure that the database connection uses the correct credentials and points to the database you created earlier.

10. Testing:
   - Test your application thoroughly to ensure the following:
     - Users can log in and log out.
     - The task list only shows tasks created by the logged-in user.
     - Users can create, update, and delete their own tasks.
     - Tasks are properly saved in the MySQL database.

---

Evaluation Criteria:
Database Configuration: Correctly set up MySQL as the database backend in Django.
Authentication: Properly implemented user login and logout using Django’s built-in authentication system.
CRUD Operations: Functional task creation, reading, updating, and deletion views.
Model Design: Correct task model design with appropriate relationships.
Form Handling: Correct usage of Django forms to handle task data.
URLs and Routing: Proper URL routing for CRUD operations.
Templates: Clean, organized, and functional templates for task management.
Code Organization: Proper organization of code (views, models, forms, etc.).
Testing: Thorough testing of each feature to ensure functionality.
