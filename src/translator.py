
import re
import requests
from bs4 import BeautifulSoup
from typing import Optional


CITY_CHANGE_INDEX = {
    '基隆市': 1,
    '臺北市': 2,
    '新北市': 3,
    '桃園市': 4,
    '新竹市': 5,
    '新竹縣': 6,
    '苗栗縣': 7,
    '臺中市': 8,
    '彰化縣': 9,
    '南投縣': 10,
    '雲林縣': 11,
    '嘉義市': 12,
    '嘉義縣': 13,
    '臺南市': 14,
    '高雄市': 15,
    '屏東縣': 16,
    '臺東縣': 17,
    '花蓮縣': 18,
    '宜蘭縣': 19,
    '澎湖縣': 20,
    '金門縣': 21,
    '連江縣': 22
}

CITY_CITYAREA = {
    "基隆市": ["仁愛區", "信義區", "中正區", "中山區", "安樂區", "暖暖區", "七堵區"],
    "臺北市": ["中正區", "大同區", "中山區", "松山區", "大安區", "萬華區", "信義區", "士林區", "北投區", "內湖區", "南港區", "文山區"],
    "新北市":
    ["萬里區", "金山區", "板橋區", "汐止區", "深坑區", "石碇區", "瑞芳區", "平溪區", "雙溪區", "貢寮區", "新店區", "坪林區", "烏來區", "永和區", "中和區", "土城區",
     "三峽區", "樹林區", "鶯歌區", "三重區", "新莊區", "泰山區", "林口區", "蘆洲區", "五股區", "八里區", "淡水區", "三芝區", "石門區"],
    "桃園市": ["中壢區", "平鎮區", "龍潭區", "楊梅區", "新屋區", "觀音區", "桃園區", "龜山區", "八德區", "大溪區", "復興區", "大園區", "蘆竹區"],
    "新竹市": ["東區", "北區", "香山區"],
    "新竹縣": ["竹北市", "湖口鄉", "新豐鄉", "新埔鎮", "關西鎮", "芎林鄉", "寶山鄉", "竹東鎮", "五峰鄉", "橫山鄉", "尖石鄉", "北埔鄉", "峨眉鄉"],
    "苗栗縣":
    ["竹南鎮", "頭份市", "三灣鄉", "南庄鄉", "獅潭鄉", "後龍鎮", "通霄鎮", "苑裡鎮", "苗栗市", "造橋鄉", "頭屋鄉", "公館鄉", "大湖鄉", "泰安鄉", "銅鑼鄉", "三義鄉",
     "西湖鄉", "卓蘭鎮"],
    "臺中市":
    ["中區", "東區", "南區", "西區", "北區", "北屯區", "西屯區", "南屯區", "太平區", "大里區", "霧峰區", "烏日區", "豐原區", "后里區", "石岡區", "東勢區", "和平區",
     "新社區", "潭子區", "大雅區", "神岡區", "大肚區", "沙鹿區", "龍井區", "梧棲區", "清水區", "大甲區", "外埔區", "大安區"],
    "彰化縣":
    ["彰化市", "芬園鄉", "花壇鄉", "秀水鄉", "鹿港鎮", "福興鄉", "線西鄉", "和美鎮", "伸港鄉", "員林市", "社頭鄉", "永靖鄉", "埔心鄉", "溪湖鎮", "大村鄉", "埔鹽鄉",
     "田中鎮", "北斗鎮", "田尾鄉", "埤頭鄉", "溪州鄉", "竹塘鄉", "二林鎮", "大城鄉", "芳苑鄉", "二水鄉"],
    "南投縣": ["南投市", "中寮鄉", "草屯鎮", "國姓鄉", "埔里鎮", "仁愛鄉", "名間鄉", "集集鎮", "水里鄉", "魚池鄉", "信義鄉", "竹山鎮", "鹿谷鄉"],
    "雲林縣":
    ["斗南鎮", "大埤鄉", "虎尾鎮", "土庫鎮", "褒忠鄉", "東勢鄉", "臺西鄉", "崙背鄉", "麥寮鄉", "斗六市", "林內鄉", "古坑鄉", "莿桐鄉", "西螺鎮", "二崙鄉", "北港鎮",
     "水林鄉", "口湖鄉", "四湖鄉", "元長鄉"],
    "嘉義市": ["東區", "西區"],
    "嘉義縣":
    ["番路鄉", "梅山鄉", "竹崎鄉", "阿里山鄉", "中埔鄉", "大埔鄉", "水上鄉", "鹿草鄉", "太保市", "朴子市", "東石鄉", "六腳鄉", "新港鄉", "民雄鄉", "大林鎮", "溪口鄉",
     "義竹鄉", "布袋鎮"],
    "臺南市":
    ["中西區", "東區", "南區", "北區", "安平區", "安南區", "永康區", "歸仁區", "新化區", "左鎮區", "玉井區", "楠西區", "南化區", "仁德區", "關廟區", "龍崎區", "官田區",
     "麻豆區", "佳里區", "西港區", "七股區", "將軍區", "學甲區", "北門區", "新營區", "後壁區", "白河區", "東山區", "六甲區", "下營區", "柳營區", "鹽水區", "善化區",
     "大內區", "山上區", "新市區", "安定區"],
    "高雄市":
    ["新興區", "前金區", "苓雅區", "鹽埕區", "鼓山區", "旗津區", "前鎮區", "三民區", "楠梓區", "小港區", "左營區", "仁武區", "大社區", "東沙群島", "南沙群島", "岡山區",
     "路竹區", "阿蓮區", "田寮區", "燕巢區", "橋頭區", "梓官區", "彌陀區", "永安區", "湖內區", "鳳山區", "大寮區", "林園區", "鳥松區", "大樹區", "旗山區", "美濃區",
     "六龜區", "內門區", "杉林區", "甲仙區", "桃源區", "那瑪夏區", "茂林區", "茄萣區"],
    "屏東縣":
    ["屏東市", "三地門鄉", "霧臺鄉", "瑪家鄉", "九如鄉", "里港鄉", "高樹鄉", "鹽埔鄉", "長治鄉", "麟洛鄉", "竹田鄉", "內埔鄉", "萬丹鄉", "潮州鎮", "泰武鄉", "來義鄉",
     "萬巒鄉", "崁頂鄉", "新埤鄉", "南州鄉", "林邊鄉", "東港鎮", "琉球鄉", "佳冬鄉", "新園鄉", "枋寮鄉", "枋山鄉", "春日鄉", "獅子鄉", "車城鄉", "牡丹鄉", "恆春鎮",
     "滿州鄉"],
    "臺東縣":
    ["臺東市", "綠島鄉", "蘭嶼鄉", "延平鄉", "卑南鄉", "鹿野鄉", "關山鎮", "海端鄉", "池上鄉", "東河鄉", "成功鎮", "長濱鄉", "太麻里鄉", "金峰鄉", "大武鄉", "達仁鄉"],
    "花蓮縣": ["花蓮市", "新城鄉", "秀林鄉", "吉安鄉", "壽豐鄉", "鳳林鎮", "光復鄉", "豐濱鄉", "瑞穗鄉", "萬榮鄉", "玉里鎮", "卓溪鄉", "富里鄉"],
    "宜蘭縣": ["宜蘭市", "頭城鎮", "礁溪鄉", "壯圍鄉", "員山鄉", "羅東鎮", "三星鄉", "大同鄉", "五結鄉", "冬山鄉", "蘇澳鎮", "南澳鄉", "釣魚臺"],
    "澎湖縣": ["馬公市", "西嶼鄉", "望安鄉", "七美鄉", "白沙鄉", "湖西鄉"],
    "金門縣": ["金沙鎮", "金湖鎮", "金寧鄉", "金城鎮", "烈嶼鄉", "烏坵鄉"],
    "連江縣": ["南竿鄉", "北竿鄉", "莒光鄉", "東引鄉"]
}


