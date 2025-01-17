import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans

# Load the dataset
def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        print("Data loaded successfully.")
        return data
    except FileNotFoundError:
        print("Error: File not found. Ensure the dataset is in the correct path.")
        exit()

# Preprocess the dataset
def preprocess_data(data):
    # Handle missing values
    data.fillna(method='ffill', inplace=True)

    # Convert purchase_date to datetime
    data['purchase_date'] = pd.to_datetime(data['purchase_date'])

    # Extract hour from purchase_date
    data['hour'] = data['purchase_date'].dt.hour

    # Encode gender
    data['gender'] = data['gender'].map({'Male': 0, 'Female': 1})

    print("Data preprocessing complete.")
    return data

# Analyze shopping trends
def analyze_trends(data):
    print("Analyzing trends...")

    # Popular products
    popular_products = data['product_category'].value_counts()

    # Peak shopping hours
    peak_hours = data['hour'].value_counts()

    # Demographic analysis
    age_spending = data.groupby('age')['transaction_amount'].sum()

    return popular_products, peak_hours, age_spending

# Visualize insights
def visualize_insights(popular_products, peak_hours, age_spending):
    print("Visualizing insights...")

    # Popular products
    plt.figure(figsize=(10, 6))
    sns.barplot(x=popular_products.index, y=popular_products.values, palette="viridis")
    plt.title("Most Purchased Products")
    plt.xlabel("Product Category")
    plt.ylabel("Number of Purchases")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("popular_products.png")
    plt.show()

    # Peak shopping hours
    plt.figure(figsize=(10, 6))
    sns.lineplot(x=peak_hours.index, y=peak_hours.values, marker='o', color="coral")
    plt.title("Peak Shopping Hours")
    plt.xlabel("Hour of Day")
    plt.ylabel("Number of Purchases")
    plt.tight_layout()
    plt.savefig("peak_shopping_hours.png")
    plt.show()

    # Age vs Spending
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=age_spending.index, y=age_spending.values, color="blue", s=100)
    plt.title("Age-wise Spending Trends")
    plt.xlabel("Age")
    plt.ylabel("Total Spending")
    plt.tight_layout()
    plt.savefig("age_spending_trends.png")
    plt.show()

# Perform clustering (optional)
def perform_clustering(data):
    print("Performing customer clustering...")

    # Select features for clustering
    X = data[['age', 'transaction_amount']].dropna()

    # Apply KMeans clustering
    kmeans = KMeans(n_clusters=3, random_state=42)
    data['cluster'] = kmeans.fit_predict(X)

    # Visualize clusters
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='age', y='transaction_amount', hue='cluster', palette='viridis', data=data, s=100)
    plt.title("Customer Clustering")
    plt.xlabel("Age")
    plt.ylabel("Transaction Amount")
    plt.legend(title="Cluster")
    plt.tight_layout()
    plt.savefig("customer_clustering.png")
    plt.show()

# Save insights to a report
def save_report(data, popular_products, peak_hours, age_spending):
    print("Saving report...")

    summary = {
        'Top Products': popular_products.head(5).to_dict(),
        'Peak Hours': peak_hours.head(3).to_dict(),
        'Age-wise Spending': age_spending.head(5).to_dict()
    }

    # Save processed data
    data.to_csv("processed_shopping_data.csv", index=False)

    # Save summary report
    with open("shopping_trends_report.txt", "w") as file:
        for key, value in summary.items():
            file.write(f"{key}:\n{value}\n\n")

    print("Report saved as 'shopping_trends_report.txt'.")

# Main function
def main():
    # File path for the dataset
    file_path = "shopping_data.csv"

    # Load the dataset
    data = load_data(file_path)

    # Preprocess the dataset
    data = preprocess_data(data)

    # Analyze shopping trends
    popular_products, peak_hours, age_spending = analyze_trends(data)

    # Visualize insights
    visualize_insights(popular_products, peak_hours, age_spending)

    # Perform clustering (optional)
    perform_clustering(data)

    # Save insights to a report
    save_report(data, popular_products, peak_hours, age_spending)

if __name__ == "__main__":
    main()
