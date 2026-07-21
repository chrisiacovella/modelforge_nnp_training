qm9_schnet_E
===========================

 * Dataset : qm9
 * Potential : schnet

Description:
------------

Training of the SchNet potential on the QM9 dataset. Local interactions are computed with a cutoff of 5 Å. Only per-system energy appears in the loss function. 

Experiments:
------------


- "qm9_schnet_E_ps123_ds42_lr0.005_normTrue_rbf64"
  - Modelforge Configuration file: [exp.config_file](./config_ps123_ds42_lr0.005_normTrue_rbf64.toml)
  - per_atom_energy normalization: 
  - initial learning rate: 
  
  - loss component: `per_atom_energy` : weight = 1
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_atom_force` : weight = 0.01
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - WandB link: [[ ]]

- "qm9_schnet_E_ps124_ds43_lr0.005_normTrue_rbf64"
  - Modelforge Configuration file: [exp.config_file](./config_ps124_ds43_lr0.005_normTrue_rbf64.toml)
  - per_atom_energy normalization: 
  - initial learning rate: 
  
  - loss component: `per_atom_energy` : weight = 1
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_atom_force` : weight = 0.01
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - WandB link: [[ ]]

- "qm9_schnet_E_ps125_ds44_lr0.005_normTrue_rbf64"
  - Modelforge Configuration file: [exp.config_file](./config_ps125_ds44_lr0.005_normTrue_rbf64.toml)
  - per_atom_energy normalization: 
  - initial learning rate: 
  
  - loss component: `per_atom_energy` : weight = 1
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_atom_force` : weight = 0.01
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - WandB link: [[ ]]

- "qm9_schnet_E_ps123_ds42_lr0.002_normTrue_rbf64"
  - Modelforge Configuration file: [exp.config_file](./config_ps123_ds42_lr0.002_normTrue_rbf64.toml)
  - per_atom_energy normalization: 
  - initial learning rate: 
  
  - loss component: `per_atom_energy` : weight = 1
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_atom_force` : weight = 0.01
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - WandB link: [[ ]]

- "qm9_schnet_E_ps124_ds43_lr0.002_normTrue_rbf64"
  - Modelforge Configuration file: [exp.config_file](./config_ps124_ds43_lr0.002_normTrue_rbf64.toml)
  - per_atom_energy normalization: 
  - initial learning rate: 
  
  - loss component: `per_atom_energy` : weight = 1
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_atom_force` : weight = 0.01
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - WandB link: [[ ]]

- "qm9_schnet_E_ps125_ds44_lr0.002_normTrue_rbf64"
  - Modelforge Configuration file: [exp.config_file](./config_ps125_ds44_lr0.002_normTrue_rbf64.toml)
  - per_atom_energy normalization: 
  - initial learning rate: 
  
  - loss component: `per_atom_energy` : weight = 1
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_atom_force` : weight = 0.01
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - WandB link: [[ ]]

- "qm9_schnet_E_ps123_ds42_lr0.001_normTrue_rbf64"
  - Modelforge Configuration file: [exp.config_file](./config_ps123_ds42_lr0.001_normTrue_rbf64.toml)
  - per_atom_energy normalization: 
  - initial learning rate: 
  
  - loss component: `per_atom_energy` : weight = 1
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_atom_force` : weight = 0.01
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - WandB link: [[ ]]

- "qm9_schnet_E_ps124_ds43_lr0.001_normTrue_rbf64"
  - Modelforge Configuration file: [exp.config_file](./config_ps124_ds43_lr0.001_normTrue_rbf64.toml)
  - per_atom_energy normalization: 
  - initial learning rate: 
  
  - loss component: `per_atom_energy` : weight = 1
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_atom_force` : weight = 0.01
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - WandB link: [[ ]]

- "qm9_schnet_E_ps125_ds44_lr0.001_normTrue_rbf64"
  - Modelforge Configuration file: [exp.config_file](./config_ps125_ds44_lr0.001_normTrue_rbf64.toml)
  - per_atom_energy normalization: 
  - initial learning rate: 
  
  - loss component: `per_atom_energy` : weight = 1
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_atom_force` : weight = 0.01
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - WandB link: [[ ]]

- "qm9_schnet_E_ps123_ds42_lr0.0005_normTrue_rbf64"
  - Modelforge Configuration file: [exp.config_file](./config_ps123_ds42_lr0.0005_normTrue_rbf64.toml)
  - per_atom_energy normalization: 
  - initial learning rate: 
  
  - loss component: `per_atom_energy` : weight = 1
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_atom_force` : weight = 0.01
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - WandB link: [[ ]]

