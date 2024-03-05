# AirBnB Clone Project - README

![Website logo](Assets/HBNB IMAGE.png)

## Project Description:
This project aims to develop an AirBnB clone, a web-based platform that connects travelers with hosts who have accommodations available for rent. The clone will replicate key features of the original AirBnB platform, including user authentication, property listings, booking management, and reviews.

## Command Interpreter Description:
The command interpreter is a command-line interface (CLI) tool developed for managing and interacting with the AirBnB clone project. It allows users to perform various actions, such as creating, updating, and deleting objects like users, places, amenities, and bookings. The command interpreter also provides functionality for searching and filtering listings, managing bookings, and accessing user profiles.

## How to Start the Command Interpreter:
1. Clone the repository from GitHub:
```
git clone https://github.com/your_username/AirBnB_clone.git
```
2. Navigate to the project directory:
```
cd AirBnB_clone
```
3. Run the command interpreter:
```
./console.py
```
## How to Use the Command Interpreter:
Once the command interpreter is launched, you can start interacting with it by typing commands at the prompt. Here are some basic commands and examples of their usage:
- Help Command:
```
(hbnb) help
```
Displays a list of available commands and their descriptions.
- Create Command:
```
(hbnb) create User
```
Creates a new user object.
- Show Command:
```
(hbnb) show User 1234-5678-9012
```
Displays detailed information about the specified user object.
- Update Command:
```
(hbnb) update User 1234-5678-9012 name "John Doe"
```
Updates the name attribute of the specified user object.
- Delete Command:
```
(hbnb) destroy User 1234-5678-9012
```