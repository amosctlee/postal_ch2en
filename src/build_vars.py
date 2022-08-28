import requests
from bs4 import BeautifulSoup
from typing import List


CITY_OPTIONS: List[str] = None
CITYAREA_ACCOUNT = None
CITYAREA = None


def build_citarea_account():
    '''
    從網站的 js 觀察如何使用 city 來取得 cityarea

        function getCityarea(aa,i){
            alert(aa+":"+i);
            window.document.form1.cityarea.length = cityarea_account[i] - cityarea_account[i-1];
            index = cityarea_account[i-1] + 1;
            for (j = 0; j < window.document.form1.cityarea.length; j ++) {
                window.document.form1.cityarea.options[j].value = cityarea[index + j];
                window.document.form1.cityarea.options[j].text = cityarea[index + j];
                if(aa == window.document.form1.cityarea.options[j].value) window.document.form1.cityarea.options[j].selected = true;
            }
        }
    '''

    global CITYAREA_ACCOUNT
    if CITYAREA_ACCOUNT is not None:
        return
    CITYAREA_ACCOUNT = [
        0, 7, 19, 48, 61, 64, 77, 95,
        124, 150, 163, 183, 185, 203,
        240, 280, 313, 329, 342, 355,
        361, 367, 371, 373
    ]


