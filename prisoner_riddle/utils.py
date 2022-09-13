import progressbar


def create_progressbar(count: int):

    widgets = [
        ' [', progressbar.Timer(format= 'elapsed time: %(elapsed)s'), '] ',
        progressbar.Bar('*'),
        ' (', progressbar.ETA(), ') ',
    ]
    
    return progressbar.ProgressBar(max_value=count, 
                                   widgets=widgets).start()