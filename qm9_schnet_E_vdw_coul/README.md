qm9_schnet_E_coul_vdw
===========================

 * Dataset : qm9
 * Potential : schnet

Description:
------------

Training of the SchNet potential on the QM9 dataset. This additionally predicts the partial charges on each atom. Local interactions are computed with a cutoff of 5 Å. van der Waals interactions are computed using the DFT-D3 method with a cutoff of 15 Å. The partial charges are used to compute the Coulombic interaction between particles with cutoff of 15 Å. The training includes loss terms for the total system energy, which includes van der Waals and Coulombic energy contributions (`per_system_energy`) and partial charges (`per_atom_charge`).

Experiments:
------------


- "qm9_schnet_E_coul_vdw_ps123_ds42"
  - Modelforge Configuration file: [exp.config_file](./config_ps123_ds42.toml)
  
  - loss component: `per_atom_energy` : weight = 0.001
    - MSE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_atom_charge` : weight = 1.0
    - MSE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - WandB link: [[ ]]

- "qm9_schnet_E_coul_vdw_ps124_ds43"
  - Modelforge Configuration file: [exp.config_file](./config_ps124_ds43.toml)
  
  - loss component: `per_atom_energy` : weight = 0.001
    - MSE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_atom_charge` : weight = 1.0
    - MSE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - WandB link: [[ ]]

- "qm9_schnet_E_coul_vdw_ps125_ds44"
  - Modelforge Configuration file: [exp.config_file](./config_ps125_ds44.toml)
  
  - loss component: `per_atom_energy` : weight = 0.001
    - MSE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - loss component: `per_atom_charge` : weight = 1.0
    - MSE of test set: [[ ]]
    - RMSE of test set: [[ ]]
  
  - WandB link: [[ ]]



