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
            instructions = step['html_instructions']
            distance = step['distance']['text']
            duration = step['duration']['text']
            travel_mode = step['travel_mode']

            print(f"\n{instructions} ({distance}, {duration})")

            if travel_mode == 'TRANSIT':
                transit_details = step['transit_details']
                line_name = transit_details['line']['name']
                vehicle_type = transit_details['line']['vehicle']['type']
                departure_stop = transit_details['departure_stop']['name']
                arrival_stop = transit_details['arrival_stop']['name']
                num_stops = transit_details['num_stops']

                print(f"  - 電車名: {line_name}")
                print(f"  - 乗り物タイプ: {vehicle_type}")
                print(f"  - 出発駅: {departure_stop}")
                print(f"  - 到着駅: {arrival_stop}")
                print(f"  - 停車駅数: {num_stops}")

    else:
        print("ルートを取得できませんでした。")

# 開始駅と到着駅を入力
origin = "Machida Station, Tokyo, Japan"
destination = "Kumano Hongu Onsen, Wakayama, Japan"

# 最適な乗換案内を取得
get_directions(origin, destination)
