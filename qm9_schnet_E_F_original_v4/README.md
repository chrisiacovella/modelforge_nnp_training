qm9_schnet_E
===========================

 * Dataset : qm9
 * Potential : schnet

Description:
------------

Training of the SchNet potential on the QM9 dataset. Local interactions are computed with a cutoff of 5 Å. Only per-system energy appears in the loss function. 

Experiments:
------------


- "qm9_schnet_E_ps123_ds42_lr0.0005_normTrue_force_1"
  - Modelforge Configuration file: [exp.config_file](./config_ps123_ds42_lr0.0005_normTrue_force_1.toml)
  - per_atom_energy normalization: 
  - initial learning rate: 
  
  - loss component: `per_system_energy` : weight = 1
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_atom_force` : weight = 1
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - WandB link: [[ ]]

- "qm9_schnet_E_ps124_ds43_lr0.0005_normTrue_force_1"
  - Modelforge Configuration file: [exp.config_file](./config_ps124_ds43_lr0.0005_normTrue_force_1.toml)
  - per_atom_energy normalization: 
  - initial learning rate: 
  
  - loss component: `per_system_energy` : weight = 1
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_atom_force` : weight = 1
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - WandB link: [[ ]]

- "qm9_schnet_E_ps125_ds44_lr0.0005_normTrue_force_1"
  - Modelforge Configuration file: [exp.config_file](./config_ps125_ds44_lr0.0005_normTrue_force_1.toml)
  - per_atom_energy normalization: 
  - initial learning rate: 
  
  - loss component: `per_system_energy` : weight = 1
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_atom_force` : weight = 1
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - WandB link: [[ ]]

- "qm9_schnet_E_ps126_ds45_lr0.0005_normTrue_force_1"
  - Modelforge Configuration file: [exp.config_file](./config_ps126_ds45_lr0.0005_normTrue_force_1.toml)
  - per_atom_energy normalization: 
  - initial learning rate: 
  
  - loss component: `per_system_energy` : weight = 1
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_atom_force` : weight = 1
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - WandB link: [[ ]]

- "qm9_schnet_E_ps123_ds42_lr0.0005_normTrue_force_0.1"
  - Modelforge Configuration file: [exp.config_file](./config_ps123_ds42_lr0.0005_normTrue_force_0.1.toml)
  - per_atom_energy normalization: 
  - initial learning rate: 
  
  - loss component: `per_system_energy` : weight = 1
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_atom_force` : weight = 0.1
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - WandB link: [[ ]]

- "qm9_schnet_E_ps124_ds43_lr0.0005_normTrue_force_0.1"
  - Modelforge Configuration file: [exp.config_file](./config_ps124_ds43_lr0.0005_normTrue_force_0.1.toml)
  - per_atom_energy normalization: 
  - initial learning rate: 
  
  - loss component: `per_system_energy` : weight = 1
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_atom_force` : weight = 0.1
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - WandB link: [[ ]]

- "qm9_schnet_E_ps125_ds44_lr0.0005_normTrue_force_0.1"
  - Modelforge Configuration file: [exp.config_file](./config_ps125_ds44_lr0.0005_normTrue_force_0.1.toml)
  - per_atom_energy normalization: 
  - initial learning rate: 
  
  - loss component: `per_system_energy` : weight = 1
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_atom_force` : weight = 0.1
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - WandB link: [[ ]]

- "qm9_schnet_E_ps126_ds45_lr0.0005_normTrue_force_0.1"
  - Modelforge Configuration file: [exp.config_file](./config_ps126_ds45_lr0.0005_normTrue_force_0.1.toml)
  - per_atom_energy normalization: 
  - initial learning rate: 
  
  - loss component: `per_system_energy` : weight = 1
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_atom_force` : weight = 0.1
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - WandB link: [[ ]]

- "qm9_schnet_E_ps123_ds42_lr0.0005_normTrue_force_0.01"
  - Modelforge Configuration file: [exp.config_file](./config_ps123_ds42_lr0.0005_normTrue_force_0.01.toml)
  - per_atom_energy normalization: 
  - initial learning rate: 
  
  - loss component: `per_system_energy` : weight = 1
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_atom_force` : weight = 0.01
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - WandB link: [[ ]]

- "qm9_schnet_E_ps124_ds43_lr0.0005_normTrue_force_0.01"
  - Modelforge Configuration file: [exp.config_file](./config_ps124_ds43_lr0.0005_normTrue_force_0.01.toml)
  - per_atom_energy normalization: 
  - initial learning rate: 
  
  - loss component: `per_system_energy` : weight = 1
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_atom_force` : weight = 0.01
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - WandB link: [[ ]]

- "qm9_schnet_E_ps125_ds44_lr0.0005_normTrue_force_0.01"
  - Modelforge Configuration file: [exp.config_file](./config_ps125_ds44_lr0.0005_normTrue_force_0.01.toml)
  - per_atom_energy normalization: 
  - initial learning rate: 
  
  - loss component: `per_system_energy` : weight = 1
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_atom_force` : weight = 0.01
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - WandB link: [[ ]]

- "qm9_schnet_E_ps126_ds45_lr0.0005_normTrue_force_0.01"
  - Modelforge Configuration file: [exp.config_file](./config_ps126_ds45_lr0.0005_normTrue_force_0.01.toml)
  - per_atom_energy normalization: 
  - initial learning rate: 
  
  - loss component: `per_system_energy` : weight = 1
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_atom_force` : weight = 0.01
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - WandB link: [[ ]]

- "qm9_schnet_E_ps123_ds42_lr0.0005_normTrue_force_0.001"
  - Modelforge Configuration file: [exp.config_file](./config_ps123_ds42_lr0.0005_normTrue_force_0.001.toml)
  - per_atom_energy normalization: 
  - initial learning rate: 
  
  - loss component: `per_system_energy` : weight = 1
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_atom_force` : weight = 0.001
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - WandB link: [[ ]]

- "qm9_schnet_E_ps124_ds43_lr0.0005_normTrue_force_0.001"
  - Modelforge Configuration file: [exp.config_file](./config_ps124_ds43_lr0.0005_normTrue_force_0.001.toml)
  - per_atom_energy normalization: 
  - initial learning rate: 
  
  - loss component: `per_system_energy` : weight = 1
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_atom_force` : weight = 0.001
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - WandB link: [[ ]]

- "qm9_schnet_E_ps125_ds44_lr0.0005_normTrue_force_0.001"
  - Modelforge Configuration file: [exp.config_file](./config_ps125_ds44_lr0.0005_normTrue_force_0.001.toml)
  - per_atom_energy normalization: 
  - initial learning rate: 
  
  - loss component: `per_system_energy` : weight = 1
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_atom_force` : weight = 0.001
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - WandB link: [[ ]]

- "qm9_schnet_E_ps126_ds45_lr0.0005_normTrue_force_0.001"
  - Modelforge Configuration file: [exp.config_file](./config_ps126_ds45_lr0.0005_normTrue_force_0.001.toml)
  - per_atom_energy normalization: 
  - initial learning rate: 
  
  - loss component: `per_system_energy` : weight = 1
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_atom_force` : weight = 0.001
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - WandB link: [[ ]]



