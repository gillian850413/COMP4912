import pandas as pd
import numpy as np

#map each battle to pokemon data
def connect(data):
    data['First_pokemon_stats'] = data.First_pokemon.map(attr_dict)
    data['Second_pokemon_stats'] = data.Second_pokemon.map(attr_dict)

    data['First_pokemon'] = data.First_pokemon.map(type_dict)
    data['Second_pokemon'] = data.Second_pokemon.map(type_dict)
    
    return data

#calculate stat difference of two pokemons
def stat_diff(data):
    attr_diff_col = ['HP_diff', 'Atk_diff', 'Def_diff', 'SpAtk_diff', 'SpDef_diff', 'Speed_diff', 'Legend_diff']
    attr_diff = []
    for row in data.itertuples():
        attr_diff.append(np.array(row.First_pokemon_stats) - np.array(row.Second_pokemon_stats))
        
    attr_df = pd.DataFrame(attr_diff, columns=attr_diff_col)
    data = pd.concat([data, attr_df], axis=1)
    data.drop(['First_pokemon_stats', 'Second_pokemon_stats'], axis=1, inplace=True)
    return data

def type_effect(data):
    p1_type1 = []
    p1_type2 = []
    p2_type1 = []
    p2_type2 = []

    k = 0
    for row in data.itertuples(): 
        nested_type = [[1, 1], [1, 1]]

        for i in range(2):
            for j in range(2):
                fst_atk_type = type_chart.loc[type_chart['Attacking'] == row.First_pokemon[i]]
                fst_atk_eff = fst_atk_type[row.Second_pokemon[j]].item()
                nested_type[0][i] = nested_type[0][i] * fst_atk_eff
                
                sec_atk_type = type_chart.loc[type_chart['Attacking'] == row.Second_pokemon[i]]
                sec_atk_eff = sec_atk_type[row.First_pokemon[j]].item()
                nested_type[1][i] = nested_type[1][i] * sec_atk_eff 
                
        
        p1_type1.append(nested_type[0][0])
        p1_type2.append(nested_type[0][1])
        p2_type1.append(nested_type[1][0])
        p2_type2.append(nested_type[1][1])
        
        k += 1
        print(k)



    
    data = data.assign(P1_type1=p1_type1, P1_type2=p1_type2, P2_type1=p2_type1, P2_type2=p2_type2)
    data = data.drop(['First_pokemon', 'Second_pokemon'], axis=1)
    
    return data


pokemon = pd.read_csv("/Users/gillianchiang/Desktop/Course/year4_sem2/COMP4912/Data/pokemon-challenge/pokemon.csv")
combats = pd.read_csv("/Users/gillianchiang/Desktop/Course/year4_sem2/COMP4912/Data/pokemon-challenge/combats.csv")

#train_new_df = pd.read_csv("/Users/gillianchiang/Desktop/Course/year4_sem2/COMP4912/Notebook/output.csv")
type_chart = pd.read_csv("/Users/gillianchiang/Desktop/Course/year4_sem2/COMP4912/Data/pokemon-challenge/poke_type_chart.csv")

#change legendary and mega from T/F into 1/0
pokemon['Legendary'] = pokemon['Legendary'].map({False: 0, True:1})
pokemon['Name'] = pokemon['Name'].fillna('Primeape')
pokemon['Type 2'] = pokemon['Type 2'].fillna('None')

type_df = pokemon.iloc[:, 0:4]
type_df = type_df.drop('Name', axis=1)

attribute = ['HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']
attribute.insert(0, '#')
attribute.append('Legendary')
attr_df = pokemon.loc[:, attribute]

#create dictionaries
type_dict = type_df.set_index('#').T.to_dict('list')
attr_dict = attr_df.set_index('#').T.to_dict('list')

#change winner from pokemon# to 0 (first pokemon win) or 1 (second pokemon win)
combats2 = combats.copy()
combats2['Winner'] = np.where(combats2['Winner'] == combats['First_pokemon'], 0, 1)


#map the battle to pokemons data
try:
    train_df = connect(combats2)
except TypeError:
    pass

#calculate difference
train_new_df = stat_diff(train_df)

#calculate type effectiveness
type_chart["None"] = 1
type_chart = type_chart.set_value('18', 'Attacking', 'None').fillna(1.0).copy()    
train_new_df = type_effect(train_new_df)






    