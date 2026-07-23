qm9_schnet_E
===========================

 * Dataset : qm9
 * Potential : schnet

Description:
------------

Training of the SchNet potential on the QM9 dataset. Local interactions are computed with a cutoff of 5 Å. Only per-system energy appears in the loss function. 

Experiments:
------------


- "qm9_schnet_E_ps123_ds42_lr0.0001_normTrue_force_0.001_threshold0.01"
  - Modelforge Configuration file: [exp.config_file](./config_ps123_ds42_lr0.0001_normTrue_force_0.001_threshold0.01.toml)
  - per_atom_energy normalization: 
  - initial learning rate: 
  
  - loss component: `per_system_energy` : weight = 1
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_atom_force` : weight = 0.001
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - WandB link: [[ ]]

- "qm9_schnet_E_ps124_ds43_lr0.0001_normTrue_force_0.001_threshold0.01"
  - Modelforge Configuration file: [exp.config_file](./config_ps124_ds43_lr0.0001_normTrue_force_0.001_threshold0.01.toml)
  - per_atom_energy normalization: 
  - initial learning rate: 
  
  - loss component: `per_system_energy` : weight = 1
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_atom_force` : weight = 0.001
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - WandB link: [[ ]]

- "qm9_schnet_E_ps125_ds44_lr0.0001_normTrue_force_0.001_threshold0.01"
  - Modelforge Configuration file: [exp.config_file](./config_ps125_ds44_lr0.0001_normTrue_force_0.001_threshold0.01.toml)
  - per_atom_energy normalization: 
  - initial learning rate: 
  
  - loss component: `per_system_energy` : weight = 1
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_atom_force` : weight = 0.001
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - WandB link: [[ ]]

- "qm9_schnet_E_ps123_ds42_lr0.0005_normTrue_force_0.001_threshold0.01"
  - Modelforge Configuration file: [exp.config_file](./config_ps123_ds42_lr0.0005_normTrue_force_0.001_threshold0.01.toml)
  - per_atom_energy normalization: 
  - initial learning rate: 
  
  - loss component: `per_system_energy` : weight = 1
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_atom_force` : weight = 0.001
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - WandB link: [[ ]]

- "qm9_schnet_E_ps124_ds43_lr0.0005_normTrue_force_0.001_threshold0.01"
  - Modelforge Configuration file: [exp.config_file](./config_ps124_ds43_lr0.0005_normTrue_force_0.001_threshold0.01.toml)
  - per_atom_energy normalization: 
  - initial learning rate: 
  
  - loss component: `per_system_energy` : weight = 1
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_atom_force` : weight = 0.001
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - WandB link: [[ ]]

- "qm9_schnet_E_ps125_ds44_lr0.0005_normTrue_force_0.001_threshold0.01"
  - Modelforge Configuration file: [exp.config_file](./config_ps125_ds44_lr0.0005_normTrue_force_0.001_threshold0.01.toml)
  - per_atom_energy normalization: 
  - initial learning rate: 
  
  - loss component: `per_system_energy` : weight = 1
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_atom_force` : weight = 0.001
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - WandB link: [[ ]]

- "qm9_schnet_E_ps123_ds42_lr0.0001_normTrue_force_0.0001_threshold0.01"
  - Modelforge Configuration file: [exp.config_file](./config_ps123_ds42_lr0.0001_normTrue_force_0.0001_threshold0.01.toml)
  - per_atom_energy normalization: 
  - initial learning rate: 
  
  - loss component: `per_system_energy` : weight = 1
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_atom_force` : weight = 0.0001
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - WandB link: [[ ]]

- "qm9_schnet_E_ps124_ds43_lr0.0001_normTrue_force_0.0001_threshold0.01"
  - Modelforge Configuration file: [exp.config_file](./config_ps124_ds43_lr0.0001_normTrue_force_0.0001_threshold0.01.toml)
  - per_atom_energy normalization: 
  - initial learning rate: 
  
  - loss component: `per_system_energy` : weight = 1
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_atom_force` : weight = 0.0001
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - WandB link: [[ ]]

