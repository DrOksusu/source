import pyautogui
import pyperclip
import time
                            
pyautogui.hotkey('win', 's')
time.sleep(1)
text = '덴트웹'
pyperclip.copy(text)
time.sleep(3)
# 각 문자 사이에 일정한 지연시간을 두고 입력합니다.
pyautogui.hotkey('ctrl', 'v')
time.sleep(1)
pyautogui.press('enter')
time.sleep(25)                              

secret = 'ok4275ok^^'
pyperclip.copy(secret)
pyautogui.hotkey('ctrl', 'v')
time.sleep(1)
pyautogui.press('enter')
time.sleep(5)


pyautogui.hotkey('win', 's')
time.sleep(1)
text2 = '카카오톡'
pyperclip.copy(text2)
time.sleep(1)
# 각 문자 사이에 일정한 지연시간을 두고 입력합니다.
pyautogui.hotkey('ctrl', 'v')
time.sleep(1)
pyautogui.press('enter')
time.sleep(13)
kakao_secret = 'ok2010ok!!'
pyperclip.copy(kakao_secret)
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')
time.sleep(5)

pyautogui.hotkey('win', 's')
time.sleep(1)
text3 = 'chrome'
pyperclip.copy(text3)
time.sleep(1)
pyautogui.hotkey('ctrl', 'v')
time.sleep(2)
pyautogui.press('enter')
time.sleep(5)
# 크롬 창을 최대화합니다.
pyautogui.hotkey('win', 'up')
time.sleep(3)

# 주소 표시줄에 포커스를 맞춤
pyautogui.hotkey('alt','d')
time.sleep(1)

# 유튜브 주소를 복사
youtube_address = 'www.youtube.com'
pyperclip.copy(youtube_address)

# 주소 표시줄에 유튜브 주소를 붙여넣기
pyautogui.hotkey('ctrl', 'v')
time
pyautogui.press('enter')
time.sleep(5)

# 검색창을 활성화
pyautogui.press('/')
time
youtube_search = '감미로운 음악'
pyperclip.copy(youtube_search)
time.sleep(1)

# 검색창에 감미로운 음악을 붙여넣기
pyautogui.hotkey('ctrl', 'v')
time.sleep(1)
pyautogui.press('enter')

# 결과가 나올 때까지 기다리기
time.sleep(5)

# 검색창에 감미로운 음악을 한번더 붙여넣기
pyautogui.hotkey('ctrl', 'v')
time.sleep(2)
pyautogui.press('enter')

# 결과가 나올 때까지 기다리기
time.sleep(10)

# 첫 번째 검색 결과를 선택하고 재생
for _ in range(8):
    pyautogui.press('tab')
    time.sleep(2)

time.sleep(3)
pyautogui.press('enter')
