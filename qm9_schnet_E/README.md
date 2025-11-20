qm9_schnet_E
===========================

 * Dataset : qm9
 * Potential : schnet

Description:
------------

Training of the SchNet potential on the QM9 dataset. Local interactions are computed with a cutoff of 5 Å. Only per-system energy appears in the loss function. 

Experiments:
------------


- "qm9_schnet_E_ps123_ds42"
  - Modelforge Configuration file: [exp.config_file](./config_ps123_ds42.toml)
  
  - loss component: `per_atom_energy` : weight = 1
    - MSE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - WandB link: [[ ]]

- "qm9_schnet_E_ps124_ds43"
  - Modelforge Configuration file: [exp.config_file](./config_ps124_ds43.toml)
  
  - loss component: `per_atom_energy` : weight = 1
    - MSE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - WandB link: [[ ]]

- "qm9_schnet_E_ps125_ds44"
  - Modelforge Configuration file: [exp.config_file](./config_ps125_ds44.toml)
  
  - loss component: `per_atom_energy` : weight = 1
    - MSE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - WandB link: [[ ]]



