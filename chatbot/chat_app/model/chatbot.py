import pandas as pd
import pickle
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
import urllib.request
from konlpy.tag import Okt
from tqdm import tqdm
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.layers import Embedding, Dense, LSTM
from tensorflow.keras.models import Sequential
from tensorflow.keras.models import load_model
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
import tensorflow as tf
import os
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.utils import to_categorical
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, Dense, SimpleRNN




class Load_chatbot:
    def __init__(self):
        # 훈련 모델 불러오기
        # self로 지정된 변수들은 모두 전역변수로 사용가능
        self.model = keras.models.load_model("C:/pukyung_202301/2_27_proj/chatbot/chat_app/model/model_best.h5")
        self.df = pd.read_csv("C:/pukyung_202301/2_27_proj/교수정보.csv")
        
        ### 챗봇 데이터 만들기
        chatbot_data =  pd.DataFrame({'rule':self.df["교수명"], '전공':self.df["전공"], '전화번호':self.df["전화번호"], '연구실':self.df["연구실"], '이메일':self.df["이메일"], '강의평':self.df["강의평"]})
        self.chat_dic = {}
        i = 0
        for rule in chatbot_data["rule"]:
            self.chat_dic[i] = rule
            i+=1
        self.professor_name = ""
            
    def chat_prof(self, req, professor_name):
        for i in range(len(self.df)):
            if self.df["교수명"][i] == professor_name:
                val = i
                break
                
        if req == "전공":
            return "{} 교수님의 전공은 {}입니다.".format(professor_name, self.df["전공"][val])
        elif req == "연구실":
            return "{} 교수님의 연구실은 {}입니다.".format(professor_name, self.df["연구실"][val])
        elif req == "이메일":
            return "{} 교수님의 이메일은 {}입니다.".format(professor_name, self.df["이메일"][val])
        elif req == "전화번호":
            return "{} 교수님의 전화번호는 {}입니다.".format(professor_name, self.df["전화번호"][val])
        elif req in self.chat_dic.values():
            return req
        else :
            return "전공/연구실/이메일/전화번호/강의평/강의평가 만 입력해주세요"
        
    def non_answer(self, req):
        try :
            if not professor_name: # 전역 변수가 비어있으면 교수님 이름 입력받기
                req = req
                if req in self.chat_dic.values(): # 입력받은 교수님 이름이 chat_dic.values() 경우에만 전역 변수에 저장합니다.
                    professor_name = req
                elif req == "exit":
                    return "ChatBot : 감사합니다"
                else : 
                    return "ChatBot : 다시 입력해주세요: "
        except :
            return "알 수 없는 오류가 발생했습니다. 종료합니다."
            
            
                    
    def answer(self):
                        
        try:            
            # 전역 변수가 비어있지 않은 경우에는 해당 교수님 정보를 출력합니다.   
            print("ChatBot : {} 교수님에 대해 더 알고싶은 정보를 입력해 주세요.(전공/연구실/이메일/전화번호/강의평/강의평가)\n(다른 교수님을 원하시면 성함을, 더 알고싶은 정보가 없으면 '없어'를 입력해주세요): ".format(professor_name))
            req = input("나 : ")
            print("---------------------------------------------")
            if req == "없어":
                print("감사합니다")
                print("---------------------------------------------")
                
            ### 질문을 함수에 보내서 응답메세지 받아오기
            elif req in self.chat_dic.values():
                professor_name = req
            else :
                print("ChatBot : ", self.chat_prof(req, professor_name))
                print("---------------------------------------------")
                    
        except :
            print("알 수 없는 오류가 발생했습니다. 종료합니다.")
            print("---------------------------------------------")
            