from collections import Counter
import random

def findWeakness(type1, type2):
    #The plan is to use a hash map (dictionary, that has 4 sections, weak against, strong against, immune to, normal to) then use the counter to be able to consider the type 2 aswell
    type_characteristics = {

        "Normal": {
            "SuperEffective": [],
            "NotEffective": ["Rock", "Steel"],
            "Resistant": ["Ghost"],
            "Normal": ["Normal", "Fire", "Water", "Electric", "Grass", "Ice", "Fighting", "Poison", "Ground", "Flying", "Psychic", "Bug", "Dragon", "Dark", "Fairy"]
        },
        "Fire": {
            "SuperEffective": ["Bug", "Steel", "Grass", "Ice"],
            "NotEffective": ["Rock", "Fire", "Water", "Dragon"],
            "Resistant": [],
            "Normal": ["Normal", "Electric", "Psychic", "Ground", "Flying", "Poison", "Ghost", "Fighting", "Dark", "Fairy"]
        },
        "Water": {
            "SuperEffective": ["Fire", "Ground", "Rock"],
            "NotEffective": ["Water", "Grass", "Dragon"],
            "Resistant": [],
            "Normal": ["Normal", "Electric", "Ice", "Steel", "Fairy", "Ghost", "Psychic", "Flying", "Bug", "Poison", "Dark", "Fighting"]
        },
        "Electric": {
            "SuperEffective": ["Water", "Flying"],
            "NotEffective": ["Grass", "Electric", "Dragon"],
            "Resistant": ["Ground"],
            "Normal": ["Normal", "Fire", "Electric", "Ice", "Fighting", "Poison", "Steel", "Ghost", "Psychic", "Bug", "Rock", "Dark", "Fairy"]
        },
        "Grass": {
            "SuperEffective": ["Water", "Ground", "Rock"],
            "NotEffective": ["Flying", "Poison", "Bug", "Steel", "Fire", "Grass", "Dragon"],
            "Resistant": [],
            "Normal": ["Normal", "Electric", "Ice", "Psychic", "Ghost", "Dark", "Fairy", "Fighting"]
        },
        "Ice": {
            "SuperEffective": ["Flying", "Ground", "Grass", "Dragon"],
            "NotEffective": ["Steel", "Fire", "Water", "Ice"],
            "Resistant": [],
            "Normal": ["Normal", "Electric", "Psychic", "Fighting", "Rock", "Ghost", "Dark", "Fairy", "Bug", "Poison"]
        },
        "Fighting": {
            "SuperEffective": ["Normal", "Ice", "Rock", "Dark", "Steel"],
            "NotEffective": ["Poison", "Flying", "Psychic", "Bug", "Fairy"],
            "Resistant": [],
            "Normal": ["Normal", "Fire", "Water", "Electric", "Grass", "Ice", "Fighting", "Poison", "Ground", "Flying", "Psychic", "Bug", "Dragon", "Ghost", "Fairy"]
        },
        "Poison": {
            "SuperEffective": ["Grass", "Fairy"],
            "NotEffective": ["Poison", "Ground", "Rock", "Ghost", "Steel"],
            "Resistant": [],
            "Normal": ["Normal", "Fire", "Water", "Electric", "Ice", "Fighting", "Psychic", "Bug", "Dragon", "Dark", "Fairy", "Flying"]
        },
        "Ground": {
            "SuperEffective": ["Fire", "Electric", "Poison", "Rock", "Steel"],
            "NotEffective": ["Bug", "Grass"],
            "Resistant": ["Electric"],
            "Normal": ["Normal", "Water", "Ice", "Fighting", "Psychic", "Ground", "Flying", "Ghost", "Dragon", "Dark", "Fairy"]
        },
        "Flying": {
            "SuperEffective": ["Grass", "Fighting", "Bug"],
            "NotEffective": ["Electric", "Rock", "Steel"],
            "Resistant": ["Ground"],
            "Normal": ["Normal", "Fire", "Water", "Electric", "Ice", "Psychic", "Ghost", "Dragon", "Dark", "Fairy"]
        },
        "Psychic": {
            "SuperEffective": ["Fighting", "Poison"],
            "NotEffective": ["Steel", "Psychic"],
            "Resistant": ["Dark"],
            "Normal": ["Normal", "Fire", "Water", "Electric", "Grass", "Ice", "Psychic", "Ghost", "Dragon", "Fairy", "Bug", "Rock"]
        },
        "Bug": {
            "SuperEffective": ["Grass", "Psychic", "Dark"],
            "NotEffective": ["Fire", "Fighting", "Poison", "Flying", "Ghost", "Steel"],
            "Resistant": [],
            "Normal": ["Normal", "Water", "Electric", "Ice", "Ground", "Bug", "Dragon", "Fairy", "Rock"]
        },
        "Rock": {
            "SuperEffective": ["Fire", "Ice", "Flying", "Bug"],
            "NotEffective": ["Fighting", "Ground", "Steel"],
            "Resistant": [],
            "Normal": ["Normal", "Water", "Electric", "Grass", "Psychic", "Rock", "Dragon", "Dark", "Fairy", "Poison"]
        },
        "Ghost": {
            "SuperEffective": ["Psychic", "Ghost"],
            "NotEffective": ["Dark"],
            "Resistant": ["Normal", "Fighting"],
            "Normal": ["Normal", "Fire", "Water", "Electric", "Grass", "Ice", "Poison", "Ground", "Flying", "Bug", "Rock", "Dragon", "Fairy", "Steel"]
        },
        "Dragon": {
            "SuperEffective": ["Dragon"],
            "NotEffective": ["Steel"],
            "Resistant": [],
            "Normal": ["Normal", "Fire", "Water", "Electric", "Grass", "Ice", "Fighting", "Poison", "Ground", "Flying", "Psychic", "Bug", "Dark", "Fairy"]
        },
        "Dark": {
            "SuperEffective": ["Psychic", "Ghost"],
            "NotEffective": ["Fighting", "Dark", "Fairy"],
            "Resistant": [],
            "Normal": ["Normal", "Fire", "Water", "Electric", "Grass", "Ice", "Poison", "Ground", "Flying", "Bug", "Rock", "Dragon", "Steel"]
        },
        "Steel": {
            "SuperEffective": ["Ice", "Rock", "Fairy"],
            "NotEffective": ["Fire", "Water", "Electric", "Steel"],
            "Resistant": [],
            "Normal": ["Normal", "Grass", "Psychic", "Ghost", "Dragon", "Dark", "Flying", "Bug"]
        },
        "Fairy": {
            "SuperEffective": ["Fighting", "Dragon", "Dark"],
            "NotEffective": ["Poison", "Steel", "Fire"],
            "Resistant": [],
            "Normal": ["Normal", "Water", "Electric", "Grass", "Ice", "Ground", "Flying", "Psychic", "Bug", "Rock", "Ghost", "Fairy"]
        }
    }

    def findNotEffective():
        not_effective1 = Counter(type_characteristics[type1]['NotEffective'])
        not_effective2 = Counter(type_characteristics[type2]['NotEffective'])
        combined_not_effective = not_effective1 + not_effective2
        double_not_effective = (not_effective1 & not_effective2)
        normal_effective1 = Counter(type_characteristics[type1]['Normal'])
        normal_effective2 = Counter(type_characteristics[type2]['Normal'])
        combined_normal_effective = normal_effective1 + normal_effective2
        resistant1 = Counter(type_characteristics[type1]["Resistant"])
        resistant2 = Counter(type_characteristics[type2]["Resistant"])
        combined_resistant = resistant1 + resistant2

        new_not_effective = (combined_normal_effective & combined_not_effective)
        new_resistant = (combined_resistant)

        # Find the best out of the three

        if len(new_resistant) > 0:
            i = random.randint(0, len(new_resistant) - 1)
            return f"{list(new_resistant.keys())[i]}"
        elif len(double_not_effective) > 0:
            i = random.randint(0, len(double_not_effective) - 1)
            return f"{list(double_not_effective.keys())[i]}"
        elif len(new_not_effective) > 0:
            i = random.randint(0, len(new_not_effective) - 1)
            return f"{new_not_effective[i]}"

    if type2 not in type_characteristics:
        if len(type_characteristics[type1]['Resistant']) > 0:
            i = random.randint(0, len(type_characteristics[type1]['Resistant']) - 1)
            return f"{list(type_characteristics[type1]['Resistant'])[i]}"
        if len(type_characteristics[type1]['NotEffective']) > 0:
            i = random.randint(0, len(type_characteristics[type1]['NotEffective']) - 1)
            return f"{list(type_characteristics[type1]['NotEffective'])[i]}"
    else:
        return findNotEffective()