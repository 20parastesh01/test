class Test:
    def Answer(self, inputs:list):
        
        score = []
        user_input_len = len(inputs[0])


        for i in range(len(inputs)):
            score.append(0)
        
        for i in range(user_input_len):

            for j in range(len(inputs)):
                inputs_a = inputs.copy()
                inputs_a.remove(inputs[j])
                print(inputs_a)

                for n in range(len(inputs_a)):

                    if inputs[j][i] == inputs_a[n][i]:
                        score[j] += 5

                    else:
                        score[j] += 10
                        
        print(score)



letter = input("Enter a letter: ")
print("Enter name|city|food|color starting with the letter. Use spaces to separate them.")

user_input = 0
inputs = []
while user_input != '1':
    user_input = input("Enter your answer. Exit by typing '1': ")
    if user_input == '1':
        break
    else:
        inputs.append(user_input.split())

test = Test()
print(type(test))
test.Answer(inputs) 