from flask import Flask, render_template, request, redirect

# imports for Bokeh plotting
from bokeh.plotting import figure
from bokeh.embed import file_html, components
import pandas as pd
from pandas import DataFrame
import numpy as np

TOOLS="resize,pan,wheel_zoom,box_zoom,reset,tap,previewsave,box_select,poly_select,lasso_select"
app = Flask(__name__)

app.vars={}
app.selected = []

@app.route('/')
def main():
  return redirect('/index')

@app.route('/index',methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template('layout.html')
    else:
        # request was a POST
        app.vars['ticker_symbol'] = request.form['ticker_info']
        #app.vars['closing_price'] = 'off'
        #app.vars['closing_price'] = request.form['close_price']
        #app.vars['adj_closing_price'] = request.form['adj_closingPrice']
        #app_lulu.vars['age'] = request.form['age_lulu']
        app.selected = request.form.getlist('choices')
        f = open('%s.txt'%(app.vars['ticker_symbol'],),'w')
        f.write('Ticker symbol: %s\n'%(app.vars['ticker_symbol']))
        if bool(app.selected):
            f.write('\n'.join(app.selected))
        f.close()
        return redirect('/graph')


#def index():
#  return render_template('index.html')
@app.route('/graph', methods=['GET','POST'])
def Plot1():
    if request.method == 'POST':
        return redirect(url_for('index'))
    ticker_sym = app.vars['ticker_symbol'].upper()
    num = len(app.selected)
    # link to the download data
    url = 'https://www.quandl.com/api/v3/datasets/WIKI/' + ticker_sym + \
          '/data.csv?start_date=2014-12-01'
    df = pd.read_csv(url, parse_dates = ['Date'])
    
    # create a new plot with default tools, using figure
    graph_title = 'From Quandle WIKI - ' + ticker_sym + ' in the past year'
    plot = figure(tools=TOOLS, title=graph_title, x_axis_label='date', y_axis_label='price', x_axis_type='datetime', plot_width=700, plot_height=500)
    # plot the requested features
    if 'closing_price' in app.selected:
        plot.line(df['Date'], df['Close'], legend="Closing price", color='red', alpha=0.5, line_width=3)
    if 'adj_closingPrice' in app.selected:
        plot.line(df['Date'], df['Adj. Close'], legend="Adjusted Closing price", color='orange', alpha=0.5, line_width=3)
    if 'open_price' in app.selected:
        plot.line(df['Date'], df['Open'], legend="Open price", color='blue', alpha=0.5, line_width=3)
    if 'adj_open_price' in app.selected:
        plot.line(df['Date'], df['Adj. Open'], legend="Adjusted Open price", color='green', alpha=0.5, line_width=3)
    script, div = components(plot)   
    return render_template('graph.html', ticker=ticker_sym, script=script, div=div)	

if __name__ == '__main__':
  # app.run(port=33507)
    app.debug=True
    app.run()