def build_cityarea():
    '''
    從 js 取得 cityarea 的值
    https://www.post.gov.tw/post/FileCenter/post_ww2/zip_code/UTF8/internet/_city_v2.js

        resp = requests.get(
            'https://www.post.gov.tw/post/FileCenter/post_ww2/zip_code/UTF8/internet/_city_v2.js',
            headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
            }
        )
    '''
    global CITYAREA
    if CITYAREA is not None:
        return
    cityarea = {}
    cityarea[1] = "仁愛區"
    cityarea[2] = "信義區"
    cityarea[3] = "中正區"
    cityarea[4] = "中山區"
    cityarea[5] = "安樂區"
    cityarea[6] = "暖暖區"
    cityarea[7] = "七堵區"
    cityarea[8] = "中正區"
    cityarea[9] = "大同區"
    cityarea[10] = "中山區"
    cityarea[11] = "松山區"
    cityarea[12] = "大安區"
    cityarea[13] = "萬華區"
    cityarea[14] = "信義區"
    cityarea[15] = "士林區"
    cityarea[16] = "北投區"
    cityarea[17] = "內湖區"
    cityarea[18] = "南港區"
    cityarea[19] = "文山區"
    cityarea[20] = "萬里區"
    cityarea[21] = "金山區"
    cityarea[22] = "板橋區"
    cityarea[23] = "汐止區"
    cityarea[24] = "深坑區"
    cityarea[25] = "石碇區"
    cityarea[26] = "瑞芳區"
    cityarea[27] = "平溪區"
    cityarea[28] = "雙溪區"
    cityarea[29] = "貢寮區"
    cityarea[30] = "新店區"
    cityarea[31] = "坪林區"
    cityarea[32] = "烏來區"
    cityarea[33] = "永和區"
    cityarea[34] = "中和區"
    cityarea[35] = "土城區"
    cityarea[36] = "三峽區"
    cityarea[37] = "樹林區"
    cityarea[38] = "鶯歌區"
    cityarea[39] = "三重區"
    cityarea[40] = "新莊區"
    cityarea[41] = "泰山區"
    cityarea[42] = "林口區"
    cityarea[43] = "蘆洲區"
    cityarea[44] = "五股區"
    cityarea[45] = "八里區"
    cityarea[46] = "淡水區"
    cityarea[47] = "三芝區"
    cityarea[48] = "石門區"
    cityarea[49] = "中壢區"
    cityarea[50] = "平鎮區"
    cityarea[51] = "龍潭區"
    cityarea[52] = "楊梅區"
    cityarea[53] = "新屋區"
    cityarea[54] = "觀音區"
    cityarea[55] = "桃園區"
    cityarea[56] = "龜山區"
    cityarea[57] = "八德區"
    cityarea[58] = "大溪區"
    cityarea[59] = "復興區"
    cityarea[60] = "大園區"
    cityarea[61] = "蘆竹區"
    cityarea[62] = "東區"
    cityarea[63] = "北區"
    cityarea[64] = "香山區"
    cityarea[65] = "竹北市"
    cityarea[66] = "湖口鄉"
    cityarea[67] = "新豐鄉"
    cityarea[68] = "新埔鎮"
    cityarea[69] = "關西鎮"
    cityarea[70] = "芎林鄉"
    cityarea[71] = "寶山鄉"
    cityarea[72] = "竹東鎮"
    cityarea[73] = "五峰鄉"
    cityarea[74] = "橫山鄉"
    cityarea[75] = "尖石鄉"
    cityarea[76] = "北埔鄉"
    cityarea[77] = "峨眉鄉"
    cityarea[78] = "竹南鎮"
    cityarea[79] = "頭份市"
    cityarea[80] = "三灣鄉"
    cityarea[81] = "南庄鄉"
    cityarea[82] = "獅潭鄉"
    cityarea[83] = "後龍鎮"
    cityarea[84] = "通霄鎮"
    cityarea[85] = "苑裡鎮"
    cityarea[86] = "苗栗市"
    cityarea[87] = "造橋鄉"
    cityarea[88] = "頭屋鄉"
    cityarea[89] = "公館鄉"
    cityarea[90] = "大湖鄉"
    cityarea[91] = "泰安鄉"
    cityarea[92] = "銅鑼鄉"
    cityarea[93] = "三義鄉"
    cityarea[94] = "西湖鄉"
    cityarea[95] = "卓蘭鎮"
    cityarea[96] = "中區"
    cityarea[97] = "東區"
    cityarea[98] = "南區"
    cityarea[99] = "西區"
    cityarea[100] = "北區"
    cityarea[101] = "北屯區"
    cityarea[102] = "西屯區"
    cityarea[103] = "南屯區"
    cityarea[104] = "太平區"
    cityarea[105] = "大里區"
    cityarea[106] = "霧峰區"
    cityarea[107] = "烏日區"
    cityarea[108] = "豐原區"
    cityarea[109] = "后里區"
    cityarea[110] = "石岡區"
    cityarea[111] = "東勢區"
    cityarea[112] = "和平區"
    cityarea[113] = "新社區"
    cityarea[114] = "潭子區"
    cityarea[115] = "大雅區"
    cityarea[116] = "神岡區"
    cityarea[117] = "大肚區"
    cityarea[118] = "沙鹿區"
    cityarea[119] = "龍井區"
    cityarea[120] = "梧棲區"
    cityarea[121] = "清水區"
    cityarea[122] = "大甲區"
    cityarea[123] = "外埔區"
    cityarea[124] = "大安區"
    cityarea[125] = "彰化市"
    cityarea[126] = "芬園鄉"
    cityarea[127] = "花壇鄉"
    cityarea[128] = "秀水鄉"
    cityarea[129] = "鹿港鎮"
    cityarea[130] = "福興鄉"
    cityarea[131] = "線西鄉"
    cityarea[132] = "和美鎮"
    cityarea[133] = "伸港鄉"
    cityarea[134] = "員林市"
    cityarea[135] = "社頭鄉"
    cityarea[136] = "永靖鄉"
    cityarea[137] = "埔心鄉"
    cityarea[138] = "溪湖鎮"
    cityarea[139] = "大村鄉"
    cityarea[140] = "埔鹽鄉"
    cityarea[141] = "田中鎮"
    cityarea[142] = "北斗鎮"
    cityarea[143] = "田尾鄉"
    cityarea[144] = "埤頭鄉"
    cityarea[145] = "溪州鄉"
    cityarea[146] = "竹塘鄉"
    cityarea[147] = "二林鎮"
    cityarea[148] = "大城鄉"
    cityarea[149] = "芳苑鄉"
    cityarea[150] = "二水鄉"
    cityarea[151] = "南投市"
    cityarea[152] = "中寮鄉"
    cityarea[153] = "草屯鎮"
    cityarea[154] = "國姓鄉"
    cityarea[155] = "埔里鎮"
    cityarea[156] = "仁愛鄉"
    cityarea[157] = "名間鄉"
    cityarea[158] = "集集鎮"
    cityarea[159] = "水里鄉"
    cityarea[160] = "魚池鄉"
    cityarea[161] = "信義鄉"
    cityarea[162] = "竹山鎮"
    cityarea[163] = "鹿谷鄉"
    cityarea[164] = "斗南鎮"
    cityarea[165] = "大埤鄉"
    cityarea[166] = "虎尾鎮"
    cityarea[167] = "土庫鎮"
    cityarea[168] = "褒忠鄉"
    cityarea[169] = "東勢鄉"
    cityarea[170] = "臺西鄉"
    cityarea[171] = "崙背鄉"
    cityarea[172] = "麥寮鄉"
    cityarea[173] = "斗六市"
    cityarea[174] = "林內鄉"
    cityarea[175] = "古坑鄉"
    cityarea[176] = "莿桐鄉"
    cityarea[177] = "西螺鎮"
    cityarea[178] = "二崙鄉"
    cityarea[179] = "北港鎮"
    cityarea[180] = "水林鄉"
    cityarea[181] = "口湖鄉"
    cityarea[182] = "四湖鄉"
    cityarea[183] = "元長鄉"
    cityarea[184] = "東區"
    cityarea[185] = "西區"
    cityarea[186] = "番路鄉"
    cityarea[187] = "梅山鄉"
    cityarea[188] = "竹崎鄉"
    cityarea[189] = "阿里山鄉"
    cityarea[190] = "中埔鄉"
    cityarea[191] = "大埔鄉"
    cityarea[192] = "水上鄉"
    cityarea[193] = "鹿草鄉"
    cityarea[194] = "太保市"
    cityarea[195] = "朴子市"
    cityarea[196] = "東石鄉"
    cityarea[197] = "六腳鄉"
    cityarea[198] = "新港鄉"
    cityarea[199] = "民雄鄉"
    cityarea[200] = "大林鎮"
    cityarea[201] = "溪口鄉"
    cityarea[202] = "義竹鄉"
    cityarea[203] = "布袋鎮"
    cityarea[204] = "中西區"
    cityarea[205] = "東區"
    cityarea[206] = "南區"
    cityarea[207] = "北區"
    cityarea[208] = "安平區"
    cityarea[209] = "安南區"
    cityarea[210] = "永康區"
    cityarea[211] = "歸仁區"
    cityarea[212] = "新化區"
    cityarea[213] = "左鎮區"
    cityarea[214] = "玉井區"
    cityarea[215] = "楠西區"
    cityarea[216] = "南化區"
    cityarea[217] = "仁德區"
    cityarea[218] = "關廟區"
    cityarea[219] = "龍崎區"
    cityarea[220] = "官田區"
    cityarea[221] = "麻豆區"
    cityarea[222] = "佳里區"
    cityarea[223] = "西港區"
    cityarea[224] = "七股區"
    cityarea[225] = "將軍區"
    cityarea[226] = "學甲區"
    cityarea[227] = "北門區"
    cityarea[228] = "新營區"
    cityarea[229] = "後壁區"
    cityarea[230] = "白河區"
    cityarea[231] = "東山區"
    cityarea[232] = "六甲區"
    cityarea[233] = "下營區"
    cityarea[234] = "柳營區"
    cityarea[235] = "鹽水區"
    cityarea[236] = "善化區"
    cityarea[237] = "大內區"
    cityarea[238] = "山上區"
    cityarea[239] = "新市區"
    cityarea[240] = "安定區"
    cityarea[241] = "新興區"
    cityarea[242] = "前金區"
    cityarea[243] = "苓雅區"
    cityarea[244] = "鹽埕區"
    cityarea[245] = "鼓山區"
    cityarea[246] = "旗津區"
    cityarea[247] = "前鎮區"
    cityarea[248] = "三民區"
    cityarea[249] = "楠梓區"
    cityarea[250] = "小港區"
    cityarea[251] = "左營區"
    cityarea[252] = "仁武區"
    cityarea[253] = "大社區"
    cityarea[254] = "東沙群島"
    cityarea[255] = "南沙群島"
    cityarea[256] = "岡山區"
    cityarea[257] = "路竹區"
    cityarea[258] = "阿蓮區"
    cityarea[259] = "田寮區"
    cityarea[260] = "燕巢區"
    cityarea[261] = "橋頭區"
    cityarea[262] = "梓官區"
    cityarea[263] = "彌陀區"
    cityarea[264] = "永安區"
    cityarea[265] = "湖內區"
    cityarea[266] = "鳳山區"
    cityarea[267] = "大寮區"
    cityarea[268] = "林園區"
    cityarea[269] = "鳥松區"
    cityarea[270] = "大樹區"
    cityarea[271] = "旗山區"
    cityarea[272] = "美濃區"
    cityarea[273] = "六龜區"
    cityarea[274] = "內門區"
    cityarea[275] = "杉林區"
    cityarea[276] = "甲仙區"
    cityarea[277] = "桃源區"
    cityarea[278] = "那瑪夏區"
    cityarea[279] = "茂林區"
    cityarea[280] = "茄萣區"
    cityarea[281] = "屏東市"
    cityarea[282] = "三地門鄉"
    cityarea[283] = "霧臺鄉"
    cityarea[284] = "瑪家鄉"
    cityarea[285] = "九如鄉"
    cityarea[286] = "里港鄉"
    cityarea[287] = "高樹鄉"
    cityarea[288] = "鹽埔鄉"
    cityarea[289] = "長治鄉"
    cityarea[290] = "麟洛鄉"
    cityarea[291] = "竹田鄉"
    cityarea[292] = "內埔鄉"
    cityarea[293] = "萬丹鄉"
    cityarea[294] = "潮州鎮"
    cityarea[295] = "泰武鄉"
    cityarea[296] = "來義鄉"
    cityarea[297] = "萬巒鄉"
    cityarea[298] = "崁頂鄉"
    cityarea[299] = "新埤鄉"
    cityarea[300] = "南州鄉"
    cityarea[301] = "林邊鄉"
    cityarea[302] = "東港鎮"
    cityarea[303] = "琉球鄉"
    cityarea[304] = "佳冬鄉"
    cityarea[305] = "新園鄉"
    cityarea[306] = "枋寮鄉"
    cityarea[307] = "枋山鄉"
    cityarea[308] = "春日鄉"
    cityarea[309] = "獅子鄉"
    cityarea[310] = "車城鄉"
    cityarea[311] = "牡丹鄉"
    cityarea[312] = "恆春鎮"
    cityarea[313] = "滿州鄉"
    cityarea[314] = "臺東市"
    cityarea[315] = "綠島鄉"
    cityarea[316] = "蘭嶼鄉"
    cityarea[317] = "延平鄉"
    cityarea[318] = "卑南鄉"
    cityarea[319] = "鹿野鄉"
    cityarea[320] = "關山鎮"
    cityarea[321] = "海端鄉"
    cityarea[322] = "池上鄉"
    cityarea[323] = "東河鄉"
    cityarea[324] = "成功鎮"
    cityarea[325] = "長濱鄉"
    cityarea[326] = "太麻里鄉"
    cityarea[327] = "金峰鄉"
    cityarea[328] = "大武鄉"
    cityarea[329] = "達仁鄉"
    cityarea[330] = "花蓮市"
    cityarea[331] = "新城鄉"
    cityarea[332] = "秀林鄉"
    cityarea[333] = "吉安鄉"
    cityarea[334] = "壽豐鄉"
    cityarea[335] = "鳳林鎮"
    cityarea[336] = "光復鄉"
    cityarea[337] = "豐濱鄉"
    cityarea[338] = "瑞穗鄉"
    cityarea[339] = "萬榮鄉"
    cityarea[340] = "玉里鎮"
    cityarea[341] = "卓溪鄉"
    cityarea[342] = "富里鄉"
    cityarea[343] = "宜蘭市"
    cityarea[344] = "頭城鎮"
    cityarea[345] = "礁溪鄉"
    cityarea[346] = "壯圍鄉"
    cityarea[347] = "員山鄉"
    cityarea[348] = "羅東鎮"
    cityarea[349] = "三星鄉"
    cityarea[350] = "大同鄉"
    cityarea[351] = "五結鄉"
    cityarea[352] = "冬山鄉"
    cityarea[353] = "蘇澳鎮"
    cityarea[354] = "南澳鄉"
    cityarea[355] = "釣魚臺"
    cityarea[356] = "馬公市"
    cityarea[357] = "西嶼鄉"
    cityarea[358] = "望安鄉"
    cityarea[359] = "七美鄉"
    cityarea[360] = "白沙鄉"
    cityarea[361] = "湖西鄉"
    cityarea[362] = "金沙鎮"
    cityarea[363] = "金湖鎮"
    cityarea[364] = "金寧鄉"
    cityarea[365] = "金城鎮"
    cityarea[366] = "烈嶼鄉"
    cityarea[367] = "烏坵鄉"
    cityarea[368] = "南竿鄉"
    cityarea[369] = "北竿鄉"
    cityarea[370] = "莒光鄉"
    cityarea[371] = "東引鄉"
    cityarea[372] = "東沙群島"
    cityarea[373] = "南沙群島"
    cityarea[374] = "釣魚臺"
    CITYAREA = cityarea


