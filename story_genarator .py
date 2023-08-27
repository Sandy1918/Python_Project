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
    {hero_in}:-hey how r u
    *************next scene**************
    {hero}:- i am great
    ***************next scene************
    near coffee machine {hero_in} went to drink coffee
    now {hero} also follows
    ***************next scene**************
    {side_actor}:-there is no coffee cups
    """
    return dialogues_1


hero=get_input("hero")
hero_in=get_input("hero_in")
side_actor=get_input("side_actor")
num=100
arr=[]
lst=tuple(count(num))
print(introduction(hero, hero_in, side_actor))


