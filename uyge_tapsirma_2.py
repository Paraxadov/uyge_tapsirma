import logging
from Login_aza import login, password
from logging.handlers import TimedRotatingFileHandler

user_login = input("Login kirgiz: ")
parol = input("Parol kirgiz: ")

logger = logging.getLogger("InfoLogger")
logger.setLevel(logging.INFO)

logging.basicConfig(filename="parol.log", level = logging.ERROR)

consule_handler = logging.StreamHandler()
consule_handler.setLevel(logging.INFO)  

def login_tekseriw(lgn):
    if user_login == login:
        '''Login tekseriw ushin'''
        logger.info("Login duris kiritildi")
    else:
        logger.info("Login qate kiritildi")
        
def parol_tekseriw(psd):
    if parol == password:
        '''Parol tekseriw ushin'''
        logger.info("Parol duris kiritildi")
    else:
        logger.info("Parol qate kitildi")
        

try:
    handler = TimedRotatingFileHandler('Info.log', 
                                    when="midnight", 
                                    interval = 1, 
                                    backupCount = 7)

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    consule_handler.setFormatter(formatter)
    
    logger.addHandler(handler)
    logger.addHandler(consule_handler)

    logger.info("Loginge kiriw ushin hareket ettildi")
    
    login_tekseriw(user_login)
    parol_tekseriw(parol)
    
    logger.info("Login ham parol tekserildi")
    
except Exception as qatesi:
    logging.error(f"Qateshilik: {qatesi}")