class Birds:
    def __init__(self, bird, sound, weight, speed, item=False):
        self.bird = bird
        self.sound = sound
        self.weight = weight
        self.speed = speed
        self.item = item
# 아이템을 가지고있는 앵무샌는 참새 비둘기 단 러버덕 닭은 X2가 안됨
    def crying(self):
        print(f'{self.bird}(이)가 "{self.sound}" 울음소리를 냈습니다.')


    def fly(self):
        print(f'{self.bird}가 날고있습니다.')

    def run(self):
        result = self.weight * self.speed
        if self.item :
            print(result)
            print(f'{self.bird}가 {result*2}속력으로 달립니다.')
        else:
            print(f'{self.bird}가 {result}속력으로 달립니다.')

앵무새 = Birds('앵무새', '짹', 2, 3, True)
참새 = Birds('참새', '짹', 3, 2, True)
비둘기 = Birds('비둘기', '구구', 4, 3, True)
닭 = Birds('닭', '꼬끼오', 4, 1)
러버덕 = Birds('러버덕', '꽉꽉', 100, 0)

bird_dict = {
    "앵무새": 앵무새,
    "참새": 참새,
    "비둘기": 비둘기,
    "닭": 닭,
    "러버덕": 러버덕
}

def birds():
    while True:
        print("="*30)
        select= input('새와 행동을 입력해 주세요. "종료" 입력시 종료.\n(예:참새,소리내기):')

        if select == '종료':
            return

        try:
            A, B = select.split(',')
        except ValueError as e:
            print('","로 새와 행동을 구분하시오')
            continue



        if A not in bird_dict:
            print('목록에 없는 새 입니다.')
            continue

        bird = bird_dict[A]
        if B == '날기':
            if A == "러버덕":
                print('러버덕은 날 수 없습니다.')
            else :
                bird.fly()
        elif B == '소리내기':
            bird.crying()
        elif B == '달리기':
            if A == "러버덕":
                print('러버덕은 달릴 수 없습니다.')
            else :
                bird.run()
        else:
            print('알 수 없는 입력입니다.')
            continue
            


if __name__ == '__main__':
    birds()