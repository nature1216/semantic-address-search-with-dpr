# 시맨틱(semantic) 기반 위치 정보 추정 기술
### 위치를 묻는 query에 대해 POI(point of interest)를 제공해주는 지도 웹 서비스
<br>
<br>



![images](https://img.shields.io/github/license/minji-o-j/AI-Speaker-for-Senior-Citizen?style=flat-square)
![image](https://img.shields.io/badge/language-Python-blueviolet?style=flat-square&logo=Python)
![image](https://img.shields.io/badge/language-Javascript-blueviolet?style=flat-square&logo=Javascript)
![image](https://img.shields.io/badge/Latest%20Update-231211-9cf?style=flat-square)


---
## 프로젝트 개요
### 목표
 - 학교 내의 객체,건물,공간 등의 위치를 잘 모르는 새내기나 외부인들이 편하게 위치를 물어보았을 때, 지도에 정확한 위치를 표시해주는 것
<br>
<br>


### 내용
 - POI마다 좌표 정보와 위치를 설명하는 텍스트들을 매핑하였다.
 - 사용자가 입력한 전북대학교 내 위치에 대한 질의를 받고, 가장 큰 유사도를 보이는 좌표 값을 출력하여 지도에 보여준다.
 - 현재 수집한 전북대학교 데이터 셋의 위치 범위는 '중앙도서관','공대','자연대','농대' 근처 이다.
 - 현재 수집한 전북대학교 데이터 셋의 객체 종류는 '벤치','pm주차장','구조물','교내상가','흡연구역','쓰레기처리장','지름길','공간','건물' 이 있다.
 - 특정 쿼리에 대한 이스터에그가 존재하며, ['토끼','뽀시래기','귀요미'] 를 입력했을 때 학교에서 키우는 토끼의 집을 알 수 있다.
<br>
<br>



---
## 개발 스택
<img width="600" alt="image" src="https://github.com/lalala5772/algorithm/assets/65425885/75894e8b-d7f8-4196-af01-3964d37f73b0">
<br>
<br>



---
  
## Branch
- main: 최종적으로 사용된 코드들
- models: 구현한 NLP DPR 모델들
- client: 쿼리를 묻고 결과를 받아온 좌표를 지도로 시각화하는 웹(html,css,js) 코드
- server: 쿼리를 받고 모델을 실행시켜 결과 값을 반환하는 flask(python) 코드
- nature1216: 프로젝트를 진행하며 작성했지만 최종에서 사용하지 않은 코드 - 정보 수집을 위한 크롤러
- lalala5772: 프로젝트를 진행하며 작성했지만 최종에서 사용하지 않은 코드 - 한국어 형태소 분석기(tokenizer)
<br>
<br>




---
## 주요 기능
### DPR
<img width="580" alt="image" src="https://github.com/lalala5772/algorithm/assets/65425885/a0dfb0cb-38cb-413d-8ac0-7d041aaa8e6b">  
<br>
<br>



### koBert base의 모델을 추가 학습한 내용
- 학습 데이터는  Question-Document Pair 형태로 구성
- Document는 주어진 Question과 나타내는 위치가 일치하는 설명 텍스트에 해당
  - e.g. {‘docid’:’1’, ‘qid’:’1’, ‘query’:’공대 7호관 옆 흡연구역으로 와주세요.’, ‘positive_passage’:’(쿼리가 설명하는 위치에 대한 설명)’}
- Positive passage: Question에 대한 정확한 답변이나 관련 정보를 포함하는 document
- Negative passage: Question과 관련성이 낮거나 무관한 정보를 포함하는 document
- **Question에 대해 positive(=정답) passage는 가까워지고, negative(=정답이 아님) passage와는 멀어지도록 함**
<br>
<br>




### 성능 지표
<img width="460" alt="image" src="https://github.com/lalala5772/algorithm/assets/65425885/fbe0aceb-524c-4f87-b7ce-e6743760e8b5">  
<br>
- 약간의 Overfitting이 있긴 하여도, 그만큼 정확한 좌표 값을 return할 수 있다는 것에 의의가 있음.
<br>
<br>


---

## 실행 결과
<img width="800" alt="image" src="https://github.com/lalala5772/algorithm/assets/65425885/6f4e98fa-5396-4b45-81de-5d82815a33a2">


<img width="800" alt="image" src="https://github.com/lalala5772/algorithm/assets/65425885/1ab6505e-97a4-492e-9663-80daafef0ca9">


<img width="800" alt="image" src="https://github.com/lalala5772/algorithm/assets/65425885/1c1ac0d0-654c-4e34-952d-df7cc2108565">


<img width="800" alt="스크린샷 2023-12-11 오전 12 48 45" src="https://github.com/lalala5772/algorithm/assets/65425885/ec8590cb-0eaf-407f-809f-60c8d52d4c49">

<br><br>


---

## 개발자
### [오키duckey]
- 김자연: 데이터 수집 및 가공, dpr 모델 개발, 서버 개발
- 이미르: 데이터 수집 및 가공, dpr 모델 개발, 클라이언트 개발
<br><br>

---

## 개발 기간

![9월](https://github.com/lalala5772/algorithm/assets/65425885/68618242-71cc-4a2c-b286-398f8c53fce7)

<br><br>
