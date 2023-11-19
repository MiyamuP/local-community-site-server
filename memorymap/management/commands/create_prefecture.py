from django.core.management.base import BaseCommand
from memorymap.models import Prefecture

class Command(BaseCommand):
    help = 'Creates 47 prefectures in the database'

    def handle(self, *args, **options):
        prefectures_data = [
            {"prefecture_name": "北海道", "prefecture_id": 1, "lat":43.06417 , "lon":141.34694},
            # {"prefecture_name": "青森", "prefecture_id": 2},
            # {"prefecture_name": "岩手", "prefecture_id": 3},
            # {"prefecture_name": "宮城", "prefecture_id": 4},
            # {"prefecture_name": "秋田", "prefecture_id": 5},
            # {"prefecture_name": "山形", "prefecture_id": 6},
            # {"prefecture_name": "福島", "prefecture_id": 7},
            # {"prefecture_name": "茨城", "prefecture_id": 8},
            # {"prefecture_name": "栃木", "prefecture_id": 9},
            # {"prefecture_name": "群馬", "prefecture_id": 10},
            # {"prefecture_name": "埼玉", "prefecture_id": 11},
            # {"prefecture_name": "千葉", "prefecture_id": 12},
            {"prefecture_name": "東京", "prefecture_id": 13, "lat":35.6895 , "lon":139.6917},
            # {"prefecture_name": "神奈川", "prefecture_id": 14},
            # {"prefecture_name": "新潟", "prefecture_id": 15},
            # {"prefecture_name": "富山", "prefecture_id": 16},
            # {"prefecture_name": "石川", "prefecture_id": 17},
            # {"prefecture_name": "福井", "prefecture_id": 18},
            # {"prefecture_name": "山梨", "prefecture_id": 19},
            # {"prefecture_name": "長野", "prefecture_id": 20},
            # {"prefecture_name": "岐阜", "prefecture_id": 21},
            # {"prefecture_name": "静岡", "prefecture_id": 22},
            # {"prefecture_name": "愛知", "prefecture_id": 23},
            # {"prefecture_name": "三重", "prefecture_id": 24},
            # {"prefecture_name": "滋賀", "prefecture_id": 25},
            # {"prefecture_name": "京都", "prefecture_id": 26},
            {"prefecture_name": "大阪", "prefecture_id": 27, "lat": 34.6937, "lon":135.5023 },
            # {"prefecture_name": "兵庫", "prefecture_id": 28},
            # {"prefecture_name": "奈良", "prefecture_id": 29},
            # {"prefecture_name": "和歌山", "prefecture_id": 30},
            # {"prefecture_name": "鳥取", "prefecture_id": 31},
            # {"prefecture_name": "島根", "prefecture_id": 32},
            # {"prefecture_name": "岡山", "prefecture_id": 33},
            # {"prefecture_name": "広島", "prefecture_id": 34},
            # {"prefecture_name": "山口", "prefecture_id": 35},
            # {"prefecture_name": "徳島", "prefecture_id": 36},
            # {"prefecture_name": "香川", "prefecture_id": 37},
            # {"prefecture_name": "愛媛", "prefecture_id": 38},
            # {"prefecture_name": "高知", "prefecture_id": 39},
            # {"prefecture_name": "福岡", "prefecture_id": 40},
            # {"prefecture_name": "佐賀", "prefecture_id": 41},
            # {"prefecture_name": "長崎", "prefecture_id": 42},
            # {"prefecture_name": "熊本", "prefecture_id": 43},
            # {"prefecture_name": "大分", "prefecture_id": 44},
            # {"prefecture_name": "宮崎", "prefecture_id": 45},
            # {"prefecture_name": "鹿児島", "prefecture_id": 46},
            # {"prefecture_name": "沖縄", "prefecture_id": 47},
        ]

        for data in prefectures_data:
            prefecture = Prefecture(**data)
            prefecture.save()

        self.stdout.write(self.style.SUCCESS('Successfully created 47 prefectures.'))