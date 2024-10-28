# Lucas Brinks
# 10/28/24
# list stats

scores = [34,98,74,69,58,100]

num_scores = len(scores)

average_score = sum(scores) / num_scores

print(f'You took {num_scores} test and here are your most notable scores:')
print(f'Your lowest score was {min(scores)}')
print(f'Your best score was {max(scores)}')
print(f'The average of your scores is {average_score:.2f}')


distances = [480,438,4640,2814,4594]
average_distance = sum(distances) / len(distances)

print(f'The shortest trip is {min(distances)}')
print(f'The longest trip is {max(distances)}')
print(f'The average trip {average_distance:.2f}')