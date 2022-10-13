# bird-Image_Classification(Object Detection) 

## yolov4 

1. **이론**
   1. YOLOv4(You Only Look Once)
   2. Object Detection 
   3. 모델 설명
  
2. **학습데이터 수집 & 라벨링작업** 
    - 데이터 구성 : train image (class 당 100장으로 
    1. 데이터 수집 
    2. 라벨링 작업 (lableImg) 
    
3. **yolov4훈련 과정**

4. **Object Detection 실행하기** 

   - image detection
   - video detection
   - wepcam detection 
   
5.  **느낀점**

6.  **결론** 

    ## 1. 이론

    ### 1.1. Yolov4(You only look once)

    **YOLO**는
    -  One-Stage Detectors 제품군에 속합니다.
       - 단계 감지(원샷 감지라고도 함)는 이미지를 한 번만 보는 것입니다.
    - Yolo는 CV(Computer vision)에서 object detection(이미지에 사각박스를 만드는 작업)분야에 해당되는 기술입니다.
    - R-CNN(regional-CNN), Fast R-CNN, Faster R-CNN 등과 비교하여 처리속도가 빠르기때문에 실시간 detection이 가능합니다.
    ![alt text](https://github.com/hoya012/deep_learning_object_detection/raw/master/assets/deep_learning_object_detection_history.PNG)
    (이미지 출처:  https://github.com/hoya012/deep_learning_object_detection )

    ![alt text](https://wikidocs.net/images/page/162467/0_Yolo_v4_Table.png)
    위의 사진을 보게 되면 YOLOv4 는
    1.  YOLOv4는 높은 처리 프레임 속도를 유지하며 state-of-the art 정확도를 자랑합니다.
    2.  Tesla V100 (GPU환경) 에서 대략 65FPS의 추론 속도로 MS COCO에 대해 43.5% AP의 정확도를 달성하였습니다. 
    더욱 자세한 모델에 대한 설명은 [링크](https://wikidocs.net/163565)에 들어가시면 나와있습니다. 

    ### 1.2 Object Detection 
        여러개의 사물이 존재하는 상황에서 각 사물의 위치와 이름을 찾는 작업입니다. : 객체 탐지 

      입력이미지에서 클래스의 후보 영역을 추출하는 기술 구현이며 간단하게 과정을 알아보겠습니다. 
        
      1.  Region Proposal   
          사진에서 물체가 있을 법한 위치를 찾는 작업이며 이미지에서 다양한 형태의 윈도우(window) 를 슬라이딩하여 물체가 존재하는지 확인합니다.
            
      2.  Selective search   
          인접한 영역끼리 유사성을 측정하여 큰 영역으로 차례대로 통합해 나갑니다. 
            
      3. Intersection over uion   
          사물이 유사하다고 평가하는 방법입니다.   
          IoU : 두 바운딩 박스가 겹치는 비율을 의미합니다.   
          만약 mAP@0.5 라면 정답과 예측의 IoU 가 50% 이상일때 정답으로 판별하겠다는 의미입니다.   
          같은 클래스끼리 IoU 가 50% 이상일 때 낮은 confidence 의 box 를 제거한다는 의미입니다.   
          
      4.  NMS (None Maximum Suppression)   
          여러개의 바운딩 박스를 하나로 통합하는 방법입니다. 
          IoU 가 특정 임계점 (Threshold) 이상인 중복 box 제거합니다. 

      5.  R - CNN    
          warped image 를 CNN 에 넣어 이미지 feature 를 추출하고 → SVM 에 넣고 CLASS 분류 결과 얻습니다. → feature 을 regressor 에 넣어 bounding box 예측하게 됩니다.

     ### 1.3. 모델 설명

    먼저 이미지(훈련이미지)를 448x448x3(가로 세로 448, RGB 색상채널이라서 3개가 있음)로 조정해준 다음, 컨볼루셔널 레이어를 통해서 학습하고, 검출하게 됩니다.
    자세한 모델 설명은 [링크](https://curt-park.github.io/2017-03-26/yolo/) 를 클릭하면 볼 수 있습니다. 
    darknet 모델을 깃허브 [링크](https://github.com/AlexeyAB/darknet.git) 에서 다운받았고 해당 모델 학습환경에 맞추어 설정합니다.  
    
    ## 2. 학습데이터 수집 & 라벨링작업
    
      ### 2.1.데이터 수집 & 정제 

      데이터 수집은 google, naver, Bing 홈페이지에서 이미지수집하였고 python 언어로 selenium package 를 활용해 코드를 짠 뒤 HJ_crawling module 로 만들었습니다. 

      데이터 정제는 아예관계없는 사진 ( 사료, 인물 등) 다른 동물, 다른 피사체에 비해 많이 작은 사진, 중복되는 사진 등을 처리하였습니다. 


      ### 2.2.라벨링 작업 (lableImg) 

     **6개의 클래스** 
      1. 사랑앵무새(잉꼬) : Budgerigar
      2. 왕관앵무새 : Cockatiel
      3. 후투티 : hoopoe
      4. 까마귀 : Corvus
      5. 참새 : Passer
      6. 모란앵무 : Agapornis
      
      종별로 100장 총 600장으로 훈련을 했습니다. 
      ![alt text](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/1b6a426a-afc1-438c-838e-4defb02574aa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221009%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221009T123947Z&X-Amz-Expires=86400&X-Amz-Signature=cf7da78d44bd768a70c5866c05d8585c48cbcbaad429c70b725efd7671eb9fbd&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)
          
    ## 3. yolov4훈련 과정
    
      - 리눅스 명령어를 이용해 GPU , CUDNN 을 사용하겠다고 변경
      - 사물 검출에 필요한 코드(4가지) 를 GitHub 주소에서 다운 받습니다.   
       1. creating-files-data-and-name.py   
       2. creating-train-and-test-txt-files.py   
       3. 'Custom Object detection live video.ipynb'   
       4. Rename_files.ipynb      
       
     역할 : 훈련시키기 전에 파일들의 이름을 바꾸고 변경하는 코드들입니다. 

     - 학습하다 메모리 초과로 중단되는것을 막기 위해 배치사이즈 조정합니다. 
     - 19번재 라인 maxbatch 값또한 변경합니다
        - macbatch = classes * 2000 
     - 21번째 라인에서는 maxbatch *0.8 , maxbatch * 0.9 값으로 변경합니다. 
     - 기존 darknet 에서는 클래스 개수가 80 개였는데 지금 클래스 수에 맞게 6개로 변경합니다. 
     - 합성곱 시 쓰이는 filter 의 갯수또한 클래스 수에 맞게 다시 계산하여 값을 변경합니다. 
        - filters = (4+1+classes) *3 

      이렇게 각자 환경설정에 맞게 값을 변경한 뒤   
      labelled_data.data(라벨데이터), yolov4_custom.cfg(환경설정) , yolov4.conv.137(컨볼루션층) 을 가지고 데이터를 훈련시킵니다. 
      
      데이터를 훈련 한 뒤 로컬로 weights 와 cfg 파일을 내려 받습니다. 

    ## 4. Object Detection 실행하기 
      
      - image detection 
        
        사랑앵무 정확도 높음 
        ![detection1](https://user-images.githubusercontent.com/95748637/194758402-4d18f286-6af9-440e-a921-bb46404f247e.png)
        
        후투티(hoopoe) 정확도 높음 
        ![hoopoetest](https://user-images.githubusercontent.com/95748637/194759985-46ffc729-9d72-4dd8-9eae-779e9b1c1bfc.png)
        
        모란앵무도 높음 
        ![test3](https://user-images.githubusercontent.com/95748637/194759993-79b21219-12fb-4292-93e5-5a98eb6540bf.png)
        
        **모란앵무중 사랑앵무와 비슷한 모란앵무를 사랑앵무로 잘못 판단.**
        ![agapornis test](https://user-images.githubusercontent.com/95748637/194760035-1bddf66e-fba5-4d07-b516-ec1b8287cf5a.png)
        
        참새(passer) 정확도 높음 
        ![passer_test](https://user-images.githubusercontent.com/95748637/194760600-b37c888d-daa2-47e3-886e-3b4940562550.png)
        
        
       
        
      - video detection 
        
        
      - wepcam detection 
      
        
    ## 5. 느낀점    
    
    이미지 디텍션은 정확도가 높게 나오지만 , 비디오 디텍션이나, 웹캠 디텍션은 이미지에비해 성능이 떨어짐을 볼 수 있습니다.   
    - 이미지 디텍션 정확도가 보통 0.80-90 정도   
    - 비디오, 웹캠 디텍션 정확도는 보통 0.30-0.50 사이 의 정확도   
    
    학습사진들이 대부분 옆모습이기 때문에 사진또한 옆모습으로 주어지면 정확도가 높게 나오지만 비디오, 웹캠 같은경우는 움직이는 물체이기때문에 옆모습이 아닌 모습들도 탐지 되기 때문에 정확도가 낮게 나온것으로 유추 됩니다.   
    또한 까마귀같은 경우는 거의 검정색인 새의 실루엣 정도로 학습이 되었기 때문에 다른 새종류가 어둡게 나오는 경우 무조건 까마귀로 예측하게 되는 경우도 있습니다. 
     
    모란앵무와 사랑앵무의 차이는 육안으로 **콧구멍**이 보이는 새는 사랑앵무이고,  보이지 않는 새는 모란앵무인 것으로 판별이 가능하나, 아직 거기까지는 이미지 학습이 되지 않은것으로 보입니다. 
    학습데이터가 다양해야한다는것과, 종에서도 색깔별로 조금더 클래스를 세분화 하여 학습시키면 더 명확하게 구별할 수 있을거라 생각한다. 
    
    ## 6. 결론 
    
    1. 종마다 특징이 잘 나타나는 얼굴 사진들을 더 추가해야할 것 : 콧구멍의 육안구별 유무를 위해 
    2. 종들의 특성을 조금더 세분화 (새의 색상) 하여 클래스를 재조정하고 학습하기 
    
    이렇게 두가지 정도를 조금더 개선하면 좀 더 나은 예측율을 가진 Birds Object Detection Model (yolov4) 가 될 것이라 예측합니다. 
    
    감사합니다. 

    
      
      
      
      
      
      
