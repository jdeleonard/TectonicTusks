Architecture Diagram:

![Architecture Model](/assets/ArchDiagram.png)
  - Our Architecture Style is a Repository Style. We will have our main GUI that the user interacts with, and based on the button clicked and information entered, data will be updated, created, or deleted from a database. The database is our central repository of information which the whole python GUI revolves around. <br>
  The diagram above also shows a separate table that holds information about past days inventory counts that the user has to manually click a button to save into. The user is then able to retrieve that saved data for reference and comparison.



  <h4>Class Structures (Java):</h4>
    =MainForm //This is the primary class of our program<br>
        methods:<br>
       -deleteItem // Calls delete frames<br>
       -OnQuit // close program<br>
       -onSwitchPanels // switch current pannel<br>
       -refreshGrid // destorys current pannel<br>
       -onInsertNewItem // opens frame for new item inserstion<br>
       -onPastFoodClick //<br>
       -onSaveForDay //<br>
       -takeOrders // call the order screen<br>'
       -UpdateButton // Updates database as new information is being input <br>
    =deleteFrame //this class controls the delete frame and function<br>
    =OrderPanel //This is the class that controls the UI for ordering<br>
       methods:<br>
      -Initializer // Creates the ordering pannel <br>
      -InitUI // Adds ordering buttons to the order panel menu and spaces them in rows of 3, buttons based on class Recipies <br>
    =OrderButton //This class creates buttons for the OrderPanel<br>
      -Initializer // Creates a button, sets instance variables to the Recipie the button is for, sets name, and calls updateStatus <br>
      -OnButtonClicked // Activates on the press of the button, reduces items from the inventory for it's own recipie <br>
      -updateStatus // Updates button appearance based on the inventory <br>
    =OrderFrame //Creates a frame for the OrderPanel<br>
      -Initializer // Creates a frame and calls InitUI<br>
      -InitUI // Sets the OrderFrame pannel to OrderPanel, sets frame name, and centers the frame<br>
    =Recipies //Data structure class (linked list) that contains name and a dictionary "recipie"<br>
      -Initializer // Sets name, ingredients, and a link to the next recipie node<br>
      -getLastRecipie // Returns the last recipie, mainly used for adding to the end of linked list<br>
      -getNumRecipies // Returns the total amount of recipies n the linked list<br>
      -addRecipie // Adds a recipie to the end of the linked list, returns added item<br>
      -searchRecipie // Searches data structure for node that contains the inputted name, returns that node<br>
      -checkIfPresent // Searches through all the recipies ingredients to make sure they're in the inventory<br>
      -checkAvailability // Searches through all the items ingredients to maek sure there's enough of the ingredient to produce recipie<br>
      -getLowestDaysTillExperation // Returns the amount of days till the expiration on the ingredient expiring the soonest<br>
      -printRecipieNode // Prints the nodes name and ingreidents, used for debugging
      -firstRecipie // global variable for recipies, starting the linked list


Control Issues:
  - Our design is reliant mainly on an application that interacts with and updates a database based off of information that is input into the application. The application itself is user controlled with manual operations. Everything operates sequentially as well, as the user ultimately decides when updated information will be sent to the database using the "UpdateButton" function and when it will save to a separate table in the database using the "onSaveforDay" function. There is no behind the scenes updating really taking place.
