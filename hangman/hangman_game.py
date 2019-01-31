"""  
PIYAWAT CHOEYCHIT
"""
import json, random, os, string, re

# Set the wrong number of times.
all_turn = 10
# Set the score when answering correctly.
add_score = 5

def select_cate(number):
    """ Function's select Category """
    with open(files[number] +'.json')  as data_file:  
        data = json.load(data_file)
        cur_question = data[random.randint(0,len(data)-1)]
        print("Hint: ", cur_question["hint"])
        print()
        hang_game(cur_question["ans"])


def check_letter(letter):
        """ Function's check character """
        if letter.isdigit() or letter in string.punctuation or ' ' in letter:
                return False
        return True

def hang_game(answer):
        """ Function's main game """
        turn = all_turn
        score=0
        text_pass = []
        text_wrong = []
        [print("_", end=" ") if check_letter(t) else print(t, end=" ") for t in answer]
        print("  score", score ,", remaining wrong guess ",turn)
        while turn > 0 and len(text_pass) < len(set(re.sub('[^A-Za-z]+', '', answer))):
                print(">",end=" ")
                inp = input()
                print()
                if inp in text_wrong or inp in text_pass:
                        print("You have already entered the letters used.")
                else:
                        if inp not in answer:
                                text_wrong.append(inp)
                                turn-=1
                        for c in answer:
                                if c in text_pass or not check_letter(c):
                                        print(c, end=" ")
                                elif c == inp:
                                        print(c, end=" ")
                                        score+=add_score;
                                        text_pass.append(c)
                                else:
                                        print("_", end=" ")
                        print("  score", score ,", remaining wrong guess ",turn ,end="")
                        if text_wrong:
                                print(", wrong guessed:", *text_wrong, sep=" ")
                        print()
        
        print("finished!!")
        print("final Score = ", score, "| Wrong = ", all_turn-turn)

files = [f[:-5] for f in os.listdir('.') if os.path.isfile(f) and f.endswith('json')]
print("Select Category:\n")
[print(i,".",files[i-1]) for i in range(1,len(files)+1)]
print()
print(">",end=" ")
select_cate(int(input())-1)
