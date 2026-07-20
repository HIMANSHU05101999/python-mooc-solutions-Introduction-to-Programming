# Write your solution here
import random

class WordGame():
    def __init__(self, rounds: int):
        self.wins1 = 0
        self.wins2 = 0
        self.rounds = rounds

    def round_winner(self, player1_word: str, player2_word: str):
        # determine a random winner
        return random.randint(1, 2)

    def play(self):
        print("Word game:")
        for i in range(1, self.rounds+1):
            print(f"round {i}")
            answer1 = input("player1: ")
            answer2 = input("player2: ")

            if self.round_winner(answer1, answer2) == 1:
                self.wins1 += 1
                print("player 1 won")
            elif self.round_winner(answer1, answer2) == 2:
                self.wins2 += 1
                print("player 2 won")
            else:
                pass # it's a tie

        print("game over, wins:")
        print(f"player 1: {self.wins1}")
        print(f"player 2: {self.wins2}")

class LongestWord(WordGame):
    def __init__(self, rounds):
        super().__init__(rounds)
    
    def round_winner(self, player1_word, player2_word):
        if len(player1_word)>len(player2_word):
            return 1
        elif len(player1_word)==len(player2_word):
            return
        else:
            return 2 
        
class MostVowels(WordGame):
    def __init__(self, rounds):
        super().__init__(rounds)

    def round_winner_my_sol(self, player1_word, player2_word):
        vowels=['a','e','i','o','u']
        vowel_count_p1=0
        vowel_count_p2=0
        for vowel in vowels:
            for letter in player1_word:
                if vowel==letter:
                    vowel_count_p1+=1
            for letter in player2_word:
                if vowel==letter:
                    vowel_count_p2+=1
        if vowel_count_p1>vowel_count_p2:
            return 1
        elif vowel_count_p1==vowel_count_p2:
            return 0
        else:
            return 2
            
#Refactored to make this program modular and less complex
    def count_vowels(self, word):
        vowels=['a','e','i','o','u']
        vowel_count=0
        for vowel in vowels:
            for letter in word:
                if letter in vowels:
                    vowel_count+=1
        return vowel_count

    def round_winner(self, player1_word, player2_word):
        if self.count_vowels(player1_word)>self.count_vowels(player2_word):
            return 1
        elif self.count_vowels(player1_word)<self.count_vowels(player2_word):
            return 2
        else:
            return 0

class RockPaperScissors(WordGame):
    def __init__(self, rounds):
        super().__init__(rounds)

    def round_winner(self, player1_word, player2_word):
        word_list=['rock','paper','scissors']
        possible_pairs=[('rock','paper'),('paper','scissors'),('scissors','rock')]
        if (player1_word,player2_word) in possible_pairs:
            return 2
        elif (player2_word,player1_word) in possible_pairs:
            return 1
        elif player1_word in word_list and player2_word not in word_list:
            return 1
        elif player2_word in word_list and player1_word not in word_list:
            return 2
        else: 
            return 0


def main():
    p = MostVowels(4)
    p.play()
if __name__=="__main__":
    main()