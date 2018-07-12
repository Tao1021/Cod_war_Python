# Here are the questions :

# Mary wrote a recipe book and is about to publish it, but because of a new European law, she needs to update and include all measures in grams.

# Given all the measures in tablespoon (tbsp) and in teaspoon (tsp), considering 1 tbsp = 15g and 1 tsp = 5g, append to the end of the measurement the biggest equivalent integer (rounding up).

# Examples
# "2 tbsp of butter"    -->  "2 tbsp (30g) of butter"

# "1/2 tbsp of oregano" -->  "1/2 tbsp (8g) of oregano"

# "1/2 tsp of salt"     -->  "1/2 tbsp (3g) of salt"

# "Add to the mixing bowl and coat well with 1 tbsp of olive oil & 1/2 tbsp of dried dill" -->
# "Add to the mixing bowl and coat well with 1 tbsp (15g) of olive oil & 1/2 tbsp (8g) of dried dill"




import math 
def convert_recipe(recipe):
    new_recipe= recipe.split(" ")
    for num in range(len(new_recipe)):
        if new_recipe[num] == "tbsp":
            arry=new_recipe[num-1].split("/")
            if len(arry)== 1:
                info=int(arry[0])*15
                new_recipe.insert(num+1, '('+str(info)
+'g'+')')
            elif len(arry)> 1:
                new_num=int(arry[0])/int(arry[1])
                info= math.ceil(15* new_num)
                new_recipe.insert(num+1, '('+str(info)+'g'+')')
        elif new_recipe[num] =="tsp":
            arry=new_recipe[num-1].split("/")
            if len(arry)== 1:
                info=int(arry[0])*5
                new_recipe.insert(num+1, '('+str(info)+'g'+')')
            elif len(arry)> 1:
                new_num=int(arry[0])/int(arry[1])
                info= math.ceil(5* new_num)
                new_recipe.insert(num+1, '('+str(info)+'g'+')')
    updated_recipe=" ".join(new_recipe) 
    print(updated_recipe)
            
            
            
            
    return  updated_recipe