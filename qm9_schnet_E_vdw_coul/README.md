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
  
  - loss component: `per_system_energy` : weight = 0.001
    - MAE of test set: 2.197763204574585 kJ/mol
    - RMSE of test set: 4.373259544372559 kJ/mol
  
  - loss component: `per_atom_charge` : weight = 1.0
    - MAE of test set: 0.008152000606060028 e
    - RMSE of test set: 0.0122105423361063 e
  
  - WandB link: [https://wandb.ai/modelforge_nnps/modelforge_nnp_training/runs/bkmdmu9t](https://wandb.ai/modelforge_nnps/modelforge_nnp_training/runs/bkmdmu9t)

- "qm9_schnet_E_coul_vdw_ps124_ds43"
  - Modelforge Configuration file: [exp.config_file](./config_ps124_ds43.toml)
  
  - loss component: `per_system_energy` : weight = 0.001
    - MAE of test set: 2.5332868099212646 kJ/mol
    - RMSE of test set: 7.7914838790893555 kJ/mol
  
  - loss component: `per_atom_charge` : weight = 1.0
    - MAE of test set: 0.008977385237812996 e
    - RMSE of test set: 0.013508602976799011 e
  
  - WandB link: [https://wandb.ai/modelforge_nnps/modelforge_nnp_training/runs/t2n5csrt](https://wandb.ai/modelforge_nnps/modelforge_nnp_training/runs/t2n5csrt)

- "qm9_schnet_E_coul_vdw_ps125_ds44"
  - Modelforge Configuration file: [exp.config_file](./config_ps125_ds44.toml)
  
  - loss component: `per_system_energy` : weight = 0.001
    - MAE of test set: 3.210378408432007 kJ/mol
    - RMSE of test set: 4.696059703826904 kJ/mol
  
  - loss component: `per_atom_charge` : weight = 1.0
    - MAE of test set: 0.010209120810031891 e
    - RMSE of test set: 0.015202808193862438 e
  
  - WandB link: [https://wandb.ai/modelforge_nnps/modelforge_nnp_training/runs/86ribtt0](https://wandb.ai/modelforge_nnps/modelforge_nnp_training/runs/86ribtt0)



