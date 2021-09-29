from botBase import GeneralAssistant 

class AcademyAssistant (GeneralAssistant):
    def __init__(self, channel, header_length, header_title):
        super().__init__(channel, header_length, header_title)

    def build_header(self):
        super().build_header()
    
    def post_message(self, course, isStart, isNow):
        full_message =  self.header
        full_message += "[과목명] " + course + "\n"

        if isStart:
            if isNow:
                full_message += "[안내문] 수업 시작했습니다.\n"
            
            else:
                full_message += "[안내문] 수업 시작 5분 전입니다.\n" 

        else:
            if isNow:
                full_message += "[안내문] 수업 끝났습니다.\n"
            
            else:
                full_message += "[안내문] 수업 종료 5분 전입니다.\n" 
        
        full_message += self.getTimeStamp()

        self.send_message(full_message)

    def send_message(self, text):
        super().send_message(text)

    def getTimeStamp(self):
        return super().getTimeStamp()

if __name__ == "__main__" :
    bot = AcademyAssistant("학업", 31, '3개월만 버티자')
    bot.post_message("재무관리", False, True)

