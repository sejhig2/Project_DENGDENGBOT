import speech_recognition as sr
import requests
from bs4 import BeautifulSoup
import random
import speak


class speech():
    def __init__(self):

        # microphone에서 auido source를 생성합니다
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)
            global location
            location = r.recognize_google(audio, language='ko')


        # 구글 웹 음성 API로 인식하기 (하루에 제한 50회)
        try:
            print("Google Speech Recognition thinks you said : " + location)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

    #def wetter(location):
        Finallocation = location + "날씨"
        LocationInfo = ""
        NowTemp = ""
        CheckDust = []

        url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=' + Finallocation
        hdr = {'User-Agent': (
            'mozilla/5.0 (windows nt 10.0; win64; x64) applewebkit/537.36 (khtml, like gecko) chrome/78.0.3904.70 safari/537.36')}
        req = requests.get(url, headers=hdr)
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')

        # 오류 확인하기
        ErroCheck = soup.find('span', {'class': 'btn_select'})

        if 'None' in str(ErroCheck):
            print("Error 지명 검색에서 오류났다")
        else:
            # 지역정보
            for i in soup.select('span[class=btn_select]'):
                LocationInfo = i.text

            # 현재 온도 알려주기
            NowTemp = soup.find('span', {'class': 'todaytemp'}).text + soup.find('span', {'class': 'tempmark'}).text[2:]

            # 날씨 캐스트
            WeatherCast = soup.find('p', {'class': 'cast_txt'}).text

            # 내일 오전, 오후 온도 및 상태 확인하기
            tomorrowArea = soup.find('div', {'class': 'tomorrow_area'})
            tomorrowCheck = tomorrowArea.find_all('div', {'class': 'main_info morning_box'})

            # 오늘 오전 온도, 오후 온도, 체감온도도
            TodayMorningTemp = soup.find('span', {'class': 'min'}).text
            TodayAfternoonTemp = soup.find('span', {'class': 'max'}).text
            TodayFeelTemp = soup.find('span', {'class': 'sensible'}).text[5:]
            # 자외전 지수
            TodayUV = soup.find('span', {'class': 'indicator'}).text[4:-2] + " " + soup.find('span', {
                'class': 'indicator'}).text[-2:]

            # 미세먼지, 초 미세먼지, 오존 지수
            CheckDust1 = soup.find('div', {'class': 'sub_info'})
            CheckDust2 = CheckDust1.find('div', {'class': 'detail_box'})
            for i in CheckDust2.select('dd'): CheckDust.append(i.text)
            FineDust = CheckDust[0][:-2] + " " + CheckDust[0][-2:]
            UltraFineDust = CheckDust[1][:-2] + " " + CheckDust[1][-2:]
            Ozon = CheckDust[2][:-2] + " " + CheckDust[2][-2:]

            sagen = ""
            if FineDust[-2:] == "좋음":
                sagen = random.choice(["밖에 나가기 딱이네요", "산책하기 좋겠네요", "공기가 맑을 것 같아요.", "상쾌한 공기가 기다리고 있어요."])
            elif FineDust[-2:] == "보통":
                sagen = random.choice(["밖에 나가는 것도 나쁘지 않겠네요", "바람쐬러 나가기 좋겠네요.", "나들이라도 계획해보시는게 어떠세요?"])
            elif FineDust[-2:] == "나쁨":
                sagen = random.choice(
                    ["공기가 안 좋으니 조심하셔야겠어요", "밖에 나가실거라면 미세먼지 조심하셔야겠어요.", "혹시 모르니 마스크를 챙기시는게 어떨까요?", "폐건강에 유의하셔야겠어요."])
            elif FineDust[-4:] == "매우나쁨":
                sagen = random.choice(["야외 활동을 자제하셔야할 것 같아요.", "밖에 나갈 땐 마스크를 꼭 챙기셔야겠어요.", "공기가 안 좋으니 실내에 계시는게 어떨까요?",
                                       "정말 조심해야할 공기 상태에요."])

            # 내일 오전 상태
            tomorrowMState1 = tomorrowCheck[0].find('div', {'class': 'info_data'})
            tomorrowMState2 = tomorrowMState1.find('ul', {'class': 'info_list'})
            tomorrowMState3 = tomorrowMState2.find('p', {'class': 'cast_txt'}).text
            tomorrowMState4 = tomorrowMState2.find('div', {'class': 'detail_box'})
            tomorrowMState5 = tomorrowMState4.find('span').text.strip()
            tomorrowMState = tomorrowMState3 + " " + tomorrowMState5

            # 내일 오전 오후 온도
            tomorrowArea = soup.find('div', {'class': 'tomorrow_area'})
            tomorrowCheck = tomorrowArea.find_all('div', {'class': 'main_info morning_box'})

            # 내일 오전 온도
            tomorrowMoring1 = tomorrowCheck[0].find('span', {'class': 'todaytemp'}).text
            tomorrowMoring2 = tomorrowCheck[0].find('span', {'class': 'tempmark'}).text[2:]
            tomorrowMoring = tomorrowMoring1 + tomorrowMoring2

            # 내일 오후 온도
            tomorrowAfter1 = tomorrowCheck[1].find('p', {'class': 'info_temperature'})
            tomorrowAfter2 = tomorrowAfter1.find('span', {'class': 'todaytemp'}).text
            tomorrowAfter3 = tomorrowAfter1.find('span', {'class': 'tempmark'}).text[2:]
            tomorrowAfter = tomorrowAfter2 + tomorrowAfter3

            # 내일 오후 상태
            tomorrowAState1 = tomorrowCheck[1].find('div', {'class': 'info_data'})
            tomorrowAState2 = tomorrowAState1.find('ul', {'class': 'info_list'})
            tomorrowAState3 = tomorrowAState2.find('p', {'class': 'cast_txt'}).text
            tomorrowAState4 = tomorrowAState2.find('div', {'class': 'detail_box'})
            tomorrowAState5 = tomorrowAState4.find('span').text.strip()
            tomorrowAState = tomorrowAState3 + " " + tomorrowAState5

            print("=========================================")
            print("안녕하세요 " + LocationInfo + " 날씨를 알려드릴게요.")
            print("=========================================")
            print("현재온도는" + NowTemp + "이고 체감 온도는" + TodayFeelTemp + "에요.\n미세먼지는 현재" + FineDust + "이라고 해요\n" + sagen)
            print("현재온도: " + NowTemp)
            print("체감온도: " + TodayFeelTemp)
            print("오전/오후 온도: " + TodayMorningTemp + "/" + TodayAfternoonTemp)
            print("현재 상태: " + WeatherCast)
            print("현재 자외선 지수: " + TodayUV)
            print("현재 미세먼지 농도: " + FineDust)
            print("현재 초미세먼지 농도: " + UltraFineDust)
            print("현재 오존 지수: " + Ozon)
            print("=========================================")
            print(LocationInfo + " 내일 날씨 정보입니다.")
            print("=========================================")
            print("내일 오전 온도: " + tomorrowMoring)
            print("내일 오전 상태: " + tomorrowMState)
            print("내일 오후 온도: " + tomorrowAfter)
            print("내일 오후 상태: " + tomorrowAState)
            announcement = ("안녕하세요 " + LocationInfo + " 날씨를 알려드릴게요." + "현재온도는" + NowTemp + "도 이고 체감 온도는" + TodayFeelTemp + "에요." + sagen)
            speak.speak(announcement)