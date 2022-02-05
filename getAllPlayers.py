import CoDAPI
import OCR


def start():
   print('--- Start recognize text from image ---')
   #OCR.get_string(OCR.src_path + "savage.png")
   #OCR.get_string(OCR.src_path + "savage3.png")
   #OCR.get_string(OCR.src_path + "savage2.png")
   #OCR.get_string(OCR.src_path + "savage4.png")
   #OCR.get_string(OCR.src_path + "savage5.png")
   OCR.get_string("./Images/savage.png")
   print(OCR.usernamesOCR)
   print("------ Done -------")

def getStats():
   print("----- Checking againgst callofduty.com ------")
   for x in range(OCR.usernamesOCR.__len__()):
      CoDAPI.getUsernames(OCR.usernamesOCR[x])
      if CoDAPI.break_loop.__len__() == 1:
         raise Exception("RATE LIMIT EXECEEDED")
         break
   print("------ Done -------")
   print("------ Convert to CSV ------")
   CoDAPI.listToCSV()
   print("------ Done -------")


#print("------ Convert to CSV ------")
#CoDAPI.listToCSV()
#print("------ Done -------")

#print(CoDAPI.usernames_check_xbl)
#print(CoDAPI.usernames_check_psn)
#print(CoDAPI.usernames_check_atv_id)
#start()
