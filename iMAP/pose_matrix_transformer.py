import numpy as np

poses_path = "C:/Users/DS/Documents/RTAB-Map/space2/poses.txt"
traj_path = "C:/Users/DS/Documents/RTAB-Map/space2/traj_w_c.txt"

with open(poses_path, 'r') as f:
    lines = f.readlines()

with open(traj_path, 'w') as f:
    for line in lines:
        values = list(map(float, line.strip().split()))
        if len(values) == 12:  # 3x4 행렬
            pose = np.vstack([np.array(values).reshape(3,4), [0,0,0,1]])
        elif len(values) == 16:  # 4x4 행렬
            pose = np.array(values).reshape(4,4)
        else:
            continue
        f.write(' '.join(str(x) for x in pose.flatten()) + '\n')
