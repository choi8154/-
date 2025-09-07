class Birds:
    def __init__(self, bird, sound):
        self.bird = bird
        self.sound = sound

    def crying(self):
        print(f'{self.bird}(이)가 "{self.sound}" 울음소리를 냈습니다.')


    def fly(self):
        print(f'{self.bird}가 날고있습니다.')

앵무새 = Birds('앵무새', '짹')
참새 = Birds('참새', '짹')
비둘기 = Birds('비둘기', '구구')
닭 = Birds('닭', '꼬끼오')
러버덕 = Birds('러버덕', '꽉꽉')

bird_dict = {
    "앵무새": 앵무새,
    "참새": 참새,
    "비둘기": 비둘기,
    "닭": 닭,
    "러버덕": 러버덕
}

def birds():
    try:
        A, B = input('새와 행동을 입력해 주세요.(예:참새,소리내기):').split(",")
    except ValueError as e:
        print('","로 새와 행동을 구분하시오')

    bird = bird_dict[A]
    if A not in bird_dict:
        print('목록에 없는 새 입니다.')
        return
    
    if B == '날기':
        bird.fly()
    elif B == '소리내기':
        bird.crying()
    else:
        print('알 수 없는 입력입니다.')
        return


if __name__ == '__main__':
    birds()