import matplotlib.pyplot as plt

run = []
arms = []
legs = []
core = []
dater = []
datea = []
datel = []
datec = []

for act in User.Profile.Activity:
    if  act.activity = 'r':
        run.append(act.rep)
        dater.append(act.date)
    elif act.activity = 'l':
        legs.append(act.rep)
        datel.append(act.date)
    elif act.activity = 'c':
        core.append(act.rep)
        datec.append(act.date)
    elif act.activity = 'a':
        arms.append(act.rep)
        datea.append(act.date)


plt.plot(dater,run)
plt.ylabel('Reps / Distance')
plt.xlabel('Date')

