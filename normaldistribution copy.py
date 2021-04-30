import plotly.figure_factory as ff
import pandas as pd
import csv 
import statistics
df=pd.read_csv("student.csv")
reading_list=df["reading"].tolist()
mean=statistics.mean(reading_list)
mode=statistics.mode(reading_list)
median=statistics.median(reading_list)
sd=statistics.stdev(reading_list)
print(mean)
print(mode)
print(median)
print(sd)
reading_first_std_deviation_start, reading_first_std_deviation_end = mean-sd, mean+sd
reading_second_std_deviation_start, reading_second_std_deviation_end = mean-(sd*2),mean+(sd*2)
reading_third_std_deviation_start, reading_third_std_deviation_end = mean-(sd*3),mean+(sd*3)
print(reading_first_std_deviation_end)
print(reading_second_std_deviation_end)
print(reading_third_std_deviation_end)
#fig=ff.create_distplot([df["reading(Inches)"].tolist()],["reading"],show_hist=True)
#fig.show()