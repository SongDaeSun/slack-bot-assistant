import requests

class bot_info ():

    def __init__(self, channel, header_length, header_title):

        f = open("myToken.txt", 'r')
        lines = f.readlines()
        self.token = lines[0]

        self.channel = channel

        self.header_length = header_length
        self.header_title = header_title


        self.build_header()

    def build_header(self):
        deco_num = int((self.header_length - len(self.header_title))/2)
        deco = '_' * deco_num
        self.header = deco + self.header_title + deco + '\n'


    def build_message(self, text):
        built_message =  self.header + text + '\n'

        return built_message
        
 
    def post_message(self, text):

        full_message = self.build_message(text)

        response = requests.post("https://slack.com/api/chat.postMessage",
            headers={"Authorization": "Bearer "+self.token},
            data={"channel": "#" + self.channel, "text": full_message}
        )
        print(response)
    
    

bot = bot_info("학업", 32, '수업알림')
bot.post_message("test")


