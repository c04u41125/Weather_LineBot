from bs4 import BeautifulSoup as bs
import requests

def action(loc):
    res = requests.get("https://weather.com/zh-TW/weather/today/l/"+loc)
    soup = bs(res.text)
    time = soup.find_all("div",class_="CurrentConditions--header--kbXKR")                                          #縣市地點
    temp = soup.find_all("div",class_="Column--temp--1sO_J")                                                           #溫度
    wind = soup.find_all("span",class_="Wind--windWrapper--3Ly7c undefined")                                           #風速
    aqi = soup.find_all("div",class_="AirQuality--col--3I-4C")                                                         #空氣指標
    rain = soup.find_all("span",class_="Column--precip--3JCDO")                                                        #降雨機率
    sit = soup.find_all("div",class_="CurrentConditions--phraseValue--mZC_p")                                          #天氣概況
    basic=str(time[0].h1.text.split(",")[1][1:])
    show_time='當前時間:'+str(time[0].span.text.split(" ")[1])
    ans = f'{basic}\n{show_time}\n溫度 {temp[0].span.text}C\n{rain[2].text}\n空氣品質指標 {aqi[0].text}\n{wind[0].text}\n{sit[0].text}'    # return ans
    return ans
    # print(ans)
# action('6b221b26e046a442e03dc46fbe91d5874c6461afde61187dd4126bddeea1e2aa')
