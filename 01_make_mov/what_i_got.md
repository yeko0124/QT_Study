### 아직 정리 중,,

# 1. tqdm

      from tqdm import tqdm
* Self-taught about tqdm, especially processing bar. 

* This is how it is used in python.
        
        # desc: description / images: list=[path/to/image.*] 
        # images = [/Users/name/Desktop/seq_imgs/filename_0001.png, /Users/name/Desktop/seq_imgs/filename_0002.png]  
  
          for image in tqdm(images, desc="Creating GIF", unit="image"): 
                  frames.append(imageio.imread(os.path.join(self.dpath, image)))
* tqdm을 사용하지 않을거면,

      for image in images:
  
  처럼, images를 바로 for loop에 넣어주면 되는데, tqdm을 쓰게 될 경우, tqdm으로 감싸는 느낌인 듯.
  

## 2. imageio -> gif
    import imageio

* I am not sure, but according to i studied today, **imageio** is a module which can create images to gif.

  * frame = [] : image들을 하나하나 적용해서 append할 빈 리스트가 필요함 

        frames = []
        for image in tqdm(images, desc="Creating GIF", unit="image"):
              frames.append(imageio.imread(os.path.join(self.dpath, image)))
  
  여기서 >> imread(os.path.join(self.dpath, image)) 를 설명하자면, 
  imageio가 video를 만들 때는, cv2를 넣으면 되는데, 뭐 여튼 이미지가 있는 경로와 이미지의 경로를 함께 join 시켜서 
  frames라는 리스트에 append를 하게 된다. 이때 imageio.imread라는 모듈을 사용해서 이미지를 읽어옴

### 추가 설명
imread는 이미지를 읽어오는 함수. imageio.imread와 cv2.imread는 각각 이미지를 읽어오는 데 사용

-  ####  imageio.imread:
    imageio는 다양한 이미지 및 비디오 파일 형식을 지원하는 파이썬 라이브러리로,
    imageio.imread 함수는 이미지 파일을 읽어 NumPy 배열로 반환한다고 함. 
  
    ```
    import imageio
    image = imageio.imread('path/to/image.jpg')

-    ####  cv2.imread:

    cv2는 OpenCV(Open Source Computer Vision Library)의 파이썬 바인딩으로, 이미지 처리 및 컴퓨터 비전 작업에 사용.
  cv2.imread 함수는 이미지 파일을 읽어 NumPy 배열로 반환한다고 함.
  기본적으로 이미지를 BGR 포맷으로 읽어옴. (BGR format: )
사용법:
python
Copy code
import cv2
image = cv2.imread('path/to/image.jpg')
  * 
    
            imageio.mimsave(out, frames, duration=1/24)
  
    mimsave( <최종 output의 경로> , <)
    
## 3. OpenCv -> cv2 : image, video
## 4. enumerate
## 5. file.shape
## 6. pyseq.Sequence -> format ways (eg. %l, %f, %h, etc.)
## 7. list sorted(reverse=True or False)