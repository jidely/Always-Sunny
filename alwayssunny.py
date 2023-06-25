import random

def alwayssunny():
    season = random.randint(1,15)
    max_episode = {1: 7, 4: 13, 7: 13, 3: 15, 5: 12, 6: 14, 15: 8}.get(season, 10)
    episode = random.randint(1,max_episode)

    watched = f'Season {season}, Episode {episode}'
    
    with open("watched.txt","r") as f:
        if watched not in f.read():
            with open("watched.txt","a") as f:
                f.write(watched + '\n')
            print(watched)
        else:
            print('Try Again'+f"You have already seen this episode{watched}")
            alwayssunny()

alwayssunny()
