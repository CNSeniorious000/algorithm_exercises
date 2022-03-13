# import numpy as np
# import numba as nb
from random import random


def main():
    time = 0
    wait_time = 0
    target = 13_500_000 / 1000
    waiting = []

    while time < 24 * 365 * 5:
        new = random() * 40 + 4
        
        time_next = random() * 30 + 15  # 倒计时
        
        new_waiting = []  # 新船来了, 过多久才走

        for t in waiting:
            if t > time_next:
                new_waiting.append(t - time_next)
                wait_time += time_next
            else:
                wait_time += t
        if new > time_next:
            new_waiting.append(new - time_next)
        time += time_next
        waiting = new_waiting
    return wait_time < target

main()
            
