import sys
import random
import pandas as pd
#import matplotlib.pyplot as plt
import quandl

from io import BytesIO
from flask import Flask, make_response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

quandl.ApiConfig.api_key = sys.argv[1]

data = quandl.Dataset('WIKI/AMZN').data().to_pandas()

# info on DataFrame
# data.info()
# plot
#close = data['Adj. Close']
#close.plot()
#plt.show()

app = Flask(__name__)

@app.route('/plot.png')
def plot():
  fig = Figure()  
  p = fig.add_subplot(1, 1, 1)
  close = data['Adj. Close']
  p.plot(close)

  canvas = FigureCanvas(fig)
  output = BytesIO()
  canvas.print_png(output)
  response = make_response(output.getvalue())
  response.mimetype = 'image/png'
  return response

if __name__ == '__main__':
  app.run(debug=True)
