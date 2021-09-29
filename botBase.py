import requests
import time

class GeneralAssistant():

    def __init__(self, channel, header_length, header_title):

        f = open("myToken.txt", 'r')
        lines = f.readlines()
        self.token = lines[0]

        self.channel = channel

        self.header_length = header_length
        self.header_title = header_title


        self.build_header()

    def build_header(self):
        self.header = "_" * self.header_length + '\n'
        self.header += self.header_title +'\n'


    def post_message(self, text):
        full_message =  self.header + text + '\n' + self.getTimeStamp()

        self.send_message(full_message)

    
    def getTimeStamp(self):
        tm = time.localtime(1575142526.500323)
        string = time.strftime('%Y-%m-%d %I:%M:%S %p', tm)
        
        return string
        
        
 
    def send_message(self, text):
        requests.post("https://slack.com/api/chat.postMessage",
            headers={"Authorization": "Bearer "+self.token},
            data={"channel": "#" + self.channel, "text": text}
        )

if __name__ == "__main__" :
    bot = GeneralAssistant("학업", 32, '수업알림')
    bot.post_message("test")


