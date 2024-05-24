import logging
import os

def another_run():
    app_setting_value = os.environ['myAppSetting']
    LogConn_value = os.environ['LogConn']
    SQLConn_value = os.environ['SQLConn']
    SFTPConn_value = os.environ['SFTPConn']
    logging.info("app_setting_value = " + app_setting_value)
    logging.info("LogConn = " + LogConn_value)
    logging.info("SQLConn = " + SQLConn_value)
    logging.info("SFTPConn = " + SFTPConn_value)
    logging.info('Another python script executed.')