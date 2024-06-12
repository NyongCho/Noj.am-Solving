def solution(record):
    answer = []
    user = {}
    for msg in record:
        s = list(msg.split())
        l = len(s)
        if l == 3:
            user[s[1]] = s[2]
            
    for msg in record:
        s = list(msg.split())
        l = len(s)
        if l == 2:
            answer.append(f"{user[s[1]]}님이 나갔습니다.")
        if l == 3:
            if s[0] == "Enter":
                answer.append(f"{user[s[1]]}님이 들어왔습니다.")
        
    return answer