#!/bin/bash
#SBATCH --job-name=ext_dataset_v1.4c_ps125_ds44_fl0.001_tmqm_openff_aimnet2
#SBATCH --partition=gpu
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=64G
#SBATCH --gres=gpu:a100:1
#SBATCH --time=3-00:00:00
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
echo "python /data1/choderaj/iacovec/modelforge/scripts/perform_training.py --condensed_config_path config_ext_dataset_v1.4c_ps125_ds44_fl0.001.toml --accelerator 'gpu' --device [0]"
srun python /data1/choderaj/iacovec/modelforge/scripts/perform_training.py --condensed_config_path config_ext_dataset_v1.4c_ps125_ds44_fl0.001.toml --accelerator 'gpu' --device [0]