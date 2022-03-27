import sys


input = sys.stdin.readline

n = int(input())
volunteers = map(int, input().split())
super_viewer, viewer = map(int, input().split())

ans: int = 0
for volunteer in volunteers:
    num_volunteer = volunteer - super_viewer
    ans += 1

    if num_volunteer > 0:
        if num_volunteer % viewer == 0:
            ans += num_volunteer // viewer
        else:
            ans += num_volunteer // viewer + 1

print(ans)
