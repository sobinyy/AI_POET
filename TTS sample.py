import os
from google.cloud import speech

from gtts import gTTS
import pygame
import time
from pydub import AudioSegment


os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"C:\Users\LG\Desktop\2025\구글 클라우드\turnkey-channel-454904-b0-33a5c7635740.json"


def text_to_speech(text, lang='ko', save_dir='C:/Users/LG/Desktop/2025/구글 클라우드', filename='output.mp3'):
    # 절대경로 설정
    mp3_filename = os.path.join(save_dir, filename)
    
    # 텍스트를 MP3 파일로 변환
    tts = gTTS(text=text, lang=lang)
    tts.save(mp3_filename)
    
    print(f"음성 파일이 {mp3_filename} 로 저장되었습니다.")
    
    # pygame을 사용하여 음성 출력
    pygame.mixer.init()
    pygame.mixer.music.load(mp3_filename)
    pygame.mixer.music.play()
    
    # 음성이 끝날 때까지 대기
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)
    
    return mp3_filename

if __name__ == "__main__":
    text = input("앵무새에게 들려줄 문장을 입력하세요: ")
    text_to_speech(text)
