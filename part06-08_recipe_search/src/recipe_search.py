# Write your solution here
def read_file_dict(filename: str):
    from pathlib import Path
    filename=Path(__file__).parent/filename
    with open(filename) as file:
        rows = []
        for row in file:
            rows.append(row.strip().split(";"))
            print(row)
 
   



def read_file(recipe_file: str):
    from pathlib import Path
    #recipe_file=Path(__file__).parent/recipe_file
    recipe_list=[]
    ingerdient_list=[]
    with open(recipe_file) as file:
        for line in file:
            new_line=line.strip()
            ingerdient_list.append(new_line)
            if new_line=="":
                recipe_list.append(ingerdient_list)
                if "" in ingerdient_list:
                    ingerdient_list.remove("")
                ingerdient_list=[]
        if ingerdient_list:
            recipe_list.append(ingerdient_list)
    return(recipe_list)

def search_by_name(recipe_file: str, recipe: str):
    
    recipe_list=read_file(recipe_file)
    recipe_found=[]
    for i in range(len(recipe_list)):
        if recipe in (recipe_list[i][0]).lower():
            recipe_found.append(recipe_list[i][0])
    return (recipe_found)


def search_by_time(recipe_file: str, prep_time: int):
    
    recipe_list=read_file(recipe_file)
        
    recipe_found=[]
    for i in range(len(recipe_list)):
        if prep_time >= int(recipe_list[i][1]):
            recipe_found.append((recipe_list[i][0],recipe_list[i][1]))
    

    return_string=[]
    for item in recipe_found:
        return_string.append(f"{item[0]}, preparation time {item[1]} min")
    return (return_string)

def search_by_ingredient(recipe_file: str, ingredient: str):
    recipe_list=read_file(recipe_file)
        
    recipe_found=[]
    for i in range(len(recipe_list)):
        if ingredient in (recipe_list[i]):
            recipe_found.append((recipe_list[i][0],recipe_list[i][1]))
   

    return_string=[]
    for item in recipe_found:
        return_string.append(f"{item[0]}, preparation time {item[1]} min")
    return (return_string)


def main():
    found_recipes = search_by_name("recipes1.txt", "cake")

    for recipe in found_recipes:
        print(recipe)

    found_recipes = search_by_time("recipes1.txt", 20)

    for recipe in found_recipes:
        print(recipe)

    found_recipes = search_by_ingredient("recipes1.txt", "eggs")

    for recipe in found_recipes:
        print(recipe)

if __name__=="__main__":        
    print(read_file_dict("recipes1.txt"))