""" Userbot module containing various scrapers. """
import os, random
from time import sleep
from html import unescape
from selenium import webdriver
from urllib.parse import quote_plus
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from .. import CHROME_DRIVER, CHROME_BIN


CARBONLANG = "auto"
LANG = "en"


@plus_ub(pattern="carbon", from_users=sudo)
async def carbon_api(e):
 if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
 
   """ A Wrapper for carbon.now.sh """
   a = await e.reply("`Processing..`")
   CARBON = 'https://carbon.now.sh/?l={lang}&code={code}'
   global CARBONLANG
   textx = await e.get_reply_message()
   pcode = e.text
   if pcode[8:]:
         pcodee = str(pcode[8:])
         if "|" in pcodee:
               pcode, skeme = pcodee.split("|")
         else:
               pcode = pcodee
               skeme = None
   elif textx:
         pcode = str(textx.message)
         skeme = None # Importing message to module
   code = quote_plus(pcode) # Converting to urlencoded
   await a.edit("`Making Carbon...\n25%`")
   url = CARBON.format(code=code, lang=CARBONLANG)
   chrome_options = Options()
   chrome_options.add_argument("--headless")
   chrome_options.binary_location = CHROME_BIN
   chrome_options.add_argument("--window-size=1920x1080")
   chrome_options.add_argument("--disable-dev-shm-usage")
   chrome_options.add_argument("--no-sandbox")
   chrome_options.add_argument("--disable-gpu")
   prefs = {'download.default_directory' : './'}
   chrome_options.add_experimental_option('prefs', prefs)
   driver = webdriver.Chrome(executable_path=CHROME_DRIVER, options=chrome_options)
   driver.get(url)
   await a.edit("`Be Patient...\n50%`")
   download_path = './'
   driver.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
   params = {'cmd': 'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': download_path}}
   command_result = driver.execute("send_command", params)
   driver.find_element_by_xpath('/html/body/div[1]/main/div[3]/div[2]/div[1]/div[1]/div/span[2]').click()
   if skeme != None:
         k_skeme = driver.find_element_by_xpath('/html/body/div[1]/main/div[3]/div[2]/div[1]/div[1]/div/span[2]/input')
         k_skeme.send_keys(skeme)
         k_skeme.send_keys(Keys.DOWN)
         k_skeme.send_keys(Keys.ENTER)
   else:
       color_scheme = str(random.randint(1,29))
       driver.find_element_by_id(("downshift-0-item-" + color_scheme)).click()
   driver.find_element_by_id("export-menu").click()
   driver.find_element_by_xpath("//button[contains(text(),'4x')]").click()
   driver.find_element_by_xpath("//button[contains(text(),'PNG')]").click()
   await a.edit("`Processing..\n75%`")
   # Waiting for downloading
   sleep(2.5)
   color_name = driver.find_element_by_xpath('/html/body/div[1]/main/div[3]/div[2]/div[1]/div[1]/div/span[2]/input').get_attribute('value')
   await a.edit("`Done...\n100%`")
   file = './carbon.png'
   await a.edit("`Uploading..`")
   await e.client.send_file(
         e.chat_id,
         file,
         caption="<< `Here's your carbon!` >>\n**Colour Scheme: **`{}`".format(color_name),
         force_document=True,
         reply_to=e.message.reply_to_msg_id,
         )
   os.remove('./carbon.png')
   driver.quit()
   # Removing carbon.png after uploading
   await a.delete() # Deleting msg
   
