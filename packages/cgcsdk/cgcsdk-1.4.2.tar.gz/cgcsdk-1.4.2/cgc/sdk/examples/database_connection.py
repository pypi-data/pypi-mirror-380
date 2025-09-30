#!/usr/bin/env python3
"""
PostgreSQL Database Connection Example

This script demonstrates how to:
1. Deploy a PostgreSQL database
2. Connect to the database using native psycopg2
3. Create tables and insert data
4. Query and update data
5. Handle database errors

Usage:
    python database_connection.py

Requirements:
    pip install psycopg2-binary
"""

import time
import psycopg2
from psycopg2 import errors as pg_errors
import cgc.sdk.resource as resource
import cgc.sdk.exceptions as exceptions


def deploy_postgres(db_name="example-postgres", password="example-pass-123"):
    """Deploy a PostgreSQL database resource"""

    print(f"Deploying PostgreSQL database '{db_name}'...")

    try:
        response = resource.resource_create(
            name=db_name,
            image_name="postgres:17",
            entity="postgresql",
            cpu=2,
            memory=4,
            environment_data=[
                f"POSTGRES_PASSWORD={password}",
                "POSTGRES_USER=admin",
                "POSTGRES_DB=db"
            ]
        )

        if response['code'] == 200:
            print(f"✓ PostgreSQL '{db_name}' created successfully")

            # Wait for database to be ready
            print("Waiting for database to be ready...")
            max_wait = 60
            waited = 0

            while waited < max_wait:
                if resource.resource_ready(db_name, resource.ResourceTypes.db):
                    print("✓ Database is ready!")
                    return db_name, password

                time.sleep(5)
                waited += 5
                print(f"  Still starting... ({waited}s elapsed)")

            print(f"✗ Database failed to become ready within {max_wait} seconds")
            return None, None
        else:
            print(f"✗ Failed to create database: {response.get('message', 'Unknown error')}")
            return None, None

    except exceptions.SDKException as e:
        print(f"✗ SDK Error (code {e.code}): {e}")
        return None, None


def get_database_connection_info(db_name):
    """Get database connection information from Kubernetes service"""

    # In Kubernetes, the service will be available at the service name
    # The port is typically 5432 for PostgreSQL
    return {
        'host': db_name,  # Service name in Kubernetes
        'port': 5432,
        'user': 'admin',
        'database': 'db'
    }


def connect_to_database(db_name, password, database="db"):
    """Connect to PostgreSQL database using native psycopg2"""

    print(f"Connecting to database '{db_name}'...")

    try:
        # Wait a bit more for service to be available
        print("Waiting for database service to be available...")
        time.sleep(15)

        # Get connection info
        conn_info = get_database_connection_info(db_name)

        # Connection parameters
        connection_params = {
            'host': conn_info['host'],
            'port': conn_info['port'],
            'user': conn_info['user'],
            'password': password,
            'database': database,
            'connect_timeout': 10
        }

        # Test connection with retries
        max_retries = 5
        connection = None

        for attempt in range(max_retries):
            try:
                print(f"Connection attempt {attempt + 1}/{max_retries}...")
                print(f"  Connecting to {conn_info['host']}:{conn_info['port']} as {conn_info['user']}")

                connection = psycopg2.connect(**connection_params)
                cursor = connection.cursor()

                # Test the connection
                cursor.execute("SELECT version()")
                version = cursor.fetchone()[0]
                print(f"✓ Connected to PostgreSQL")
                print(f"  Version: {version[:50]}...")

                cursor.close()
                return connection

            except Exception as e:
                print(f"  Attempt {attempt + 1} failed: {e}")
                if connection:
                    connection.close()
                if attempt < max_retries - 1:
                    print("  Retrying in 10 seconds...")
                    time.sleep(10)
                else:
                    raise

    except Exception as e:
        print(f"✗ Failed to connect: {e}")
        return None


