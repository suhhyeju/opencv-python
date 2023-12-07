# IMG Flip and Face Blurring with OpenCV
#### -  Flipping and blurring an img by detecting faces using OpenCV and Python.   

 ---
 - ### **Description and Purpose of this Project**  
   > 이 프로젝트는 OpenCV와 Python을 활용하여 이미지에서 얼굴을 검출하고, 해당 영역에 블러처리를 적용한다. 또한 얼굴 영역을 뒤집어 이미지에 다시 삽입하는 과정을 거친다.  이러한 기능은 개인의 식별을 어렵게 만들어 주어 사생활 보호와 데이터 안정성을 강화할 수 있다. 따라서 주로 이미지에서 얼굴을 익명화 하거나 민감 정보를 보호하는 데 활용할 수 있다. 이 프로젝트에서는 얼굴 검출과 다양한 이미지 처리에 대한 정보를 제공하며, 더 넓은 분야에 쓰이기 위한 기반을 제시한다.  

- ### **Key Points**    
  ##### 1. **Steps**
    > a. 이미지 불러오기: OpenCV를 사용하여 대상 이미지를 불러온다.  
    > b. 얼굴 검출: Haar Cascade 분류기를 이용하여 이미지에서 얼굴을 검출한다.  
    > c. 블러처리: 검출된 얼굴 영역에 가우시안 블러 처리를 적용한다.
    > d. 뒤집기: 검출된 얼굴 영역을 수평으로 뒤집는다.
    > e. 결과: 뒤집히고 블러처리된 얼굴이 원본 이미지에 적용된다.     
  ##### 2. **Assumption**
  > 위의 코드에서는 얼굴 이미지 검출을 기반으로 하였다.  
  ##### 3. **Reference object properties**
    > a. Python이 설치되어 있어야 한다.  
    > b. OpenCV가 설치되어 있어야 한다.  
    > c. Haar Cascade Classifier 파일(haarcascade_frontalface_default.xml)이 존재해야 한다.  
   > d. 얼굴 검출 및 처리를 수행할 대상 이미지 파일이 필요하다.   
     (해당 이미지 파일이 코드와 같은 디렉토리에 위치하거나, 코드에서 지정한 경로에 이미지가 있어야 한다.)  
- ### **Requirements (with versions)**      
  > 1. Python (3.8.13)  
  > 2. OpenCV (4.6.0)  

- ### **Results**  

202133721 박채연 202135425 서혜주 202133725 성윤지 조혜린 202235130
