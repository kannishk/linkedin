"""
import fetch from "node-fetch";

const a = await fetch("https://www.linkedin.com/in/chakshu-jain-12413b142/", {
  headers: {
    accept:
      "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-language": "en-GB;q=0.5",
    "cache-control": "max-age=0",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "sec-gpc": "1",
    "upgrade-insecure-requests": "1",
    cookie:
      'liap=true; JSESSIONID="ajax:0921315826464448745"; li_theme=system; spectroscopyId=ffb9d82f-b512-4830-bf14-f007e24a1b4e; PLAY_LANG=en; lang=v=2&lang=en-US; PLAY_SESSION=eyJhbGciOiJIUzI1NiJ9.eyJkYXRhIjp7InNlc3Npb25faWQiOiJlZGEyNDMzNC05OTczLTRiM2MtYTBhZS0zOWM5NDM1MWEzNGZ8MTYzNjI5Njk4MCIsImFsbG93bGlzdCI6Int9IiwicmVjZW50bHktc2VhcmNoZWQiOiIiLCJyZWZlcnJhbC11cmwiOiJodHRwczovL3d3dy5saW5rZWRpbi5jb20vcHJlbWl1bS9zdXJ2ZXkvP2Rlc3RSZWRpcmVjdFVSTD1odHRwcyUzQSUyRiUyRnd3dy5saW5rZWRpbi5jb20lMkZpbiUyRnNhbS1iYW5rbWFuLWZyaWVkLTgzNjdhMzQ2JTJGJTNGc2hvd1ByZW1pdW1XZWxjb21lQmFubmVyJTNEdHJ1ZSZ1cHNlbGxPcmRlck9yaWdpbj1wcmVtaXVtX2lubWFpbF9wcm9maWxlX3Vwc2VsbF9tb2RhbCIsIlJOVC1pZCI6InwwIiwicmVjZW50bHktdmlld2VkIjoiIiwiQ1BULWlkIjoiXHUwMDA3asO3JDPCkE3DqMKnMVxcw6vDvT1waSIsImV4cGVyaWVuY2UiOiIiLCJ0cmsiOiIifSwibmJmIjoxNjM2Mjk2OTk4LCJpYXQiOjE2MzYyOTY5OTh9.Umy85cnMRsOEZIoICMKfvY2f-wS4I7OY_ncG9JcK3oM; li_sugr=fc1eb578-b59b-4b87-bc02-acb4253b7c75; AMCVS_14215E3D5995C57C0A495C55%40AdobeOrg=1; _gcl_au=1.1.793949702.1637162089; li_theme_set=app; timezone=Asia/Calcutta; bcookie="v=2&1b6a7979-a858-4403-8f95-07ac23a9dea2"; bscookie="v=1&20220413091047a1bbb166-9016-476c-8cfe-f29df4a0bbc3AQECF_ruZJR64-6kIEFnsFtR4KS682Jm"; _guid=7ff76794-6971-4644-8a2d-8156b744bd58; sdsc=22%3A1%2C1657197037584%7ECONN%2C0tUWTn2ohyW2eOc0J%2BXeyfC967eM%3D; li_at=AQEDATFfwugEx2YXAAABfHlmzQkAAAGCLmTjIE0Ac_8k4XlIV7WNDtdAiljhfllWi7BZEDKCOfYwbyuTWm16OHgn899Vibm7ZJbwE-20oebLfXq-KeI6aAxaOlLdOkQZKetdtyKrWQr2YpR0mv43_GJ2; AnalyticsSyncHistory=AQJ8AP9XmzDxLQAAAYIfOXgv_k1GMST3INL5bon4OxqfqG0pBPWCU2cM_Cijop7fCjJ7CMh5yIppw6ftn3RqjQ; lms_ads=AQEWJMIxTyQC4wAAAYIfOXkYMM6Ub7GVBIIH1l-RfiNRQCnQ6Z8Ho9yUj-EmP4lmocutOUJe79Zrjfw8MlC-Tqu4tuKLSHOp; lms_analytics=AQEWJMIxTyQC4wAAAYIfOXkYMM6Ub7GVBIIH1l-RfiNRQCnQ6Z8Ho9yUj-EmP4lmocutOUJe79Zrjfw8MlC-Tqu4tuKLSHOp; at_check=true; s_fid=43AAEF455968B4A8-27E097CBCCBE32DB; s_cc=true; s_ips=800; s_sq=%5B%5BB%5D%5D; gpv_pn=developer.linkedin.com%2Fproduct-catalog; s_tp=5029; s_tslv=1658384298698; mbox=session#8ae4439dcce94dd18f209954b59ed871#1658384699|PC#8ae4439dcce94dd18f209954b59ed871.31_0#1673936299; s_plt=1.32; s_pltp=developer.linkedin.com%2Fproduct-catalog; s_ppv=developer.linkedin.com%2Fproduct-catalog%2C49%2C16%2C2471%2C3%2C6; AMCV_14215E3D5995C57C0A495C55%40AdobeOrg=-637568504%7CMCIDTS%7C19195%7CMCMID%7C20356160524514366698480121255826768153%7CMCOPTOUT-1658407277s%7CNONE%7CvVersion%7C5.1.1; UserMatchHistory=AQISTQi-ZpHYxAAAAYIgcidySU1FpDHaex2Q7aq0o3HymTspa7vKI_6i12nlkm6VVMOxaqwaoirpYGbMT5qolD_pix_7oQOpF9rbipyDJ17Qy6SITDaS5mAd2M57uALr02FJVZ2dKk97RxtpKveGJZ7jVq4wUPG8CPVOP8dJNJSqA4eDODBLRKVyFnxPoEq6UXQ5QW9Ila7GbQw0ZCD55zKGQsu1dG9DdkhEF2xlLavz-wkavvgMvYIqC5wuPnEGE3NKMuSiF-y2sbOdLbS_E2l2YY2yBpBvjRiHv3o; lidc="b=VB00:s=V:r=V:a=V:p=V:g=5879:u=950:x=1:i=1658401730:t=1658487149:v=2:sig=AQGDgzU6gIbvoJayWNfl-rC0U0DuvD5j"',
  },
  referrerPolicy: "strict-origin-when-cross-origin",
  body: null,
  method: "GET",
});

console.log(await a.text());

"""
from dotenv import dotenv_values
from linkedin_api import Linkedin
import json

