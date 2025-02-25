import site
site.addsitedir("../ARGUS")

from ARGUS_segmentation_train import ARGUS_segmentation_train

run_num = 0
device_num = 0

nnet = ARGUS_segmentation_train("ARGUS_pretrain_ar.cfg", 
        "vfold", 
        device_num=device_num)

nnet.setup_vfold_files()

for vfn in range(nnet.num_folds):
    nnet.init_model(run_num)
    nnet.setup_training_vfold(vfn, run_num)
    nnet.train_vfold(run_num)
