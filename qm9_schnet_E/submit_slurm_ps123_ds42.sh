#!/bin/bash
#SBATCH --job-name=ps123_ds42_qm9_schnet
#SBATCH --partition=gpu
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=64G
#SBATCH --gres=gpu:1
#SBATCH --time=10:00:00
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
micromamba activate test

# Execute the python command
cd $SLURM_SUBMIT_DIR
pwd
echo "python ../../modelforge/scripts/perform_training.py --condensed_config_path config_ps123_ds42.toml --accelerator 'gpu' --device [0]"
srun python ../../modelforge/scripts/perform_training.py --condensed_config_path config_ps123_ds42.toml --accelerator 'gpu' --device [0]