def create_tables(connection):
    """Create example tables"""

    print("\nCreating tables...")

    cursor = connection.cursor()

    try:
        # Create users table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                username VARCHAR(50) UNIQUE NOT NULL,
                email VARCHAR(100) UNIQUE NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        # Create posts table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS posts (
                id SERIAL PRIMARY KEY,
                user_id INTEGER REFERENCES users(id),
                title VARCHAR(200) NOT NULL,
                content TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        connection.commit()
        print("✓ Tables created successfully")

        # List tables
        cursor.execute("""
            SELECT table_name
            FROM information_schema.tables
            WHERE table_schema = 'public'
        """)

        tables = cursor.fetchall()
        print("  Available tables:")
        for table in tables:
            print(f"    - {table[0]}")

        return True

    except Exception as e:
        connection.rollback()
        print(f"✗ Error creating tables: {e}")
        return False

    finally:
        cursor.close()


def insert_sample_data(connection):
    """Insert sample data into tables"""

    print("\nInserting sample data...")

    cursor = connection.cursor()

    try:
        # Insert users
        users = [
            ("alice", "alice@example.com"),
            ("bob", "bob@example.com"),
            ("charlie", "charlie@example.com")
        ]

        user_ids = []
        for username, email in users:
            cursor.execute(
                "INSERT INTO users (username, email) VALUES (%s, %s) RETURNING id",
                (username, email)
            )
            user_id = cursor.fetchone()[0]
            user_ids.append(user_id)
            print(f"  ✓ Created user: {username} (ID: {user_id})")

        # Insert posts
        posts = [
            (user_ids[0], "Hello World", "This is my first post!"),
            (user_ids[0], "CGC SDK Tutorial", "Learning how to use the SDK..."),
            (user_ids[1], "Database Example", "PostgreSQL is awesome!"),
            (user_ids[2], "Cloud Computing", "Deploying apps in the cloud")
        ]

        for user_id, title, content in posts:
            cursor.execute(
                "INSERT INTO posts (user_id, title, content) VALUES (%s, %s, %s)",
                (user_id, title, content)
            )

        connection.commit()
        print(f"✓ Inserted {len(users)} users and {len(posts)} posts")
        return True

    except pg_errors.UniqueViolation:
        connection.rollback()
        print("  Note: Some data already exists (duplicate entries)")
        return True

    except Exception as e:
        connection.rollback()
        print(f"✗ Error inserting data: {e}")
        return False

    finally:
        cursor.close()


def query_data(connection):
    """Query and display data"""

    print("\nQuerying data...")

    cursor = connection.cursor()

    try:
        # Query 1: Count users
        cursor.execute("SELECT COUNT(*) FROM users")
        user_count = cursor.fetchone()[0]
        print(f"  Total users: {user_count}")

        # Query 2: List users with post count
        cursor.execute("""
            SELECT
                u.username,
                u.email,
                COUNT(p.id) as post_count
            FROM users u
            LEFT JOIN posts p ON u.id = p.user_id
            GROUP BY u.id, u.username, u.email
            ORDER BY post_count DESC
        """)

        print("\n  User Statistics:")
        print("  " + "-" * 50)
        print(f"  {'Username':<15} {'Email':<25} {'Posts':<5}")
        print("  " + "-" * 50)

        for row in cursor.fetchall():
            username, email, post_count = row
            print(f"  {username:<15} {email:<25} {post_count:<5}")

        # Query 3: Recent posts
        cursor.execute("""
            SELECT
                p.title,
                u.username,
                p.created_at
            FROM posts p
            JOIN users u ON p.user_id = u.id
            ORDER BY p.created_at DESC
            LIMIT 5
        """)

        print("\n  Recent Posts:")
        print("  " + "-" * 50)

        for row in cursor.fetchall():
            title, author, created = row
            print(f"  📝 {title}")
            print(f"     by {author} at {created}")

        return True

    except Exception as e:
        print(f"✗ Error querying data: {e}")
        return False

    finally:
        cursor.close()


