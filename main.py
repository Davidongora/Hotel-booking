"""
This module is responsible for the overall program flow. It controls how the user interacts with the
program and how the program behaves. It uses the other modules to interact with the user, carry out
processing, and for visualising information.

Note:   any user input/output should be done using the appropriate functions in the module 'tui'
        any processing should be done using the appropriate functions in the module 'process'
        any visualisation should be done using the appropriate functions in the module 'visual'
"""


# Task 11: Import required modules and create an empty list named 'reviews_data'.
# This will be used to store the data read from the source data file.
# TODO: Your code here
import process
import tui
import visual
import json

reviews_data=[]

def run():
    # Task 12: Call the function welcome of the module 'tui'.
    # This will display our welcome message when the program is executed.
    # TODO: Your code here
    tui.welcome()
    # Task 13: Load the data.
    # - Use the appropriate function in the module 'tui' to display a message to indicate that the data loading
    # operation has started.
    # - Load the data. Each line in the file should represent a review in the list 'reviews_data'.
    # You should appropriately handle the case where the file cannot be found or loaded.
    # - Use the appropriate functions in the module 'tui' to display a message to indicate how many reviews have
    # been loaded and that the data loading operation has completed.
    #tui.welcome()
    try:
        #path /Users/mac/Desktop/Hotel Project (2)/qho426-project-template/data/hotel_reviews.csv
        with open('hotel_reviews.csv', 'r') as file:
            for line in file:
                reviews_data.append(line.strip().split(','))
    except FileNotFoundError:
        tui.error("File not found. Please make sure 'hotel_reviews.csv' is in the current directory.")
    except Exception as e:
        tui.progress("An error occurred while loading the data: " + str(e))
    else:
        tui.error(f"{len(reviews_data)} reviews have been loaded.")
        tui.error("Data loading has completed.")
    
    
    # TODO: Your code here

    while True:
        # Task 14: Using the appropriate function in the module 'tui', display the main menu
        # Assign the value returned from calling the function to a suitable local variable
        # TODO: Your code here
        x=tui.main_menu()
        

        # Task 15: Check if the user selected the option for processing data.  If so, then do the following:
        # - Use the appropriate function in the module tui to display a message to indicate that the data processing
        # operation has started.
        # - Process the data (see below).
        # - Use the appropriate function in the module tui to display a message to indicate that the data processing
        # operation has completed.
        #
        # To process the data, do the following:
        # - Use the appropriate function in the module 'tui' to display a sub-menu of options for processing the data
        # (menu variant 1).
        # - Check what option has been selected
        #
        #   - If the user selected the option to retrieve reviews by hotel name then
        #       - Use the appropriate function in the module 'tui' to indicate that the review retrieval process
        #       has started.
        #       - Use the appropriate function in the module 'process' to retrieve the review and then appropriately
        #       display it.
        #       - Use the appropriate function in the module 'tui' to indicate that the review retrieval process has
        #       completed.
        #
        #   - If the user selected the option to retrieve reviews by review dates then
        #       - Use the appropriate function in the module 'tui' to indicate that the reviews retrieval
        #       process has started.
        #       - Use the appropriate function in the module 'process' to retrieve the reviews
        #       - Use the appropriate function in the module 'tui' to display the retrieved reviews.
        #       - Use the appropriate function in the module 'tui' to indicate that the reviews retrieval
        #       process has completed.
        #
        #   - If the user selected the option to group reviews by nationality then
        #       - Use the appropriate function in the module 'tui' to indicate that the grouping
        #       process has started.
        #       - Use the appropriate function in the module 'process' to group the reviews
        #       - Use the appropriate function in the module 'tui' to display the groupings.
        #       - If required, you may add a suitable function to the module 'tui' to display the groupings
        #       - Use the appropriate function in the module 'tui' to indicate that the grouping
        #       process has completed.
        #
        #   - If the user selected the option to summarise the reviews then
        #       - Use the appropriate function in the module 'tui' to indicate that the summary
        #       process has started.
        #       - Use the appropriate function in the module 'process' to summarise the reviews.
        #       - Add a suitable function to the module 'tui' to display the summary
        #       - Use your function in the module 'tui' to display the summary
        #       - Use the appropriate function in the module 'tui' to indicate that the summary
        #       process has completed.
        # TODO: Your code here
        
        if x == 1:
             tui.progress("Data processing", 0)  # Start progress with value 0
    
             sub_menu_choice = tui.sub_menu()
             if sub_menu_choice == 1:
                tui.progress("Review retrieval process", 10)  # Update progress with value 10
        # Rest of the code
                tui.progress("Review retrieval process", 90)  # Update progress with value 90
             elif sub_menu_choice == 2:
                 tui.progress("Reviews retrieval process", 10)
        # Rest of the code
                 tui.progress("Reviews retrieval process", 90)
             elif sub_menu_choice == 3:
                    tui.progress("Grouping process", 10)
        # Rest of the code
                    tui.progress("Grouping process", 90)
             elif sub_menu_choice == 4:
                    tui.progress("Summary process", 10)
        # Rest of the code
                    tui.progress("Summary process", 90)
             else:
                tui.error("Invalid option. Please try again.")
    
                tui.progress("Data processing", 100)  # Update progress with value 100


        # Task 21: Check if the user selected the option for visualising data.
        # If so, then do the following:
        # - Use the appropriate function in the module 'tui' to indicate that the data visualisation operation
        # has started.
        # - Visualise the data by doing the following:
        #   - call the appropriate function in the module 'tui' to determine what visualisation is to be done.
        #   - call the appropriate function in the module 'visual' to display the visual
        # - Use the appropriate function in the module 'tui' to display a message to indicate that the
        # data visualisation operation has completed.
        # TODO: Your code here
        elif x == 2:
            tui.error("Data visualisation has started.")
        visual_choice = tui.sub_menu()
        if visual_choice == 1:
                visual.display_review(reviews_data)
        elif visual_choice == 2:
                visual.display_review(reviews_data)
        else:
                tui.error("Invalid option. Please try again.")
                tui.error("Data visualisation has completed.")

        # Task 25: Check if the user selected the option for exporting reviews.  If so, then do the following:
        # - Use the appropriate function in the module 'tui' to retrieve what reviews are to be exported.
        # - Check what option has been selected
        #
        # - Use the appropriate function in the module 'tui' to indicate that the export operation has started.
        # - Export the reviews (see below)
        # - Use the appropriate function in the module 'tui' to indicate that the export operation has completed.
        #
        # To export the reviews, you should demonstrate the application of OOP principles including the concepts of
        # abstraction and inheritance.  You should create suitable classes with appropriate methods.
        # You should use these to write the reviews (either all or only those for a specific country/region) to a JSON file.
        # TODO: Your code here
        import json

