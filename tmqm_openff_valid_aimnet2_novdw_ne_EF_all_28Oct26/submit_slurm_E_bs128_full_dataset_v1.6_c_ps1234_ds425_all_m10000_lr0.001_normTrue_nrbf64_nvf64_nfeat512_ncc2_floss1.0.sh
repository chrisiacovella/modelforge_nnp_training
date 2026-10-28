#!/bin/bash
#SBATCH --job-name=E_bs128_full_dataset_v1.6_c_ps1234_ds425_all_m10000_lr0.001_normTrue_nrbf64_nvf64_nfeat512_ncc2_floss1.0_tmqm_openff_aimnet2
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
echo "python /data1/choderaj/iacovec/modelforge/scripts/perform_training.py --condensed_config_path config_E_bs128_full_dataset_v1.6_c_ps1234_ds425_all_m10000_lr0.001_normTrue_nrbf64_nvf64_nfeat512_ncc2_floss1.0.toml --accelerator 'gpu' --device [0]"
srun python /data1/choderaj/iacovec/modelforge/scripts/perform_training.py --condensed_config_path config_E_bs128_full_dataset_v1.6_c_ps1234_ds425_all_m10000_lr0.001_normTrue_nrbf64_nvf64_nfeat512_ncc2_floss1.0.toml --accelerator 'gpu' --device [0]