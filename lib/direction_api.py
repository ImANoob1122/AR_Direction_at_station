import requests
import datetime

# Google Directions API key
API_KEY = 'YOUR_API_KEY'

def get_directions(origin, destination):
    # 現在の時間を取得
    now = datetime.datetime.now()
    departure_time = int(now.timestamp())  # Unixタイムスタンプに変換

    # Google Directions APIエンドポイント
    endpoint = 'https://maps.googleapis.com/maps/api/directions/json?'

    # パラメータ
    params = {
        'origin': origin,
        'destination': destination,
        'mode': 'transit',  # 電車などの公共交通機関を使用
        'departure_time': departure_time,
        'key': API_KEY
    }

    # APIリクエスト
    response = requests.get(endpoint, params=params)
    directions = response.json()

    # レスポンスの処理
    if directions['status'] == 'OK':
        route = directions['routes'][0]
        leg = route['legs'][0]
        print(f"出発地: {leg['start_address']}")
        print(f"到着地: {leg['end_address']}")
        print(f"移動距離: {leg['distance']['text']}")
        print(f"移動時間: {leg['duration']['text']}")

        for step in leg['steps']:
            print(f"{step['html_instructions']} ({step['distance']['text']}, {step['duration']['text']})")

    else:
        print("ルートを取得できませんでした。")

# 開始駅と到着駅を入力
origin = "Machida Station, Tokyo, Japan"
destination = "Kumano Hongu Onsen, Wakayama, Japan"

# 最適な乗換案内を取得
get_directions(origin, destination)
