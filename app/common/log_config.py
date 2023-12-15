import logging
from logging.handlers import TimedRotatingFileHandler

class LogConfig:
    def log_start():
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)

        # 콘솔 핸들러 추가
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        logger.addHandler(ch)

        # TimedRotatingFileHandler 추가 (압축 파일로 저장)
        log_file_path = r'D:\python-workspace\logs\test.log'
        fh = TimedRotatingFileHandler(log_file_path, when="midnight", interval=1, backupCount=7)
        fh.suffix = "%Y-%m-%d.zip"  # 압축 파일 확장자
        fh.setLevel(logging.INFO)
        #formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        formatter = logging.Formatter("[%(asctime)s.%(msecs)03d] %(levelname)s [%(thread)d] - %(message)s", "%Y-%m-%d %H:%M:%S")
        fh.setFormatter(formatter)
        logger.addHandler(fh)
        return logger


logger = LogConfig.log_start()