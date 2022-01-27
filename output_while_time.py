# 시간과 관련된 기능을 가져옵니다.
import time

# 5초 동안 반복합니다.
output = 0
target_tick = time.time() + 5
while time.time() < target_tick:
    output += 1
print("5초 동안 반복한 횟수:", output)