def query_gov_postal(
    city: str,
    cityarea: str,
    street: str,
    lane: str = "",
    alley: str = "",
    num: str = "",
    fl: str = ""
) -> str:
    """回傳查詢結果頁面"""
    print(
        city, cityarea, street, lane, alley, num, fl
    )

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'en-US,en;q=0.9,zh-TW;q=0.8,zh;q=0.7,vi-VN;q=0.6,vi;q=0.5',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Origin': 'https://www.post.gov.tw',
        'Referer': 'https://www.post.gov.tw/post/internet/Postal/index.jsp?ID=207',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',

    }

    params = {
        'ID': '207',
    }

    def make_address_payload(
        city: str,
        cityarea: str,
        street: str,
        lane: str = "",
        alley: str = "",
        num: str = "",
        fl: str = ""
    ):
        change_city = CITY_CHANGE_INDEX[city]
        if cityarea not in CITY_CITYAREA[city]:
            raise ValueError(f"{cityarea} is not a valid cityarea in {city}")

        return {
            'do_s_1': '1',
            'vKey': 'bb59e33b-c3d9-4a71-a636-69d61093caa8\r\n',
            'showMode': '1',
            'city': city,
            'change_city': str(change_city),
            'cityarea': cityarea,
            'Street_kind': '1',  # 1: 用選單選的對應到street  2:用輸入的對應到street2
            'street': street,
            'street2': '',
            'lane': lane,
            'alley': alley,
            'num': num,
            'num_hyphen': '',
            'fl': fl,
            'hyphen': '',
            'suite': '',
            'list': 'true',
            'checkImange': '5086',
            'submit': '查詢',
        }

    data = make_address_payload(
        city=city,
        cityarea=cityarea,
        street=street,
        lane=lane,
        alley=alley,
        num=num,
        fl=fl,
    )
    response = requests.post(
        'https://www.post.gov.tw/post/internet/Postal/index.jsp',
        params=params,
        headers=headers,
        data=data
    )
    return response.text


def extract_en_address(html) -> Optional[str]:
    """從html中提取英文地址"""
    soup = BeautifulSoup(html, 'html.parser')
    address = soup.find("table", {"id": "Table6"}).find("td")
    if address:
        return address.text
    else:
        return None


def translate_address(address: str) -> Optional[str]:
    """翻譯地址"""
    # TODO: 把地址拆成縣市鄉鎮...


def test():
    test_cases = [
        {
            "city": "臺北市",
            "cityarea": "信義區",
            "street": "仁愛路四段",
            "num": "505",
        },
        {
            "city": "臺北市",
            "cityarea": "南港區",
            "street": "經貿二路",
            "num": "168",
        },
        {
            "city": "新竹市",
            "cityarea": "東區",
            "street": "力行六路",
            "num": "8",
        },
    ]
    for case in test_cases:
        result_page = query_gov_postal(**case)
        en_addr = extract_en_address(result_page)

        print(re.sub(r"\s+", " ", en_addr).strip())


test()
