from django.shortcuts import render
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import pandas as pd

csv_path = 'weathers/data/austin_weather.csv'
# Create your views here.
def index(request):
    return render(request, 'base.html')

def problem1(request):
    df = pd.read_csv(csv_path)
    context = {
        'df' : df
    }
    return render(request, 'weathers/problem1.html', context)

def problem2(request):
    df = pd.read_csv(csv_path)

    dates = pd.to_datetime(df['Date'])
    temp_high = df['TempHighF']
    temp_avg = df['TempAvgF']
    temp_low = df['TempLowF']
    
    plt.clf()
    plt.figure(figsize=(10, 6))
    plt.plot(dates, temp_high, label='High Temperature')
    plt.plot(dates, temp_avg, label='Average Temperature')
    plt.plot(dates, temp_low, label='Low Temperature')

    plt.title("Temperature Variation")
    plt.xlabel("Date")
    plt.ylabel("Temperature(Fahrenheit)")

    plt.legend()
    plt.grid(True)

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')
    buffer.close()

    context = { 
        'chart_image' : f'data:image/png;base64,{image_base64}'
    }
    return render(request, 'weathers/problem2.html', context)

def problem3(request):
    return render(request, 'weathers/problem3.html')

def problem4(request):
    return render(request, 'weathers/problem4.html')