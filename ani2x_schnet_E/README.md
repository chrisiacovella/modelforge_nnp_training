ani2x_schnet_E
===========================

 * Dataset : ani2x
 * Potential : schnet

Description:
------------

Training of the SchNet potential on the QM9 dataset. This additionally predicts the partial charges on each atom. Local interactions are computed with a cutoff of 5 Å. van der Waals interactions are computed using the DFT-D3 method with a cutoff of 15 Å. The partial charges are used to compute the Coulombic interaction between particles with cutoff of 15 Å. The training includes loss terms for the total system energy, which includes van der Waals and Coulombic energy contributions (`per_system_energy`) and partial charges (`per_atom_charge`).

Experiments:
------------


- "ani2x_schnet_E_ps123_ds42_max"
  - Modelforge Configuration file: [exp.config_file](./config_ps123_ds42_max.toml)
  - Energy shifting: 
  
  - loss component: `per_atom_energy` : weight = 1.0
    - MSE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - WandB link: [[ ]]

- "ani2x_schnet_E_ps124_ds43_max"
  - Modelforge Configuration file: [exp.config_file](./config_ps124_ds43_max.toml)
  - Energy shifting: 
  
  - loss component: `per_atom_energy` : weight = 1.0
    - MSE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - WandB link: [[ ]]

- "ani2x_schnet_E_ps125_ds44_max"
  - Modelforge Configuration file: [exp.config_file](./config_ps125_ds44_max.toml)
  - Energy shifting: 
  
  - loss component: `per_atom_energy` : weight = 1.0
    - MSE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - WandB link: [[ ]]

- "ani2x_schnet_E_ps123_ds42_mean"
  - Modelforge Configuration file: [exp.config_file](./config_ps123_ds42_mean.toml)
  - Energy shifting: 
  
  - loss component: `per_atom_energy` : weight = 1.0
    - MSE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - WandB link: [[ ]]

- "ani2x_schnet_E_ps124_ds43_mean"
  - Modelforge Configuration file: [exp.config_file](./config_ps124_ds43_mean.toml)
  - Energy shifting: 
  
  - loss component: `per_atom_energy` : weight = 1.0
    - MSE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - WandB link: [[ ]]

- "ani2x_schnet_E_ps125_ds44_mean"
  - Modelforge Configuration file: [exp.config_file](./config_ps125_ds44_mean.toml)
  - Energy shifting: 
  
  - loss component: `per_atom_energy` : weight = 1.0
    - MSE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - WandB link: [[ ]]

- "ani2x_schnet_E_ps123_ds42_min"
  - Modelforge Configuration file: [exp.config_file](./config_ps123_ds42_min.toml)
  - Energy shifting: 
  
  - loss component: `per_atom_energy` : weight = 1.0
    - MSE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - WandB link: [[ ]]

- "ani2x_schnet_E_ps124_ds43_min"
  - Modelforge Configuration file: [exp.config_file](./config_ps124_ds43_min.toml)
  - Energy shifting: 
  
  - loss component: `per_atom_energy` : weight = 1.0
    - MSE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - WandB link: [[ ]]

- "ani2x_schnet_E_ps125_ds44_min"
  - Modelforge Configuration file: [exp.config_file](./config_ps125_ds44_min.toml)
  - Energy shifting: 
  
  - loss component: `per_atom_energy` : weight = 1.0
    - MSE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - WandB link: [[ ]]



