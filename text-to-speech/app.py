from gtts import gTTS
import os

class TextToSpeech:
    
    def __init__(self):
        self.inputText = "Hi Buddy, How are you !!!"
        
    def convertTexttoSpeech(self,textInput,outputfileName,applySlowSetting):
        language_input = "en"
        if textInput is None:
            textInput = self.inputText
        gttsInstance = gTTS(text=textInput,lang=language_input,slow=applySlowSetting)
        fileNameInstance = "output/"+outputfileName+".mp3"
        gttsInstance.save(fileNameInstance)
        print("Completed Creating a Sppech file for the Text at ::"+fileNameInstance)
        return fileNameInstance
        
    def playSpeechFile(self,inputSpeechFile):
        # For MacOS we use this afplay, for windows we can use playsound/vlc.
        os.system("afplay "+inputSpeechFile) 
        print("Finished Playing the file :: "+inputSpeechFile)
        
textToSppechIns = TextToSpeech()
output_file_name = "MachesterUnited"
inputText = "Manchester United Football Club is a professional football club based in Old Trafford, Greater Manchester, England, that competes in the Premier League, the top flight of English football."
fileInstance = textToSppechIns.convertTexttoSpeech(inputText,output_file_name,False)
textToSppechIns.playSpeechFile(fileInstance)       
