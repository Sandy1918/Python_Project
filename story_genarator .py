def get_input(word_type):
    user_input=input(f"Enter a {word_type}:-")
    return user_input
def count(num):
    for i in range(num):
        i=i+1
        arr.append(i)
    return arr
def introduction(hero,hero_in,side_actor):
    dialogues_1=f"""
    {side_actor}:-counting numbers{lst}
    suddenly close up to {hero_in}
    {hero_in}:-bhairava ee chiravi ksnanam lo ina nijam cheppu 
    *************next scene**************
    {hero}:-na oopriri na gamyam anni nuve mitra    
    ***************next scene************
    kattu panna {hero_in} loyaloki padipoyindhi
    mana {hero}kuda dookadu
    ***************next scene**************
    {side_actor}:-malli pudthav ra bhairava.
    """
    return dialogues_1


hero=get_input("hero")
hero_in=get_input("hero_in")
side_actor=get_input("side_actor")
num=100
arr=[]
lst=tuple(count(num))
print(introduction(hero, hero_in, side_actor))


