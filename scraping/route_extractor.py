#HTMLから電車のルート情報（駅名・時刻・列車名・運賃・所要時間）を抽出して、JSON形式の辞書にまとめるコード

from bs4 import BeautifulSoup

# 取得したHTML（仮）
html = '''
<dt>
    <a href="/station/25850">江坂</a>
</dt>
<ul class="time">
    <li>12:17</li>  <!-- 出発時刻 -->
</ul>
<li class="transport">
  <div>
    "OsakaMetoro御堂筋線"<span class="destination"> なかもず行</span>
  </div>
</li>
<dt>
    <a href="/station/26238">淀屋橋</a>
</dt>
<ul class="time">
    <li>12:31</li>  <!-- 到着時刻 -->
    <li>12:35</li>  <!-- 発車時刻 -->
</ul>

<li class="transport">
  <div>
    "京阪本線準急"<span class="destination">" 出町柳行"</span>
  </div>
</li>
<dt>
    <a href="/station/25901">京橋(大阪府)</a>
</dt>
<ul class="time">
    <li>12:45</li>  <!-- 到着時刻 -->
</ul>
<ul class="summary">
    <li class="time">
        28
    </li>
</ul>
<li class="fare">
  "460"
</li>
<li class="transport">
  <div>
    "京阪本線準急"
    <span class="destination">"出町柳行"</span>
  </div>
</li>
'''

# BeautifulSoupでパース
soup = BeautifulSoup(html, "html.parser")

# 駅名と時刻と列車名を取得
stations = soup.find_all("dt")
times_list = soup.find_all("ul", class_="time")
trains_name = soup.find_all("li", class_="transport")

#全体の所要時間と運賃を取得
total_time_elment = soup.find("li", class_="time")
fare_element = soup.find("li", class_="fare")

fare = fare_element.text.strip() if fare_element else None
total_time = total_time_elment.text.strip().split(" ")[0] #28分だけを取得

# 駅ごとのデータを格納するリスト
route_info = []

# 駅ごとにデータを整理
for station, times, train in zip(stations, times_list, trains_name):
    station_name = station.find("a").text  # 駅名
    time_list = [time.text for time in times.find_all("li")]  # 時刻リスト
    train_name = train.find("div").text.strip() #列車名

    if len(time_list) == 1: 
        route_info.append({
            "station": station_name,
            "arrival": None if not route_info else time_list[0],
            "departure": time_list[0]if not route_info else None,
            "train_name": train_name if not route_info else None
        })
    elif len(time_list) == 2:  
        route_info.append({
            "station": station_name,
            "arrival": time_list[0],
            "departure": time_list[1],
            "train_name": train_name
        })

#最後の駅の列車名をNoneにする(降りるだけなので)
route_info[-1]["train_name"] = None


result = {
    "fare": fare,
    "total_time": total_time,
    "route_info": route_info,
}

print(result)
