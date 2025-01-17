import pandas as pd
import random
from faker import Faker

# Initialize Faker
faker = Faker()

# Generate synthetic data
def generate_dataset(file_path, num_records=1000):
    print("Generating synthetic dataset...")
    data = {
        "customer_id": [i for i in range(1, num_records + 1)],
        "age": [random.randint(18, 65) for _ in range(num_records)],
        "gender": [random.choice(["Male", "Female"]) for _ in range(num_records)],
        "location": [faker.city() for _ in range(num_records)],
        "product_category": [random.choice(["Electronics", "Clothing", "Beauty", "Books", "Home", "Sports"]) for _ in range(num_records)],
        "price": [random.randint(10, 500) for _ in range(num_records)],
        "quantity": [random.randint(1, 5) for _ in range(num_records)],
        "transaction_amount": lambda x: x["price"] * x["quantity"],
        "purchase_date": [faker.date_time_this_year() for _ in range(num_records)],
    }

    # Convert to DataFrame
    df = pd.DataFrame(data)

    # Calculate transaction amount
    df["transaction_amount"] = df["price"] * df["quantity"]

    # Save to CSV
    df.to_csv(file_path, index=False)
    print(f"Synthetic dataset saved as {file_path}.")

# Main function
if __name__ == "__main__":
    file_path = "shopping_data.csv"
    generate_dataset(file_path)