- "qm9_schnet_E_ps125_ds44_lr0.0001_normTrue_force_0.0001_threshold0.01"
  - Modelforge Configuration file: [exp.config_file](./config_ps125_ds44_lr0.0001_normTrue_force_0.0001_threshold0.01.toml)
  - per_atom_energy normalization: 
  - initial learning rate: 
  
  - loss component: `per_system_energy` : weight = 1
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_atom_force` : weight = 0.0001
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - WandB link: [[ ]]

- "qm9_schnet_E_ps123_ds42_lr0.0005_normTrue_force_0.0001_threshold0.01"
  - Modelforge Configuration file: [exp.config_file](./config_ps123_ds42_lr0.0005_normTrue_force_0.0001_threshold0.01.toml)
  - per_atom_energy normalization: 
  - initial learning rate: 
  
  - loss component: `per_system_energy` : weight = 1
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_atom_force` : weight = 0.0001
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - WandB link: [[ ]]

- "qm9_schnet_E_ps124_ds43_lr0.0005_normTrue_force_0.0001_threshold0.01"
  - Modelforge Configuration file: [exp.config_file](./config_ps124_ds43_lr0.0005_normTrue_force_0.0001_threshold0.01.toml)
  - per_atom_energy normalization: 
  - initial learning rate: 
  
  - loss component: `per_system_energy` : weight = 1
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_atom_force` : weight = 0.0001
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - WandB link: [[ ]]

- "qm9_schnet_E_ps125_ds44_lr0.0005_normTrue_force_0.0001_threshold0.01"
  - Modelforge Configuration file: [exp.config_file](./config_ps125_ds44_lr0.0005_normTrue_force_0.0001_threshold0.01.toml)
  - per_atom_energy normalization: 
  - initial learning rate: 
  
  - loss component: `per_system_energy` : weight = 1
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_atom_force` : weight = 0.0001
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - WandB link: [[ ]]

- "qm9_schnet_E_ps123_ds42_lr0.0001_normTrue_force_1e-05_threshold0.01"
  - Modelforge Configuration file: [exp.config_file](./config_ps123_ds42_lr0.0001_normTrue_force_1e-05_threshold0.01.toml)
  - per_atom_energy normalization: 
  - initial learning rate: 
  
  - loss component: `per_system_energy` : weight = 1
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_atom_force` : weight = 1e-05
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - WandB link: [[ ]]

- "qm9_schnet_E_ps124_ds43_lr0.0001_normTrue_force_1e-05_threshold0.01"
  - Modelforge Configuration file: [exp.config_file](./config_ps124_ds43_lr0.0001_normTrue_force_1e-05_threshold0.01.toml)
  - per_atom_energy normalization: 
  - initial learning rate: 
  
  - loss component: `per_system_energy` : weight = 1
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_atom_force` : weight = 1e-05
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - WandB link: [[ ]]

- "qm9_schnet_E_ps125_ds44_lr0.0001_normTrue_force_1e-05_threshold0.01"
  - Modelforge Configuration file: [exp.config_file](./config_ps125_ds44_lr0.0001_normTrue_force_1e-05_threshold0.01.toml)
  - per_atom_energy normalization: 
  - initial learning rate: 
  
  - loss component: `per_system_energy` : weight = 1
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_atom_force` : weight = 1e-05
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - WandB link: [[ ]]

- "qm9_schnet_E_ps123_ds42_lr0.0005_normTrue_force_1e-05_threshold0.01"
  - Modelforge Configuration file: [exp.config_file](./config_ps123_ds42_lr0.0005_normTrue_force_1e-05_threshold0.01.toml)
  - per_atom_energy normalization: 
  - initial learning rate: 
  
  - loss component: `per_system_energy` : weight = 1
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_atom_force` : weight = 1e-05
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - WandB link: [[ ]]

- "qm9_schnet_E_ps124_ds43_lr0.0005_normTrue_force_1e-05_threshold0.01"
  - Modelforge Configuration file: [exp.config_file](./config_ps124_ds43_lr0.0005_normTrue_force_1e-05_threshold0.01.toml)
  - per_atom_energy normalization: 
  - initial learning rate: 
  
  - loss component: `per_system_energy` : weight = 1
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_atom_force` : weight = 1e-05
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - WandB link: [[ ]]

- "qm9_schnet_E_ps125_ds44_lr0.0005_normTrue_force_1e-05_threshold0.01"
  - Modelforge Configuration file: [exp.config_file](./config_ps125_ds44_lr0.0005_normTrue_force_1e-05_threshold0.01.toml)
  - per_atom_energy normalization: 
  - initial learning rate: 
  
  - loss component: `per_system_energy` : weight = 1
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_atom_force` : weight = 1e-05
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - WandB link: [[ ]]

