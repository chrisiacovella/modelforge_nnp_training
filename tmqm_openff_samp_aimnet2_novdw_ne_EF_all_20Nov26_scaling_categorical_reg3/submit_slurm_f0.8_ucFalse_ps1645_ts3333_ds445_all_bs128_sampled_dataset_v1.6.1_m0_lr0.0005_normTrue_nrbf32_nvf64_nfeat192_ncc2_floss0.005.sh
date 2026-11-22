#!/bin/bash
#SBATCH --job-name=f0.8_ucFalse_ps1645_ts3333_ds445_all_bs128_sampled_dataset_v1.6.1_m0_lr0.0005_normTrue_nrbf32_nvf64_nfeat192_ncc2_floss0.005_tmqm_openff_aimnet2
#SBATCH --partition=gpu
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=64G
#SBATCH --gres=gpu:1
#SBATCH --time=0-96:00:00
#SBATCH --output=slurm_out/%j_%x_%N.out
#SBATCH --error=slurm_err/%j_%x_%N.err

source ${HOME}/.bashrc

# Report node in use
hostname

# Disable NCC
export NCCL_P2P_DISABLE=1

# Report CUDA info
env | sort | grep 'CUDA'

# Report GPUs available
nvidia-smi

# Activate environment
micromamba activate modelforge

# Execute the python command
cd $SLURM_SUBMIT_DIR
pwd
echo "python /data1/choderaj/iacovec/modelforge/scripts/perform_training.py --condensed_config_path config_f0.8_ucFalse_ps1645_ts3333_ds445_all_bs128_sampled_dataset_v1.6.1_m0_lr0.0005_normTrue_nrbf32_nvf64_nfeat192_ncc2_floss0.005.toml --accelerator 'gpu' --device [0]"
srun python /data1/choderaj/iacovec/modelforge/scripts/perform_training.py --condensed_config_path config_f0.8_ucFalse_ps1645_ts3333_ds445_all_bs128_sampled_dataset_v1.6.1_m0_lr0.0005_normTrue_nrbf32_nvf64_nfeat192_ncc2_floss0.005.toml --accelerator 'gpu' --device [0]