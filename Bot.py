from __future__ import unicode_literals
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import os, fnmatch
import youtube_dl




class bot():
    
    def __init__(self):
        #Start the whatsapp
        self.driver = webdriver.Chrome(service=Service('C:\Program Files (x86)/chromedriver.exe')) 
        self.driver.get("http://web.whatsapp.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(99)
        
    
    #Click in unread chats
    def unread_messages(self):
        self.driver.find_element(By.XPATH,"//div[@class='_1pJ9J']/span[@class='l7jjieqr cfzgl7ar ei5e7seu h0viaqh7 tpmajp1w c0uhu3dl riy2oczp dsh4tgtl sy6s5v3r gz7w46tb lyutrhe2 qfejxiq4 fewfhwl7 ovhn1urg ap18qm3b ikwl5qvt j90th5db aumms1qt']").click()  
        
    
    def save_image(self):
        sleep(0.5)
        
        with open('stiker.png', 'wb') as file:
            file.write(self.driver.find_element(By.XPATH,'//div[@class = "_3IfUe"]/img[@crossorigin = "anonymous"]').screenshot_as_png)
    
    def message(self, menu='Menu bot, Funcionalidades:                                                                                                                                               #stiker   #music                                                   se demorar muito para responder espere 10 segundos e pergunte denovo'):
        try:
        
            self.driver.find_element(By.XPATH,'//div[@class = "_1UWac _1LbR4"]/div[@class = "_13NKt copyable-text selectable-text"]').send_keys(menu + Keys.ENTER)
        
        
        except:
            self.driver.find_element(By.XPATH,'//div[@class = "1UWac _1LbR4 focused"]/div[@class = "_13NKt copyable-text selectable-text"]').send_keys(menu + Keys.ENTER)    
   
                    
            
    
    def last_mesage(self):
        
        messages = self.driver.find_elements(By.XPATH,"//div[starts-with(@data-id ,'false_')]/div[starts-with(@class ,'cvjcv _1Ilru')]/div[@class = 'Nm1g1 _22AX6']/div[@class = '_22Msk']/div[contains(@class , 'copyable-text')]/div[@class = '_1Gy50']/span[@class = 'i0jNr selectable-text copyable-text']/span")
        for message in messages:
            self.msg = message.text
        print(self.msg)    
            
        #messages = self.driver.find_elements(By.XPATH,"//div[starts-with(@data-id ,'false_')]/div[starts-with(@class ,'cvjcv _1Ilru')]/div[@class = 'Nm1g1 _22AX6']/div[@class = '_22Msk']/div[contains(@class , 'copyable-text')]/div[@class = '_1Gy50']/span[@class = 'i0jNr selectable-text copyable-text']/span/a")
            
    
        
        
    def extract_audio(self):
        link = self.msg[7:]
        
        if link.lower()[8] == 'y':
            
            try:
                ydl_opts = {
                    'format': 'bestaudio/best',
                    'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': '192',
                    }],
                }
                with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([link])
                    
                    file_path = 'C:\\Users\\Pedro\\OneDrive\\Área de Trabalho\\whatazap bot\\'

                    files_to_rename=fnmatch.filter(os.listdir(file_path), '*.mp3')
                    
                    for i, file_name in enumerate(files_to_rename):
                        new_file_name = 'audio' + '.mp3'

                        os.rename(file_path + file_name, 
                        file_path + new_file_name)
                        
                    
                self.driver.find_element(By.CLASS_NAME,'_2jitM').click()
                
                self.driver.find_element(By.XPATH,'//button[@class = "_2t8DP"]/input[@accept = "image/*,video/mp4,video/3gpp,video/quicktime"]').send_keys('C:\\Users\\Pedro\\OneDrive\\Área de Trabalho\\whatazap bot\\audio.mp3')
                self.driver.find_element(By.XPATH,"//div[@class = '_165_h _2HL9j']").click()
                os.remove("audio.mp3")
            except Exception as a:
                print(a)

    def goto_image(self):
        #Going to account data
        self.driver.find_element(By.CLASS_NAME,"_2rlF7").click()
        
        #click in midia, You need to change the text to your language
        self.driver.find_element(By.XPATH,"//span[text()='Arquivos de mídia, links e docs']").click()
        
        #CLick in the least image
        check_boxes = self.driver.find_elements(By.CLASS_NAME,"_23fpc")
        check_boxes[0].click()
        
        self.save_image()
        self.exit_send()
        
    
    def exit_send(self):
        
        self.driver.find_element(By.XPATH,'//div[@class = "_26lC3"]/span[@data-testid = "x-viewer"]').click()
        self.driver.find_element(By.CLASS_NAME,'_2jitM').click()
        
        self.driver.find_element(By.XPATH,'//button[@class = "_2t8DP"]/input[@accept = "image/*"]').send_keys('C:\\Users\\Pedro\\OneDrive\\Área de Trabalho\\whatazap bot\\stiker.png')

        self.driver.find_element(By.XPATH,"//div[@class = '_165_h _2HL9j']").click()
    
    def main(self):
        while True:
            try:
                self.unread_messages()
                #self.driver.maximize_window()

            except Exception as e:
               pass
           
           
            else:
                try:
                    
                    self.last_mesage()
                    if self.msg[:6] == '#audio':
                        self.extract_audio()
                    
                    if self.msg == '#fig':
                        self.goto_image()
                    self.driver.minimize_window()
                    
                    
                    
                    if self.msg == '#menu': 
                        self.message()
                        
                    
                    if self.msg == '#music':
                        self.message('Posso fazer download de qualquer video do youtube e enviar em formato mp3,                                          Para fazer isso digite "#audio Link_do_youtube"       Essa funcao pode demorar um pouco  ')
                    
                    
                    if self.msg == '#stiker':
                        self.message('Posso fazer stiker de qualquer mensagem para                                                                                             mande uma mensagem com a descrição "#fig"')    
                    
                    
                    
                    
                except Exception as e:
                    print(e)
            
                finally:
                    sleep(1.5)
                    self.driver.find_element(By.XPATH,'//span[@data-testid = "pinned"]').click()
                    self.driver.maximize_window()
                    
                
        
        
        
a = bot()
a.main()


