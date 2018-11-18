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
