import psycopg2
import random
from datetime import datetime, timedelta
import time

# RisingWave connection parameters
conn_params = {
    "dbname": "dev",
    "user": "root",
    "password": "",
    "host": "localhost",
    "port": "4566"
}

conn = psycopg2.connect(**conn_params)
cursor = conn.cursor()

countries = ['Singapore', 'Malaysia', 'USA', 'Philippines', 'Indonesia']
transaction_types = ['purchase', 'refund', 'transfer']
merchants = ['Adidas', 'Starbucks', 'Apple Store', 'Nike', 'GrabFood', 'Shopee']
locations = ['Singapore', 'Kuala Lumpur', 'Jakarta', 'Bangkok', 'Manila']
device_types = ['mobile', 'desktop', 'tablet']

# ID counters
user_id_counter = 1000
transaction_id_counter = 50000
risk_id_counter = 100000

# Active users list
user_ids = []

def random_date(start, end):
    delta = end - start
    int_delta = int(delta.total_seconds())
    random_second = random.randint(0, int_delta)
    return start + timedelta(seconds=random_second)

try:
    while True:
        # 20% chance to create a new user
        if random.random() < 0.2:
            signup_date = random_date(datetime(2022, 1, 1), datetime.now())
            country = random.choice(countries)

            cursor.execute(
                """
                INSERT INTO users (user_id, full_name, signup_date, country)
                VALUES (%s, %s, %s, %s)
                """,
                (user_id_counter, f"user{user_id_counter}", signup_date, country)
            )
            user_ids.append(user_id_counter)
            print(f"Inserted user {user_id_counter}")
            user_id_counter += 1

        if not user_ids:
            time.sleep(1)
            continue

        # Insert transaction for random user
        user_id = random.choice(user_ids)
        transaction_id = transaction_id_counter
        transaction_id_counter += 1

        amount = round(random.uniform(5, 5000), 2)
        transaction_type = random.choice(transaction_types)
        merchant_name = random.choice(merchants)
        device_type = random.choice(device_types)
        location = random.choice(locations)
        timestamp = datetime.now()

        cursor.execute(
            """
            INSERT INTO transactions (transaction_id, user_id, amount, transaction_type, merchant_name, device_type, location, timestamp)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """,
            (transaction_id, user_id, amount, transaction_type, merchant_name, device_type, location, timestamp)
        )
        print(f"Inserted transaction {transaction_id} for user {user_id}")

        # Insert risk score for same user
        risk_id = risk_id_counter
        risk_id_counter += 1
        risk_score = round(random.uniform(0, 1), 4)

        cursor.execute(
            """
            INSERT INTO user_risks (risk_id, user_id, risk_score, timestamp)
            VALUES (%s, %s, %s, %s)
            """,
            (risk_id, user_id, risk_score, timestamp)
        )
        print(f"Inserted risk {risk_id} for user {user_id} with score {risk_score}")

        conn.commit()
        time.sleep(1)

except KeyboardInterrupt:
    print("Data generation stopped.")
finally:
    cursor.close()
    conn.close()
    print("Connection closed.")
