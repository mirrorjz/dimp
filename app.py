from flask import Flask, render_template, request, redirect

# imports for Bokeh plotting
from bokeh.plotting import figure
from bokeh.embed import file_html, components
import pandas as pd
from pandas import DataFrame
import numpy as np

TOOLS="resize,pan,wheel_zoom,box_zoom,reset,tap,previewsave,box_select,poly_select,lasso_select"
app = Flask(__name__)



@app.route('/')
def main():
  return redirect('/index')

@app.route('/index')

#def index():
#  return render_template('index.html')

def Plot1():
    # load data from static folder
    filename = 'static/AAPL_past30days.csv' 
    df = pd.DataFrame.from_csv(filename, parse_dates = ['Date'])
    #coord_x = list(df['Close'].values)
    #coord_y = list(df['Close'].values)
    
    # create a new plot with default tools, using figure
    plot = figure(tools=TOOLS, title='From Quandle WIKI - AAPL\'s closing price in past month', x_axis_label='date', y_axis_label='closing price', x_axis_type='datetime', plot_width=700, plot_height=500)
    plot.line(df['Date'], df['Close'], legend="Closing price", color='red', alpha=0.5)
    
    script, div = components(plot)   
    return render_template('graph.html', script=script, div=div)	

if __name__ == '__main__':
  # app.run(port=33507)
    app.debug=True
    app.run()