def demonstrate_transactions(connection):
    """Demonstrate transaction handling"""

    print("\nDemonstrating transactions...")

    cursor = connection.cursor()

    try:
        # Start transaction (psycopg2 starts transactions automatically)
        print("  Starting transaction...")

        # Operation 1: Create a new user
        cursor.execute(
            "INSERT INTO users (username, email) VALUES (%s, %s) RETURNING id",
            ("transaction_test", "trans@example.com")
        )
        new_user_id = cursor.fetchone()[0]
        print(f"  ✓ Created user (ID: {new_user_id})")

        # Operation 2: Create multiple posts
        for i in range(3):
            cursor.execute(
                "INSERT INTO posts (user_id, title, content) VALUES (%s, %s, %s)",
                (new_user_id, f"Transaction Post {i+1}", "Testing transactions")
            )
        print("  ✓ Created 3 posts")

        # Commit transaction
        connection.commit()
        print("  ✓ Transaction committed successfully")

        # Demonstrate rollback (intentional error)
        print("\n  Testing rollback scenario...")

        try:
            # This will fail due to duplicate username
            cursor.execute(
                "INSERT INTO users (username, email) VALUES (%s, %s)",
                ("transaction_test", "another@example.com")
            )
            connection.commit()
        except pg_errors.UniqueViolation:
            connection.rollback()
            print("  ✓ Transaction rolled back (duplicate username)")

        return True

    except Exception as e:
        connection.rollback()
        print(f"  ✗ Transaction failed: {e}")
        return False

    finally:
        cursor.close()


def cleanup_database(db_name):
    """Delete the database resource"""

    print(f"\nCleaning up database '{db_name}'...")

    try:
        response = resource.resource_delete(db_name)

        if response['code'] == 200:
            print(f"✓ Database '{db_name}' deleted successfully")
            return True
        else:
            print(f"✗ Failed to delete database: {response.get('message', 'Unknown error')}")
            return False

    except Exception as e:
        print(f"✗ Error during cleanup: {e}")
        return False


def main():
    """Main execution flow"""

    print("=" * 60)
    print("CGC SDK - PostgreSQL Database Example (Native psycopg2)")
    print("=" * 60)

    # Step 1: Deploy PostgreSQL
    db_name, password = deploy_postgres()

    if not db_name:
        print("\nFailed to deploy database. Exiting.")
        return

    # Wait a bit more for database to fully initialize
    print("\nWaiting for database to fully initialize...")
    time.sleep(10)

    # Network access confirmation
    print("\n" + "=" * 60)
    print("NETWORK ACCESS CONFIRMATION")
    print("=" * 60)
    print("Database access is only available within the Kubernetes namespace network.")
    print("Access is NOT exposed via ingress - you must be within the cluster network.")
    print()
    confirmation = input("Are you currently within the namespace network? (y/N): ").lower().strip()

    if confirmation != 'y':
        print("✗ Network access not confirmed. Processing cleanup...")
        cleanup_database(db_name)
        return

    print("✓ Network access confirmed. Proceeding with database operations...")

    # Step 2: Connect to database
    connection = connect_to_database(db_name, password)

    if not connection:
        print("\nFailed to connect to database. Cleaning up...")
        cleanup_database(db_name)
        return

    try:
        # Step 3: Create tables
        if not create_tables(connection):
            print("\nFailed to create tables. Cleaning up...")
            cleanup_database(db_name)
            return

        # Step 4: Insert sample data
        insert_sample_data(connection)

        # Step 5: Query data
        query_data(connection)

        # Step 6: Demonstrate transactions
        demonstrate_transactions(connection)

        # Step 7: Final statistics
        cursor = connection.cursor()

        cursor.execute("SELECT COUNT(*) FROM users")
        final_users = cursor.fetchone()[0]

        cursor.execute("SELECT COUNT(*) FROM posts")
        final_posts = cursor.fetchone()[0]

        cursor.close()

        print("\n" + "=" * 60)
        print("Final Database Statistics:")
        print(f"  Total Users: {final_users}")
        print(f"  Total Posts: {final_posts}")
        print("=" * 60)

    finally:
        # Always close the connection
        connection.close()
        print("✓ Database connection closed")

    # Cleanup option
    user_input = input(f"\nDo you want to delete the database '{db_name}'? (y/n): ").lower()

    if user_input == 'y':
        cleanup_database(db_name)
    else:
        print(f"✓ Keeping database '{db_name}' running")
        print(f"  Connection details:")
        print(f"    Host: {db_name}")
        print(f"    User: admin")
        print(f"    Password: {password}")
        print(f"    Database: db")
        print("  Remember to delete it when you're done!")

    print("\n" + "=" * 60)
    print("Example completed!")
    print("=" * 60)


if __name__ == "__main__":
    main()