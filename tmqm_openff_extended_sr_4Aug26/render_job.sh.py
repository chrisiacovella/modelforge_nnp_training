import os
from jinja2 import Environment, FileSystemLoader, Template


def render_file(
    environment: Environment, template_path: str, data: dict, add_quotes: bool = True
) -> str:
    template = environment.get_template(template_path)
    # we want strings to be rendered with quotes around them
    # so we will preprocess the data dictionary
    if add_quotes:
        for key, value in data.items():
            if isinstance(value, str):
                data[key] = f'"{value}"'
    # convert any bool to lowercase for the .toml file
    for key, value in data.items():
        if isinstance(value, bool):
            data[key] = str(value).lower()

    return template.render(data)


if __name__ == "__main__":
    # input
    env = Environment(loader=FileSystemLoader("jinja_templates"))
    dataset_template = "dataset.jinja"
    potential_template = "potential.jinja"
    runtime_template = "runtime.jinja"
    training_template = "training.jinja"
    slurm_template = "slurm_job.jinja"
    readme_template = "README.jinja"

    # these will be used when writing out the experiment name
    dataset_name = "tmqm_openff"
    potential_name = "aimnet2"
    experiment_base_name = f"{dataset_name}"

    description = "Training of aimnet2 with tmqm_openff looking at hyperparameters for spin resolved charge model"

    # in general we will want to run multiple versions of the same basic configuration to have multiple replicates
    # we will loop over potential parameters seeds and dataset splitting seeds

    file_names = []
    experiments = {}

    versions = [
        "all_dataset_seed42_v1.4d",
    ]

    for version_select in versions:
        for force_loss in [0.001]:
            for learning_rate in [1e-4]:
                for normalize in [True, False]:
                    for number_of_radial_basis_functions in  [64]:
                        for number_of_vector_features in [16,32]:
                            for number_of_per_atom_features in [128, 256]:
                                for potential_seed, dataset_set in [(1234, 425)]:

                                    # create a run_id based on the seeds, used for defining the local cache dir
                                    run_id = f"{version_select}_ps{potential_seed}_ds{dataset_set}_fl{force_loss}_lr{learning_rate}_norm{normalize}_nrbf{number_of_radial_basis_functions}_nvf{number_of_vector_features}_nfeat{number_of_per_atom_features}"

                                    ## define dataset parameters
                                    dataset_parameters = {
                                        "dataset_cache_dir": "/data1/choderaj/iacovec/training_test/dataset",
                                        "version_select": version_select,
                                    }

                                    ## define potential parameters
                                    potential_parameters = {"potential_seed": potential_seed,
                                                            "number_of_radial_basis_functions": number_of_radial_basis_functions,
                                                            "number_of_vector_features": number_of_vector_features,
                                                            "number_of_per_atom_features": number_of_per_atom_features,
                                                            "normalize": normalize,

                                    }


                                    ## define training parameters
                                    training_parameters = {
                                        "dataset_splitting_seed": dataset_set,
                                        "project": "tmqm_openff_sr_v1",
                                        "per_atom_force_loss_weight": force_loss,
                                        "group": f"{dataset_name}_{potential_name}_all",
                                        "learning_rate": learning_rate,
                                        "tags": [
                                            f"{dataset_name}",
                                            f"{potential_name}",
                                            f"{version_select}",
                                            f"f_loss: {force_loss}",
                                            f"normalize: {normalize}",
                                            f"lr: {learning_rate}",
                                            f"n_rbf: {number_of_radial_basis_functions}",
                                            f"n_vf: {number_of_vector_features}",
                                            f"n_feat: {number_of_per_atom_features}",
                                            "all",
                                        ],
                                        "notes": f"{run_id}; training of {potential_name} on {dataset_name} with version {version_select}",
                                    }

                                    ## define runtime parameters
                                    runtime_parameters = {
                                        "experiment_name": f"{experiment_base_name}_{run_id}",
                                        "local_cache_dir": f"./cache_{run_id}",
                                    }

                                    # render the various config files
                                    dataset_config = render_file(
                                        environment=env,
                                        template_path=dataset_template,
                                        data=dataset_parameters,
                                    )
                                    potential_config = render_file(
                                        environment=env,
                                        template_path=potential_template,
                                        data=potential_parameters,
                                    )
                                    training_config = render_file(
                                        environment=env,
                                        template_path=training_template,
                                        data=training_parameters,
                                    )
                                    runtime_config = render_file(
                                        environment=env,
                                        template_path=runtime_template,
                                        data=runtime_parameters,
                                    )

                                    ## merge all of the config files into one text block
                                    condensed_config = (
                                        f"# ============================================================ #\n\n"
                                        f"{dataset_config}"
                                        f"\n\n# ============================================================ #\n\n"
                                        f"{potential_config}"
                                        f"\n\n# ============================================================ #\n\n"
                                        f"{runtime_config}"
                                        f"\n\n# ============================================================ #\n\n"
                                        f"{training_config}"
                                        f"\n\n# ============================================================ #\n"
                                    )
                                    condensed_config_file = f"config_{run_id}.toml"

                                    with open(condensed_config_file, "w") as f:
                                        f.write(condensed_config)

                                    python_cmd = (
                                        f"python /data1/choderaj/iacovec/modelforge/scripts/perform_training.py "
                                        f"--condensed_config_path config_{run_id}.toml "
                                        f"--accelerator 'gpu' --device [0]"
                                    )
                                    #
                                    slurm_script = render_file(
                                        env,
                                        slurm_template,
                                        {
                                            "job_name": f"{run_id}_{dataset_name}_{potential_name}",
                                            "python_cmd": python_cmd,
                                        },
                                        add_quotes=False,
                                    )
                                    submit_slurm = f"submit_slurm_{run_id}.sh"
                                    file_names.append(submit_slurm)

                                    with open(submit_slurm, "w+") as f:
                                        f.write(slurm_script)

                                    # import the training_config as toml file into dictionary
                                    # so we can extract the loss parameters for the readme file
                                    import toml

                                    # print(training_config)

                                    training_config_dict = toml.loads(training_config)

                                    loss_components = training_config_dict["training"]["loss_parameter"][
                                        "loss_components"
                                    ]
                                    for l in loss_components:
                                        l.replace("'", "`")

                                    loss_weights = training_config_dict["training"]["loss_parameter"]["weight"]
                                    for l in loss_weights:
                                        l.replace("'", "`")

                                    experiments[runtime_parameters["experiment_name"]] = {
                                        "experiment_name": runtime_parameters["experiment_name"],
                                        "config_file": condensed_config_file,
                                        "loss_components": loss_components,
                                        "loss_weights": loss_weights,
                                    }

    # auto generate the README file using the
    readme_content = render_file(
        env,
        readme_template,
        {
            "experiment_base_name": experiment_base_name,
            "potential_name": potential_name,
            "dataset_name": dataset_name,
            "description": description,
            "experiments": experiments,
        },
        add_quotes=False,
    )
    with open("README.md", "w+") as f:
        f.write(readme_content)

    # create a single script to submit all the slurm jobs
    with open("submit_all_slurm_jobs.sh", "w") as f:
        f.write("#!/bin/bash\n\n")
        for file_name in file_names:
            f.write(f"sbatch {file_name}\n")
