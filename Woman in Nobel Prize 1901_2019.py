import pandas as pd
import os
import seaborn as sns
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

#Change working directory
Current_directory = os.getcwd()
Current_directory


nobel = pd.read_csv("nobel_prize_awarded_1901_2019.csv")
nobel.head(5)

#Lets check if we are missing data
nobel.isnull().sum()

#Lets create some visualizations
nobel_cat = nobel.groupby(by=["Category"]).size().reset_index(name="counts")
px.bar(data_frame=nobel_cat, x="Category", y="counts", title="In general categories in which Nobel prize have been received") 

#Nobel count by gender
ByGender = nobel.groupby(by=["Gender"]).size().reset_index(name="counts")
px.bar(data_frame=ByGender, x="Gender", y="counts", title="Nobel Prize won by:")

#Lets see in what category mans have won a prize
ByGender_Man = nobel[nobel["Gender"]=="Man"]
ByGender_Man_count = ByGender_Man.groupby(by=["Category"]).size().reset_index(name="Counts")
px.bar(data_frame=ByGender_Man_count, x="Category", y="Counts", title= "Categories in which a man have received a Nobel Prize")


#Lets see in what category woman have won a prize
ByGender_woman = nobel[nobel["Gender"]=="Woman"]
ByGender_woman_count = ByGender_woman.groupby(by=["Category"]).size().reset_index(name="Counts")
px.bar(data_frame=ByGender_woman_count, x="Category", y="Counts", title= "Categories in which a woman have received a Nobel Prize")

#Countries in which women have won 
ByGender_woman_country = ByGender_woman.groupby(by=["Countries"]).size().reset_index(name="Counts")
px.bar(data_frame=ByGender_woman_country, x="Countries", y="Counts", title= "Categories in which a woman have received a Nobel Prize")

#Lets filter to chile
ByGender_woman[ByGender_woman["Countries"]=="Chile"]



#Lets put side by side man vs woman categories won 
fig = make_subplots(
    rows=1, cols=2,
    subplot_titles=("Categories in which WOMAN have won","Categories in wich a MEN have won")
)
fig.add_trace(go.Bar(x=ByGender_woman_count["Category"],y=ByGender_woman_count["Counts"]),row=1, col=1)
fig.add_trace(go.Bar(x=ByGender_Man_count["Category"],y=ByGender_Man_count["Counts"]),row=1, col=2)

nobel_cat.columns

#Lets do both genders in one 
man_vs_woman = nobel.groupby(by=["Category","Gender"]).size().reset_index(name="counts")
px.bar(data_frame=man_vs_woman, x="Category", y="counts", color="Gender",title= "man vs woman")
