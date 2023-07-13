class Test:
    def Answer(inputs):

        elements_len = 3
        score = []
        for i in range(len(inputs)):
            score.append(0)

        for i in range(1,3):
            for j in (len(inputs)):
                for n in range(1, len(inputs) - 1):
                    if input[j][i] == input[j+n][i]:
                        score[j]=+5
                    else:
                        score[j]=+10
        print(score)



letter = input("Enter a letter: ")
inputs = []
user_input = input("Enter your answer. exit by 1: ")
list = list.append(user_input)
inputs.append(list)

list = []
while user_input != '1':
    user_input = input("Enter your answer. exit by 1: ")
    list = list.append(user_input)
    inputs.append(list)

test = Test()
test.Answer(inputs) 