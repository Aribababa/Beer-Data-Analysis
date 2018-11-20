# Beer Data Analysis

*Data analysis applied to a set of crafted beer to measure a variety of parameters as correlation between the styles, IBU scale, Color and Pitch Rate. All the data were obtained from Brewer´s Friends web page [more info](https://www.brewersfriend.com/).*

## Data Context
This is a dataset of 75,000 homebrewed beers with over 176 different styles. Beer records are user-reported and are classified according to one of the 176 different styles. These recipes go into as much or as little detail as the user provided, but there's are least 5 useful columns where data was entered for each: Original Gravity, Final Gravity, ABV, IBU, and Color.

<p align="center">
  <img src="https://static.vinepair.com/wp-content/uploads/2015/08/craft-beer-definition-inside-header.jpg">
</p>

## Importing the libraries
I will be using this libraries to make the analysis. In this case all the data was stored in a MondoDB, but all the Processing is based on Pandas dataframe. The advatnage here is that you can edit the Visualization file to charge the CSV file is you do not want to set the database.

```python
import numpy as np
import pandas as pd
import missingno as msno
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(color_codes=True)
```
All the libraries can be downloaded using the pip command from Python.

## Mounting the Database

To mount the .CSV file in the Database you can use the function load_csv_file() where the parameters to run this funciotn are:
```python
    def load_csv_file(self, csv_file, setname, init_line, final_line):
        """
        Load a csv file to the database

        :param csv_file: CSV file
        :param setname: Collection Name
        :param init_line: init line of the csv file
        :param final_line: fianl line of the csv file
        :return: None
        """
```
Here is an example of how to use this function to load all the lines from a csv file.
```python
COLLECTION_NAME = "Crafted-Beer-"
COLLECTION_LIMIT = 32
indexer = 0

for i in range(0, COLLECTION_LIMIT):
	load_csv_file("file.csv", COLLECTION_NAME + str(i), indexer, indexer+1000)
	indexer += 1000
```

## Running the project.
Once you have the Database, Just simply run main.py and be sure that all the python files are in the same folder (I reccomend you to mantain the folder structure usen in the repository).

    ../Scripts> python main.py
    
   All the results are saved in the result folder, but if you want to change this route, there is a variable where you can change the parameter to set a new route
```python
   visualization = DataVisualization(path="../Results", categoty="Crafted beer")
```
Also for the Database, if you dont have a local MongoDB server, you can change the IP and the name of the database. If in the server there is no a DB called as the parameter, then it will be created.
```python
crafted_beer_db = MongoDatabase('mongodb://localhost:27017/', 'Artisanal-beer')
```
## Future work.

 -   From our data You can make selections of a beer from the unique characteristics of each style, I think that for this case a clustering technique could be useful.
