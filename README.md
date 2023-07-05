# Hotel-booking
software application that can be used to process and manage data related to the hotel reviews record

a)    The system will present the user with a text-based user interface through which a user will select options to load the data, process the data, persist the data and visualise the data.
b)    The system will load the data from a CSV file into memory.
c)    The system will allow the user to process the loaded data as follows:
- Retrieve the total number of reviews that have been loaded.
- Retrieve the reviews for a hotel where the hotel name is specified by the user.
- Retrieve the reviews for the dates specified by the user.
- Retrieve all the reviews grouped by the reviewer’s nationality.
- Retrieve a summary of all the reviews. This should include the following information for each date in ascending order:
    - the total number of negative reviews on that date
    - the total number of positive reviews on that date
    - the average rating on that date 
d)    The system will allow the user to visualise the data as follows:
- Display a pie chart showing the total number of positive and negative reviews for a specified hotel.
- Display the number of reviews per nationality of a reviewer. This should by ordered by the number of reviews, highest first, and should show the top 15 + “Other” nationalities.
- Display a suitable animated visualisation to show how the number of positive reviews, negative reviews and the average rating change over time.

e)    The system will allow the user to export reviews in the form of JSON.  The user should be able to export the following:
- All the reviews
- The reviews for a specific hotel

It is expected that you will develop a modular software application that meets the stated requirements. You have been provided with a CSV file (hotel_reviews.csv) that contains data relating to hotel reviews. This is only a sample data set and your system may be tested with a larger data set.  Your application will need to appropriately load the data contained in this file, process and visualise it.
It is envisaged that the software application will consist of at least the following modules:
Tui – This module provides a text-user interface for the software application. All communication with the user (reading user input or displaying text output) is performed using functions in this module.
Process – This module contains several user-defined functions that can be utilised to process the data.  The functions will take suitable parameters and return results consisting of processed data.
Visual – This module provides the visual interface for the software application and contains functions used to display suitable visual outputs such as charts.
Main – This module contains the main logic for the software application and utilises the other modules.
