# Gym Database Management with Python and SQL
# Objective: The aim of this assignment is to reinforce your understanding of Python's interaction with SQL databases, 
# focusing on CRUD (Create, Read, Update, Delete) operations in the context of a gym's membership and workout session management system. 
# You will work with two tables: 'Members' and 'WorkoutSessions'.

# Problem Statement: You are tasked with developing a Python application to manage a gym's database. 
# The database consists of 'Members' and 'WorkoutSessions' tables. Your role is to implement various functions to add, 
# retrieve, update, and delete records in these tables, ensuring data integrity and efficient data handling.

# Task 1: Add a Member

# Write a Python function to add a new member to the 'Members' table in the gym's database.
#     # Example code structure
#     def add_member(id, name, age):
#         # SQL query to add a new member
#         # Error handling for duplicate IDs or other constraints
# Expected Outcome: A Python function that successfully adds a new member to the 'Members' table in the gym's database. 
# The function should handle errors gracefully, such as duplicate member IDs or violations of other constraints.

import mysql.connector
from mysql.connector import Error

def add_member(name, age): # removed id as assuming it is auto-incrementing to avoid repetition.
    try:
        conn = mysql.connector.connect(
            database = db_name,
            user = user,
            password = password,
            host = host
        )

        new_member = (name, age)

        cursor = conn.cursor()
        query = "INSERT INTO Members (name, age) VALUES (%s, %s)"
        cursor.execute(query, new_member)
        conn.commit()
        print("New member was successfully added.")

    except Error as e: 
        print(f"Error: {e}")

    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close()

# Task 2: Add a Workout Session

# Develop a Python function to add a new workout session to the 'WorkoutSessions' table for a specific member.
#     # Example code structure
#     def add_workout_session(member_id, date, duration_minutes, calories_burned):
#         # SQL query to add a new workout session
#         # Error handling for invalid member ID or other constraints
# Expected Outcome: A Python function that adds a new workout session to the 'WorkoutSessions' table in the gym's database for a specific member. 
# The function should handle errors gracefully, such as invalid member IDs or violations of other constraints.

def add_workout_session(member_id, date, duration_minutes, calories_burned):
    try:
        conn = mysql.connector.connect(
            database = db_name,
            user = user,
            password = password,
            host = host
        )

        new_workout_session = (member_id, date, duration_minutes, calories_burned)  # TODO do I need to convert the duration_minutes to 00:00:00? Or assumer VARCHAR?

        cursor = conn.cursor()
        query = "INSERT INTO Members (member_id, date, duration_minutes, calories_burned) VALUES (%s, %s, %s, %s))"
        cursor.execute(query, new_workout_session)
        conn.commit()
        print("New workout session was successfully added.")
        
    except Error as e: 
        print(f"Error: {e}")

    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close()

# Task 3: Updating Member Information

# Implement a function to update the age of a member. Ensure that your function checks if the member exists before attempting the update.
#     # Example code structure
#     def update_member_age(member_id, new_age):
#         # SQL query to update age
#         # Check if member exists
#         # Error handling
# Expected Outcome: A Python function that updates the age of a member and handles cases where the member does not exist.

def update_member_age(member_id, new_age):
    try:
        conn = mysql.connector.connect(
            database = db_name,
            user = user,
            password = password,
            host = host
        )

        update_member_age = (new_age, member_id)

        cursor = conn.cursor()
        query = """
        Update Members
        SET age = %s
        WHERE id = %s"""
        cursor.execute(query, update_member_age)
        conn.commit()
        print("Member's age was successfully updated.")

    except Error as e: 
        print(f"Error: {e}")

    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close()


# Task 4: Delete a Workout Session

# Create a Python function to delete a workout session based on its session ID. Include error handling for cases where the session ID does not exist.
#     # Example code structure
#     def delete_workout_session(session_id):
#         # SQL query to delete a session
#         # Error handling for non-existent session ID
# Expected Outcome: A Python function that can delete a workout session using its session ID, with proper error handling for invalid IDs.

def delete_workout_session(session_id):
    try:
        conn = mysql.connector.connect(
            database = db_name,
            user = user,
            password = password,
            host = host
        )

        cursor = conn.cursor()

        session_to_remove = (session_id, )
        
        query = "DELETE FROM WorkoutSessions WHERE session_id = %s"
        cursor.execute(query, session_to_remove)
        conn.commit()
        print("Workout session was successfully removed.")

    except Error as e: 
        print(f"Error: {e}")

    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close()


# Question 2: Advanced Data Analysis in Gym Management System
# Objective: The goal of this assignment is to advance your SQL querying skills within Python, 
# focusing on specific SQL functions and clauses like BETWEEN. You will be working with the same gym 
# database as in the previous assignment, comprising the Members and WorkoutSessions tables.

# Problem Statement: As a part of the gym's management team, you need to conduct an in-depth 
# analysis of the membership data. Your task is to develop Python functions that execute advanced SQL queries for 
# distinct department identification, employee count in each department, and age-based employee filtering.

# Task 1: SQL BETWEEN Usage

# Problem Statement: Retrieve the details of members whose ages fall between 25 and 30.
# Expected Outcome: A list of members (including their names, ages, etc) who are between the ages of 25 and 30.
# Example Code Structure:
#     def get_members_in_age_range(start_age, end_age):
#         # SQL query using BETWEEN
#         # Execute and fetch results
# Note: The database structure used for this assignment is the same as the previous one, consisting of the Members and WorkoutSessions tables.

def get_members_in_age_range(start_age, end_age):    
    try:
        conn = mysql.connector.connect(
            database = db_name,
            user = user,
            password = password,
            host = host
        )

        cursor = conn.cursor()

        age_range = (start_age, end_age)

        query = """
        SELECT * FROM Members
        WHERE age BETWEEN %s AND %s;"""
        cursor.execute(query, age_range)
        for row in cursor.fetchall():
            print(row)

    except Error as e: 
        print(f"Error: {e}")

    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close()