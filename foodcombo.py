def make_food_combos(food_dict,key_list,lower_bound,upper_bound,sum):
    if upper_bound == 0:
        return
    if lower_bound <= sum <= upper_bound:
        yield[]
    if sum > upper_bound or not key_list:
        return
    for solution in make_food_combos(food_dict,key_list[1:], lower_bound, upper_bound,sum + food_dict[key_list[0]]):
        yield [key_list[0]] + solution
    for solution in make_food_combos(food_dict,key_list[1:], lower_bound, upper_bound,sum):
        yield solution



food_price=({"pizza":15,"burger":8,"pasta":5,"salad":12,"beer":5,"fruits":5})
set_of_food_combos = []
for value in make_food_combos(food_price,food_price.keys(),15,20,0):
    if value not in set_of_food_combos:
        set_of_food_combos.append(value)

print set_of_food_combos