def build_city_options() -> List[str]:
    '''
    從 html 取得 city 的值
    '''

    global CITY_OPTIONS
    if CITY_OPTIONS is None:
        resp = requests.get(
            "https://www.post.gov.tw/post/internet/Postal/index.jsp?ID=207",
            headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
            },
        )
        soup = BeautifulSoup(resp.text, "html.parser")
        city_options = soup.find("select", {"id": "city"}).find_all("option")
        CITY_OPTIONS = [option.text for option in city_options if option.get("value") != "%"]


def build():
    last = 1
    cities_range = []
    for i in CITYAREA_ACCOUNT[1:]:
        cities_range.append((last, i))
        last = i + 1

    city_cityarea = {}
    city_change_index = {}
    for i_city, cityarea_range in zip(enumerate(CITY_OPTIONS), cities_range):

        city_change_index[i_city[1]] = i_city[0] + 1
        city_cityarea[i_city[1]] = [CITYAREA[i] for i in range(cityarea_range[0], cityarea_range[1] + 1)]

    return city_cityarea, city_change_index


if __name__ == "__main__":
    build_citarea_account()
    build_cityarea()
    build_city_options()

    CITY_CITYAREA, CITY_CHANGE_INDEX = build()

    print(CITY_CITYAREA)
    print(CITY_CHANGE_INDEX)
