tmqm_openff
===========================

 * Dataset : tmqm_openff
 * Potential : aimnet2

Description:
------------

Training of aimnet2 with tmqm_openff looking at hyperparameters for spin resolved charge model

Experiments:
------------


- "tmqm_openff_valid_dataset_v1.4_3sep26_ps1234_ds425_fl0.001_lr0.0001_normTrue_nrbf64_nvf16_nfeat128"
  - Modelforge Configuration file: [exp.config_file](./config_valid_dataset_v1.4_3sep26_ps1234_ds425_fl0.001_lr0.0001_normTrue_nrbf64_nvf16_nfeat128.toml)
  
  - loss component: `per_system_energy` : weight = 0.01
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_system_dipole_moment` : weight = 10000.0
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_atom_charge` : weight = 0.01
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_atom_force` : weight = 0.001
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - WandB link: [[ ]]

- "tmqm_openff_valid_dataset_v1.4_3sep26_ps1345_ds435_fl0.001_lr0.0001_normTrue_nrbf64_nvf16_nfeat128"
  - Modelforge Configuration file: [exp.config_file](./config_valid_dataset_v1.4_3sep26_ps1345_ds435_fl0.001_lr0.0001_normTrue_nrbf64_nvf16_nfeat128.toml)
  
  - loss component: `per_system_energy` : weight = 0.01
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_system_dipole_moment` : weight = 10000.0
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_atom_charge` : weight = 0.01
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_atom_force` : weight = 0.001
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - WandB link: [[ ]]



