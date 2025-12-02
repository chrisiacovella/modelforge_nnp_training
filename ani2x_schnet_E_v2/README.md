ani2x_schnet_E
===========================

 * Dataset : ani2x
 * Potential : schnet

Description:
------------

Training of the SchNet potential on the QM9 dataset. This additionally predicts the partial charges on each atom. Local interactions are computed with a cutoff of 5 Å. van der Waals interactions are computed using the DFT-D3 method with a cutoff of 15 Å. The partial charges are used to compute the Coulombic interaction between particles with cutoff of 15 Å. The training includes loss terms for the total system energy, which includes van der Waals and Coulombic energy contributions (`per_system_energy`) and partial charges (`per_atom_charge`).

Experiments:
------------


- "ani2x_schnet_E_ps123_ds42_lr0.001"
  - Modelforge Configuration file: [exp.config_file](./config_ps123_ds42_lr0.001.toml)
  - Learning rate: 0.001
  
  - loss component: `per_atom_energy` : weight = 1.0
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - WandB link: [[ ]]

- "ani2x_schnet_E_ps124_ds43_lr0.001"
  - Modelforge Configuration file: [exp.config_file](./config_ps124_ds43_lr0.001.toml)
  - Learning rate: 0.001
  
  - loss component: `per_atom_energy` : weight = 1.0
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - WandB link: [[ ]]

- "ani2x_schnet_E_ps125_ds44_lr0.001"
  - Modelforge Configuration file: [exp.config_file](./config_ps125_ds44_lr0.001.toml)
  - Learning rate: 0.001
  
  - loss component: `per_atom_energy` : weight = 1.0
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - WandB link: [[ ]]

- "ani2x_schnet_E_ps123_ds42_lr0.0009"
  - Modelforge Configuration file: [exp.config_file](./config_ps123_ds42_lr0.0009.toml)
  - Learning rate: 0.0009
  
  - loss component: `per_atom_energy` : weight = 1.0
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - WandB link: [[ ]]

- "ani2x_schnet_E_ps124_ds43_lr0.0009"
  - Modelforge Configuration file: [exp.config_file](./config_ps124_ds43_lr0.0009.toml)
  - Learning rate: 0.0009
  
  - loss component: `per_atom_energy` : weight = 1.0
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - WandB link: [[ ]]

- "ani2x_schnet_E_ps125_ds44_lr0.0009"
  - Modelforge Configuration file: [exp.config_file](./config_ps125_ds44_lr0.0009.toml)
  - Learning rate: 0.0009
  
  - loss component: `per_atom_energy` : weight = 1.0
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - WandB link: [[ ]]

- "ani2x_schnet_E_ps123_ds42_lr0.0005"
  - Modelforge Configuration file: [exp.config_file](./config_ps123_ds42_lr0.0005.toml)
  - Learning rate: 0.0005
  
  - loss component: `per_atom_energy` : weight = 1.0
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - WandB link: [[ ]]

- "ani2x_schnet_E_ps124_ds43_lr0.0005"
  - Modelforge Configuration file: [exp.config_file](./config_ps124_ds43_lr0.0005.toml)
  - Learning rate: 0.0005
  
  - loss component: `per_atom_energy` : weight = 1.0
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - WandB link: [[ ]]

- "ani2x_schnet_E_ps125_ds44_lr0.0005"
  - Modelforge Configuration file: [exp.config_file](./config_ps125_ds44_lr0.0005.toml)
  - Learning rate: 0.0005
  
  - loss component: `per_atom_energy` : weight = 1.0
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - WandB link: [[ ]]



