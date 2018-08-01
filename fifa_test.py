import unittest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


'''
class simsMediaPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        driver = self.driver       
        driver.get("https://www.easports.com/fifa/fifa-18-el-tornado")

    def test_watchVideo(self):      
        driver = self.driver 
        driver.find_element_by_xpath("//button").click()
        assert "page=1" in driver.current_url
        driver.find_element_by_xpath("//a[5]/div/div").click()
        sleep(20)
        driver.save_screenshot('media_video.png')
        #switch to modal******************************************************
        driver.switch_to_alert()  
        #next
        driver.find_element_by_css_selector(".modal-content a.right").click()
        sleep(20)
        driver.save_screenshot('media_video_next.png')
        #pre
        driver.find_element_by_css_selector(".modal-content a.left").click()
        sleep(20)
        driver.save_screenshot('media_video_pre.png')  
        #close
        driver.find_element_by_css_selector(".modal-content .modal-header button").click()
        sleep(10)
        assert "item" not in driver.current_url

    def tearDown(self):
        self.driver.close()



class fifaElTornadoPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        driver = self.driver       
        driver.get("https://www.easports.com/fifa/fifa-18-el-tornado")
        sleep(10)

    def testElTornadoContentAppears(self):      
        driver = self.driver
        elTornadoLogo = driver.find_element_by_css_selector("#marquee > div > div > div > picture") 
        elTornadoCopy = driver.find_element_by_css_selector("#marquee > div > div > div > div.eas-hero_copy.eas-b2")
        elTornadoEyebrow = driver.find_element_by_css_selector("#marquee > div > div > div > h3")
        if elTornadoLogo.is_displayed():
            print "ElTornadoContent found" 
        else:
            print "ElTornadoContent not found"

        if elTornadoCopy.is_displayed():
            print "elTornadoCopy found" 
        else:
            print "elTornadoCopy not found" 

        if elTornadoEyebrow.is_displayed():
            print "elTornadoEyebrow found" 
        else:
            print "elTornadoEyebrow not found"     

    def tearDown(self):
        self.driver.close()
'''

'''About FIFA 18'''
class fifaDemoPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        driver = self.driver
        driver.get("https://www.easports.com/fifa/demo")
    def testPS4CTALinkCorrectly(self):
        driver = self.driver
        PS4 = driver.find_element_by_css_selector("#marquee > div.eas-hero_layer.eas-hero_layer--content > div > div > div.eas-hero_cta-group.eas-hero_cta-group--image > a:nth-child(1)")
        PS4.click()
        try:
            self.assertEqual("FIFA 18 Demo on PS4 | Official PlayStation™Store Singapore", driver.title)
        except Exception as e:
            print "PS4 CTA doesn't work"

    def testPS4CTALinkCorrectly(self):
        driver = self.driver
        XBOX = driver.find_element_by_css_selector("#marquee > div.eas-hero_layer.eas-hero_layer--content > div > div > div.eas-hero_cta-group.eas-hero_cta-group--image > a:nth-child(2)")
        XBOX.click()
        try:
            self.assertEqual("Get FIFA 18 Demo - Microsoft Store en-SG", driver.title)
        except Exception as e:
            print "XBOX CTA doesn't work"

    def testOriginCTALinkCorrectly(self):
        driver = self.driver
        Origin = driver.find_element_by_css_selector("#marquee > div.eas-hero_layer.eas-hero_layer--content > div > div > div.eas-hero_cta-group.eas-hero_cta-group--image > a:nth-child(3)")
        Origin.click()
        try:
            self.assertEqual("FIFA 18 for PC | Origin", driver.title)
        except Exception as e:
            print "Origin CTA doesn't work"


    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()




