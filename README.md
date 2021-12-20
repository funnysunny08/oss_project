# 오픈소스 소프트웨어 텀 프로젝트 보고서
## 1. 기본 정보

- 분반: 오픈소스 소프트웨어(목 1~4)
- 컴퓨터공학과 20101281 전선희
- 프로젝트명: 메일 알리미
## 2. 프로젝트 개요 및 동기
 우리는 매일 아침 눈을 뜨자마자 핸드폰으로 그 날의 날씨, 주가, 점심 메뉴 등을 검색하며 하루를 준비한다. 나는 이러한 정보들을 정리하여 한 번에 알려주는 시스템이 있으면 좋을 것 같다는 생각이 들어 매일 아침 메일을 통해 내가 원하는 정보들을 종합하여 알려주는 시스템을 기획해보고자 하였다.
## 3. 프로젝트 설명
1. 우선 사용자의 개인 정보를 입력합니다. 이때 구와 동은 사용자의 주요 출몰 지역으로 설정하였습니다. 이러한 개인 정보를 바탕으로 사용자가 원하는 정보들을 추출합니다.
![](https://images.velog.io/images/funnysunny08/post/3f1e4a6b-e9d4-4faf-99f2-f7bc7a9afb24/info.png)
2. 날씨 정보를 추출하는 것은 네이버 날씨 화면을 selector 이용하여 크롤링하였습니다.
![](https://images.velog.io/images/funnysunny08/post/2d3bea12-9092-446b-9bfa-5c13d28477b0/weather.png)
3. 미세 먼지 정보는 서울시에서 제공하는 대기질 관련 open api를 활용하였습니다. PM 70 이상이면 미세 먼지가 심하다고 판단하여 마스크 착용을 권하도록 하였습니다.
![](https://images.velog.io/images/funnysunny08/post/87dc177d-8672-4240-a45a-7c9c35595838/misae.png)
4. 식사 메뉴는 네이버에서 제공하는 오픈 API를 활용하여 사용자의 기호에 맞는 식당을 추천하도록 하였습니다. (client_id와 secret은 깃허브에는 지워서 올렸습니다😃)
![](https://images.velog.io/images/funnysunny08/post/baceefef-35b7-42b3-b589-b2fa41aafec0/matjip.png)
5. 주식 정보를 예측하는 것은 LSTM이라는 인공지능 모델을 이용하여 예측하도록 하였습니다. 그리고 png 파일로 저장하여 사용자에게 같이 첨부하도록 하였습니다.
(이 부분은 각종 자료와 유튜브를 보며 공부하며 클론 코딩하였습니다. [참조 유튜브링크](https://www.youtube.com/watch?v=sG_WeGbZ9A4))

![](C:\전선희\서울과기대\2학년2학기\오픈소스소프트웨어\oss_morning\project\savefig_gs.png)

1. 마지막으로 메일 보내는 부분입니다. 앞에서 구한 정보들을 활용하여 사용자에게 메일을 보냅니다. 
  ![](https://images.velog.io/images/funnysunny08/post/bfd43c50-ba09-4a32-a937-890c4e359e34/mail1.png)
  ![](https://images.velog.io/images/funnysunny08/post/f7ab8a3e-ab9c-4330-a4a1-ea91250eb490/mail2.png)

## 4. 결과물
main_mail.py를 실행한 결과물입니다.
![](https://images.velog.io/images/funnysunny08/post/eb57c8d4-6056-4fe0-9121-47d9b9c4ce09/result_mail.png)


## 5. 느낀 점 및 고찰
 우선 파이썬 하나로 이렇게나 많은 일들을 다양하게 할 수 있다는 사실에 매우 놀랐다. 그 중 파이썬으로 이메일을 보낼 수 있다는 것을 이번에 처음 알게 되었는데 정말 신기했다..😄 이후에 매일 아침마다 자동으로 메일을 보내는 기능도 추가해 보고싶다! 그리고 처음에는 사용자를 위한 정보를 추출하는 과정에서 웹 페이지 크롤링만을 사용할까 했는데 다양한 방식을 공부하고 익히고 싶어 네이버 오픈 API, 공공 데이터 등을 활용해 보았다. 마지막으로 딥러닝으로 주가 예측한 부분은 아직 실력이 부족하여 클론 코딩하였지만 방학 중에 더 공부하여 혼자 힘으로 딥러닝을 이용한 데이터 분석 프로젝트도 진행해보고 싶다. 