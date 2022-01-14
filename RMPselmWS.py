from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def work(hotman):
        flameo="https://www.ratemyprofessors.com/search/teachers?query="
        profRMP = flameo+hotman #full link of the prof

        browser=webdriver.Firefox()
        browser.get(profRMP) #opens the URL
        #browser.maximize_window() #dont need fulls creen

        time.sleep(0)
        print("checking...")

        #Ignores  cookies
        try:
                main = WebDriverWait(browser, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "ReactModal__Body--open"))
                )
                main.click()

                main.send_keys(Keys.ESCAPE)

        except:
                print("miss1")
                browser.quit()
        ##


        try:    #gets quality value of RMP
                main = WebDriverWait(browser, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, ".CardNumRating__CardNumRatingNumber-sc-17t4b9u-2"))
                )

               # print(main) #prints out the element
                print(main.text)  # got the the value of the RMP, now as text
                print("hit2")

                outF = open("myOutFile.txt", "a")
                outF.write(hotman)
                outF.write(",")
                outF.write(main.text)                           #gets the value and stores it
                outF.write("\n")
                outF.close()

        except:
                print("miss2") #no prof found under that name :(

                outF = open("myOutFile.txt", "a")
                outF.write(hotman)
                outF.write(",0? \n")  # gets the value and stores it
                outF.close()
                browser.quit()
                return ()




        print("done \n")

        outF.close()  #just in case
        time.sleep(2) #gives it time to catchup
        browser.quit()
        return()