<strong>User Stories</strong> <br/><br/>
1.1: Update Inventory <br>

As a restaurant employee, I want to be able to easily update inventory in a fast and timely matter so I can update inventory quickly on busy days. <br><br>

Elaboration: Users should have the ability to easily update information without having to focus on pressing too many buttons or navigating too many windows to update or add one item. To do this, we will have ease of access by having two major buttons at the top of the chart stating whether information will need to be created or deleted. Users will also be able to update inventory table simply by clicking on the respective box they want to update and typing. <br><br>

Constraints: none <br><br>

Effort Estimation: 4 hours <br><br>

Acceptance Test: We will test each button is working correctly by pretending to be a worker ourselves and simulating adding inventory products, updating current inventory and deleting inventory that is no longer needed. <br><br><br>

----------------

1.2: Adding/Deleting List Items <br><br>

As a restaurant employee, I want to be easily be able to add new items to the inventory sheet, and also delete any items I no longer want on the sheet. <br><br>

Elaboration: Users should be able to easily add products (rows) into the inventory sheet/database, and should just also be able to delete items from said inventory sheet or database.

Constraints: None <br><br>

Effort Estimation: 4 hours <br><br>

Acceptance Test: We will attempt to enter in new, fake, food items and then try to delete them -- at each stage checking if the inventory sheet updates with the addition or deletion. <br><br><br>

----------------

1.3 Updating Expiration Dates

As a restaurant employee, I want to easily be able to update and change the expiration dates for any product on the inventory sheet. <br><br>

Elaboration: Users should be able to update expiration dates for inventory sheet items, this should also have live, responsive, refreshes with updated letting color and such.

Contraints: None <br><br>

Effort Estimation: 2 hours <br><br>

Acceptance Test: We will insert new items into the inventory sheet, and then attempt to edit/change the expiration dates and see if the sheet and database will edit. <br><br><br>

----------------

2.1: Visually Appealing and Helpful  <br><br>

As an older employee, I want to be able to read the inventory table without straining my eyes so I can continue to do my job in a fast and timely manner. <br><br>

Elaboration: Users should be able to read the inventory table easily without struggling with too much clutter. To ensure this, our table will be evenly spaced, have medium sized fonts, and potentially have color implemented to make rows easier to read. <br><br> 

Constraints: None <br><br>

Effort Estimation: 2 hours <br><br>

Acceptance Test: We will have people from different age groups practice updating inventory, and receive their feedback as to how easy it was to navigate and read. <br><br><br>

----------------

2.2: Expiring Dates Stand Out <br><br>

As a restaurant employee, I want to easily tell if and when a product is expiring. <br><br>

Elaboration: Users should be able to easily see when a product is expiring from the expiration spreadsheet. This would include red lettering for the dates if a product is about to, or had expired.

Constraints: None <br><br>

Effort Estimation: 1 hours <br><br>

Acceptance Test: We will enter in fake expiration dates, and see what colors the lettering is based on the fake dates -- expiration test cases would be before the date, on the date, and after the date <br><br><br>

----------------

2.3: Feature Accessibility <br><br>

As a restaurant employee, I want to be able to get to any option/feature that I need to from the main inventory sheet. <br><br>

Elaboration: Users should be able to access all system features from the main inventory sheet. This will be done with a main menubar at the top of the screen that has a button/option for the function. <br><br>

Contraints: The Creation of a Menubar <br><br>

Effort Estimation: 4 hours <br><br>

Acceptance Test: We will list out all of our features and functions, and attempt to get to them from the main inventory sheet. And if this is not possible, we will add a menubar option for the feature. <br><br><br>

----------------

3.1: Be able to publish/post/finalize counts for a day <br><br>

As a restaurant manager, I want ot be able to finalize inventory counts once per day that would be almost unchangable once finalized. <br><br>

Elaboration: Users should be able to save and finalize a set of counts for a day that would be saved and retrievable. This would happen with a button. <br><br>

Contraints: A separate database table to hold past day's counts <br><br>

Effort Estimation: 6 hours <br><br>

----------------

3.2: Look at Percents <br><br>

As a restaurant manager, I want to be able to see the difference in inventory between the last day and today. <br><br>

Elaboration: Users should be able to see the difference in inventory counts across different days in percentage form. <br><br>

Contraints: A separate database table to hold past day's counts <br><br>

Effort Estimation: 3 hours <br><br>

Acceptance Test: We will manually calculate some deviation percentages, and then cross check what the system determines the variations to be.

----------------

4.1: Multiple Updates <br><br>

As a restaurant owner, I want multiple employees to be able to update the system at once so inventory is reflecting as accurately as possible. <br><br>

Elaboration: Multiple users should be able to use the system at once and have inventory updating in real time to ensure accuracy. <br><br>

Constraints: System requirements <br><br>

Effort Estimation: 4-6 hours <br><br>

Acceptance Test: We will have two people trying to update the system at once, and see how quickly information is updating <br><br><br>

----------------

5.1: Food Entering <br><br>

As a restaurant employee, I want to be able to enter food into the system and dynamically change the amount of inventory. <br><br>

Elaboration: A user should be able to click a button and it subtract from the inventory counts based on the item clicked. <br><br>

Constraints: None <br><br>

Effor Estimation: 5-6 hours <br><br>

Acceptance Test: We will manually calculate how much food should be used based on an item click, we will click the item and check by how much the inventory was lowered. <br><br><br>

-----------------

