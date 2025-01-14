
import sys
import os

scene = sys.argv[1]

dataset_dir = "/content/drive/MyDrive/AI_Capstone/data/nerf_synthetic/"
log_dir = "/content/drive/MyDrive/AI_Capstone/log/Synthetic NeRF/TensoRF_origin"

content= f'''
dataset_name = blender
datadir = {os.path.join(dataset_dir,scene)}
expname =  {scene}_tensorf
basedir = {log_dir}


#------ Number images ------
train_indexs    = [26, 86, 2, 55, 75, 16, 73, 93]
val_indexs      = [0,8,16,24,32,40,48,56,64,72,80,88,96]
test_indexs     = [0,8,16,24,32,40,48,56,64,72,80,88,96,104,112,120,128,136,144,152,160,168,176,184,192]

# N_train_imgs  = 8
# N_val_imgs    = 13
# N_test_imgs   = 25

n_iters = 15000
batch_size = 4096

N_voxel_init = 2097156 # 128**3
N_voxel_final = 27000000 # 300**3
upsamp_list = [2000,3000,4000,5500,7000]
update_AlphaMask_list = [2000,4000]

N_vis = 5
vis_every = 10000

render_test = 1

n_lamb_sigma = [16,16,16]
n_lamb_sh = [48,48,48]
model_name = TensorVMSplit


shadingMode = MLP_Fea
fea2denseAct = softplus

view_pe = 2
fea_pe = 2

L1_weight_inital = 8e-5
L1_weight_rest = 4e-5
rm_weight_mask_thre = 1e-4

## please uncomment following configuration if hope to training on cp model
#model_name = TensorCP
#n_lamb_sigma = [96]
#n_lamb_sh = [288]
#N_voxel_final = 125000000 # 500**3
#L1_weight_inital = 1e-5
#L1_weight_rest = 1e-5
'''

cur_dir = os.path.join(os.getcwd(),os.path.dirname(sys.argv[0]))
file_name = f'{scene}.txt'
save_path = os.path.join(cur_dir,file_name)


with open(save_path, 'w') as file:
    file.write(content)
