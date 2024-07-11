import mysql.connector

def connect_db(user, password, host='localhost', port='3306', database='db'):
    try:
        connection = mysql.connector.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def execute_sql_file(connection, sql_file_path):
    cursor = connection.cursor()
    with open(sql_file_path, 'r') as sql_file:
        sql_commands = sql_file.read().split(';')
        for command in sql_commands:
            if command.strip():
                try:
                    cursor.execute(command)
                except mysql.connector.Error as err:
                    print(f"Error executing command: {command}")
                    print(f"MySQL Error: {err}")
    connection.commit()

def main():
    user = 'root'
    password = '12345'
    host = 'localhost'
    port = '3306'
    
    sql_file_path = 'backend/sql_file.sql'
    
    connection = connect_db(user, password, host, port)
    if not connection:
        print("Error connecting to MySQL")
        exit(1)

    execute_sql_file(connection, sql_file_path)
    
    print("SQL commands executed successfully")
    connection.close()

if __name__ == '__main__':
    main()