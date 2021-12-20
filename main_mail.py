import smtplib, os
from email import encoders
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from info import x, name, gu, dong
from weather import weather, gion
from misae import PM, danger
from matjip import matjip

fromaddress = 'seonheui08@gmail.com'
pw = 'your_password'

toaddress = ['rosa7536@naver.com']

# 이메일제목
msg = MIMEMultipart()
msg['Subject'] = '{}님 좋은 아침입니다!😊'.format(name)

# 이메일 내용 입력
date_mail = '{}님 좋은 아침입니다🌞 \n 오늘은 {}년 {}월 {}일입니다!\n'.format(name, x.year, x.month, x.day)
weather_mail = '{} {}의 오늘 날씨는 {}입니다. {} 입니다🙂\n'.format(gu, dong, weather, gion)
misae_mail = '오늘의 미세먼지 농도는 PM {} 입니다.'.format(PM)
add = '\n'
if danger == True:
    add = '마스크를 착용해주세요!😷\n'
matjip_mail = '오늘 식사는 "{}" 추천드립니다!\n'.format(matjip)
end_mail = '오늘 하루도 화이팅하세요!!💪'
full_mail = date_mail + weather_mail + misae_mail + add + matjip_mail + end_mail

text = MIMEText(full_mail)

# 이메일 제목과 내용 합치기
msg.attach(text)

s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login(fromaddress, pw)

# #파일 첨부
files = r'C:\전선희\서울과기대\2학년2학기\오픈소스소프트웨어\oss_project\savefig_gs.png'
files = files.encode('utf-8')

part = MIMEBase("application", "octet-stream")
part.set_payload(open(files, 'rb').read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', 'attachment', filename='{}님 주식예측보고서.png'.format(name))
msg.attach(part)

for i in toaddress:
    msg['To'] = i
    s.sendmail(fromaddress, i, msg.as_string())

s.quit()
