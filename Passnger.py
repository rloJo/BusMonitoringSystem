#Passenger.py
class passenger: #승객을 나타내는 passenger class정의
    passenger =0 #승객 변수 생성
    def Init(self): #승객변수 초기화 함수
        passenger=0

    def On(self): #On함수 호출 시 승객변수 1증가
        self.passenger+=1

    def Off(self): #Off함수 호출 시 승객 변수 1감소
        self.passenger-=1

    def GetPassenger(self ): #객체의 passenger변수 값 return 함수
        return self.passenger
