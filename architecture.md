<strong> Architecture Page

![Architecture Model](/assets/ArchitectureModel.png) 

<br><br>
- Our Architecture will follow a repository style. This style consists of a central data store (database) and data accessing component. This style fits very well with our project as our whole project is dependent on a database and our application interface operates on the database (repository).<br>
- The diagram above depicts how our architecture will function. Our application stores all of the food’s inventory information into a database (our repository). The application then interacts and operates on the database to manipulate and change the information within it. We also plan to have backups of the database per day for comparison.