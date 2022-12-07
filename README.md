# DataSciencesProject
# Introduction
   The objective of this project was to determine what types of deaths are increasing and what types are decreasing. To do this I imported my data set: "annual_deaths_by_causes.csv" and used numpy, pandas and matplotlib to create visulaizations for my findings. Before doing this project, I predicted the following; Deaths caused by diseases would have a steady decline because of advancement of technology. Deaths due to natural causes would increase because people live longer as time goes on. Deaths by car crashes would decrease due to the betterment of car safety technology. Deaths by drug use would go down. And finally, deaths by violence and terrorist attacks would go up
# Selection of Data
  The data used in this project can be found on kaggle listed: "World Deaths and Causes [1990 - 2020]". This csv file is comprised of every countries death statistics from 1990 to 2020. The columns consist of: "country", "code", "year", then 33 causes of death. "Code" meaning a 3 character string that represents the country. Then there is 7273 rows of data. 
  Data Preview:![image](https://user-images.githubusercontent.com/71041789/206055538-a1563e4e-66cb-4b45-9686-0f7c8a7d5fea.png)
To clean the data I simply created it into a dataframe and copied that dataframe multiple times for all my uses. In all dataframes I removed the "code" column. I also removed the year column. I also cleaned the data by clearing out all the "NaN" values from the dataset.
# Methods
Tools:
  - Numpy
  - Pandas
  - Matplotlib(also style)
  - VS Code as my IDE
#
Main Methods Used:
  - Pandas Dataframes
      - drop()
      - describe()
      - mean()
      - groupby()
  - matplotlib plotting
      - .plot()
      - savefig()

# Results
  The following are the resulting graphs from the code:
![image](https://user-images.githubusercontent.com/71041789/206060092-0510a8ef-6524-4167-bead-69c19b8b6080.png)
![image](https://user-images.githubusercontent.com/71041789/206061031-a4fbab16-bb20-42cb-ac53-9ecefb350854.png)
![image](https://user-images.githubusercontent.com/71041789/206061078-1871862b-aeb2-44a2-b826-ae695d4e8be2.png)
![image](https://user-images.githubusercontent.com/71041789/206061109-30c2d7f0-ae4d-4400-a676-06938e0fed5e.png)
![image](https://user-images.githubusercontent.com/71041789/206061142-5c41fafb-30cf-410a-8254-c3d53d554598.png)
![image](https://user-images.githubusercontent.com/71041789/206061175-6100c6b6-f864-4f2b-9f49-160a2d14c7d6.png)
![image](https://user-images.githubusercontent.com/71041789/206061202-40783014-5276-49e9-8640-4babb95a5345.png)
![image](https://user-images.githubusercontent.com/71041789/206061232-8b4f9c68-4923-4897-b046-d39dca69f140.png)

# Discussion
The only graph that is incorrect is the violence graph. The terrorism line drops down to 0 in a couple of places. This might be because of incorrect values under the terrorism column of the data. Using .dropna() did not solve this problem. In the future I could of had more graphs on death statistics based on countries. I also would like to do more on each countries death statistics. I would like to have a graph with all the countries overlayed but in a way where it was not cluttered.
Any data on country specific graphs I would like to do.

# Summary
Overall my hypothosis was very close to the final results. Death by old age either stayed stagnant or increased. Heart attack and cancer deaths also increased which is in line as well. Deaths from car collisions decreased. Drug overdose had a steady, slight increase. Although overall violence either stayed stagnant or decreased slightly which was suprising to me. It also makes sense that self harm stayed the same the entire time.

# References
[Kaggle Data Set](https://www.kaggle.com/datasets/madhurpant/world-deaths-and-causes-1990-2019)
