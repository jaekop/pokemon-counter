import pandas as pd
import tkinter as tk
from PIL import Image, ImageTk
import collections
import logic

"""
    import re (regex or string splitting)
    df = dataframe
    df.head(x) is x amoutn of rows down starting from index 0
    df.tail(x) is the same but startin gform the bottom
    df.row["Name"]
    df.columns tells us the labels for the x axis, you can also cite a specific column to find all the instances of that column
    df.iloc[1] tells me the labels for on specific index. 3d arr -> 2d and it can be df.iloc[1, 2] to get one instance of data
    df.loc[df['Type 1'] == 'Fire'] or df.loc[(df['Type 1'] == 'Fire') & (df['Generation'] == 1)]

    How to check for instance sin the entire list,
    for index, row in df.iterrows():
    
    .contains("^this menas the start")

    if I wanter to change a type name
    df.loc[df['Type 1'] == 'Fire', 'Type 1'] = 'Flamer'

    df.describe = a bunch of stats

    df.sort_values("Names") Sorts the data set by names alphabetically.
    or df.sort_values(['Type 1', 'HP'], ascending=[0, 1])

    pf['Total'] = pf.iloc[:, 4:10].sum(axis=1)
    cols = list(pf.columns.values)
    pf = pf[cols[0:4] + [cols[-1]] + cols[4:12]]
    pf.drop(columns=['Total'])
    pf.sort_values('Total', ascending=False)
    print(pf.head(10))
    pf.to_csv('modified.csv', index=False, sep='yada')
    pf.to_excel('.xlsx')

    df.reset_index(drop = True or else it just makes a new one)
    """

#D9C690

def GUIsetup(courage, imagerefs):
    bg = tk.PhotoImage(file=r"C:\Users\lostv\OneDrive\Documents\Python_Projects\Personal\Project_5_PokemonPandas\bg.png")
    imagerefs.append(bg)
    # garbage collection 

    canvas = tk.Canvas(courage, width=1200, height=900)
    canvas.place(x=0,y=0)
    canvas.create_image(0, 0, anchor=tk.NW, image=bg)

    courage.geometry("800x600")
    courage.resizable(False, False)
    courage.configure(bg='#EDE2C3')
    title = tk.Label(courage, text="Welcome To Pokemon\nCounter Generator", bg='#D9C690', font=("DePixel", 23), fg='Black')
    title.place(x=200,y=10)

