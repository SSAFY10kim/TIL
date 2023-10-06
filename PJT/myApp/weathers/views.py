from django.shortcuts import render
import pandas as pd
import matplotlib.pyplot as plt
plt.switch_backend('Agg')

csv_path = 'weathers/data/austin_weather.csv'

def example(request):
    x = [1, 2, 3, 4, 5]
    y = [1, 2, 3, 4, 5]

    # 그래프 초기화
    plt.clf()

    # plot 생성
    plt.plot(x, y)
    plt.title('Test Graph')
    plt.xlabel('x label')
    plt.ylabel('y label')
    plt.grid(True)

    # 그래프 이미지를 임시로 저장할 버퍼 생성
    buffer = BytesIO()
    # 그래프를 버퍼에 저장. 이미지 형식은 png 로 설정
    plt.savefig(buffer, format='png')
    # 버퍼의 내용을 base64 로 인코딩
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')
    buffer.close()

    context = {
        # 저장된 이미지의 경로
        'chart_image': f'data:image/png;base64,{image_base64}',
    }
    return render(request, 'example.html', context)


def problem1(request):
    df = pd.read_csv(csv_path)
    context = {
        'df': df
    }
    return render(request, 'problem1.html', context)

import base64
from io import BytesIO

def problem2(request):
    df = pd.read_csv(csv_path)
    dates = pd.to_datetime(df['Date'])  # 'Date' 컬럼을 날짜 형식으로 변환
    temp_high = df['TempHighF']
    temp_avg = df['TempAvgF']
    temp_low = df['TempLowF']

    # 그래프 초기화
    plt.clf()

    
    # 큰 그림 생성
    plt.figure(figsize=(10, 6))  # 원하는 크기로 수정 (가로 10, 세로 6)

    # 선 그래프 그리기
    plt.plot(dates, temp_high, label='High Temperature')
    plt.plot(dates, temp_avg, label='Average Temperature')
    plt.plot(dates, temp_low, label='Low Temperature')

    # 축과 범례 설정
    plt.xlabel('Date')
    plt.ylabel('Temperature (Fahrenheit)')
    plt.title('Temperature Variation')
    plt.legend()
    plt.grid(True)

    # django view 에서 이미지 형식의 데이터를 직접 전송할 수 없음
    # 버퍼로 저장 -> template 으로 전송해야함
    # BytesIO(): 그래프 이미지를 임시로 저장할 버퍼
    buffer = BytesIO()
    # 그래프를 버퍼에 저장. 이미지 형식은 png 로 설정
    plt.savefig(buffer, format='png')
    # 버퍼의 내용을 base64 로 인코딩
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')
    # data:image/png;base64:
    buffer.close()

    context = {
        'chart_image': f'data:image/png;base64,{image_base64}',
    }
    return render(request, 'problem2.html', context)


def problem3(request):
    df = pd.read_csv(csv_path)
    # 사용할 필드만 가져오기
    df = df[['Date', 'TempHighF', 'TempAvgF', 'TempLowF']]
    df['Date'] = pd.to_datetime(df['Date'])  # 'Date' 컬럼을 날짜 형식으로 변환
    
    # 평균값 계산이 가능하도록 타입을 변환
    df['TempHighF'] = pd.to_numeric(df['TempHighF'])
    df['TempAvgF'] = pd.to_numeric(df['TempAvgF'])
    df['TempLowF'] = pd.to_numeric(df['TempLowF'])

    # 월 별 평균값 계산
    monthly_data = df.groupby(df['Date'].dt.to_period('M')).mean()

    # 월별 데이터
    months = monthly_data['Date']
    temp_high = monthly_data['TempHighF']
    temp_avg = monthly_data['TempAvgF']
    temp_low = monthly_data['TempLowF']

    # 그래프 초기화
    plt.clf()

    # 선 그래프 그리기
    # 큰 그림 생성
    plt.figure(figsize=(10, 6))  # 원하는 크기로 수정 (가로 10, 세로 6)
    plt.plot(months, temp_high, label='High Temperature')
    plt.plot(months, temp_avg, label='Average Temperature')
    plt.plot(months, temp_low, label='Low Temperature')

    # 축과 범례 설정
    plt.xticks(rotation=45)  # x 축 레이블 45도 회전
    plt.xlabel('Date')
    plt.ylabel('Temperature (Fahrenheit)')
    plt.title('Temperature Variation')
    plt.legend()
    plt.grid(True)

    # django view 에서 이미지 형식의 데이터를 직접 전송할 수 없음
    # 버퍼로 저장 -> template 으로 전송해야함
    # BytesIO(): 그래프 이미지를 임시로 저장할 버퍼
    buffer = BytesIO()
    # 그래프를 버퍼에 저장. 이미지 형식은 png 로 설정
    plt.savefig(buffer, format='png')
    # 버퍼의 내용을 base64 로 인코딩
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')
    # data:image/png;base64:
    buffer.close()

    context = {
        'chart_image': f'data:image/png;base64,{image_base64}',
    }
    return render(request, 'problem3.html', context)

def problem4(request):
    df = pd.read_csv(csv_path)

    # 결측치 처리 - 한 칸 띄워쓰기로 되어있음
    df['Events'] = df['Events'].replace(' ', 'No Events')

    # 분리된 다중값을 단일 값으로 변환하여 카운트
    # 다중값 - 쉼표(,) 좌우로 공백이 들어가 있어 아래와 같이 split 하여 계산
    event_counts = df['Events'].str.split(' , ').explode().value_counts()

    # 그래프 초기화
    plt.clf()

    plt.bar(event_counts.index, event_counts.values)
    plt.xlabel('Events')
    plt.ylabel('Count')
    plt.title('Event Counts')
    # plt.xticks(rotation=45)  # x축 레이블 회전
    plt.legend()
    plt.grid(True)

    # django view 에서 이미지 형식의 데이터를 직접 전송할 수 없음
    # 버퍼로 저장 -> template 으로 전송해야함
    # BytesIO(): 그래프 이미지를 임시로 저장할 버퍼
    buffer = BytesIO()
    # 그래프를 버퍼에 저장. 이미지 형식은 png 로 설정
    plt.savefig(buffer, format='png')
    # 버퍼의 내용을 base64 로 인코딩
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')
    # data:image/png;base64:
    buffer.close()

    context = {
        'chart_image': f'data:image/png;base64,{image_base64}',
    }
    return render(request, 'problem4.html', context)
