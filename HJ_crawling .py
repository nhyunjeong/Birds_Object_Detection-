############### 1. Google Image Crawling ###############

def google_scroll_image (keyword,folder_name) :

    import urllib.request                     # 파이썬에서 웹의 url 을 인식할 수 있게 하는 모듈 
    from  bs4 import BeautifulSoup
    from selenium import webdriver          # 웹 애플리케이션의 테스트를 자동화하기 위한 프레임 워크(크롬 웹크라우져 자동제어 위함)
    from selenium.webdriver.common.keys import Keys   # 키보드를 알아서 눌러야해서 필요한 모듈 
    from selenium.webdriver.common.by import By # 셀레니움 4.3.0버전 업뎃되면서 바뀐 find_element 
    import time                                # 중간중간 sleep 을 걸어야 해서 time 모듈 import
    from  tqdm import tqdm_notebook
    import os  # os 패키지 (폴더생성) 
    
    ########################### url 받아오기 ###########################

    # 웹브라우져로 크롬을 사용할거라서 크롬 드라이버를 다운받아 위의 위치에 둔다
    # 팬텀 js로 하면 백그라운드로 실행할 수 있음
    
    binary = 'C:\\data\\chromedriver_win32\\chromedriver.exe'

    # 브라우져를 인스턴스화
    browser = webdriver.Chrome(binary)

    # 구글의 이미지 검색 url 받아옴(키워드를 아무것도 안 쳤을때의 url)
    browser.get("https://www.google.co.kr/imghp?hl=ko&tab=wi&ei=l1AdWbegOcra8QXvtr-4Cw&ved=0EKouCBUoAQ")

    # 검색창에 검색 키워드를 입력하기 위해 웹페이지의 검색창의 클래스 이름찾아서 해당 좌표 지정 (그 좌표는 elem 객체에 넣음 )
    elem = browser.find_element(By.XPATH,"//*[@class='gLFyf gsfi']") 



    ########################### 검색어 입력 ###########################

    # elem 이 input 창과 연결되어 스스로 햄버거를 검색
    elem.send_keys(keyword)

    # 웹에서의 submit 은 엔터의 역할을 함
    elem.submit()

    ########################### 반복할 횟수 ###########################


    # 스크롤을 내리려면 브라우져 이미지 검색결과 부분(바디부분)에 마우스 클릭 한번 하고 End키를 눌러야함
    for i in tqdm_notebook(range(0,10), desc = '이미지 검색 1'):
        browser.find_element(By.XPATH,"//body").send_keys(Keys.END)
        time.sleep(3)                  # END 키 누르고 내려가는데 시간이 걸려서 sleep 해줌
    
    # 결과더보기
    browser.find_element(By.XPATH,"//*[@class='mye4qd']").send_keys(Keys.ENTER)
    
    for i in tqdm_notebook(range(0,10),desc = '이미지 검색 2'):
        browser.find_element(By.XPATH,"//body").send_keys(Keys.END)
        time.sleep(3)
    
    time.sleep(3)                      # 네트워크 느릴까봐 안정성 위해 sleep 해줌
    html = browser.page_source         # 크롬브라우져에서 현재 불러온 소스 가져옴
    soup = BeautifulSoup(html, "lxml") # html 코드를 검색할 수 있도록 설정


    ########################### url & 그림파일 저장 ###########################

    # 이미지에 대한 상세 url 을 params리스트에 담는 함수 
    params = []      
    imgList = soup.find_all("img", class_="rg_i Q4LuWd")  # 구글 이미지 url 이 있는 img 태그의 _img 클래스에 가서
    
    for im in imgList:
        try :
            params.append(im["src"])                   # params 리스트에 image url 을 담음
        except KeyError:
            params.append(im["data-src"])  # src 에서 못가져오면 data-src 에서 가져와라

    # 이미지의 상세 url 의 값이 있는 src 가 없을 경우
    # data-src 로 가져오시오 ~ 
    print('%d개의 이미지 파일을 찾았습니다.'%len(params))
    
    path = 'C:\\image_crawling_data\\google_' + folder_name # d드라이브 밑에 저장할 폴더 이름
    os.mkdir(path)  #폴더 생성
    
    # enumerate 를 이용하여 번호와 함께 이미지를 가져오도록 하는데 1 번부터 가져와라 
    for idx, p in  tqdm_notebook(enumerate(params,1), desc = '이미지 파일 저장'):  
        # 다운받을 폴더경로 입력
        urllib.request.urlretrieve(p, path +'\\google_'+keyword+'_' + str(idx) + ".jpg") # 새로만든 폴더아래에 크롤링이미지저장 

    # enumerate 는 리스트의 모든 요소를 인덱스와 쌍으로 추출
    # 하는 함수 . 숫자 1은 인덱스를 1부터 시작해라 ~

    # 끝나면 브라우져 닫기
    browser.quit()
    print('%s 에 이미지 파일 %d개가 저장되었습니다.'%(path,len(params)))
	
	
	
	
	
	
	
	
	
	
	
############### 2. Naver Image Crawling  ###############

