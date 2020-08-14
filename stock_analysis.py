from pandas_datareader import data
from bokeh.models.annotations import Title
import datetime

from bokeh.plotting import figure,show,output_file

start=datetime.datetime(2020,1,30)
end=datetime.datetime(2020,7,30)
hours_12 = 12*60*60*1000  #calculating the miliseconds in 12 hours



df=data.DataReader(name='amzn',data_source='yahoo',start=start,end=end)  #The analyzed entity is Amazon,in the last 6 months


p=figure(x_axis_type='datetime', width=1000,height=300,sizing_mode="scale_width")


t=Title()
t.text="Candlestick Chart"
p.title=t
p.grid.grid_line_alpha=0.6
t.text_font_size="24pt"            # defining the css of the title 
t.align="center"
date_increase = df.index[df.Close>df.Open]
date_decrease = df.index[df.Close<df.Open]
p.segment(df.index,df.High,df.index,df.Low,color="black")
p.rect(date_increase,(df.Close+df.Open)/2, hours_12, abs(df.Open-df.Close),fill_color="green",line_color="black")
p.rect(date_decrease,(df.Close+df.Open)/2, hours_12, abs(df.Open-df.Close),fill_color="red",line_color="black")
output_file("CS.html")
show(p)
# print(df)