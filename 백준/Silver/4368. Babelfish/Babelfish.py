import sys

def main():
    input = sys.stdin.read  # 표준 입력에서 데이터 읽기
    data = input().splitlines()  # 줄 단위로 읽기
    
    dictionary = {}
    i = 0
    # 사전 입력 처리
    while data[i]:
        english, foreign = data[i].split()
        dictionary[foreign] = english
        i += 1
    
    # 공백 줄 넘기기
    i += 1
    
    # 메시지 처리
    result = []
    while i < len(data):
        word = data[i]
        if word in dictionary:
            result.append(dictionary[word])
        else:
            result.append("eh")
        i += 1
    
    # 결과 출력
    sys.stdout.write("\n".join(result) + "\n")

if __name__ == "__main__":
    main()
