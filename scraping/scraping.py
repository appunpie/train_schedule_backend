# 出発駅と到着駅を受け取ってスクレイピングするコード（サイト：Yahoo!路線情報）

import requests
from bs4 import BeautifulSoup

departure_station = input("出発駅を入力: ")
arrival_station = input("到着駅を入力: ")

# URLを動的に作成
url = f"https://transit.yahoo.co.jp/search/result?from={departure_station}&to={arrival_station}"

# HTML取得 & パース
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# 駅名、時刻、列車名を取得
stations = soup.find_all("dt")
times_list = soup.find_all("ul", class_="time")
trains_name = soup.find_all("li", class_="transport")

# 全体の所要時間と運賃を取得
total_time_element = soup.find("li", class_="time")
fare_element = soup.find("li", class_="fare")

fare = fare_element.text.strip() if fare_element else None
total_time = total_time_element.text.strip() if total_time_element else None

# 駅ごとのデータを格納するリスト
route_info = []

# 駅名の取得ロジック修正
station_names = []
for station in stations:
    a_tag = station.find("a")  # <a>タグを探す
    if a_tag:  # aタグがある場合のみ
        station_names.append(a_tag.text.strip())  # 駅名を取得

# データ整理
for idx, (station_name, times, train) in enumerate(zip(station_names, times_list, trains_name)):

    time_list = [time.text.strip() for time in times.find_all("li")]  # 時刻リスト
    train_name = train.find("div").text.strip() if train.find("div") else None  # 列車名

    # 出発駅（最初の駅）
    if idx == 0:
        route_info.append({
            "station": station_name,
            "arrival": None,
            "departure": time_list[0] if time_list else None,
            "train_name": train_name
        })
    # 到着駅（最後の駅）
    elif idx == len(station_names) - 1:
        route_info.append({
            "station": station_name,
            "arrival": time_list[0] if time_list else None,
            "departure": None,
            "train_name": None  # 降りるだけなので列車名なし
        })
    # 途中駅
    else:
        route_info.append({
            "station": station_name,
            "arrival": time_list[0] if len(time_list) > 0 else None,
            "departure": time_list[1] if len(time_list) > 1 else None,
            "train_name": train_name
        })

# 結果を辞書にまとめる
result = {
    "fare": fare,
    "total_time": total_time,
    "route_info": route_info,
}

# 結果を出力
print(result)
