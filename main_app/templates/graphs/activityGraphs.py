import matplotlib.pyplot as plt

run = []
arms = []
legs = []
core = []
dater = []
datea = []
datel = []
datec = []
lw = 0
cw = 0
aw = 0
for act in User.Activity:
    if  act.activity = 'r':
        run.append(act.rep)
        dater.append(act.date)
    elif act.activity = 'l':
        legs.append(act.rep)
        datel.append(act.date)
        lw += act.weight
    elif act.activity = 'c':
        core.append(act.rep)
        datec.append(act.date)
        cw += act.weight
    elif act.activity = 'a':
        arms.append(act.rep)
        datea.append(act.date)
        aw += act.weight
 
plt.plot(dater,run,'ro',datea,arms,'bo',datec,core,'go',datel,legs,'yo')
plt.ylabel('Reps / Distance')
plt.xlabel('Date')
console.log(plt.show());
return 
    {
    graph :plt.show()
    weights = f"arms:{aw}   legs:{lw}   core:{cw}"
    }
