# movies-sqlite-python

The table creation method is dependent on the created movie table, which in turn checks if the movies table already exists. The existing table is dropped and a new table is created with the defined table attributes under the CREATE_TABLE method.
Preparing the data method accepts all inputs for creating the database, and is prepared as a list of all desired rows for table input.
Respectively, the Insert data method inserts the values prepared for the column names.
The retrieving data parameters are passed as inputs from the list for actors to the RETRIEVE_DATA method.
The RETRIEVE_ALL_DATA method fetches all the data present in table MOVIES
