import mysql.connector
from tkinter import messagebox

def Save_Data_MySql(B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R):
    try:
        # Establish connection to MySQL
        mydb = mysql.connector.connect(host='localhost', user='root', password='Patro202172112')
        mycursor = mydb.cursor()
        print("Connection established!")
    except mysql.connector.Error as err:
        messagebox.showerror("Connection", f"Database connection not established! Error: {err}")
        return

    try:
        # Create the database if it doesn't exist
        mycursor.execute("CREATE DATABASE IF NOT EXISTS Heart_Data")
        mycursor.execute("USE Heart_Data")

        # Create the table if it doesn't exist
        command = """
        CREATE TABLE IF NOT EXISTS data (
            user INT AUTO_INCREMENT PRIMARY KEY,
            Name VARCHAR(50),
            Date VARCHAR(50),
            DOB VARCHAR(100),
            age VARCHAR(100),
            sex VARCHAR(100),
            Cp VARCHAR(100),
            trestbps VARCHAR(100),
            chol VARCHAR(100),
            fbs VARCHAR(100),
            restecg VARCHAR(100),
            thalach VARCHAR(100),
            exang VARCHAR(100),
            oldpeak VARCHAR(100),
            slope VARCHAR(100),
            ca VARCHAR(100),
            thal VARCHAR(100),
            smoker VARCHAR(100)
        )
        """
        mycursor.execute(command)

        # Insert data into the table
        insert_command = """
        INSERT INTO data (Name, Date, DOB, age, sex, Cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal, smoker)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R)
        mycursor.execute(insert_command, values)

        # Commit the transaction
        mydb.commit()
        messagebox.showinfo("Register", "New User added successfully!")

    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"An error occurred: {err}")

    finally:
        # Close the connection
        mydb.close()


def Update_Data_MySql(user, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R):
    """Update an existing record in the MySQL database."""
    try:
        # Establish connection to MySQL
        mydb = mysql.connector.connect(host='localhost', user='root', password='Patro202172112')
        mycursor = mydb.cursor()
        print("Connection established!")
    except mysql.connector.Error as err:
        messagebox.showerror("Connection", f"Database connection not established! Error: {err}")
        return

    try:
        # Use the correct database
        mycursor.execute("USE Heart_Data")

        # Update the record in the table
        update_command = """
        UPDATE data
        SET Name=%s, Date=%s, DOB=%s, age=%s, sex=%s, Cp=%s, trestbps=%s, chol=%s, fbs=%s, restecg=%s, 
            thalach=%s, exang=%s, oldpeak=%s, slope=%s, ca=%s, thal=%s, smoker=%s
        WHERE user=%s
        """
        # Add user to the values tuple
        values = (B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, user)
        mycursor.execute(update_command, values)

        # Commit the transaction
        mydb.commit()
        messagebox.showinfo("Update", "User data updated successfully!")

    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"An error occurred: {err}")

    finally:
        # Close the connection
        mydb.close()
