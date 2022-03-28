Requirements Specification for Restaurant Management System

1.	Introduction


  I.	Purpose of Product

  The purpose of this project is to create an application for computers that will, mainly and most importantly, allow the tracking and notation of a restaurant’s food  inventory. Ideally this product would be used by restaurant employee to take note of the inventory for the day, and enter that information into this system for easy  tracking and inspecting.


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





 3.  Functional Requirements


 4.  System and Non-functional Requirements

  I.  External Interface Requirements

  Our application is designed to run on a windows operating system using an SQL database server. Therefore at a minimum requires:

  NF.4.1.1: Windows 10 TH1 1507 or greater

  NF.4.1.2: Windows 10 Server 2016 or greater

  NF.4.1.3: Minimum OS includes minimum .NET framework.


  II. Performance Requirements
In order to ensure the system is running accurately, we do require sufficient memory space to be able to store information to the database as well as a sufficient processor to be able to compile and move data in a timely matter. The minimum requirements are:

  NF.4.2.1: Minimum of 6 GB hard disk space and an additional 4 GB for database storage.

  NF.4.2.2: Access to an internet connection

  NF.4.2.3: Minimum x64 processor 1.4 GHz

  NF.4.2.4: Minimum of 2 GB RAM


  III. Design Constraints

  Our biggest constraint is memory because as database size increases, the memory required to run the application will also increase as well.


  IV. Quality Requirements

  To ensure good quality we: 

  NF.4.4.1: Recommend at least 4 GB of memory and should be increased as database size increases to ensure optimal performance.

  NF.4.4.2: Recommend an 800x600 resoultion monitor or higher

  NF.4.4.3: Recommend using a x64 processor 2.0 GHz to ensure good quality

  V.  Other Requirements