- "qm9_schnet_E_ps123_ds42_lr0.0001_normTrue_force_0.001_threshold0.001"
  - Modelforge Configuration file: [exp.config_file](./config_ps123_ds42_lr0.0001_normTrue_force_0.001_threshold0.001.toml)
  - per_atom_energy normalization: 
  - initial learning rate: 
  
  - loss component: `per_system_energy` : weight = 1
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_atom_force` : weight = 0.001
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - WandB link: [[ ]]

- "qm9_schnet_E_ps124_ds43_lr0.0001_normTrue_force_0.001_threshold0.001"
  - Modelforge Configuration file: [exp.config_file](./config_ps124_ds43_lr0.0001_normTrue_force_0.001_threshold0.001.toml)
  - per_atom_energy normalization: 
  - initial learning rate: 
  
  - loss component: `per_system_energy` : weight = 1
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_atom_force` : weight = 0.001
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - WandB link: [[ ]]

- "qm9_schnet_E_ps125_ds44_lr0.0001_normTrue_force_0.001_threshold0.001"
  - Modelforge Configuration file: [exp.config_file](./config_ps125_ds44_lr0.0001_normTrue_force_0.001_threshold0.001.toml)
  - per_atom_energy normalization: 
  - initial learning rate: 
  
  - loss component: `per_system_energy` : weight = 1
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_atom_force` : weight = 0.001
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - WandB link: [[ ]]

- "qm9_schnet_E_ps123_ds42_lr0.0005_normTrue_force_0.001_threshold0.001"
  - Modelforge Configuration file: [exp.config_file](./config_ps123_ds42_lr0.0005_normTrue_force_0.001_threshold0.001.toml)
  - per_atom_energy normalization: 
  - initial learning rate: 
  
  - loss component: `per_system_energy` : weight = 1
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_atom_force` : weight = 0.001
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - WandB link: [[ ]]

- "qm9_schnet_E_ps124_ds43_lr0.0005_normTrue_force_0.001_threshold0.001"
  - Modelforge Configuration file: [exp.config_file](./config_ps124_ds43_lr0.0005_normTrue_force_0.001_threshold0.001.toml)
  - per_atom_energy normalization: 
  - initial learning rate: 
  
  - loss component: `per_system_energy` : weight = 1
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_atom_force` : weight = 0.001
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - WandB link: [[ ]]

- "qm9_schnet_E_ps125_ds44_lr0.0005_normTrue_force_0.001_threshold0.001"
  - Modelforge Configuration file: [exp.config_file](./config_ps125_ds44_lr0.0005_normTrue_force_0.001_threshold0.001.toml)
  - per_atom_energy normalization: 
  - initial learning rate: 
  
  - loss component: `per_system_energy` : weight = 1
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_atom_force` : weight = 0.001
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - WandB link: [[ ]]

- "qm9_schnet_E_ps123_ds42_lr0.0001_normTrue_force_0.0001_threshold0.001"
  - Modelforge Configuration file: [exp.config_file](./config_ps123_ds42_lr0.0001_normTrue_force_0.0001_threshold0.001.toml)
  - per_atom_energy normalization: 
  - initial learning rate: 
  
  - loss component: `per_system_energy` : weight = 1
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_atom_force` : weight = 0.0001
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - WandB link: [[ ]]

- "qm9_schnet_E_ps124_ds43_lr0.0001_normTrue_force_0.0001_threshold0.001"
  - Modelforge Configuration file: [exp.config_file](./config_ps124_ds43_lr0.0001_normTrue_force_0.0001_threshold0.001.toml)
  - per_atom_energy normalization: 
  - initial learning rate: 
  
  - loss component: `per_system_energy` : weight = 1
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_atom_force` : weight = 0.0001
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - WandB link: [[ ]]

