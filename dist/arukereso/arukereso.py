from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import xlsxwriter
import math
from time import sleep
import codecs

def init_driver() -> webdriver.Chrome:
    driver = webdriver.Chrome()
    return driver

filter=open("filter.txt", "r", encoding='utf-8')
#username (email)
u = filter.readline()
u=u[u.find("=")+1:]
#password
p = filter.readline()
p=p[p.find("=")+1:]
#keresett eszköz
s = filter.readline()
s=s[s.find("=")+1:]
#eszköz paraméter (filter)
f = filter.readline()
f=f[f.find("=")+1:]
#recordok száma
d = filter.readline()
d=d[d.find("=")+1:]
d = int(d)
filter.readline()

#rendezés
alapertelmezett=filter.readline()
alapertelmezett=alapertelmezett[alapertelmezett.find("=")+1:-1]

olcso=filter.readline()
olcso=olcso[olcso.find("=")+1:-1]

#arcsokkentett=filter.readline()
#arcsokkentett=arcsokkentett[arcsokkentett.find("=")+1:-1]
#TÚLZOTTAN MEGVÁLTOZTATJA AZ OLDAL FELÉíTÉSÉT 

draga=filter.readline()
draga=draga[draga.find("=")+1:-1]

ertekeles=filter.readline()
ertekeles=ertekeles[ertekeles.find("=")+1:-1]

nevszerint=filter.readline()
nevszerint=nevszerint[nevszerint.find("=")+1:-1]

filter.readline()

armin=filter.readline()
armin=armin[armin.find("=")+1:-1]
armin=int(armin)

armax=filter.readline()
armax=armax[armax.find("=")+1:-1]
armax=int(armax)

#Idő kinyerése az órából
from time import gmtime, strftime
t=strftime("%Y-%m-%d %H-%M-%S", gmtime())
t=str(t)

filenev = s[:-1]+'_'+t

filter.close

#Blépés az oldalra
def login(driver):
    
    driver.get("https://www.arukereso.hu/belepes/")
    
    driver.maximize_window()
    
    username = driver.find_element(By.NAME, "uname")
    WebDriverWait(driver, 5).until(EC.visibility_of(username))
    username.send_keys(u)
    sleep(2)
    password = driver.find_element(By.NAME, "password")
    WebDriverWait(driver, 5).until(EC.visibility_of(password))
    password.send_keys(p)
    sleep(1)

    password.send_keys(Keys.RETURN)
    
#Kersés az oldalon  
def search(driver):

    search = driver.find_element(By.NAME, 'st')
    WebDriverWait(driver, 5).until(EC.visibility_of(search))
    search.send_keys(s)
    sleep(2)

#txt-ben megadott filterre szűrés
def filters(driver):
    
    try:
        filter=driver.find_element(By.XPATH, '//input[@type="text"]')
        filter.send_keys(f)
        filter.send_keys(Keys.RETURN)
        sleep(3)

    except:
        home=driver.find_element(By.XPATH, '//*[@id="page-header"]/div/div/div[1]')
        home.click()

        search = driver.find_element(By.NAME, 'st')
        WebDriverWait(driver, 5).until(EC.visibility_of(search))
        search.send_keys(f," ",s)
        sleep(2)

#az x-el jelölt szempont szrinti rndezés 
def rendezes(driver):
    lista=driver.find_element(By.ID, 'order-dropdown')
    lista.click()

    if alapertelmezett=='x':
        rendez=driver.find_element(By.XPATH, '//li/a[@data-akorderby="5"]')
        rendez.send_keys(Keys.RETURN)

    if olcso=='x':
        rendez=driver.find_element(By.XPATH, '//li/a[@data-akorderby="1"]')
        rendez.send_keys(Keys.RETURN)

    if draga=='x':
        rendez=driver.find_element(By.XPATH, '//li/a[@data-akorderby="2"]')
        rendez.send_keys(Keys.RETURN)

    if ertekeles=='x':
        rendez=driver.find_element(By.XPATH, '//li/a[@data-akorderby="7"]')
        rendez.click()

    if nevszerint=='x':
         rendez=driver.find_element(By.XPATH, '//li/a[@data-akorderby="3"]')
         rendez.send_keys(Keys.RETURN)

    sleep (5)

#txt min és max ár szűrés
def ar_range(driver):
    try:
        lenyit=driver.find_element(By.XPATH, '//*[@id="morefilter-ar"]/a')
        
        lenyit.click()
        sleep(1)
        min=driver.find_element(By.XPATH, '//*[@id="cf_ar"]/input[2]')
        driver.execute_script("arguments[0].click();", min)
        sleep(1)
        min.send_keys(armin)

        max=driver.find_element(By.XPATH, '//*[@id="cf_ar"]/input[3]')
        max.send_keys(armax)

        ok=driver.find_element(By.XPATH, '//*[@id="cf_ar"]/span[2]')
        ok.click()
        sleep(3)
    except:
        min=driver.find_element(By.XPATH, '//input[@name="minprice"]')
        min.send_keys(armin)

        max=driver.find_element(By.XPATH, '//input[@name="maxprice"]')
        max.send_keys(armax)
        ok=driver.find_element(By.XPATH, '//*[@id="search-form-ok"]')
        ok.click()
        sleep(3)

#az egységek megkersése, és sorban beleírása egy új excel fájlba
def items(driver):
    end = 1
    workbook = xlsxwriter.Workbook(filenev+'.xlsx')
    worksheet= workbook.add_worksheet()

    k = math.floor((d)/25)+1
    end=1
    for j in range (k):
        
        items = driver.find_elements_by_xpath("//h2/a[@title]")
        x=len(items)
        sor=0+x*j
        

        for item in items:                
            
            nev=item.text

            item_ar=driver.find_element(By.XPATH, '//div/a[@class="price"][@*[contains(., "'+nev+'")]]')
            ar = item_ar.text
                            
            ar=ar.replace("Ft-tól","")
            ar=ar.replace("Ft","")
            ar=ar.replace(" ","")
            ar=int(ar)

            try:
                if end == d+1:
                    workbook.close()
                    quit
                else:
                    end=end+1
                    worksheet.write(sor,0, nev)
                    worksheet.write(sor,1, ar)
                    sor=sor+1
                continue
            except:
                
                if end == d+1:
                    workbook.close()
                    quit
                else:
                    end=end+1
                    continue
                

            worksheet.write(sor,0, nev)
            worksheet.write(sor,1, ar)

        try:
            next= driver.find_element(By.XPATH,'//a[@data-akpage [contains(., "Következő")]]' )
        
            try:
                next.click()
            except:
                next= driver.find_element(By.XPATH,'//a[@data-akpage [contains(., "Következő")]] [@onclick[contains(.,"normalProducts")]]' )
                next.click()
        except:
           workbook.close()
           quit
        sleep(3)

   

    workbook.close()


driver=init_driver()
login(driver)
search(driver)
filters(driver)
rendezes(driver)
ar_range(driver)
items(driver)
sleep (5)

driver.close()



    
