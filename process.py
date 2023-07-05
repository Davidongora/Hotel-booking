"""
This module is responsible for processing the data.  Each function in this module will take a list of reviews,
process it and return the desired result.
"""

"""
Task 16 - 20: Write suitable functions to process the data.

Each of the functions below should follow the pattern:
- Take a list of reviews (where each review is a list of data values) as a parameter.
- Process the list of reviews appropriately.  You may use the module 'tui' to retrieve any additional information 
required from the user to complete the processing.
- Return a suitable result

The required functions are as follows:
- Retrieve the total number of reviews that have been loaded.
- Retrieve the reviews for a hotel where the hotel name is specified by the user.
- Retrieve the reviews for the dates specified by the user.
- Retrieve all the reviews grouped by the reviewer’s nationality.
- Retrieve a summary of all the reviews. This should include the following information for each date in ascending order:
    - the total number of negative reviews on that date
    - the total number of positive reviews on that date
    - the average rating on that date
"""

# TODO: Your code here
import tui
def get_total_reviews(reviews):
    return len(reviews)
#print(get_total_reviews())

def retrieve_reviews_by_hotel(reviews):
    hotel_name = tui.hotel_name()
    hotel_reviews = []
    for review in hotel_reviews:
        if review[1] == hotel_name:
           hotel_reviews.append(review)
    return hotel_reviews

def get_reviews_by_dates(reviews):
    review_dates = tui.review_dates()
    date_reviews = []

    for review in reviews:
        if review[0] in review_dates:
            date_reviews.append(review)
    return date_reviews

def group_reviews_by_nationality(reviews):
    grouped_reviews = {}
    for review in reviews:
        nationality = review[2]
        if nationality in grouped_reviews:
            grouped_reviews[nationality].append(review)
        else:
            grouped_reviews[nationality] = [review]
    return grouped_reviews

def get_reviews_summary(reviews):
    
    summaries = []
    for review in reviews:
        date = review[0]
        rating = review[5]
        sentiment = 'Positive' if rating >= 3 else 'Negative'
        summaries.append((date, sentiment, rating))
    summaries.sort()
    return summaries