- "qm9_schnet_E_ps125_ds44_lr0.0001_normTrue_force_0.0001_threshold0.001"
  - Modelforge Configuration file: [exp.config_file](./config_ps125_ds44_lr0.0001_normTrue_force_0.0001_threshold0.001.toml)
  - per_atom_energy normalization: 
  - initial learning rate: 
  
  - loss component: `per_system_energy` : weight = 1
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_atom_force` : weight = 0.0001
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - WandB link: [[ ]]

- "qm9_schnet_E_ps123_ds42_lr0.0005_normTrue_force_0.0001_threshold0.001"
  - Modelforge Configuration file: [exp.config_file](./config_ps123_ds42_lr0.0005_normTrue_force_0.0001_threshold0.001.toml)
  - per_atom_energy normalization: 
  - initial learning rate: 
  
  - loss component: `per_system_energy` : weight = 1
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_atom_force` : weight = 0.0001
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - WandB link: [[ ]]

- "qm9_schnet_E_ps124_ds43_lr0.0005_normTrue_force_0.0001_threshold0.001"
  - Modelforge Configuration file: [exp.config_file](./config_ps124_ds43_lr0.0005_normTrue_force_0.0001_threshold0.001.toml)
  - per_atom_energy normalization: 
  - initial learning rate: 
  
  - loss component: `per_system_energy` : weight = 1
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_atom_force` : weight = 0.0001
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - WandB link: [[ ]]

- "qm9_schnet_E_ps125_ds44_lr0.0005_normTrue_force_0.0001_threshold0.001"
  - Modelforge Configuration file: [exp.config_file](./config_ps125_ds44_lr0.0005_normTrue_force_0.0001_threshold0.001.toml)
  - per_atom_energy normalization: 
  - initial learning rate: 
  
  - loss component: `per_system_energy` : weight = 1
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_atom_force` : weight = 0.0001
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - WandB link: [[ ]]

- "qm9_schnet_E_ps123_ds42_lr0.0001_normTrue_force_1e-05_threshold0.001"
  - Modelforge Configuration file: [exp.config_file](./config_ps123_ds42_lr0.0001_normTrue_force_1e-05_threshold0.001.toml)
  - per_atom_energy normalization: 
  - initial learning rate: 
  
  - loss component: `per_system_energy` : weight = 1
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_atom_force` : weight = 1e-05
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - WandB link: [[ ]]

- "qm9_schnet_E_ps124_ds43_lr0.0001_normTrue_force_1e-05_threshold0.001"
  - Modelforge Configuration file: [exp.config_file](./config_ps124_ds43_lr0.0001_normTrue_force_1e-05_threshold0.001.toml)
  - per_atom_energy normalization: 
  - initial learning rate: 
  
  - loss component: `per_system_energy` : weight = 1
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_atom_force` : weight = 1e-05
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - WandB link: [[ ]]

- "qm9_schnet_E_ps125_ds44_lr0.0001_normTrue_force_1e-05_threshold0.001"
  - Modelforge Configuration file: [exp.config_file](./config_ps125_ds44_lr0.0001_normTrue_force_1e-05_threshold0.001.toml)
  - per_atom_energy normalization: 
  - initial learning rate: 
  
  - loss component: `per_system_energy` : weight = 1
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_atom_force` : weight = 1e-05
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - WandB link: [[ ]]

- "qm9_schnet_E_ps123_ds42_lr0.0005_normTrue_force_1e-05_threshold0.001"
  - Modelforge Configuration file: [exp.config_file](./config_ps123_ds42_lr0.0005_normTrue_force_1e-05_threshold0.001.toml)
  - per_atom_energy normalization: 
  - initial learning rate: 
  
  - loss component: `per_system_energy` : weight = 1
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_atom_force` : weight = 1e-05
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - WandB link: [[ ]]

- "qm9_schnet_E_ps124_ds43_lr0.0005_normTrue_force_1e-05_threshold0.001"
  - Modelforge Configuration file: [exp.config_file](./config_ps124_ds43_lr0.0005_normTrue_force_1e-05_threshold0.001.toml)
  - per_atom_energy normalization: 
  - initial learning rate: 
  
  - loss component: `per_system_energy` : weight = 1
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_atom_force` : weight = 1e-05
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - WandB link: [[ ]]

- "qm9_schnet_E_ps125_ds44_lr0.0005_normTrue_force_1e-05_threshold0.001"
  - Modelforge Configuration file: [exp.config_file](./config_ps125_ds44_lr0.0005_normTrue_force_1e-05_threshold0.001.toml)
  - per_atom_energy normalization: 
  - initial learning rate: 
  
  - loss component: `per_system_energy` : weight = 1
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_atom_force` : weight = 1e-05
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - WandB link: [[ ]]



