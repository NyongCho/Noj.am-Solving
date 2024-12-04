def solve_encryption():
    import sys
    input = sys.stdin.readline
    
    # 매핑 읽기
    mapping = [input().strip() for _ in range(27)]
    N = int(input())
    T = input().strip()
    
    # 문자를 인덱스로 변환
    char_to_idx = {chr(i): i-65 for i in range(65, 91)}
    char_to_idx['_'] = 26
    idx_to_char = {v:k for k,v in char_to_idx.items()}
    
    # 순열 배열 생성
    perm = [char_to_idx[c] for c in mapping]
    
    # 사이클 찾기
    visited = [False] * 27
    cycles = []
    for i in range(27):
        if not visited[i]:
            cycle = []
            curr = i
            while not visited[curr]:
                visited[curr] = True
                cycle.append(curr)
                curr = perm[curr]
            cycles.append(cycle)
    
    # 각 문자가 어느 사이클의 어느 위치에 있는지 저장
    char_to_cycle = {}
    char_to_pos = {}
    for cycle in cycles:
        length = len(cycle)
        for i, char in enumerate(cycle):
            char_to_cycle[char] = cycle
            char_to_pos[char] = i
    
    # 문자열 변환
    result = []
    for c in T:
        idx = char_to_idx[c]
        cycle = char_to_cycle[idx]
        pos = char_to_pos[idx]
        new_pos = (pos + N) % len(cycle)
        result.append(idx_to_char[cycle[new_pos]])
    
    print(''.join(result))

solve_encryption()