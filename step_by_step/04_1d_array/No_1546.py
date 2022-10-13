n = int(input())
new_score = []

score = list(map(int, input().split(" ")))
max_num = max(score)

new_score_sum = (sum(score) / max_num) * 100

new_mean = new_score_sum/n

print("%.2f" % new_mean)