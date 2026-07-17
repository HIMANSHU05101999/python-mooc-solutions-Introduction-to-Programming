# WRITE YOUR SOLUTION HERE:
class ListHelper:
    @classmethod
    def frequency(cls,my_list: list):
        temp_dict={}
        for item in my_list:
            count=0
            if item not in temp_dict:
                for i in my_list:
                    if item == i:
                        count+=1
                temp_dict[item]=count
        return temp_dict

    @classmethod
    def greatest_frequency(cls, my_list: list):
        freq=cls.frequency(my_list)
        temp=0
        ret_key=0
        for key,val in freq.items():
            if temp<val:
                temp=val
                ret_key=key
        return ret_key
        
    @classmethod
    def doubles(cls, my_list):
        freq=cls.frequency(my_list)
        count=0            
        for key,val in freq.items():
            if val>=2:
                count+=1
        return count

def main():
    numbers = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
    print(ListHelper.greatest_frequency(numbers))
    print(ListHelper.doubles(numbers))
if __name__=="__main__":
    main()
        
