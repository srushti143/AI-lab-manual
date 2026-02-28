facts = {"raining","cloudy"}
rules = [ (["raining"],"wet_ground"), (["cloudy"],"maybe_rain"), (["raining","cloudy"],"umbrella_needed") ]

changed = True
while changed:
    changed = False
    for pre, con in rules:
        if con not in facts and all(p in facts for p in pre):
            facts.add(con)
            changed = True

print("All facts:", facts)