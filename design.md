Architecture Diagram:

![Architecture Model](/assets/ArchDiagram.png)
  - Our Architecture Style is a Repository Style. We will have our main GUI that the user interacts with, and based on the button clicked and information entered, data will be updated, created, or deleted from a database. The database is our central repository of information which the whole python GUI revolves around. <br>
  The diagram above also shows a separate table that holds information about past days inventory counts that the user has to manually click a button to save into. The user is then able to retrieve that saved data for reference and comparison.



  <h4>Class Structures:</h4>
    =MainForm //This is the primary class of our program
        methods:
       -deleteItem // Calls delete frames
       -OnQuit // close program
       -onSwitchPanels // switch current pannel
       -refreshGrid // destorys current pannel
       -onInsertNewItem // opens frame for new item inserstion
       -onPastFoodClick //
       -onSaveForDay //
       -takeOrders // call the order screen
       -UpdateButton // Updates database as new information is being input 
    =deleteFrame //this class controls the delete frame and function
    =OrderPanel //This is the class that controls the UI for ordering
       methods:
      -Initializer // Creates the ordering pannel 
      -InitUI // Adds ordering buttons to the order panel menu and spaces them in rows of 3, buttons based on class Recipies 
    =OrderButton //This class creates buttons for the OrderPanel
      -Initializer // Creates a button, sets instance variables to the Recipie the button is for, sets name, and calls updateStatus
      -OnButtonClicked // Activates on the press of the button, reduces items from the inventory for it's own recipie 
      -updateStatus // Updates button appearance based on the inventory 
    =OrderFrame //Creates a frame for the OrderPanel
      -Initializer // Creates a frame and calls InitUI
      -InitUI // Sets the OrderFrame pannel to OrderPanel, sets frame name, and centers the frame
    =Recipies //Data structure class (linked list) that contains name and a dictionary "recipie"
      -Initializer // Sets name, ingredients, and a link to the next recipie node
      -getLastRecipie // Returns the last recipie, mainly used for adding to the end of linked list
      -getNumRecipies // Returns the total amount of recipies n the linked list
      -addRecipie // Adds a recipie to the end of the linked list, returns added item
      -searchRecipie // Searches data structure for node that contains the inputted name, returns that node
      -checkIfPresent // Searches through all the recipies ingredients to make sure they're in the inventory
      -checkAvailability // Searches through all the items ingredients to maek sure there's enough of the ingredient to produce recipie
      -getLowestDaysTillExperation // Returns the amount of days till the expiration on the ingredient expiring the soonest
      -printRecipieNode // Prints the nodes name and ingreidents, used for debugging
      -firstRecipie // global variable for recipies, starting the linked list
    =InventoryGrid // Grid that displays the main Inventory Sheet information
      -Initializer // Creates the Inventory Sheet grid (default sheet when starting the application)
      -shouldBeRed // Determines of a pulled expiration date is past the current time -- if so, tells the Grid to put that lettering in red
    =PastFoodFrame // The frame that displays the past-saved food stored in the database
      -Initializer // Creates the frame with the PastDatePanel showing
      -displayPastGrid // The functions for showing the PastFoodPanel after date is selected
    =PastFoodPanel // The panel that shows the grid for saved inventory from previous days
    =PastDatePanel // The panel that allows the user to select a date for inventory retrieval
    =PastFoodGrid // The grid that retrieves the information from the database and is applied to the PastFoodPanel based on inputted date
    


General Layout:
  - In general, this system has a system has a core background frame that every GUI item builds off of. That core frame is the Inventory Sheet Frame. This frame has the the whole menubar attached at the top, and from here, the user should be able to do anything they want/need to do. This is the highest level frame, and is the parent frame for every frame that will be generated based on the user's actions. So the Inventory Sheet frame is the parent of the "Insert" Frame, the "Past Food" Frame, the "Take an Order" Frame, etc.
  - The program is run with the "main.py" file, and everything should be accessible from executing this file -- meaning that, usually, every frame will be created from "main.py".

Database Layout:
  - The database tables do not change in their core types and columns. The main inventory sheet is one table called "food", while the backups and saved inventory counts are in a second table called "past_food". The table schemas are found in the "db_setup.py" file.
  - Any changes to inventory counts will only affect the "food" table, the "past_food" table is only for saving data and reading data, not modifying -- there are not (and shouldn't be) any ways to modify the data already in the "past_food" table.
  - In the "past_food" table, the main way data is retrieved is based on the 'date' column -- which is the date that the counts are saved.


Control Issues:
  - Our design is reliant mainly on an application that interacts with and updates a database based off of information that is input into the application. The application itself is user controlled with manual operations. Everything operates sequentially as well, as the user ultimately decides when updated information will be sent to the database using the "UpdateButton" function and when it will save to a separate table in the database using the "onSaveforDay" function. There is no behind the scenes updating really taking place.
