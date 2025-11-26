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
  
  - loss component: `per_system_energy` : weight = 1
    - MAE of test set: 2.450139284133911 kJ/mol
    - RMSE of test set: 4.709739685058594 kJ/mol
  
  - WandB link: [https://wandb.ai/modelforge_nnps/modelforge_nnp_training/runs/1vbeog3a](https://wandb.ai/modelforge_nnps/modelforge_nnp_training/runs/1vbeog3a)

- "qm9_schnet_E_ps124_ds43"
  - Modelforge Configuration file: [exp.config_file](./config_ps124_ds43.toml)
  
  - loss component: `per_system_energy` : weight = 1
    - MAE of test set: 2.3385796546936035 kJ/mol
    - RMSE of test set: 7.070258140563965 kJ/mol
  
  - WandB link: [https://wandb.ai/modelforge_nnps/modelforge_nnp_training/runs/diqmibem](https://wandb.ai/modelforge_nnps/modelforge_nnp_training/runs/diqmibem)

- "qm9_schnet_E_ps125_ds44"
  - Modelforge Configuration file: [exp.config_file](./config_ps125_ds44.toml)
  
  - loss component: `per_system_energy` : weight = 1
    - MAE of test set: 2.971144199371338 kJ/mol
    - RMSE of test set: 4.29482889175415 kJ/mol
  
  - WandB link: [https://wandb.ai/modelforge_nnps/modelforge_nnp_training/runs/glo0zvvu](https://wandb.ai/modelforge_nnps/modelforge_nnp_training/runs/glo0zvvu)



