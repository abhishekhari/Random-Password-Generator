# Password Manager with User Profiles

A Python-based GUI Password Manager with user authentication, profile management, and password recovery features. Each user's data is stored securely and isolated from other users.

## Features

- **User Registration**: Create new user profiles with a username, password, and security question.
- **User Login**: Authenticate users before granting access to their password manager.
- **Password Recovery**: Recover forgotten passwords using a security question.
- **Isolated User Data**: Each user's passwords are stored in a separate file, ensuring privacy.
- **Password Generation**: Generate strong random passwords.
- **Password Management**: Save and view passwords associated with different accounts.

## Requirements

- Python 3.x
- Tkinter (usually included with Python)
- JSON (for storing user data)

## Installation

1. **Clone the repository or download the script:**

    ```bash
    git clone https://github.com/your-username/password-manager.git
    ```

    Alternatively, you can download the `password_manager.py` file directly.

2. **Navigate to the project directory:**

    ```bash
    cd password-manager
    ```

3. **Run the Application:**

    Run the `password_manager.py` script using Python:

    ```bash
    python password_manager.py
    ```

    This will open the login window of the password manager.

## Usage

### 1. **Login or Register**

   - **Login**: Enter your username and password to log in.
   - **Register**: If you don’t have an account, click the "Register" button to create a new account.

### 2. **User Registration**

   - Choose a unique username.
   - Set a strong password.
   - Provide a security question and answer for password recovery.
   - Your data will be stored securely and you will be redirected to the login page.

### 3. **Password Recovery**

   - If you forget your password, click "Forgot Password?" on the login screen.
   - Enter your username and answer the security question correctly to reset your password.

### 4. **Password Management**

   - After logging in, you can generate new passwords, save them, and view saved passwords.
   - All passwords are stored in a separate file associated with your username (e.g., `admin_data.json`).

### 5. **Isolated Data Storage**

   - Each user’s data is stored separately in a JSON file named after their username. No data is shared between users.

## Example

1. **Registering a New User:**
   - Username: `user1`
   - Password: `password123`
   - Security Question: `What is your pet's name?`
   - Security Answer: `Fluffy`

2. **Generating and Saving a Password:**
   - Account Name: `Email`
   - Generated Password: `Xy9!#aB2s@`

3. **Data Storage:**
   - User data stored in `users.json`.
   - Passwords stored in `user1_data.json`.

## File Structure

- `password_manager.py` - The main Python script for the application.
- `users.json` - JSON file storing user profiles, passwords, and security questions (auto-generated).
- `*_data.json` - JSON files storing individual users' passwords (auto-generated based on username).

## Notes

- **Security**: Passwords are hashed using SHA-256 before being stored.
- **Data Privacy**: Each user’s passwords are isolated in their own file.
- **Persistent Storage**: User data and passwords are stored in JSON files, ensuring data persists across sessions.
- **User Management**: Users can register, log in, and reset their passwords securely.

## Contributing

If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.
