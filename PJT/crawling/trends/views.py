from django.shortcuts import render, redirect
from .forms import KeywordForm
from .models import Keyword, Trend
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Create your views here.
def index(request):
    return render(request, 'base.html')

def keyword(request):
    keywords = Keyword.objects.all()
    if request.method == "POST":
        form = KeywordForm(request.POST)
        form.save()
        return redirect('trends:keyword')
    else:
        form = KeywordForm()
    context = {
        'form' : form,
        'keywords' : keywords,
    }
    return render(request, 'trends/keyword.html', context)


def delete_keyword(request, pk):
    keyword = Keyword.objects.get(pk=pk)
    keyword.delete()
    return redirect('trends:keyword')


def crawling(request):
    keywords = Keyword.objects.all()
    result = []
    for keyword in keywords:      
        url = f"https://www.google.com/search?q={keyword.name}"
        # 크롬 브라우저가 열린다. 이 때, 동적인 내용들이 모두 채워짐
        driver = webdriver.Chrome()
        driver.get(url)

        # 열린 페이지 소스를 받아옴
        html = driver.page_source 
        soup = BeautifulSoup(html, "html.parser")

        # div 태그 중 id 가 result-stats 인 요소 검색
        result_stats = soup.select_one("div#result-stats")
        string_data = result_stats.text.split()[-2][:-1]
        result = int(string_data.replace(',', ''))

        if Trend.objects.filter(name=keyword.name, search_period="all").exists():
            trend = Trend.objects.get(name=keyword.name, search_period="all")
            trend.result = result
            trend.save()
        else:
            Trend.objects.create(name=keyword.name, result=result, search_period="all")
    
    trends = Trend.objects.filter(search_period="all")
    context = {
        'trends': trends
    }
    return render(request, 'trends/crawling.html', context)

import matplotlib.pyplot as plt
plt.switch_backend("Agg")
import base64
from io import BytesIO

def histogram(request):
    trends = Trend.objects.filter(search_period="all")
    x = []
    y = []

    for trend in trends:
        x.append(trend.name)
        y.append(trend.result)

    plt.clf()

    plt.figure(figsize=(10, 6))
    plt.bar(x, y, label='Trends')

    plt.xticks(rotation=45)
    plt.xlabel('Keyword')
    plt.ylabel('Result')
    plt.title('Technology Trend Analysis')
    plt.legend()
    plt.grid(True)

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')
    buffer.close()

    context = {
        'chart_img' : f'data:image/png;base64,{image_base64}'
    }
    return render(request, 'trends/histogram.html', context)

def advanced(request):
    keywords = Keyword.objects.all()
    result = []
    for keyword in keywords:
        url = f"https://www.google.com/search?q={keyword.name}&tbs=qdr:y"

        driver = webdriver.Chrome()
        driver.get(url)

        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        result_stats = soup.select_one("div#result-stats")
        string_data = result_stats.text.split()[-2][:-1]
        result = int(string_data.replace(',', ''))

        if Trend.objects.filter(name=keyword.name, search_period="year").exists():
            trend = Trend.objects.get(name=keyword.name, search_period="year")
            trend.result = result
            trend.save()
        else:
            Trend.objects.create(name=keyword.name, result=result, search_period="year")
    trends = Trend.objects.filter(search_period="year")
    x = []
    y = []

    for trend in trends:
        x.append(trend.name)
        y.append(trend.result)

    plt.clf()

    plt.figure(figsize = (10, 6))
    plt.bar(x, y, label="Trends")

    # plt.xticks(rotation=45)
    plt.xlabel('Keyword')
    plt.ylabel('Result')
    plt.title('Technology Trend Analysis')
    plt.legend()
    plt.grid(True)

    buffer = BytesIO()
    plt.savefig(buffer, format='png')

    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')
    buffer.close()

    context = {
        'chart_img' : f'data:image/png;base64,{image_base64}',
    }
    return render(request, 'trends/advanced.html', context)