import requests

config = dotenv_values(".env")
api = Linkedin(config['USERNAME'], config['PASSWORD'])
data = json.load(open("./people.json", "r"))

coo = 'liap=true; JSESSIONID="ajax:0921315826464448745"; li_theme=system; spectroscopyId=ffb9d82f-b512-4830-bf14-f007e24a1b4e; PLAY_LANG=en; lang=v=2&lang=en-US; PLAY_SESSION=eyJhbGciOiJIUzI1NiJ9.eyJkYXRhIjp7InNlc3Npb25faWQiOiJlZGEyNDMzNC05OTczLTRiM2MtYTBhZS0zOWM5NDM1MWEzNGZ8MTYzNjI5Njk4MCIsImFsbG93bGlzdCI6Int9IiwicmVjZW50bHktc2VhcmNoZWQiOiIiLCJyZWZlcnJhbC11cmwiOiJodHRwczovL3d3dy5saW5rZWRpbi5jb20vcHJlbWl1bS9zdXJ2ZXkvP2Rlc3RSZWRpcmVjdFVSTD1odHRwcyUzQSUyRiUyRnd3dy5saW5rZWRpbi5jb20lMkZpbiUyRnNhbS1iYW5rbWFuLWZyaWVkLTgzNjdhMzQ2JTJGJTNGc2hvd1ByZW1pdW1XZWxjb21lQmFubmVyJTNEdHJ1ZSZ1cHNlbGxPcmRlck9yaWdpbj1wcmVtaXVtX2lubWFpbF9wcm9maWxlX3Vwc2VsbF9tb2RhbCIsIlJOVC1pZCI6InwwIiwicmVjZW50bHktdmlld2VkIjoiIiwiQ1BULWlkIjoiXHUwMDA3asO3JDPCkE3DqMKnMVxcw6vDvT1waSIsImV4cGVyaWVuY2UiOiIiLCJ0cmsiOiIifSwibmJmIjoxNjM2Mjk2OTk4LCJpYXQiOjE2MzYyOTY5OTh9.Umy85cnMRsOEZIoICMKfvY2f-wS4I7OY_ncG9JcK3oM; li_sugr=fc1eb578-b59b-4b87-bc02-acb4253b7c75; AMCVS_14215E3D5995C57C0A495C55%40AdobeOrg=1; _gcl_au=1.1.793949702.1637162089; li_theme_set=app; timezone=Asia/Calcutta; bcookie="v=2&1b6a7979-a858-4403-8f95-07ac23a9dea2"; bscookie="v=1&20220413091047a1bbb166-9016-476c-8cfe-f29df4a0bbc3AQECF_ruZJR64-6kIEFnsFtR4KS682Jm"; _guid=7ff76794-6971-4644-8a2d-8156b744bd58; sdsc=22%3A1%2C1657197037584%7ECONN%2C0tUWTn2ohyW2eOc0J%2BXeyfC967eM%3D; li_at=AQEDATFfwugEx2YXAAABfHlmzQkAAAGCLmTjIE0Ac_8k4XlIV7WNDtdAiljhfllWi7BZEDKCOfYwbyuTWm16OHgn899Vibm7ZJbwE-20oebLfXq-KeI6aAxaOlLdOkQZKetdtyKrWQr2YpR0mv43_GJ2; AnalyticsSyncHistory=AQJ8AP9XmzDxLQAAAYIfOXgv_k1GMST3INL5bon4OxqfqG0pBPWCU2cM_Cijop7fCjJ7CMh5yIppw6ftn3RqjQ; lms_ads=AQEWJMIxTyQC4wAAAYIfOXkYMM6Ub7GVBIIH1l-RfiNRQCnQ6Z8Ho9yUj-EmP4lmocutOUJe79Zrjfw8MlC-Tqu4tuKLSHOp; lms_analytics=AQEWJMIxTyQC4wAAAYIfOXkYMM6Ub7GVBIIH1l-RfiNRQCnQ6Z8Ho9yUj-EmP4lmocutOUJe79Zrjfw8MlC-Tqu4tuKLSHOp; at_check=true; s_fid=43AAEF455968B4A8-27E097CBCCBE32DB; s_cc=true; s_ips=800; s_sq=%5B%5BB%5D%5D; gpv_pn=developer.linkedin.com%2Fproduct-catalog; s_tp=5029; s_tslv=1658384298698; mbox=session#8ae4439dcce94dd18f209954b59ed871#1658384699|PC#8ae4439dcce94dd18f209954b59ed871.31_0#1673936299; s_plt=1.32; s_pltp=developer.linkedin.com%2Fproduct-catalog; s_ppv=developer.linkedin.com%2Fproduct-catalog%2C49%2C16%2C2471%2C3%2C6; AMCV_14215E3D5995C57C0A495C55%40AdobeOrg=-637568504%7CMCIDTS%7C19195%7CMCMID%7C20356160524514366698480121255826768153%7CMCOPTOUT-1658407277s%7CNONE%7CvVersion%7C5.1.1; UserMatchHistory=AQISTQi-ZpHYxAAAAYIgcidySU1FpDHaex2Q7aq0o3HymTspa7vKI_6i12nlkm6VVMOxaqwaoirpYGbMT5qolD_pix_7oQOpF9rbipyDJ17Qy6SITDaS5mAd2M57uALr02FJVZ2dKk97RxtpKveGJZ7jVq4wUPG8CPVOP8dJNJSqA4eDODBLRKVyFnxPoEq6UXQ5QW9Ila7GbQw0ZCD55zKGQsu1dG9DdkhEF2xlLavz-wkavvgMvYIqC5wuPnEGE3NKMuSiF-y2sbOdLbS_E2l2YY2yBpBvjRiHv3o; lidc="b=VB00:s=V:r=V:a=V:p=V:g=5879:u=950:x=1:i=1658401730:t=1658487149:v=2:sig=AQGDgzU6gIbvoJayWNfl-rC0U0DuvD5j"'
cookies = {}
for i in coo.split('; '):
    cookies[i.split("=")[0]] = i.split("=")[1]

res = requests.get('https://www.linkedin.com/in/pallavi-chauhan-ba6a99193', cookies=cookies)

print(res.status_code)
if "OPEN_TO_WORK" in res.text:
    print("Work")


# print(cookies)
# filtered_data = []
# for user in data:
#     url = "https://www.linkedin.com/in/" + user['public_id'] + '/'
#     res = requests.get(url, cookies=cookies)
#     if 'OPEN_TO_WORK' in res.text:
#         print("Found some")
#         filtered_data.append(user)
#     else:
#         print("Skipping this one...")



