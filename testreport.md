<strong> 1. Component Testing </strong>

  - Database Functions Testing
    - One of the larged modules that we tested separated were all the database functions. All of these functions can be found in the db_functions.py file. Every single one of these functions was tested throughly to make sure that all database operations were consistant and correct -- to be called later by GUI buttons and actions.
    - All of these functions were further integrated into the system -- a different function being used in almost every button event call, this is why we needed to make sure that these functions were correct and worked.
    - Most of these functions were tested with the following steps:
      - First, we created basic fake food information and manually entered them into the database
        - An example of these fake items was: Pizza, 8.0 Slices
      - Then, based on the type of database function, modified this fake information, retrieved this fake information, or saved this fake information.
      - In the case of a function whose purpose was to modify information (in this case fake information)
        - We would manually pass the function the id of the fake rows, and then go look through the database to see if the information was corrected modified.
        - Example: An updateRow function, for testing, would be manually passed the id of Pizza, and attempt to set the 8.0 Slices to 24.0 Slices. After calling this function, we would go look in the database to see if the row indeed says 24.0 instead of 8.0 for the Pizza slices.
        - Passing id integers works best for testing in this case because we can only change information in the database if we specify specifially which row/item we want to change. So in order to identify the row, we pass the id to make sure the right item is being modified. This also fits in our end system, because the application will be passing ids to these functions in order to change specific rows.

      - In the case of a function whose purpose was to retrieve information:
        - The main testing of information retrieval was done using specially placed print statements to see the state of the information at various points.
        - We would again pass the function fake information for testing, and get the function to retrieve data based on the passed information.
        - Example: A getAllRows function, for testing, would manually be passed a table to get all the rows from, and we would save the returned tuple into a variable. We would then print out that tuple and compare the information from the tuple to the information that we manually went to go look at in the database file. If the rows, values, and information matched (in their order also), we knew that the function was working properly.
        - Manually passing a table or id is best in these situations because we are, in most cases, retrieving information on everything in a table, or everything about a table. The system will use these types of functions to gather necessary information based on a table, so passing a table makes the most sense in testing.

      - In the case of a function whose purpose was to save information:
        - These functions were mainly tested by entering manually passing information to the function with strings and seeing if the end database picture matched the information passed.
        - Example: A saveDaysInventory function would manually be passed a tuple containing rows of information corresponding to food rows in the main 'food' table of the database. We would then go look in the database file to see if all the rows and values match the values and ordering of the tuple correctly. If the information and values all lined up as expected and wanted, we knew that our function worked properly.
        - Passing the function strings and tuples is the best choice because that is how the database best communcations with python, through the passing of tuples in order to insert, delete, and modify information.



<strong> 2. System Testing </strong>


  - Recipie Addition testing
    - Components for recipies (food order panel, recipie addition panel) were both added into the larger system to be tested.
      - Both components were introduced to the main system through the menu bar
      - Components can speak to eachother through a file with saved information about the recipies
      - Navigating through panels, adding recipies through the recipie addition panel and then loading the order screen to make sure
      changes were saved.

<strong> 3. Acceptance Testing </strong>

  - 1.2 Adding/Deleting List Items
    - Accepted.
    - This test had the following steps:
       - Create Fake Food Items
       - Enter those fake food items into the inventory application (using GUI)
       - Go manually look at the database rows and determine if the fake item is now a row in the table
         - This was done with an application called "sqlite3.exe" which allows the user to manually open a database file for reading and writing
       - Once the new entry was verified, we went back to the GUI
       - We attempted to delete that same fake item we just added to the inventory database.
       - After selecting the right id/name and clicking delete, we again manually checked the database file to determine if that row still existed.
       - Once we verified that the row was now gone, we concluded our Acceptance Test to be 'Accepted'.

  - 2.2 Expiring Dates Stand Out
    - Accepted.
    - This test had to following steps:
      - Create 3 fake food items. One with an expiration date earlier than testing day, one with an expiration date on the same day as the testing day, and one with an expiration date later than the testing day.
        - This covers every scenario of what an exipiration date could be in relation to the current date.
      - Add these items into the database
      - Refresh the inventory sheet (either manually with a restart, or with functions)
      - Look at the color of each fake food item case -- where the expiried product should be red and non-expiried product has the normal black lettering
        - Note that we wanted the lettering of the text to be red even when the product expiration date was the same as the current date
      - As we observed that the expiried product was all in red, and the non-expiried product was in black, we concluded our Acceptance Test to be 'Accepted'

  - 2.3 Feature Accessibility
    - Accepted.
    - This test had to following steps:
      - Create a list of all (current) possible high-level functions that the application contains. These include:
        - Inserting Inventory Items
        - Deleting Inventory Items
        - Viewing Inventory Posts from the past
        - Order Items that dynamically edit the inventory
      - We then started our application where we were brought to the main, home page with the current day's inventoy counts.
      - We then attempted to get to each of the high-level functions without having to leave the main page
        - Each one of the functions was accessed through a menubar at the top of the application
      - After each high-level function, we returned to the main Inventory Sheet page, and tried to get to the next high-level function
      - Each high-level function was accessible from the main page, which is why we marked this Acceptance Test to be 'Accepted'

  - 3.1 Be able to publish/post/finalize counts for a day
    -  Accepted.
    - This test had the following steps:
      - Add multiple rows/items into the database as fake food items
      - After items have been added, attempt to post/save the data for the day through the menubar button
      - We then went manually into the database file and, with the same sqlite3.exe program, inspected the 'past_food' table to see if today's entry was saved inside the table.
      - After inspecting and querying the database directly, we found that the current day's inventory counts saved to another table to be saved and retrieved later, which caused us to determine that this Acceptance Test was 'Accepted'

  - 5.1 Food Entering
    - Accepted.
    - This test had the following steps:
      - Create a list of all possibilities of recipies to be added, including name changes, ingredient changes, and amount of ingredients
      - Load pre saved data into the recipies.txt file to make sure that recipies got initialized properly from the file.
      - Added different types of recipies from the add recipie screen.
      - Verify the added recipies from the recipie screen saved properly in the file.
      - Load the saved data from the recipie screen to make sure that saved data initialized properly.
