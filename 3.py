class KB: 
    def __init__(s): s.f=set()
    def tell(s,f): s.f.add(f)

class WumpusAgent:
    def __init__(s): 
        s.kb=KB(); s.gold=False
    def run(s):
        world={(0,0):["Breeze"],(0,1):["Stench"],(1,0):[],(1,1):["Breeze"]}
        for loc, percepts in world.items():
            for p in percepts: s.kb.tell((p,loc))
            if "Glitter" in percepts: s.gold=True
        print("Gold found" if s.gold else "Gold not found")

WumpusAgent().run()