- "qm9_schnet_E_ps124_ds43_lr0.0005_normTrue_rbf64"
  - Modelforge Configuration file: [exp.config_file](./config_ps124_ds43_lr0.0005_normTrue_rbf64.toml)
  - per_atom_energy normalization: 
  - initial learning rate: 
  
  - loss component: `per_atom_energy` : weight = 1
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_atom_force` : weight = 0.01
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - WandB link: [[ ]]

- "qm9_schnet_E_ps125_ds44_lr0.0005_normTrue_rbf64"
  - Modelforge Configuration file: [exp.config_file](./config_ps125_ds44_lr0.0005_normTrue_rbf64.toml)
  - per_atom_energy normalization: 
  - initial learning rate: 
  
  - loss component: `per_atom_energy` : weight = 1
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_atom_force` : weight = 0.01
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - WandB link: [[ ]]

- "qm9_schnet_E_ps123_ds42_lr0.0001_normTrue_rbf64"
  - Modelforge Configuration file: [exp.config_file](./config_ps123_ds42_lr0.0001_normTrue_rbf64.toml)
  - per_atom_energy normalization: 
  - initial learning rate: 
  
  - loss component: `per_atom_energy` : weight = 1
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_atom_force` : weight = 0.01
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - WandB link: [[ ]]

- "qm9_schnet_E_ps124_ds43_lr0.0001_normTrue_rbf64"
  - Modelforge Configuration file: [exp.config_file](./config_ps124_ds43_lr0.0001_normTrue_rbf64.toml)
  - per_atom_energy normalization: 
  - initial learning rate: 
  
  - loss component: `per_atom_energy` : weight = 1
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_atom_force` : weight = 0.01
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - WandB link: [[ ]]

- "qm9_schnet_E_ps125_ds44_lr0.0001_normTrue_rbf64"
  - Modelforge Configuration file: [exp.config_file](./config_ps125_ds44_lr0.0001_normTrue_rbf64.toml)
  - per_atom_energy normalization: 
  - initial learning rate: 
  
  - loss component: `per_atom_energy` : weight = 1
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_atom_force` : weight = 0.01
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - WandB link: [[ ]]

- "qm9_schnet_E_ps123_ds42_lr0.005_normTrue_rbf128"
  - Modelforge Configuration file: [exp.config_file](./config_ps123_ds42_lr0.005_normTrue_rbf128.toml)
  - per_atom_energy normalization: 
  - initial learning rate: 
  
  - loss component: `per_atom_energy` : weight = 1
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_atom_force` : weight = 0.01
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - WandB link: [[ ]]

- "qm9_schnet_E_ps124_ds43_lr0.005_normTrue_rbf128"
  - Modelforge Configuration file: [exp.config_file](./config_ps124_ds43_lr0.005_normTrue_rbf128.toml)
  - per_atom_energy normalization: 
  - initial learning rate: 
  
  - loss component: `per_atom_energy` : weight = 1
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_atom_force` : weight = 0.01
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - WandB link: [[ ]]

- "qm9_schnet_E_ps125_ds44_lr0.005_normTrue_rbf128"
  - Modelforge Configuration file: [exp.config_file](./config_ps125_ds44_lr0.005_normTrue_rbf128.toml)
  - per_atom_energy normalization: 
  - initial learning rate: 
  
  - loss component: `per_atom_energy` : weight = 1
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_atom_force` : weight = 0.01
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - WandB link: [[ ]]

- "qm9_schnet_E_ps123_ds42_lr0.002_normTrue_rbf128"
  - Modelforge Configuration file: [exp.config_file](./config_ps123_ds42_lr0.002_normTrue_rbf128.toml)
  - per_atom_energy normalization: 
  - initial learning rate: 
  
  - loss component: `per_atom_energy` : weight = 1
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_atom_force` : weight = 0.01
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - WandB link: [[ ]]

- "qm9_schnet_E_ps124_ds43_lr0.002_normTrue_rbf128"
  - Modelforge Configuration file: [exp.config_file](./config_ps124_ds43_lr0.002_normTrue_rbf128.toml)
  - per_atom_energy normalization: 
  - initial learning rate: 
  
  - loss component: `per_atom_energy` : weight = 1
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_atom_force` : weight = 0.01
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - WandB link: [[ ]]

