def binary_swp(data, path_to_swp_scripts):
    '''
    This funciton allows the user to use the csv file from the orignal net_dx fucntion. It converts this csv and
    all rows and columns into a numpy array.
    '''
    import numpy as np
    import matlab.engine
    eng = matlab.engine.start_matlab()

    os.chdir(path_to_swp_scripts)
    A_list = matlab.double(data.tolist())
    SWP = eng.small_world_propensity(A_list, 'bin')

    return SWP
