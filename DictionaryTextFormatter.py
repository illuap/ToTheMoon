
import datetime
from loguru import logger

class DictionaryTextFormatter():

    def get_formatted_list(dic: dict, limit: int):

        end = len(dic) if limit == 0 else limit 
        i = 0
        string = ""

        for key in dic.keys():
            string += string + f"{ key } - {dic[key]} \n"

            
            i += 1
            if i == limit:
                break

        return string

    def write_formatted_list(dic: dict, limit: int):
        end = len(dic) if limit == 0 else limit 
        i = 0
        d = datetime.datetime.now()
        print(d)
        print(f"{ d.year }-{ d.month }-{ d.day }-{ d.hour }-{ d.minute }")
        try:
            print(f"{ d.year }-{ d.month }-{ d.day }-{ d.hour }-{ d.minute }")
            file = open(f"Files/mentions_{ d.year }_{ d.month }_{ d.day }_{ d.hour }-{ d.minute }.txt", "w" )
            for key in dic.keys():
                file.write(f"{ key } - {dic[key]} \n")

                i += 1
                if i == limit:
                    break
        except:
            logger.error("Failed to write to file.")
        #finally:
            #file.close()