- "qm9_schnet_E_ps125_ds44_lr0.002_normTrue_rbf128"
  - Modelforge Configuration file: [exp.config_file](./config_ps125_ds44_lr0.002_normTrue_rbf128.toml)
  - per_atom_energy normalization: 
  - initial learning rate: 
  
  - loss component: `per_atom_energy` : weight = 1
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_atom_force` : weight = 0.01
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - WandB link: [[ ]]

- "qm9_schnet_E_ps123_ds42_lr0.001_normTrue_rbf128"
  - Modelforge Configuration file: [exp.config_file](./config_ps123_ds42_lr0.001_normTrue_rbf128.toml)
  - per_atom_energy normalization: 
  - initial learning rate: 
  
  - loss component: `per_atom_energy` : weight = 1
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_atom_force` : weight = 0.01
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - WandB link: [[ ]]

- "qm9_schnet_E_ps124_ds43_lr0.001_normTrue_rbf128"
  - Modelforge Configuration file: [exp.config_file](./config_ps124_ds43_lr0.001_normTrue_rbf128.toml)
  - per_atom_energy normalization: 
  - initial learning rate: 
  
  - loss component: `per_atom_energy` : weight = 1
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_atom_force` : weight = 0.01
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - WandB link: [[ ]]

- "qm9_schnet_E_ps125_ds44_lr0.001_normTrue_rbf128"
  - Modelforge Configuration file: [exp.config_file](./config_ps125_ds44_lr0.001_normTrue_rbf128.toml)
  - per_atom_energy normalization: 
  - initial learning rate: 
  
  - loss component: `per_atom_energy` : weight = 1
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_atom_force` : weight = 0.01
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - WandB link: [[ ]]

- "qm9_schnet_E_ps123_ds42_lr0.0005_normTrue_rbf128"
  - Modelforge Configuration file: [exp.config_file](./config_ps123_ds42_lr0.0005_normTrue_rbf128.toml)
  - per_atom_energy normalization: 
  - initial learning rate: 
  
  - loss component: `per_atom_energy` : weight = 1
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_atom_force` : weight = 0.01
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - WandB link: [[ ]]

- "qm9_schnet_E_ps124_ds43_lr0.0005_normTrue_rbf128"
  - Modelforge Configuration file: [exp.config_file](./config_ps124_ds43_lr0.0005_normTrue_rbf128.toml)
  - per_atom_energy normalization: 
  - initial learning rate: 
  
  - loss component: `per_atom_energy` : weight = 1
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_atom_force` : weight = 0.01
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - WandB link: [[ ]]

- "qm9_schnet_E_ps125_ds44_lr0.0005_normTrue_rbf128"
  - Modelforge Configuration file: [exp.config_file](./config_ps125_ds44_lr0.0005_normTrue_rbf128.toml)
  - per_atom_energy normalization: 
  - initial learning rate: 
  
  - loss component: `per_atom_energy` : weight = 1
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_atom_force` : weight = 0.01
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - WandB link: [[ ]]

- "qm9_schnet_E_ps123_ds42_lr0.0001_normTrue_rbf128"
  - Modelforge Configuration file: [exp.config_file](./config_ps123_ds42_lr0.0001_normTrue_rbf128.toml)
  - per_atom_energy normalization: 
  - initial learning rate: 
  
  - loss component: `per_atom_energy` : weight = 1
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_atom_force` : weight = 0.01
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - WandB link: [[ ]]

- "qm9_schnet_E_ps124_ds43_lr0.0001_normTrue_rbf128"
  - Modelforge Configuration file: [exp.config_file](./config_ps124_ds43_lr0.0001_normTrue_rbf128.toml)
  - per_atom_energy normalization: 
  - initial learning rate: 
  
  - loss component: `per_atom_energy` : weight = 1
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_atom_force` : weight = 0.01
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - WandB link: [[ ]]

- "qm9_schnet_E_ps125_ds44_lr0.0001_normTrue_rbf128"
  - Modelforge Configuration file: [exp.config_file](./config_ps125_ds44_lr0.0001_normTrue_rbf128.toml)
  - per_atom_energy normalization: 
  - initial learning rate: 
  
  - loss component: `per_atom_energy` : weight = 1
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_atom_force` : weight = 0.01
    - MAE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - WandB link: [[ ]]