class ReviewExporter:
    def __init__(self, reviews):
        self.reviews = reviews

    def export_all_reviews(self):
        self._export_reviews(self.reviews)

    def export_reviews_by_country(self, country):
        country_reviews = [review for review in self.reviews if review['country'] == country]
        self._export_reviews(country_reviews)

    def _export_reviews(self, reviews):
        with open('reviews.json', 'w') as file:
            json.dump(reviews, file, indent=4)
            # You can customize the formatting options as needed

# ... (other code)

if x == 3:
    export_option = tui.get_export_option()
    if export_option == 1:
        tui.progress("Exporting all reviews.", value=50)
        exporter = ReviewExporter(reviews_data)
        exporter.export_all_reviews()
    elif export_option == 2:
        country = tui.get_country()
        tui.progress(f"Exporting reviews for {country}.", value=50)
        exporter = ReviewExporter(reviews_data)
        exporter.export_reviews_by_country(country)
    else:
        tui.error("Invalid option. Please try again.")
    tui.progress("Export operation has completed.", value=100)

        # Task 26: Check if the user selected the option for exiting the program.
        # If so, then break out of the loop
        # TO#DO: Your code here
elif x == 4:
   break
        # Task 27: If the user selected an invalid option then use the appropriate function of the
        # module tui to display an error message
        # TODO: Your code here
else:
            tui.error("Invalid option. input 1-4")

pass  # can remove


if __name__ == "__main__":
    run()
