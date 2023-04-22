#펄스널 컬러
colors = ["빨강", "노랑", "파랑", "초록", "보라",] #색깔 추가
for i, color in enumerate(colors):
    print(f"{i+1}. {color}")

while True:
    try:
        answer_1 = int(input("좋아하는 색깔을 선택해주세요: "))
        if 1 <= answer_1 <= len(colors):
            break
        else:
            print("잘못된 선택입니다.")
    except ValueError:
        print("숫자를 입력해주세요.")

favorite_color = colors[answer_1-1]

#얼굴형
face_share = ["둥근", "역삼각형", "계란", "긴얼굴", "사각형"]
for i, face in enumerate(face_share):
    print(f"{i+1}. {face}")

while True:
    try:
        answer_2 = int(input("자신의 얼굴형을 선택해주세요: "))
        if 1 <= answer_2 <= len(face_share):
            break
        else:
            print("잘못된 선택입니다.")
    except ValueError:
        print("숫자를 입력해주세요.")

my_face = face_share[answer_2-1]

#체형
body_share = ["삼각형", "직사각형", "역삼각형", "모래시계형", "원형"] 
for i, body in enumerate(body_share):
    print(f"{i+1}. {body_share}")

while True:
    try:
        answer_3 = int(input("자신의 체형을 선택해주세요: "))
        if 1 <= answer_3 <= len(colors):
            break
        else:
            print("잘못된 선택입니다.")
    except ValueError:
        print("숫자를 입력해주세요.")

my_body = body_share[answer_3-1]