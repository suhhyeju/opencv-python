# IMG Flip and Face Blurring with OpenCV
#### -  Flipping and blurring an img by detecting faces using OpenCV and Python.   

 ---
 - ### **Description and Purpose of this Project**  
   > This project uses OpenCV and Python to detect faces in images and apply blur processing to the corresponding areas. It also goes through the process of flipping the face area and reinserting into the image. These functions can make it difficult to identify individuals, enhancing privacy and data stability. Therefore, it can be used to anonymize faces or protect sensitive information in images. This project provides information on face detection and various image processing, and presents a foundation for wider range of fields.

- ### **Key Points**    
  ##### 1. **Steps**
    > a. Import Image: Use OpenCV to import the target image. 
    > b. Face detection: Use the Haar Cascade classifier to detect faces in images. 
    > c. Blur processing: Apply Gaussian blur processing to the detected face area.
    > d. Flip: Flip the detected face area horizontally.
    > e. Results: The flipped, blurry face will be applied to the original image.
   
  ##### 2. **Assumption**
  > The above code is based on face image detection.
  ##### 3. **Reference object properties**
    > a. Python must be installed.
    > b. OpenCV must be installed.
    > c. The Haar Cascade Classifier file (haarcascade_frontalface_default.xml) must exist.
   >d. A target image file is required to perform face detection and processing.
     (The image file must be located in the same directory as the code, or the image must be in the path specified in the code.)
- ### **Requirements (with versions)**      
  > 1. Python (3.8.13)  
  > 2. OpenCV (4.6.0)  

- ### **Results**  
  ![original](./images/cha.png)  
  ![blur](./images/cha_blur.png)  
  ![original2](./images/go.png)  
  ![blur2](./images/go_blur.png)  

202133721 박채연 202135425 서혜주 202133725 성윤지 조혜린 202235130
