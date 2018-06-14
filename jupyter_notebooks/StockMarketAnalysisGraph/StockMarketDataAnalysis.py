
# coding: utf-8

# In[15]:


import pandas
pandas.core.common.is_list_like = pandas.api.types.is_list_like
from pandas_datareader import data
import datetime
from bokeh.plotting import figure,show, output_file
# import fix_yahoo_finance as yf 
# yf.pdr_override() 

start = datetime.datetime(2017,10,1)
end = datetime.datetime(2018,5,10)

# df=data.get_data_yahoo(tickers="GOOG",start= start, end = end)


df = data.DataReader('AAPL','iex',start,end)
# df.index = df.index.map(lambda x: datetime.datetime.strptime(x,"%Y-%m-%d"))
df.index = pandas.to_datetime(df.index)


# df = data.DataReader('GOOG','iex',start,end)

def inc_dec(c, o):
    if c > o:
        value ="Increase"
    elif c < o:
        value = "Decrease"
    else:
        value = "Equal"
    return value

df["Status"] = [inc_dec(c , o) for c, o in zip(df["close"], df["open"])]

df["Middle"] = (df["open"]+df["close"])/2
df["Height"] = abs(df.close-df.open)


# from bokeh.models import ColumnDataSource
# cds_increase = ColumnDataSource(df[df.Status=="Increased"])
# cds_decrease = ColumnDataSource(df[df.Status=="Decreased"])

# p = figure(x_axis_type='datetime',width=1000, height=300)
# p.title.text = "CandleStick Chart"

# hours_12 = 12*60*60*1000

# p.rect(df.index[df.Status == "Increase"], df.Middle[df.Status=="Increase"],
#       hours_12, df.Height[df.Status == "Increase"], fill_color="green", line_color="black")

# p.rect(df.index[df.Status == "Decrease"], df.Middle[df.Status=="Decrease"],
#       hours_12, df.Height[df.Status == "Decrease"], fill_color="red", line_color="black")

# 

# output_file("CS.html")
# show(p)

# from bokeh.plotting import figure, output_file, show

# plot = figure(plot_width=300, plot_height=300)
# plot.rect(x=[1, 2, 3], y=[1, 2, 3], width=10, height=20, color="#CAB2D6",
#           width_units="screen", height_units="screen")


# show(plot)

# p = figure ( x_axis_type='datetime', width=1000, height=300)
# p.title.text="CandleStick chart"

# hours_12 = 12*60*60*1000

# p.rect(df.index[df.close > df.open], (df.open + df.close)/2, hours_12, abs(df.open-df.close))

# output_file("CS1.html")
# show(p)

p = figure(x_axis_type='datetime',width=1000, height=300, sizing_mode='scale_width')
p.title.text = "CandleStick Chart"
p.grid.grid_line_alpha=0.3 #level of transparency : 0 = completly remove

hours_12 = 12*60*60*1000

p.segment(df.index, df.high, df.index, df.low)
p.rect(df.index[df.Status == "Increase"], df.Middle[df.Status=="Increase"],
      hours_12, df.Height[df.Status == "Increase"], fill_color="#CCFFFF", line_color="black")

p.rect(df.index[df.Status == "Decrease"], df.Middle[df.Status=="Decrease"],
      hours_12, df.Height[df.Status == "Decrease"], fill_color="#F08080", line_color="black")

output_file("CS.html")
show(p)

