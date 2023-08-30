


## Project Requirements

- [Project Requirements](https://my.learn.co/courses/653/pages/phase-3-project-cli?module_item_id=95439)

### Minimum Requirements:

* A CLI application that solves a real-world problem and adheres to best practices.
* A database created and modified with SQLAlchemy ORM with 2+ related tables.
* A well-maintained virtual environment using Pipenv.
* Proper package structure in your application.
* Use of lists and dicts.

### Stretch Goals:

* A database created and modified with SQLAlchemy ORM with 3+ related tables.
* Use of many-to-many relationships with SQLAlchemy ORM.
* Use of additional data structures, such as ranges and tuples.


## Project Proposals

### Idea 1

#### Main idea: 
Nail Salon Inventory Tracker 

#### User story: 
The Nail Salon Inventory Tracker would be an ADMIN tool where those with ADMIN Perms would be able to access the CLI and select between a couple options, for instance, 'View Current Inventory'; 'Add Inventory'; 'Running Low/Order ASAP'


#### How I will use the concepts I recently learned to meet the project requirements:

- Object Oriented Python - Each Product in Inventory will be an Object 

-  Database Tables & Object Relationships - Inventory table (name, price, quantity, id); name 'nail polisher' will have their own table (type, color, brand) and so will 'nail tips' (type, size, shape) 

- Aggregate and Association Methods - Hopefully I can successfully have an add inventory method, and get low inventory method as well

- Use of Data Structures - lists to store items from the database & dictionaries to store low inventory items 

#### What area I think will be most challenging: 
Probably making sure that the inventory updates correctly for existing and new products as well as making sure that the CLI connects as a whole.


### Idea 2

#### Main idea: 
Bowling Software 

#### User story: 
The program would have a sign in/up option and keeps track of player table (name, age - must be over X years if an adult is not present, shoe size, score) where score table is a foreign key with points per round attribute

#### How I will use the concepts I recently learned to meet the project requirements:

- Object Oriented Python - Each player would be an object 
- Database Tables & Object Relationships - 2 database tables: player table & score table where score would be the foreign key to player table 
- Aggregate and Association Methods - update player points; start over; new match 
- Use of Data Structures - Lists could be used to store player data or round scores. Dictionaries might be useful for organizing and manipulating specific data points.

#### What area I think will be most challenging: 
Making sure that the methods work properly






