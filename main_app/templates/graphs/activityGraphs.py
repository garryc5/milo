def activityParce()
    run = ''
    arms = ''
    legs = ''
    core = ''
    dater = ''
    datea = ''
    datel = ''
    datec = ''
    lw = 0
    cw = 0
    aw = 0
    for act in User.Activity:
        if  act.activity = 'r':
            run += f"Distance:  {act.rep}  "
            dater += f"Date:  {act.date}  "
        elif act.activity = 'l':
            legs += f"Reps:  {act.rep}  "
            datel += f"Date:  {act.date}  "
            lw += act.weight
        elif act.activity = 'c':
            core += f"Reps:  {act.rep}  "
            datec += f"Date:  {act.date}  "
            cw += act.weight
        elif act.activity = 'a':
            arms += f"Reps:  {act.rep}  "
            datea += f"Date:  {act.date}  "
            aw += act.weight
    
    plt.plot(dater,run,'ro',datea,arms,'bo',datec,core,'go',datel,legs,'yo')
    plt.ylabel('Reps / Distance')
    plt.xlabel('Date')
    console.log(plt.show());
    return 
        {
        'run' : run,
        'runDates':dater,
        'legs': legs,
        'legDates':datel,
        'arms': arms,
        'armDates':datea,
        'core': core,
        'coreDates':datec,
        'weights' : f"arms:{aw}   legs:{lw}   core:{cw}"
        }
