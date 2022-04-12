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
       -takeOrders // call the order screen<br>
    =deleteFrame //this class controls the delete frame and function<br>
       