def main():
    def on_enter(event):
        # Because the lambda function needs it to be always in scope
        global suggestion_label, suggestion_pokemons
        if suggestion_label is not None:
            suggestion_label.destroy()
            suggestion_pokemons.destroy()
        poke = ans_box.get()
        if poke.lower() in pf['Name'].str.lower().values:
            poke_id = pf[pf['Name'].str.lower() == poke.lower()]['Pokedex ID'].iloc[0]
            poke_t1 = pf[pf['Name'].str.lower() == poke.lower()]['Type 1'].iloc[0]
            poke_t2 = pf[pf['Name'].str.lower() == poke.lower()]['Type 2'].iloc[0]
            poke_att = pf[pf['Name'].str.lower() == poke.lower()]['Attack'].iloc[0]
            poke_def = pf[pf['Name'].str.lower() == poke.lower()]['Defense'].iloc[0]
            poke_satt = pf[pf['Name'].str.lower() == poke.lower()]['Sp. Atk'].iloc[0]
            poke_sdef = pf[pf['Name'].str.lower() == poke.lower()]['Sp. Def'].iloc[0]

            plan = stats(poke_att, poke_def, poke_satt, poke_sdef, 0)

            best = logic.findWeakness(poke_t1, poke_t2)

            if plan == "Physical":
                flying_types = pf[(pf['Type 1'] == best) | (pf['Type 2'] == best)]
                sorted_flying_types = flying_types.sort_values(by=['Attack', 'Defense'], ascending=[False, False])
                best_name = sorted_flying_types.iloc[0]['Name']
                best_name_index = sorted_flying_types.iloc[0]['Pokedex ID']
            elif plan == "Physical & Special":
                flying_types = pf[(pf['Type 1'] == best) | (pf['Type 2'] == best)]
                sorted_flying_types = flying_types.sort_values(by=['Attack', 'Sp. Def'], ascending=[False, False])
                best_name = sorted_flying_types.iloc[0]['Name']
                best_name_index = sorted_flying_types.iloc[0]['Pokedex ID']
            elif plan == "Special & Physical":
                flying_types = pf[(pf['Type 1'] == best) | (pf['Type 2'] == best)]
                sorted_flying_types = flying_types.sort_values(by=['Sp. Atk', 'Defense'], ascending=[False, False])
                best_name = sorted_flying_types.iloc[0]['Name']
                best_name_index = sorted_flying_types.iloc[0]['Pokedex ID']
            elif plan == "Special":
                flying_types = pf[(pf['Type 1'] == best) | (pf['Type 2'] == best)]
                sorted_flying_types = flying_types.sort_values(by=['Sp. Atk', 'Sp. Def'], ascending=[False, False])
                best_name = sorted_flying_types.iloc[0]['Name']
                best_name_index = sorted_flying_types.iloc[0]['Pokedex ID']
            l1, l2, l3, l4, title = createImage(poke_id, imagerefs, courage, poke_t1, poke_t2, best_name, best_name_index, best)
            return
        pokemon_checker1 = pf[pf['Name'].str.lower().str.contains(poke.lower())]
        pokemon_checker2 = stringSplitta(poke.lower(), pf['Name'])
        if not (pokemon_checker1.empty):
            # This method checks if its missing any letters ahead of it using contain
            suggestion_label = tk.Label(courage, text="POKEMON NOT REGISTERED\n Did you mean", bg="#D9C690", font=("DePixel", 14))
            fa = '\n'.join(pokemon_checker1['Name'].drop_duplicates())
            suggestion_pokemons = tk.Label(courage, text=fa, bg="#D9C690", font=("DePixel", 14))
            suggestion_label.place(x=200,y=120)
            suggestion_pokemons.place(x=200,y=179)
        else:
            # This method checks if they contain 75 or more percent of the same characters, to try to predict misspellings.
            suggestion_label = tk.Label(courage, text="POKEMON NOT REGISTERED\n Did you mean", bg="#D9C690", font=("DePixel", 14))
            fa = '\n'.join(pokemon_checker2) if pokemon_checker2 else "No suggestions found"  
            suggestion_pokemons = tk.Label(courage, text=fa, bg="#D9C690", font=("DePixel", 14))
            suggestion_label.place(x=200,y=120)
            suggestion_pokemons.place(x=200,y=179)

    imagerefs = []
    courage = tk.Tk()
    GUIsetup(courage, imagerefs)

    pf = pd.read_csv('real_pokemon.csv')
    # p_name = input("Enter the name of any pokemon, ")
    ans_box = tk.Entry(courage, width=23, font=('DePixel', 10))
    ans_box.place(x=100,y=520)
    ans_box.bind("<Return>", on_enter)

    courage.mainloop()

def stringSplitta(istr, poke_names):
    matches = []
    counter1 = collections.Counter(istr)
    for names in poke_names:
        nameslow = names.lower()
        counter2 = collections.Counter(nameslow)
        denominator = max(sum(counter1.values()), sum(counter2.values()))
        #Numerator takes the common values and counts em
        numerator = sum((counter1 & counter2).values())
        if (numerator/denominator) >= .75:
            matches.append(names)
    return matches if matches else False

