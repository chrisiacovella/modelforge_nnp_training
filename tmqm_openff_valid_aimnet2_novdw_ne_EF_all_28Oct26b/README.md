tmqm_openff
===========================

 * Dataset : tmqm_openff
 * Potential : aimnet2

Description:
------------

Training of aimnet2 with tmqm_openff looking at hyperparameters for spin resolved charge model

Experiments:
------------


- "tmqm_openff_E_bs128_full_dataset_v1.6_c_ps1234_ds425_all_m10000_lr0.0008_normTrue_nrbf64_nvf64_nfeat256_ncc2_floss1.0"
  - Modelforge Configuration file: [exp.config_file](./config_E_bs128_full_dataset_v1.6_c_ps1234_ds425_all_m10000_lr0.0008_normTrue_nrbf64_nvf64_nfeat256_ncc2_floss1.0.toml)
  
  - loss component: `per_system_energy` : weight = 1
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_system_dipole_moment` : weight = 10000
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_atom_charge` : weight = 0.0
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_atom_force` : weight = 1.0
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - WandB link: [[ ]]

- "tmqm_openff_E_bs128_full_dataset_v1.6_c_ps1345_ds435_all_m10000_lr0.0008_normTrue_nrbf64_nvf64_nfeat256_ncc2_floss1.0"
  - Modelforge Configuration file: [exp.config_file](./config_E_bs128_full_dataset_v1.6_c_ps1345_ds435_all_m10000_lr0.0008_normTrue_nrbf64_nvf64_nfeat256_ncc2_floss1.0.toml)
  
  - loss component: `per_system_energy` : weight = 1
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_system_dipole_moment` : weight = 10000
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_atom_charge` : weight = 0.0
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_atom_force` : weight = 1.0
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - WandB link: [[ ]]

- "tmqm_openff_E_bs128_full_dataset_v1.6_c_ps1234_ds425_all_m10000_lr0.0008_normTrue_nrbf64_nvf64_nfeat512_ncc2_floss1.0"
  - Modelforge Configuration file: [exp.config_file](./config_E_bs128_full_dataset_v1.6_c_ps1234_ds425_all_m10000_lr0.0008_normTrue_nrbf64_nvf64_nfeat512_ncc2_floss1.0.toml)
  
  - loss component: `per_system_energy` : weight = 1
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_system_dipole_moment` : weight = 10000
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_atom_charge` : weight = 0.0
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_atom_force` : weight = 1.0
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - WandB link: [[ ]]

- "tmqm_openff_E_bs128_full_dataset_v1.6_c_ps1345_ds435_all_m10000_lr0.0008_normTrue_nrbf64_nvf64_nfeat512_ncc2_floss1.0"
  - Modelforge Configuration file: [exp.config_file](./config_E_bs128_full_dataset_v1.6_c_ps1345_ds435_all_m10000_lr0.0008_normTrue_nrbf64_nvf64_nfeat512_ncc2_floss1.0.toml)
  
  - loss component: `per_system_energy` : weight = 1
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_system_dipole_moment` : weight = 10000
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_atom_charge` : weight = 0.0
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_atom_force` : weight = 1.0
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - WandB link: [[ ]]

- "tmqm_openff_E_bs128_full_dataset_v1.6_c_ps1234_ds425_all_m10000_lr0.0008_normTrue_nrbf64_nvf64_nfeat256_ncc2_floss10.0"
  - Modelforge Configuration file: [exp.config_file](./config_E_bs128_full_dataset_v1.6_c_ps1234_ds425_all_m10000_lr0.0008_normTrue_nrbf64_nvf64_nfeat256_ncc2_floss10.0.toml)
  
  - loss component: `per_system_energy` : weight = 1
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_system_dipole_moment` : weight = 10000
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_atom_charge` : weight = 0.0
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_atom_force` : weight = 10.0
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - WandB link: [[ ]]

- "tmqm_openff_E_bs128_full_dataset_v1.6_c_ps1345_ds435_all_m10000_lr0.0008_normTrue_nrbf64_nvf64_nfeat256_ncc2_floss10.0"
  - Modelforge Configuration file: [exp.config_file](./config_E_bs128_full_dataset_v1.6_c_ps1345_ds435_all_m10000_lr0.0008_normTrue_nrbf64_nvf64_nfeat256_ncc2_floss10.0.toml)
  
  - loss component: `per_system_energy` : weight = 1
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_system_dipole_moment` : weight = 10000
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_atom_charge` : weight = 0.0
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_atom_force` : weight = 10.0
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - WandB link: [[ ]]

- "tmqm_openff_E_bs128_full_dataset_v1.6_c_ps1234_ds425_all_m10000_lr0.0008_normTrue_nrbf64_nvf64_nfeat512_ncc2_floss10.0"
  - Modelforge Configuration file: [exp.config_file](./config_E_bs128_full_dataset_v1.6_c_ps1234_ds425_all_m10000_lr0.0008_normTrue_nrbf64_nvf64_nfeat512_ncc2_floss10.0.toml)
  
  - loss component: `per_system_energy` : weight = 1
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_system_dipole_moment` : weight = 10000
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_atom_charge` : weight = 0.0
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_atom_force` : weight = 10.0
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - WandB link: [[ ]]

- "tmqm_openff_E_bs128_full_dataset_v1.6_c_ps1345_ds435_all_m10000_lr0.0008_normTrue_nrbf64_nvf64_nfeat512_ncc2_floss10.0"
  - Modelforge Configuration file: [exp.config_file](./config_E_bs128_full_dataset_v1.6_c_ps1345_ds435_all_m10000_lr0.0008_normTrue_nrbf64_nvf64_nfeat512_ncc2_floss10.0.toml)
  
  - loss component: `per_system_energy` : weight = 1
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_system_dipole_moment` : weight = 10000
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_atom_charge` : weight = 0.0
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_atom_force` : weight = 10.0
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - WandB link: [[ ]]



