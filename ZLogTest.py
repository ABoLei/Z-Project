from PythonLog import zLogger
import logging

LogPath = 'your log file path. ex:C:\\'
clsLog = zLogger(LogPath, 1,"ChenYu")
clsLog.write("info","Test My Log");

#取得同一個 Logging Name 就可以使用同一個 logging 寫入，無須作物件傳遞的動作
#log 就可以直接寫入同一個log檔裡(log1.log)
log = logging.getLogger("ChenYu")
log.info("This is outside Message.")