def createImage(poke_id, image_refs, courage, t1, t2, rec_name, rec_id, best):
    var = 70
    global l1, l2, l3, l4, title
    if l1 is not None:
        l1.destroy()
        l2.destroy()
        l4.destroy()
        if l3 is not None:
            l3.destroy()
        if title is not None:
            title.destroy()
        
    imagepath = f"C:\\Users\\lostv\\OneDrive\\Documents\\Python_Projects\\Personal\\Project_5_PokemonPandas\\pokemon_images\\{poke_id}.png"
    image = Image.open(imagepath)
    image_res = image.resize((240, 160), Image.LANCZOS)
    image_real = ImageTk.PhotoImage(image_res)
    image_refs.append(image_real)

    t1_path = f"C:\\Users\\lostv\\OneDrive\\Documents\\Python_Projects\\Personal\\Project_5_PokemonPandas\\types\\{t1}.png"
    t1mage = Image.open(t1_path)
    t1res = t1mage.resize((100, 100), Image.LANCZOS)
    t1_real = ImageTk.PhotoImage(t1res)
    image_refs.append(t1_real)

    if t2 == t2:
        t2_path = f"C:\\Users\\lostv\\OneDrive\\Documents\\Python_Projects\\Personal\\Project_5_PokemonPandas\\types\\{t2}.png"
        t2mage = Image.open(t2_path)
        t2res = t2mage.resize((100, 100), Image.LANCZOS)
        t2_real = ImageTk.PhotoImage(t2res)
        image_refs.append(t2_real)
        l3 = tk.Label(courage, image=t2_real, bg="#EDE2C3")
        l3.place(x=250,y=350)
    else:
        var = 150
        l3 = None

    t3_path = f"C:\\Users\\lostv\\OneDrive\\Documents\\Python_Projects\\Personal\\Project_5_PokemonPandas\\types\\{best}.png"
    t3mage = Image.open(t3_path)
    t3res = t3mage.resize((100, 100), Image.LANCZOS)
    t3_real = ImageTk.PhotoImage(t3res)
    image_refs.append(t3_real)
    #Name and Image
    t3imagepath = f"C:\\Users\\lostv\\OneDrive\\Documents\\Python_Projects\\Personal\\Project_5_PokemonPandas\\pokemon\\icons\\{rec_id}.png"
    t3image = Image.open(t3imagepath)
    t3image_res = t3image.resize((240, 160), Image.LANCZOS)
    t3image_real = ImageTk.PhotoImage(t3image_res)
    image_refs.append(t3image_real)
    
    title = tk.Label(courage, text=rec_name, bg='#D9C690', font=("DePixel", 14), fg='Black')
    title.place(x=450,y=500)

    l1 = tk.Label(courage, image=image_real, bg="#EDE2C3")
    l1.place(x=90,y=200)
    l2 = tk.Label(courage, image=t1_real, bg="#EDE2C3")
    l2.place(x=var,y=350)
    l4 = tk.Label(courage, image=t3_real, bg="#EDE2C3")
    l4.place(x=550,y=350)
    l5 = tk.Label(courage, image=t3image_real, bg="#EDE2C3")
    l5.place(x=485,y=200)
    return l1, l2, l3, l4, title

def stats(att, deff, spatt, spdef, hp):
    def eval():
        scale = {'Att': att, 'Def': deff,"Sp. Att": spatt, 'Sp. Def': spdef, 'HP': hp}
        if (scale['Att'] >= scale['Sp. Att']):
            patt = True
        else:
            patt = False
        if (scale['Def'] >= scale['Sp. Def']):
            pdef = True
        else:
            pdef = False
        return patt, pdef
    p1, p2 = eval()
    if p1 and p2:
        return "Physical"
    elif p1:
        return "Physical & Special"
    elif p2:
        return "Special & Physical"
    else:
        return "Special"
    
if __name__ == "__main__":
    #Need to declare these in the full scope bc they are global.
    suggestion_label = None
    suggestion_pokemons = None
    l1 = None
    l2 = None
    l3 = None
    l4 = None
    title = None
    main()