def naver_image_scroll(keyword,folder_name) :
    import urllib.request                     # 파이썬에서 웹의 url 을 인식할 수 있게 하는 모듈 
    from  bs4 import BeautifulSoup
    from selenium import webdriver          # 웹 애플리케이션의 테스트를 자동화하기 위한 프레임 워크(크롬 웹크라우져 자동제어 위함)
    from selenium.webdriver.common.keys import Keys   # 키보드를 알아서 눌러야해서 필요한 모듈 
    from selenium.webdriver.common.by import By # 셀레니움 4.3.0버전 업뎃되면서 바뀐 find_element 
    import time                                # 중간중간 sleep 을 걸어야 해서 time 모듈 import
    from tqdm import tqdm_notebook
    import os  # os패키지 임포트

    ########################### url 받아오기 ###########################

    # 웹브라우져로 크롬을 사용할거라서 크롬 드라이버를 다운받아 위의 위치에 둔다
    # 팬텀 js로 하면 백그라운드로 실행할 수 있음

    binary = 'C:\\data\\chromedriver_win32\\chromedriver.exe'
    #binary = '/Users/loono/Desktop/data/Chromedriver'

    # 브라우져를 인스턴스화
    browser = webdriver.Chrome(binary)

    # 구글의 이미지 검색 url 받아옴(키워드를 아무것도 안 쳤을때의 url)
    browser.get("https://search.naver.com/search.naver?where=image&amp;sm=stb_nmr&amp;")

    # 검색창에 검색 키워드를 넣기 위해서 웹페이지의 검색창의 클래스 이름을 찾아서 검색창에 해당하는 부분이 
    # 어디다라고 알려주는 elem 객체를 만듭니다.

    #elem = browser.find_element("//*[@class='gLFyf gsfi']") 
    elem = browser.find_element(By.ID, "nx_query") 

    ########################### 검색어 입력 ###########################

    # elem 이 input 창과 연결되어 스스로 키워드를 검색
    elem.send_keys(keyword)

    # 웹에서의 submit 은 엔터의 역할을 함
    elem.submit()

    ########################### 반복할 횟수 ###########################

    # 스크롤을 내리려면 브라우져 이미지 검색결과 부분(바디부분)에 마우스 클릭 한번 하고 End키를 눌러야함
    for i in tqdm_notebook(range(1, 20), desc = '이미지 검색 '):
        browser.find_element(By.XPATH, "//body").send_keys(Keys.END)
        time.sleep(5)                  # END 키 누르고 내려가는데 시간이 걸려서 sleep 해줌


    time.sleep(5)                      # 네트워크 느릴까봐 안정성 위해 sleep 해줌
    html = browser.page_source         # 크롬브라우져에서 현재 불러온 소스 가져옴
    soup = BeautifulSoup(html, "lxml") # html 코드를 검색할 수 있도록 설정


    ########################### 그림파일 저장 ###########################

    # 이미지에 대한 상세 url 을 params리스트에 담는 함수 

    params = []
    imgList = soup.find_all("img", class_="_image _listImage")  # 구글 이미지 url 이 있는 img 태그의 _img 클래스에 가서
    for im in imgList:
        try :
            params.append(im["src"])                   # params 리스트에 image url 을 담음
        except KeyError:
            params.append(im["data-src"])              # src 에서 못가져 오면 data-src 에서 가져와라 


    print('%d개의 이미지 파일을 찾았습니다.'%len(params))   
    
    path = 'C:\\image_crawling_data\\naver_' + folder_name # c드라이브 밑에 저장할 폴더 이름
    os.mkdir(path)  #폴더 생성
        # enumerate 를 이용하여 번호와 함께 이미지를 가져오도록 하는데 1 번부터 가져와라 
    for idx, p in tqdm_notebook(enumerate(params,1), desc = '이미지 파일 저장중'):
        # 다운받을 폴더경로 입력
        urllib.request.urlretrieve( p , path +'\\naver_' + keyword +'_'+ str(idx) + ".jpg")

    # 끝나면 브라우져 닫기
    browser.quit()
    print('%s 에 이미지 파일 %d개가 저장되었습니다.'%(path,len(params)))   














############### 3. BING 이미지 스크롤 함수    ###############

