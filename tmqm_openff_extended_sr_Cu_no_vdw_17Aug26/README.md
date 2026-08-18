tmqm_openff
===========================

 * Dataset : tmqm_openff
 * Potential : aimnet2_sr

Description:
------------

Training of aimnet2 sr with tmqm_openff for Cu looking at hyperparameters for spin resolved charge model

Experiments:
------------


- "tmqm_openff_all_dataset_seed42_v1.4d_ps1234_ds425_fl0_lr0.0001_normTrue_nrbf64_nvf16_nfeat128"
  - Modelforge Configuration file: [exp.config_file](./config_all_dataset_seed42_v1.4d_ps1234_ds425_fl0_lr0.0001_normTrue_nrbf64_nvf16_nfeat128.toml)
  
  - loss component: `per_system_energy` : weight = 0.01
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_system_dipole_moment` : weight = 10000.0
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_atom_charge` : weight = 0.01
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - WandB link: [[ ]]

- "tmqm_openff_all_dataset_seed42_v1.4d_ps1345_ds435_fl0_lr0.0001_normTrue_nrbf64_nvf16_nfeat128"
  - Modelforge Configuration file: [exp.config_file](./config_all_dataset_seed42_v1.4d_ps1345_ds435_fl0_lr0.0001_normTrue_nrbf64_nvf16_nfeat128.toml)
  
  - loss component: `per_system_energy` : weight = 0.01
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_system_dipole_moment` : weight = 10000.0
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_atom_charge` : weight = 0.01
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - WandB link: [[ ]]

- "tmqm_openff_all_dataset_seed42_v1.4d_ps1234_ds425_fl0_lr0.0001_normFalse_nrbf64_nvf16_nfeat128"
  - Modelforge Configuration file: [exp.config_file](./config_all_dataset_seed42_v1.4d_ps1234_ds425_fl0_lr0.0001_normFalse_nrbf64_nvf16_nfeat128.toml)
  
  - loss component: `per_system_energy` : weight = 0.01
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_system_dipole_moment` : weight = 10000.0
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_atom_charge` : weight = 0.01
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - WandB link: [[ ]]

- "tmqm_openff_all_dataset_seed42_v1.4d_ps1345_ds435_fl0_lr0.0001_normFalse_nrbf64_nvf16_nfeat128"
  - Modelforge Configuration file: [exp.config_file](./config_all_dataset_seed42_v1.4d_ps1345_ds435_fl0_lr0.0001_normFalse_nrbf64_nvf16_nfeat128.toml)
  
  - loss component: `per_system_energy` : weight = 0.01
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_system_dipole_moment` : weight = 10000.0
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_atom_charge` : weight = 0.01
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - WandB link: [[ ]]

- "tmqm_openff_all_dataset_seed42_v1.4d_ps1234_ds425_fl0.001_lr0.0001_normTrue_nrbf64_nvf16_nfeat128"
  - Modelforge Configuration file: [exp.config_file](./config_all_dataset_seed42_v1.4d_ps1234_ds425_fl0.001_lr0.0001_normTrue_nrbf64_nvf16_nfeat128.toml)
  
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

- "tmqm_openff_all_dataset_seed42_v1.4d_ps1345_ds435_fl0.001_lr0.0001_normTrue_nrbf64_nvf16_nfeat128"
  - Modelforge Configuration file: [exp.config_file](./config_all_dataset_seed42_v1.4d_ps1345_ds435_fl0.001_lr0.0001_normTrue_nrbf64_nvf16_nfeat128.toml)
  
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

- "tmqm_openff_all_dataset_seed42_v1.4d_ps1234_ds425_fl0.001_lr0.0001_normFalse_nrbf64_nvf16_nfeat128"
  - Modelforge Configuration file: [exp.config_file](./config_all_dataset_seed42_v1.4d_ps1234_ds425_fl0.001_lr0.0001_normFalse_nrbf64_nvf16_nfeat128.toml)
  
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

- "tmqm_openff_all_dataset_seed42_v1.4d_ps1345_ds435_fl0.001_lr0.0001_normFalse_nrbf64_nvf16_nfeat128"
  - Modelforge Configuration file: [exp.config_file](./config_all_dataset_seed42_v1.4d_ps1345_ds435_fl0.001_lr0.0001_normFalse_nrbf64_nvf16_nfeat128.toml)
  
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



