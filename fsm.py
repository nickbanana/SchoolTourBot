from transitions.extensions import GraphMachine

from wrapper import send_message, send_GIPHY

class TourMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.giphy_keyword = ''
        self.first_enter = True
        self.id = -1
        self.machine = GraphMachine(
            model=self,
            **machine_configs
        )
        
    def is_first_entry(self, event):
        return self.first_enter
    def is_going_to_liberal(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text == "文學院"    
    def is_going_to_science(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text == "理學院"
    def is_going_to_management(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text == "管理學院"
    def is_going_to_engineering(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text == "工學院"
    def is_going_to_eecs(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text == "電機資訊學院"
    def is_going_to_css(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text == "社會科學院"
    def is_going_to_cpd(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text == "規劃與設計學院"
    def is_going_to_bb(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text == "生物科學與科技學院"
    def is_going_to_med(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text == "醫學院"
    
    def is_going_to_detail(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text == "是"
    
    def is_going_user(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text == "否"

    def is_going_to_gif(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text == "動圖"
    def is_going_to_gif_detail(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text != "" and text != "返回":
                self.giphy_keyword = text
                return True
            else:
                return False
    def is_going_to_main_from_gif(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text == "返回"
    def on_enter_gif(self, event):
        print("I'm entering gif")

        sender_id = event['sender']['id']
        self.giphy_keyword = ''
        send_message(sender_id,"輸入任何字串來尋找GIF")
        send_message(sender_id,"輸入返回來回到主頁面")

    def on_enter_gif_detail(self, event):
        print("I'm entering gif detail")
        sender_id = event['sender']['id']
        send_GIPHY(sender_id,self.giphy_keyword)
        self.giphy_keyword = ''
        self.go_back(event)

    def on_enter_liberal(self, event):
        print("I'm entering liberal")

        sender_id = event['sender']['id']
        send_message(sender_id,"目前所檢視的是文學院")
        send_message(sender_id,"是否要檢視其所有的系所以及網站？")

    def on_enter_detail_liberal(self, event):
        print("I'm entering detail_liberal")
        sender_id = event['sender']['id']    
        send_message(sender_id,"在這學院底下的有以下幾個學系以及其網站連結：")
        send_message(sender_id,"中國文學系 http://www.chinese.ncku.edu.tw")
        send_message(sender_id,"外國語文學系 http://www.flld.ncku.edu.tw")
        send_message(sender_id,"歷史學系 http://www.his.ncku.edu.tw")
        send_message(sender_id,"臺灣文學系 http://www.twl.ncku.edu.tw")
        send_message(sender_id,"藝術研究所 http://www.art.ncku.edu.tw")
        send_message(sender_id,"考古學研究所 http://archaeology.ncku.edu.tw")
        send_message(sender_id,"戲劇碩士學位學程 http://mapd.ncku.edu.tw")
        send_message(sender_id,"華語中心 http://kclc.ncku.edu.tw")
        send_message(sender_id,"外語中心 http://flc.ncku.edu.tw?Lang=zh-tw")
        send_message(sender_id,"多元文化研究中心 http://www.cmcs.ncku.edu.tw")
        self.go_back(event)

    def on_enter_science(self, event):
        print("I'm entering science")

        sender_id = event['sender']['id']
        send_message(sender_id,"目前所檢視的是理學院")
        send_message(sender_id,"是否要檢視其所有的系所以及網站？")

    def on_enter_detail_science(self, event):
        print("I'm entering detail_science")
        sender_id = event['sender']['id']    
        send_message(sender_id,"在這學院底下的有以下幾個學系以及其網站連結：")
        send_message(sender_id,"數學系 http://www.math.ncku.edu.tw")
        send_message(sender_id,"化學系 http://www.ch.ncku.edu.tw")
        send_message(sender_id,"物理學系 http://www.phys.ncku.edu.tw/2012/ch/")
        send_message(sender_id,"地球科學系 http://www.earth.ncku.edu.tw")
        send_message(sender_id,"光電科學與工程學系 http://www.dps.ncku.edu.tw")
        send_message(sender_id,"太空與電漿科學研究所 http://www.isaps.ncku.edu.tw")
        send_message(sender_id,"理論科學研究中心 http://www.ncts.ncku.edu.tw")
        self.go_back(event)

    def on_enter_management(self, event):
        print("I'm entering management")

        sender_id = event['sender']['id']
        send_message(sender_id,"目前所檢視的是管理學院")
        send_message(sender_id,"是否要檢視其所有的系所以及網站？")

    def on_enter_detail_management(self, event):
        print("I'm entering detail_management")
        sender_id = event['sender']['id']    
        send_message(sender_id,"在這學院底下的有以下幾個學系以及其網站連結：")
        send_message(sender_id,"會計學系 http://www.acc.ncku.edu.tw")
        send_message(sender_id,"統計學系 http://www.stat.ncku.edu.tw")
        send_message(sender_id,"企業管理學系 http://www.ba.ncku.edu.tw")
        send_message(sender_id,"交通管理科學系 http://www.tcm.ncku.edu.tw")
        send_message(sender_id,"電信管理研究所 http://www.tm.ncku.edu.tw")
        send_message(sender_id,"國際企業研究所 http://www.ib.ncku.edu.tw")
        send_message(sender_id,"財務金融研究所 http://www.fin.ncku.edu.tw")
        send_message(sender_id,"體育健康與休閒研究所 http://www.pehl.ncku.edu.tw")
        send_message(sender_id,"工業與資訊管理學系暨資訊管理研究所 http://www.iim.ncku.edu.tw")
        send_message(sender_id,"數據科學研究所 http://ds.ncku.edu.tw")
        send_message(sender_id,"高階管理碩士在職專班 (EMBA) http://www.emba.ncku.edu.tw")
        send_message(sender_id,"國際經營管理研究所 (IMBA) http://www.imba.ncku.edu.tw")
        send_message(sender_id,"經營管理碩士學位學程 (AMBA) http://www.amba.ncku.edu.tw")
        self.go_back(event)

    def on_enter_engineering(self, event):
        print("I'm entering engineering")

        sender_id = event['sender']['id']
        send_message(sender_id,"目前所檢視的是工學院")
        send_message(sender_id,"是否要檢視其所有的系所以及網站？")

    def on_enter_detail_engineering(self, event):
        print("I'm entering detail_engineering")
        sender_id = event['sender']['id']    
        send_message(sender_id,"在這學院底下的有以下幾個學系以及其網站連結：")
        send_message(sender_id,"機械工程學系 http://www.me.ncku.edu.tw")
        send_message(sender_id,"化學工程學系 http://web.che.ncku.edu.tw")
        send_message(sender_id,"土木工程學系 http://www.civil.ncku.edu.tw")
        send_message(sender_id,"材料科學及工程學系 http://www.mse.ncku.edu.tw")
        send_message(sender_id,"水利及海洋工程學系 http://www.hyd.ncku.edu.tw")
        send_message(sender_id,"工程科學系 http://www.es.ncku.edu.tw")
        send_message(sender_id,"系統及船舶機電工程學系 http://w3.sname.ncku.edu.tw")
        send_message(sender_id,"航空太空工程學系 http://www.iaa.ncku.edu.tw")
        send_message(sender_id,"資源工程學系 http://www.mp.ncku.edu.tw")
        send_message(sender_id,"環境工程學系 http://www.ev.ncku.edu.tw")
        send_message(sender_id,"生物醫學工程學系 http://web.bme.ncku.edu.tw")
        send_message(sender_id,"測量及空間資訊學系 http://www.geomatics.ncku.edu.tw")
        send_message(sender_id,"海洋科技與事務研究所 http://www.iotma.ncku.edu.tw")
        send_message(sender_id,"民航研究所 http://ica.iaa.ncku.edu.tw")
        send_message(sender_id,"能源國際學士學位學程 http://ibdpe.ncku.edu.tw")
        send_message(sender_id,"尖端材料國際碩士學位學程 http://icamp.ncku.edu.tw")
        send_message(sender_id,"自然災害減災及管理國際碩士學位學程 http://www.inhmm.ncku.edu.tw")
        send_message(sender_id,"工程管理碩士在職專班 http://www.emgp.ncku.edu.tw")
        send_message(sender_id,"醫療器材創新國際碩士班 http://web.bme.ncku.edu.tw")
        self.go_back(event)
    
    def on_enter_eecs(self, event):
        print("I'm entering eecs")

        sender_id = event['sender']['id']
        send_message(sender_id,"目前所檢視的是電機資訊學院")
        send_message(sender_id,"是否要檢視其所有的系所以及網站？")

    def on_enter_detail_eecs(self, event):
        print("I'm entering detail_eecs")
        sender_id = event['sender']['id']    
        send_message(sender_id,"在這學院底下的有以下幾個學系以及其網站連結：")
        send_message(sender_id,"電機工程學系 http://www.ee.ncku.edu.tw")
        send_message(sender_id,"資訊工程學系 http://www.csie.ncku.edu.tw")
        send_message(sender_id,"醫學資訊研究所 http://www.imi.ncku.edu.tw")
        send_message(sender_id,"微電子工程研究所 http://ime.ee.ncku.edu.tw")
        send_message(sender_id,"製造資訊與系統研究所 http://www.imis.ncku.edu.tw?Lang=zh-tw")
        send_message(sender_id,"電腦與通信工程研究所 http://cce.ee.ncku.edu.tw")
        send_message(sender_id,"奈米積體電路工程碩博士學位學程 http://nice.ncku.edu.tw")
        self.go_back(event)

    def on_enter_css(self, event):
        print("I'm entering css")

        sender_id = event['sender']['id']
        send_message(sender_id,"目前所檢視的是社會科學院")
        send_message(sender_id,"是否要檢視其所有的系所以及網站？")

    def on_enter_detail_css(self, event):
        print("I'm entering detail_css")
        sender_id = event['sender']['id']    
        send_message(sender_id,"在這學院底下的有以下幾個學系以及其網站連結：")
        send_message(sender_id,"政治學系 http://www.polsci.ncku.edu.tw")
        send_message(sender_id,"經濟學系 http://economics.ncku.edu.tw")
        send_message(sender_id,"法律學系 http://www.law.ncku.edu.tw")
        send_message(sender_id,"心理學系 http://psychology.ncku.edu.tw")
        send_message(sender_id,"教育研究所 http://www.ed.ncku.edu.tw")
        send_message(sender_id,"心智影像研究中心 http://fmri.ncku.edu.tw")
        self.go_back(event)
    
    def on_enter_cpd(self, event):
        print("I'm entering cpd")

        sender_id = event['sender']['id']
        send_message(sender_id,"目前所檢視的是規劃與設計學院")
        send_message(sender_id,"是否要檢視其所有的系所以及網站？")

    def on_enter_detail_cpd(self, event):
        print("I'm entering detail_cpd")
        sender_id = event['sender']['id']    
        send_message(sender_id,"在這學院底下的有以下幾個學系以及其網站連結：")
        send_message(sender_id,"建築學系 http://www.arch.ncku.edu.tw")
        send_message(sender_id,"都市計劃學系 http://www.up.ncku.edu.tw")
        send_message(sender_id,"工業設計學系 http://www.ide.ncku.edu.tw")
        send_message(sender_id,"創意產業設計研究所 http://www.icid.ncku.edu.tw")
        send_message(sender_id,"科技藝術碩士學位學程 http://technoart.ncku.edu.tw")
        self.go_back(event)

    def on_enter_bb(self, event):
        print("I'm entering bb")

        sender_id = event['sender']['id']
        send_message(sender_id,"目前所檢視的是生物科學與科技學院")
        send_message(sender_id,"是否要檢視其所有的系所以及網站？")

    def on_enter_detail_bb(self, event):
        print("I'm entering detail_bb")
        sender_id = event['sender']['id']    
        send_message(sender_id,"在這學院底下的有以下幾個學系以及其網站連結：")
        send_message(sender_id,"生命科學系 http://www.bio.ncku.edu.tw")
        send_message(sender_id,"生物科技與產業科學系 http://dbbs.ncku.edu.tw?Lang=zh-tw")
        send_message(sender_id,"熱帶植物科學研究所 http://www.itps.ncku.edu.tw")
        send_message(sender_id,"轉譯農業科學博士學位學程 http://www.tas.ncku.edu.tw")
        self.go_back(event)

    def on_enter_med(self, event):
        print("I'm entering med")

        sender_id = event['sender']['id']
        send_message(sender_id,"目前所檢視的是醫學院")
        send_message(sender_id,"是否要檢視其所有的系所以及網站？")

    def on_enter_detail_med(self, event):
        print("I'm entering detail_med")
        sender_id = event['sender']['id']    
        send_message(sender_id,"在這學院底下的有以下幾個學系以及其網站連結：")
        send_message(sender_id,"醫學系 http://med.hosp.ncku.edu.tw/")
        send_message(sender_id,"藥學系 http://pharmacy.ncku.edu.tw")
        send_message(sender_id,"護理學系 http://www.nursing.ncku.edu.tw")
        send_message(sender_id,"物理治療學系 http://www.pt.ncku.edu.tw")
        send_message(sender_id,"職能治療學系 http://ot.ncku.edu.tw/")
        send_message(sender_id,"醫學檢驗生物技術學系 http://mt.ncku.edu.tw")
        send_message(sender_id,"臨床藥學與藥物科技研究所 http://clpharm.ncku.edu.tw")
        send_message(sender_id,"基礎醫學研究所 http://basicmed.med.ncku.edu.tw")
        send_message(sender_id,"行為醫學研究所 http://www.behmed.ncku.edu.tw")
        send_message(sender_id,"分子醫學研究所 http://imm.med.ncku.edu.tw")
        send_message(sender_id,"口腔醫學研究所 http://www.iom.ncku.edu.tw/")
        send_message(sender_id,"臨床醫學研究所 http://icmmed.ncku.edu.tw")
        send_message(sender_id,"健康照護科學研究所 http://ahs.ncku.edu.tw")
        send_message(sender_id,"老年學研究所 http://www.iog.ncku.edu.tw")
        send_message(sender_id,"食品安全衛生暨風險管理研究所 http://www.dfsr.ncku.edu.tw")
        self.go_back(event)

    def on_enter_user(self, event):
        print("Entering User")
        sender_id = event['sender']['id']
        send_message(sender_id,"這是成大簡易學系檢索系統，可輸入學院查詢")
        send_message(sender_id,"能檢視的學院有文學院、理學院、管理學院")
        send_message(sender_id,"工學院、電機資訊學院、社會科學院")
        send_message(sender_id,"規劃與設計學院、生物科學與科技學院以及醫學院")
        self.first_enter = False


    