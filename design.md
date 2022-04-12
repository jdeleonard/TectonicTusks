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
       
Control Issues:
  - Our design is reliant mainly on an application that interacts with and updates a database based off of information that is input into the application. The application itself is user controlled with manual operations. Everything operates sequentially as well, as the user ultimately decides when updated information will be sent to the database using the "UpdateButton" function and when it will save to a separate table in the database using the "onSaveforDay" function. There is no behind the scenes updating really taking place. 