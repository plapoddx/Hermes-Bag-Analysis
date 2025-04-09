import psycopg2

def test_postgres_connection():
    
    try:
        conn = psycopg2.connect(
            dbname= 'db',
            user= 'user',
            password='pw',
            host= 'host',
            port= 'port'    
        )
        conn.close()
        print("✅ PostgreSQL connection successful!")
        return True
    
    except Exception as e:
        print("❌ PostgreSQL Connection failed:", e)
        return False