import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

plt.style.use("ggplot")

df_complete = pd.read_csv ('annual_deaths_by_causes.csv')
df_transpose_start = df_complete
print(df_complete)
df_transpose_start=df_transpose_start.drop(['year', 'code'],  axis=1)

df_percentages = df_complete
df_transpose = df_transpose_start.transpose()

df_percentages.drop('country', inplace=True, axis=1)
df_percentages.drop('code', inplace=True, axis=1)

basic_numerical_stats = df_complete.dropna().describe()
print(f"Basis Stats: \n{basic_numerical_stats}\n")
file_name = "basic_stats.csv"
basic_numerical_stats.to_csv(file_name, sep='\t', encoding='utf-8')
most_deaths = df_complete.mean()
del most_deaths['year']
most_deaths.to_csv("mean_deaths.csv", sep='\t', encoding='utf-8')

#biggest killer by number
most_deaths.plot(kind='bar', title = "Mean Worldwide Types of Deaths", figsize=(10,10))
plt.savefig('biggest_killers.png')
plt.show()
plt.close()

# transpose data
file_name_t = "basic_stats_transpose.csv"

basic_numerical_stats_t = df_transpose.dropna().describe()
basic_numerical_stats_t.to_csv(file_name_t, sep='\t', encoding='utf-8')
df_transpose['country'] = df_transpose.index

print(df_transpose)

# combine all countries 
df_percentages = df_percentages.set_index('year')
res = df_percentages.div(df_percentages.sum(axis=1), axis=0)
res = res.reset_index().groupby("year").sum()
print(res)
file_name_p = "biggest_killer_percentage.csv"
res.to_csv(file_name_p, sep='\t', encoding='utf-8')


# death by old age
dby_old_age = res[["alzheimer's_diesease", "parkinson's_disease","chronic_respiratory_diseases", "diabetes_mellitus"]]
print(dby_old_age)
dby_old_age.plot(kind='line', title = "Percent of Deaths of Old Age")
plt.savefig('death_by_old_age.png')
plt.show()
plt.close()

# death by violence
dby_violence = res[["interpersonal_violence", "self_harm","conflict_and_terrorism", "terrorism"]]
print(dby_violence)
dby_violence.plot(kind='line', title = "Percent of Deaths caused by Violence")
plt.savefig('death_by_violence.png')
plt.show()
plt.close()

# death by diseases
dby_disease = res[["malaria", "hiv/aids","tuberculosis","diarrheal_diseases","chronic_kidney_disease","chronic_respiratory_diseases","chronic_liver_diseases","digestive_diseases","acute_hepatitis"]]
print(dby_disease)
dby_disease.plot(kind='line', title = "Percent of Deaths caused by Diseases", figsize=(10,10))
plt.savefig('death_by_diseases.png')
plt.show()
plt.close()

# death by car crashes
dby_car_collision = res[["road_injuries"]]
print(dby_car_collision)
dby_car_collision.plot(kind='line', title = "Percent of Deaths by Car Collision")
plt.savefig('death_by_car_collisions.png')
plt.show()
plt.close()

# death by cancer
dby_cancer = res[["neoplasms"]]
print(dby_cancer)
dby_cancer.plot(kind='line', title = "Percent of Deaths by Cancer")
plt.savefig('death_by_cancer.png')
plt.show()
plt.close()

# death by heart attack
dby_heart_attack = res[["cardiovascular_diseases"]]
print(dby_heart_attack)
dby_heart_attack.plot(kind='line', title=" Percent of Deaths by Heart Attack or Stroke")
plt.savefig('death_by_cardiovascular_diseases.png')
plt.show()
plt.close()

# death by drug use
dby_drug_use = res[["drug_use_disorders","alcohol_use_disorders"]]
print(dby_drug_use)
dby_drug_use.plot(kind='line', title=" Percent of Deaths by Drug Use")
plt.savefig('death_by_drug_use.png')
plt.show()
plt.close()

print("done")