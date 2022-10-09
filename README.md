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
   
5.  **느낀점**

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
      
        ![detection1](https://user-images.githubusercontent.com/95748637/194758402-4d18f286-6af9-440e-a921-bb46404f247e.png)
        사랑앵무 94.1 이라는 높은 정확도를 보여준다. 
        ![hoopoetest](https://user-images.githubusercontent.com/95748637/194759985-46ffc729-9d72-4dd8-9eae-779e9b1c1bfc.png)
        후투티 또한 정확도가 높게 나온다. 
        ![test3](https://user-images.githubusercontent.com/95748637/194759993-79b21219-12fb-4292-93e5-5a98eb6540bf.png)
        모란앵무도 높게 나왔다. 
        ![agapornis test](https://user-images.githubusercontent.com/95748637/194760035-1bddf66e-fba5-4d07-b516-ec1b8287cf5a.png)
        그러나 모란앵무중 사랑앵무와 비슷한 모란앵무는 사랑앵무로 잘못 판단하였다. 
        ![passer_test](https://user-images.githubusercontent.com/95748637/194760600-b37c888d-daa2-47e3-886e-3b4940562550.png)
        참새또한 높은 확률 
        
        모란앵무와 사랑앵무의 차이는 육안으로 콧구멍이 보이는 새는 사랑앵무 보이지 않는 새는 모란앵무라고 하여 판별이 가능한데 아직 거기까지는 이미지 학습이 되지 않은것으로 보입니다. 
        
        다음번 개선사항은 종마다 특징이 잘 나타나는 얼굴 사진들을 더 추가해야할 것으로 보이고 지금은 종들을 크게 뭉뚱그려 학습을 시켰는데 모란 앵무 중에서도 나뉘게 되는 부분이 있어 (예를들면 색상) 
        조금 더 세세하게 종을 나눠서 학습시키게 되면 더욱 명확히 구별할 수 있는 object detection model 이 될 수 있을거라 생각합니다. 
        
        
      - video detection 
        비디오 디텍션을 했으나 10mb 넘어 첨부가 어려운점.. 양해부탁드립니다. 
        
    ## 5. 느낀점    
      
      
      
      
      
      
      
