#from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.common.by import By
#import xlsxwriter
#driver = webdriver.Chrome('C:/Users/Váradi-Szabó András/Desktop/BIT/Python/chromedriver.exe')
#driver.get("https://www.arukereso.hu/belepes/")


x='alma'
y='körte'

print(x+' '+y)

except:
        #x = f.ljust(16)
        fooldal= driver.find_element(By.XPATH, '/html[1]/body[1]/header[1]/div[1]/div[1]/div[1]/a[1]/*[name()="svg"][1]/*[name()="use"][1]')
        fooldal.click()
        search = driver.find_element(By.NAME, 'st')
        WebDriverWait(driver, 5).until(EC.visibility_of(search))
        search.send_keys(f+' '+s)
        sleep(1)





for i in range(1, d+2):
                sor = i-1
                try:
                    item_nev = driver.find_element(By.XPATH, '(//h2/a[@data-akl2pp="%i"])' %i)
                    nev = item_nev.text

                    item_ar = driver.find_element(By.XPATH, '(//div/a[@data-akl2pp="%i"][@class="price"])' %i)
                    ar = item_ar.text 
                    if end == d+1:
                        workbook.close()
                        quit
                    else:
                     worksheet.write(sor,0, nev)
                     worksheet.write(sor,1, ar)
                     end=end+1
                    
                    
                except:
                    #worksheet.set_row(sor, options={'hidden': True})

                    if end == d+1:
                        workbook.close()
                        quit
                    else:
                     
                        continue



try:
                    item_nev = driver.find_element(By.XPATH, '(//h2/a[@data-akl2pp="%i"])' %i)
                    nev = item_nev.text

                    item_ar = driver.find_element(By.XPATH, '(//div/a[@data-akl2pp="%i"][@class="price"])' %i)
                    ar = item_ar.text
                    ar = ar.split(' Ft') [0]
                    
                    ar=int(ar)

                    if end == d+1:
                        workbook.close()
                        quit
                    else:
                        end=end+1
                    
                    
                except:
                    try:
                        item_nev = driver.find_element(By.XPATH, '(//h2/a[@data-akl2pp="%i"])' %i)
                        nev = item_nev.text

                        item_ar = driver.find_element(By.XPATH, '(//div/a[contains(@onclick, "'+str(nev)+'")][@class="price"])' %nev)
                        ar = item_ar.text
                        ar = ar[:-3]
                        ar=int(ar)
                        print(ar)

                        if end == d+1:
                            workbook.close()
                            quit
                        else:
                            end=end+1
                        continue
                    except:
                        worksheet.set_row(sor, options={'hidden': True})
                        if end == d+1:
                            workbook.close()
                            quit
                        else:
                            end=end+1
                        continue









item_nev = driver.find_element(By.XPATH, '(//div/h2/a[@data-akl2pp="%i"])' %i)
                    nev = item_nev.text

                    item_ar = driver.find_element(By.XPATH, '(//div/a[@data-akl2pp="%i"][@class="price"])' %i)
                    ar = item_ar.text
                    size = len(ar)

                    ar= ar[:size - 7]
                    ar=ar.replace(" ","")
                    ar=int(ar)
                     

                    if end == d+1:
                        workbook.close()
                        quit
                    else:
                        end=end+1






