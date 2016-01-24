import logging

#訊息輸出格式定義
format_dict = {
    1:logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'),
    }

class zLogger:
    #loggerName = 路徑及檔名 , loggerLevel = 對應輸出格式 Index , loggerSpace = 該 logger 空間名
    def __init__(self, loggerPath , loggerLevel , loggerSpace = "abc"):
        # 創建一個 logger
        self.logger = logging.getLogger(loggerSpace)
        self.logger.setLevel(logging.DEBUG)

        # 創建一個 Handler 用來寫入 log (File)
        fh = logging.FileHandler(loggerPath)
        fh.setLevel(logging.DEBUG)

        # 同上，用來輸出至控制畫面
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        # 定義輸出格式
        formatter = format_dict[int(loggerLevel)]
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 將所有 Handler 加入 logger 裡
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)
    
    # 該 class 提供一個寫入的動作
    def write(self , sType,sMessage):
        if sType.upper() == "INFO":
            self.logger.info(sMessage)
        elif sType.upper() == "ERROR":
            self.logger.error(sMessage)
        elif sType.upper() == "WARNING":
            self.logger.warning(sMessage)
        elif sType.upper() == "DEBUG":
            self.logger.debug(sMessage)

    # 提供一個回傳 logger 的方法
    def getlog(self):
        return self.logger

#   logger 等級有以下 :
#   Level 順序 :NOTSET < DEBUG < INFO < WARNING < ERROR < CRITICAL
#   設置 INFO , 那麼小於 INFO 等級的都不會輸出只輸出大於該等級的項目
#   logger.debug("foobar")       不輸出   
#   logger.info("foobar")        輸出  
#   logger.warning("foobar")     輸出  
#   logger.error("foobar")       輸出  
#   logger.critical("foobar")    輸出

#   StreamHandler:               輸出至控制台
#   FileHandler:                 輸出至文件
#   BaseRotatingHandler          可按照時間撰寫 LOG
#   SocketHandler                用 TCP 網路連接撰寫
#   DatagramHandler              用 UDP 網路連接撰寫
#   SMTPHandler                  把 LOG 寫成 EMAIL 寄送