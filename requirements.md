Requirements Specification for Restaurant Management System
1.	Introduction
I.	Purpose of Product
The purpose of this project is to create an application for computers that will, mainly and most importantly, allow the tracking and notation of a restaurant’s food inventory. Ideally this product would be used by restaurant employee to take note of the inventory for the day, and enter that information into this system for easy tracking and inspecting.
II.	Scope of Product
This project will include:
•	An update-able spreadsheet with each product listed
•	An editable sheet with expiration date tracking
•	A way to display calculations of expected usage vs. actual usage.
III.	Acronyms, Abbreviations, Definitions
IV.	References
2.	General Description of Product
I.	Context of Product
This product is meant to be found and used in the back-of-house of restaurants. This would be found on the main computer for a restaurant, so that the proper employees are able to use and modify the system/inventory sheets.
II.	Domain Model with Description
The main model for this system is a Publish-Subscribe and Repository Architectures. The system is using the Publish-Subscribe idea to registering procedures with events within the UI of the systems (window buttons, menu options, etc.), and based on which button/event is triggered, a central data store has its information changed, deleted, or new information added. This second part is what makes this product also a Repository model. This system uses a traditional database as its central data store
III.	Product Functions (general)
IV.	User Characteristics and Expectations
V.	Constraints
VI.	Assumptions and Dependencies
3.	Functional Requirements
4.	System and Non-functional Requirement
I.	External Interface Requirements
II.	Performance Requirements
III.	Design Constraints
IV.	Quality Requirements
V.	Other Requirements
