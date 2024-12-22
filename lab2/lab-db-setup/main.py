import os
import psycopg2
from loguru import logger
from time import sleep


def main():
    host = os.getenv("DB_HOST")
    port = os.getenv("DB_PORT")
    user = os.getenv("POSTGRESQL_USERNAME")
    dbname = os.getenv("POSTGRESQL_DATABASE")
    password = os.getenv("POSTGRESQL_PASSWORD")

    logger.info(f"DB_HOST = {host}")
    logger.info(f"DB_PORT = {port}")
    logger.info(f"POSTGRESQL_USERNAME = {user}")
    logger.info(f"POSTGRESQL_DATABASE = {dbname}")
    logger.info(f"POSTGRESQL_PASSWORD = {password}")

    create_table_sql = """
    CREATE TABLE logs (
        id SERIAL PRIMARY KEY,
        writer_ip VARCHAR(32),
        message VARCHAR(255)
    );
    """

    is_executed = False
    while(not is_executed):
        try:
            logger.info("Connecting to PostgreSQL database...")
            connection = psycopg2.connect(
                host=host,
                port=port,
                user=user,
                password=password,
                dbname=dbname
            )
            cursor = connection.cursor()

            logger.info("Executing SQL to create 'logs' table...")
            cursor.execute(create_table_sql)

            connection.commit()
            logger.info("success")
            is_executed = True

        except Exception as e:
            logger.error(f"Error executing SQL: {e}")
            sleep(2)

        finally:
            if 'cursor' in locals():
                cursor.close()
            if 'connection' in locals():
                connection.close()


if __name__ == "__main__":
    main()