def bing_image_scroll(keyword,folder_name):
   
    import urllib.request                     # 파이썬에서 웹의 url 을 인식할 수 있게 하는 모듈 
    from  bs4 import BeautifulSoup
    from selenium import webdriver          # 웹 애플리케이션의 테스트를 자동화하기 위한 프레임 워크(크롬 웹크라우져 자동제어 위함)
    from selenium.webdriver.common.keys import Keys   # 키보드를 알아서 눌러야해서 필요한 모듈 
    from selenium.webdriver.common.by import By # 셀레니움 4.3.0버전 업뎃되면서 바뀐 find_element 
    import time                                # 중간중간 sleep 을 걸어야 해서 time 모듈 import
    from tqdm import tqdm_notebook
    import os  # os패키지 임포트
    
    ########################### url 받아오기 ###########################

    # 웹브라우져로 크롬을 사용할거라서 크롬 드라이버를 다운받아 위의 위치에 둔다
    # 팬텀 js로 하면 백그라운드로 실행할 수 있음

    binary = 'C:\\data\\chromedriver_win32\\chromedriver.exe'

    # 브라우져를 인스턴스화
    browser = webdriver.Chrome(binary)

    #  bing 이미지 검색 url 받아옴(키워드를 아무것도 안 쳤을때의 url)
    browser.get("https://www.bing.com/?scope=images&nr=1&FORM=NOFORM")
    time.sleep(3) 
    
    # 검색창에 검색 키워드를 넣기 위해서 웹페이지의 검색창의 클래스 이름을 찾아서 검색창에 해당하는 부분이 
    # 어디다라고 알려주는 elem 객체를 만듭니다.
    elem = browser.find_element(By.ID,"sb_form_q") 

    ########################### 검색어 입력 ###########################

    # elem 이 input 창과 연결되어 스스로 키워드 를 검색
    elem.send_keys(keyword)

    # 웹에서의 submit 은 엔터의 역할을 함
    elem.submit()
    
    ########################### 반복할 횟수 ###########################

    # 스크롤을 내리려면 브라우져 이미지 검색결과 부분(바디부분)에 마우스 클릭 한번 하고 End키를 눌러야함
    for i in tqdm_notebook(range(0,40), desc = '이미지 검색 1'):
         
        browser.find_element(By.XPATH,"//body").send_keys(Keys.END)
        time.sleep(2)                  # END 키 누르고 내려가는데 시간이 걸려서 sleep 해줌


    time.sleep(2)                      # 네트워크 느릴까봐 안정성 위해 sleep 해줌
    html = browser.page_source         # 크롬브라우져에서 현재 불러온 소스 가져옴
    soup = BeautifulSoup(html, "lxml") # html 코드를 검색할 수 있도록 설정


    ########################### 그림파일 저장 ###########################

    # 이미지에 대한 상세 url 을 params리스트에 담는 함수 

    params = []
    imgList = soup.find_all("img", class_="mimg")  # bing이미지 url 이 있는 img 태그의 mimg 클래스에 가서
    for im in imgList:
        try :
            params.append(im["src"])                   # params 리스트에 image url 을 담음
        except KeyError:
            params.append(im["data-src"])              # src 에서 못가져 오면 data-src 에서 가져와라 


    imgList2 = soup.find_all("img", class_="mimg rms_img")  # bing이미지 url 이 있는 img 태그의 mimg rms_img 클래스에 가서
    for im in imgList2:
        try :
            params.append(im["src"])                   # params 리스트에 image url 을 담음
        except KeyError:
            params.append(im["data-src"])              # src 에서 못가져 오면 data-src 에서 가져와라 
            
    print('%d개의 이미지 파일을 찾았습니다.'%len(params))
    
    path = 'C:\\image_crawling_data\\bingimg_' + folder_name # c드라이브 밑에 저장할 폴더 이름
    os.mkdir(path)  #폴더 생성
    # enumerate 를 이용하여 번호와 함께 이미지를 가져오도록 하는데 1 번부터 가져와라 
    for   idx, p  in tqdm_notebook(enumerate(params,1), desc = '이미지 파일 저장'):  
#       urllib.request.urlretrieve( p ,"c:/googleimages/" +'google_'+ keyword+'_'+ str(idx) + ".jpg") #기존 코드
        urllib.request.urlretrieve(p, path +'\\bingimg_'+ keyword+'_' + str(idx) + ".jpg") # 수정코드 (새로만든폴더아래저장)


    # 끝나면 브라우져 닫기
    browser.quit()    
    print('%s 에 이미지 파일 %d개가 저장되었습니다.'%(path,len(params)))    
    


###############################################################################################
################################### 메인 함수 ###################################################   
def main() :    
    print('='*21,'데이터 수집(crawling) 작업','='*21)
    print('1. Google Image Crawling') # 
    print('2. Naver Image Crawling')
    print('3. Bing Image Crawling')
    print('='*70)
    
    num = int(input('작업 번호 선택'))
	
    if num == 1 :
        keyword = input('수집할 Google Image 키워드 입력 : \n')
        folder_name = input('\n 새로생성하여 저장할 폴더명입력하세요 d:\\image crawling\\google_fordername\n')
        
		google_scroll_image (keyword,folder_name) # 구글 이미지 스크롤링 함수 실행         
		
    elif num == 2 :
        keyword = input('수집할 Naver Image 키워드 입력 : ')
        folder_name = input('\n 새로생성하여 저장할 폴더명입력하세요 d:\\image crawling\\naver_fordername\n')  
        
		naver_image_scroll(keyword,folder_name) # 네이머 이미지 스크롤링 함수 실행 
    
	elif num == 3 :
        keyword = input('Bing Image 키워드를 입력하세요 : ')   
        folder_name = input('\n 새로생성하여 저장할 폴더명입력하세요 d:\\image crawling\\bing_fordername\n')          
        
		bing_image_scroll(keyword,folder_name) # bing 이미지 스크롤링 함수 실행 
				
