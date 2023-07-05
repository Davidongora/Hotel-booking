"""
This module is responsible for visualising the data using Matplotlib.
"""

"""
Task 22 - 24: Write suitable functions to visualise the data as follows:

- Display a pie chart showing the total number of positive and negative reviews for a specified hotel.
- Display the number of reviews per the nationality of a reviewer. This should by ordered by the number of reviews, highest first, and should show the top 15 + “Other” nationalities.
- Display a suitable animated visualisation to show how the number of positive reviews, negative reviews and the average rating change over time.

Each function should visualise the data using Matplotlib.
"""

# TODO: Your code here
import matplotlib.pyplot as plt

def visualize_reviews_by_sentiment(hotel_reviews):
    positive_reviews = sum(1 for review in hotel_reviews if review[1] == "Positive")
    negative_reviews = sum(1 for review in hotel_reviews if review[2] == "Negative")
    
    labels = ["Positive", "Negative"]
    sizes = [positive_reviews, negative_reviews]
    
    plt.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=90)
    plt.axis("equal")
    plt.title("Sentiment Analysis: Positive vs Negative Reviews")
    plt.show()



def visualize_reviews_by_nationality(reviews):
    nationality_counts = {}
    for review in reviews:
        nationality = review[2]
        nationality_counts[nationality] = nationality_counts.get(nationality, 0) + 1

    # Sort the nationalities by the number of reviews (highest first)
    sorted_counts = sorted(nationality_counts.items(), key=lambda x: x[1], reverse=True)

    # Select the top 15 nationalities and combine the rest as "Other"
    top_nationalities = [item[0] for item in sorted_counts[:15]]
    top_counts = [item[1] for item in sorted_counts[:15]]
    other_count = sum(item[1] for item in sorted_counts[15:])
    top_nationalities.append("Other")
    top_counts.append(other_count)

    # Create a bar chart
    plt.barh(range(len(top_nationalities)), top_counts, align="center")
    plt.yticks(range(len(top_nationalities)), top_nationalities)
    plt.xlabel("Number of Reviews")
    plt.ylabel("Nationality")
    plt.title("Number of Reviews per Nationality")
    plt.show()

def visualize_reviews_over_time(reviews):
    dates = [review[0] for review in reviews]
    positive_reviews = [review[3] for review in reviews]
    negative_reviews = [review[4] for review in reviews]
    average_ratings = [review[5] for review in reviews]

    # Plot the data over time
    plt.plot(dates, positive_reviews, label="Positive Reviews")
    plt.plot(dates, negative_reviews, label="Negative Reviews")
    plt.plot(dates, average_ratings, label="Average Rating")
    plt.xlabel("Date")
    plt.ylabel("Count / Rating")
    plt.title("Reviews Over Time")
    plt.legend()
    plt.show()