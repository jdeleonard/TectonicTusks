Requirements Specification for Restaurant Management System

<strong>1)	Introduction</strong>

  - I.	Purpose of Product

    - The purpose of this project is to create an application for computers that will, mainly and most importantly, allow the tracking and notation of a restaurant’s food  inventory. Ideally this product would be used by restaurant employee to take note of the inventory for the day, and enter that information into this system for easy  tracking and inspecting.


  - II.	Scope of Product

    - This project will include:
      - •	An update-able spreadsheet with each product listed
      - •	An editable sheet with expiration date tracking
      - •	A way to display calculations of expected usage vs. actual usage.


  - III.	Acronyms, Abbreviations, Definitions
    - UI = "User Interface"; refers to the visual application of the system on the computer screen -- includes the spreadsheet, buttons, etc.
    - GUI = "Graphical User Interface"; refers to the visual application of the system on the computer screen -- includes the spreadsheet, buttons, etc.


<br><br><br>
<strong>2)	General Description of Product</strong>

  - I.	Context of Product

    - This product is meant to be found and used in the back-of-house of restaurants. This would be found on the main computer for a restaurant, so that the proper employees are able to use and modify the system/inventory sheets.


  - II.	Domain Model with Description

    ![Domain Model](/assets/DomainModel.png)

    - This UML Domain Model describes the software for the application. The main and central class is the MainFrame, which contains various GUI methods, which will switch between panels. The InventoryPanel class inherits from the MainFrame class, and the MainFrame class contains a panel which is displayed in the frame from the MainFrame class. The InsertFrame and DeleteFrame classes inherit from the MainFrame class. Each of these classes also have a child Panel which can be turned on or off, which also contains GUI content. The InsertPanel and DeletePanel have methods to modify and change the food database. These methods use the attriutes of id, name, amount, unit, and expiration date to enter this information from the panels (entered by the user) into the database. The application depends on the MainFrame running in a main loop, while the children classes have objects that can be destroyed and created based on GUI actions and buttons.

  - III. Product Functions
    - The main function of this product is to have a central application and system for storing information about food inventory counts and expiration dates. The system would also be able to give information about product usage deviation and be completely self-servable -- meaning that one the user receives the software, they can do everything they need themselves.

  - IV. User Characteristics and Expectations
    - The users of this system should be able to add inventory items, delete items, update/modify counts and amounts for existing items, update/modify expiration dates for existing items, and also be able to see past days inventory counts and see the percent lost/used between days.

  - V. Constraints
    - We are dependant on wxPython being installed currently.
    - The running machine needs to be able to have read/write access in it's save place -- for changing the database.

  - VI. Assumptions and Dependencies
    - Our software/system currently depends on Python 3 being installed.
    - Our software/system currently depends on the wxPython package in order to run the application.
    - Our software/systems is being designed to work on a Windows OS machine.




<br><br><br>
<strong>3)  Functional Requirements</strong>

| Requirement ID | Requirement Statement | Status | Comments |
| --- | --- | --- | --- |
| FR001 | The application will have a home screen that displays the inventory database into a readable table. | Must | Database |
| FR002 | The application will have a menu bar that will allow the user to switch pages. | Must | |
| FR003 | The application will have an adding items screen that will allow the user to add new items to the inventory | Must | Database |
| FR004 | The application will have a screen for retrieving previous inventories from prior dates. | Want | Database |
| FR005 | The application will have a screen for comparing inventories from prior dates. | Database |
| FR006 | The application will have a database that contains the following information: A unique ID for identifying each item on the inventory, the amount of stock for that item, the units that the amount is counted by, Expiration date for the item | Must | Database |
| FR007 | The application will have a database for inventories of previous days, contains the following information: A unique ID for each date, the date of the inventory, a link to the database in the format of FR006. | Must | Database |
| FR008 | The home screen (FR001) will have a button to finalize the inventory of that day. | Must | Database |
| FR009 | The home screen (FR001) will have a button to start a fresh day’s inventory. | Must |  |
| FR010 | The home screen (FR001) will display the current day’s inventory in a table that the user is able to edit by clicking on the text and typing | Must | Database |
| FR011 | The home screen (FR001) will have a save button to save the inputted information into the database. | Must | Database |
| FR012 | The adding screen (FR003) will display boxes that the user can type into to input information about the new item being added into the inventory. The information inputted is: Food Name, amount of item, unit to measure amount, expiration Date | Must | Database|
| FR013 | The adding screen (FR003) will have an “Add Item” button that adds the inputted information from FR012 into the database | Must | Database |
| FR014 | The retrieving previous entries screen (FR004) will have a box to input a date that the user wants to retrieve the data from | Want | |
| FR015 | The retrieving previous entries screen (FR004) will have a button to retrieve the data from the inputted date (FR014). On activation, a table of the inventory for the inputted date is displayed. | Want | Database |
| FR016 | The comparing screen (FR005) will have two entry boxes for the user to type in dates to compare | Must | |
| FR017 | The comparing screen (FR005) will have a button to retrieve the inventory information on the given dates (FR016). On activation, the numerical values of the amount of inventory will be displayed and a percentage will be displayed (The difference from the two dates given). | Must | Database |
| FR018 | The adding screen (FR003) will have an input box for the user to type what item they want to remove, they type in the unique ID of the item. | Must | |
| FR019 | The adding screen (FR003) will have a button do delete the item from the database once FR018 has been inputted. | Must | |






<br><br><br>
<strong>4)  System and Non-functional Requirements</strong>

  - I.  External Interface Requirements

    - Our application is designed to run on a windows operating system using an SQL database server. Therefore at a minimum requires:
    - NF.4.1.1: Windows 10 TH1 1507 or greater
    - NF.4.1.2: Windows 10 Server 2016 or greater
    - NF.4.1.3: Minimum OS includes minimum .NET framework.


  - II. Performance Requirements
    - In order to ensure the system is running accurately, we do require sufficient memory space to be able to store information to the database as well as a sufficient processor to be able to compile and move data in a timely matter. The minimum requirements are:
    - NF.4.2.1: Minimum of 6 GB hard disk space and an additional 4 GB for database storage.
    - NF.4.2.2: Access to an internet connection
    - NF.4.2.3: Minimum x64 processor 1.4 GHz
    - NF.4.2.4: Minimum of 2 GB RAM


  - III. Design Constraints

    - Our biggest constraint is memory because as database size increases, the memory required to run the application will also increase as well.


  - IV. Quality Requirements

    - To ensure good quality we:
      - NF.4.4.2: Recommend an 800x600 resoultion monitor or higher
      - NF.4.4.3: Recommend using a x64 processor 2.0 GHz to ensure good quality


V.  Other Requirements
