import csv
import pandas as pd
import plotly.figure_factory as ff
import statistics
import random
import plotly.graph_objects as go

df = pd.read_csv("110classdata.csv")
data = df["average"].tolist()
##fig = ff.create_distplot([data],["average"],show_hist = False)


mean3 = statistics.mean(data)
print("raw mean",mean3)

stdev3 = statistics.stdev(data)
print("raw stdev",stdev3)
## for getting standard deviation and mean for any 100 data from the list
##dataset = []
##for i in range(0,100):
  ##  random_index = random.randint(0,len(data))
    ##value = data[random_index]
    ##dataset.append(value)
##meanrandom = statistics.mean(dataset)
##print(meanrandom)

##stdev2 = statistics.stdev(dataset)
##print(stdev2)

##for i in range(0,500):
  ##  random_index = random.randint(0,len(data))
    ##value = data[random_index]
    ##dataset.append(value)
##meanrandom1 = statistics.mean(dataset)
##print(meanrandom1)

##stdev3 = statistics.stdev(dataset)
##print(stdev3)







def random_set_of_mean(counter):
    dataset = []
    for i in range(0,counter):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    print(mean)
    return mean


def show_fig(mean_list):
    df = mean_list 
    mean = statistics.mean(df)
    fig = ff.create_distplot([df],["average"],show_hist = False)  
    fig.add_trace(go.Scatter(
        x = [mean,mean],
        y = [0,12],
        mode = "lines",
        name = "mean"
    ))

    
    fig.show()


def setup():
    mean_list = []
    for i in range(0,500):
        set_of_mean = random_set_of_mean(100)
        mean_list.append(set_of_mean)
    show_fig(mean_list)
    mean = statistics.mean(mean_list)
    print("mean of sampling distribution",mean)

setup()


def standard_deviation():
    mean_list = []
    for i in range(0,500):
       set_of_mean = random_set_of_mean(100)
       mean_list.append(set_of_mean)
    standard_deviation = statistics.stdev(mean_list)
    print(standard_deviation) 

standard_deviation()