def items(driver):
    end = 1
    workbook = xlsxwriter.Workbook(filenev+'.xlsx')
    worksheet= workbook.add_worksheet()

    k = math.floor((d)/25)+1

    for j in range (k):
        

        if d>=25:
            
            for i in range(1, 26):
                sor = (i-1)+25*j
                try:
                    item_nev = driver.find_element(By.XPATH, '(//div/h2/a[@data-akl2pp="%i"])' %i)
                    nev = item_nev.text

                    item_ar = driver.find_element(By.XPATH, '(//div/a[@data-akl2pp="%i"][@class="price"])' %i)
                    ar = item_ar.text
                    size = len(ar)

                    ar= ar[:size - 7]
                    ar=ar.replace(" ","")
                    ar=int(ar)
                     

                    if end == d+1:
                        workbook.close()
                        quit
                    else:
                        end=end+1
                    
                    
                except:
                    try:
                        item_nev = driver.find_element(By.XPATH, '(//div/h2/a[@data-akl2pp="%i"])' %i)
                        nev = item_nev.text
                        id=item_nev.get_attribute('href')
                        id=id[-10:]
                        id=id[0:9]


                        item_ar = driver.find_element(By.XPATH, '(//div/a[contains(@onclick, "'+str(id)+'")][@class="price"])')
                        ar = item_ar.text
                        ar = ar.replace(' Ft', '')
                        ar=ar.replace(" ","")
                        ar=int(ar)
                        #ar=ar.split("Ft", [1])
                        #ar= ar[:size - 3]

                        if end == d+1:
                            workbook.close()
                            quit
                        else:
                            end=end+1
                            worksheet.write(sor,0, nev)
                            worksheet.write(sor,1, ar)
                        continue
                    except:
                        worksheet.set_row(sor, options={'hidden': True})
                        if end == d+1:
                                workbook.close()
                                quit
                        else:
                            #end=end+1
                            continue
                    

                worksheet.write(sor,0, nev)
                
                
                worksheet.write(sor,1, ar)


            next= driver.find_element(By.XPATH,'(//a[@data-akpage="Következő >"])' )
       
            next.send_keys(Keys.RETURN)       #print (nev+ar)
            sleep(3)
        else :
            for i in range(1, d+2):
                sor = i-1
                try:
                    item_nev = driver.find_element(By.XPATH, '(//div/h2/a[@data-akl2pp="%i"])' %i)
                    nev = item_nev.text

                    item_ar = driver.find_element(By.XPATH, '(//div/a[@data-akl2pp="%i"][@class="price"])' %i)
                    ar = item_ar.text
                    size = len(ar)

                    ar= ar[:size - 7]
                     

                    if end == d+1:
                        workbook.close()
                        quit
                    else:
                        end=end+1
                    
                    
                except:
                    try:
                        item_nev = driver.find_element(By.XPATH, '(//div/h2/a[@data-akl2pp="%i"])' %i)
                        nev = item_nev.text
                        id=item_nev.get_attribute('href')
                        id=id[-10:]
                        id=id[0:9]


                        item_ar = driver.find_element(By.XPATH, '(//div/a[contains(@onclick, "'+str(id)+'")][@class="price"])')
                        ar = item_ar.text
                        ar = ar.replace(' Ft', '')
                        ar=ar.replace(" ","")
                        ar=int(ar)
                        #ar=ar.split("Ft", [1])
                        #ar= ar[:size - 3]

                        if end == d+1:
                            workbook.close()
                            quit
                        else:
                            end=end+1
                            worksheet.write(sor,0, nev)
                            worksheet.write(sor,1, ar)
                        continue
                    except:
                        worksheet.set_row(sor, options={'hidden': True})
                        if end == d+1:
                                workbook.close()
                                quit
                        else:
                            #end=end+1
                            continue
                    

                worksheet.write(sor,0, nev)
                
                ar=ar.replace(" ","")
                ar=int(ar)
                worksheet.write(sor,1, ar)

            #workbook.close()
   

    workbook.close()



    #//div[@itemprop="breadcrumb"])[%i]' %i
    #//div[@itemprop="adat-ak12pp"])[%i]' %i
    #//div[@class='name ulined-link']//a[@title='Sony WH-1000XM4'][normalize-space()='Sony WH-1000XM4']



    <a data-akpage="Következő&nbsp;>" rel="nofollow" href="https://eger.arukereso.hu/f:ar=2000-15000/?orderby=2&amp;st=vezet%C3%A9k+n%C3%A9lk%C3%BCli&amp;start=25" onclick="_akq.push(['ak.filter.changePage',this]);return false;">Következő&nbsp;&gt;</a>
    <a data-akpage="Következő&nbsp;>" href="https://www.arukereso.hu/CategorySearch.php?maxprice=15000&amp;minprice=2000&amp;orderby=2&amp;st=vezet%C3%A9k+n%C3%A9lk%C3%BCli+gaming+eg%C3%A9r&amp;start=20" onclick="_akq.push(['ak.search.normalProducts','normal-product-list',20,1]);return false;">Következő&nbsp;&gt;</a>


  <a data-akpage="Következő&nbsp;>" href="https://www.arukereso.hu/CategorySearch.php?maxprice=15000&amp;minprice=2000&amp;orderby=2&amp;st=vezet%C3%A9k+n%C3%A9lk%C3%BCli+gaming+eg%C3%A9r&amp;start=12" onclick="_akq.push(['ak.search.partnerProducts','partner-product-list',12]);return false;">Következő&nbsp;&gt;</a>  
  <a data-akpage="Következő&nbsp;>" href="https://www.arukereso.hu/CategorySearch.php?maxprice=15000&amp;minprice=2000&amp;orderby=2&amp;st=vezet%C3%A9k+n%C3%A9lk%C3%BCli+gaming+eg%C3%A9r&amp;start=20" onclick="_akq.push(['ak.search.normalProducts','normal-product-list',20,1]);return false;">Következő&nbsp;&gt;</a>
  <a data-akpage="Következő&nbsp;>" rel="nofollow" href="https://eger.arukereso.hu/f:ar=2000-15000/?orderby=2&amp;st=vezet%C3%A9k+n%C3%A9lk%C3%BCli&amp;start=25" onclick="_akq.push(['ak.filter.changePage',this]);return false;">Következő&nbsp;&gt;</a>

  //a[@data-akpage [contains(., "Következő")]][@href [contains(.,"normalProducts")]]


//a[@data-akpage [contains(., "Következő")]] [@onclick[contains(.,"normalProducts")]] | //a[@data-akpage [contains(., "Következő")]] [@rel="nofollow"])