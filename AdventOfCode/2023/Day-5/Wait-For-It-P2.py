with open('races.txt') as file:
    lines = file.readlines()

times = [''.join(lines[0].strip().split()[1:])]
distances = [''.join(lines[1].strip().split()[1:])] 
answers = []
final = 1

for time, distance in zip(times, distances):
    result = 0
    countanswer = 0
    for i in range(1, int(time) + 1):
        button = (int(time) - i)
        result = button * i
        if result >= int(distance):
            countanswer += 1
        i += 1  
    answers.append(countanswer)

for number in answers:
    final *= number

print(f"Final answer = {final}")