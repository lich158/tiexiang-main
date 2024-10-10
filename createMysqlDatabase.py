import mysql.connector

def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

def main():
    # 连接配置
    connection = mysql.connector.connect(
        host="192.168.1.211",       # 更改为你的MySQL服务器地址
        port="32560",
        user="root",   # 更改为你的MySQL用户名
        password="supersecret"  # 更改为你的MySQL密码
    )

    if connection.is_connected():
        db_name = "tx_auth"  # 你想要创建的数据库名称
        create_query = f"CREATE DATABASE {db_name}"
        create_database(connection, create_query)
        db_name = "tx_manager"  # 你想要创建的数据库名称
        create_query = f"CREATE DATABASE {db_name}"
        create_database(connection, create_query)
        connection.close()

if __name__ == "__main__":
    main()