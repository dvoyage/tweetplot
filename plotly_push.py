import os
import sys
import csv
import datetime
import time
import twitter
import plotly.plotly as py
import plotly.graph_objs as go

def plotly():

	with open('/var/www/data.csv') as f:
		reader = csv.reader(f)
		dates = []
		pings = []
		DL = []
		UL = []
		for row in reader:
			dates.append(row[0])
			pings.append(row[1])
			DL.append(row[2])
			UL.append(row[3])

	f.close()

	Download = go.Scatter(
            x = dates,
            y = DL,
            mode = 'lines+markers',
            name = 'Mb/s Download'
        )
        Ping = go.Scatter(
            x = dates,
            y = pings,
            mode = 'lines+markers',
            name = 'Pingtimes'
        )
        Upload = go.Scatter(
            x = dates,
            y = UL,
            mode = 'lines+markers',
            name = 'Mb/s Upload'
        )
        data = [Download,Ping,Upload]
        py.plot(data, filename='Fios Fail')

        filename='Fios Fails',      # name of the file as saved in your plotly account
        sharing='public'            # 'public' | 'private' | 'secret': Learn more: https://plot.ly/python/privacy

if __name__ = '__main__':
	plotly()
	print('completed')
