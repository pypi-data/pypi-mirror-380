import datetime
import textwrap
from datetime import datetime
from kubernetes.client import models as k8s
from airflow.exceptions import AirflowException
from airflow.utils.task_group import TaskGroup
from airflow.providers.google.cloud.operators.kubernetes_engine import GKEStartPodOperator
import fast_bi_dbt_runner.utils as utils


class CustomGKEStartPodOperator(GKEStartPodOperator):
    def execute(self, context):
        """
        Executes a GKEStartPodOperator task with customized exception handling.

        This custom operator extends the GKEStartPodOperator from the Airflow library.
        It overrides the execute method to catch AirflowException raised by the parent class.
        The error message is then shortened and a new AirflowException is raised with the
        shortened message. This approach allows for more concise error reporting while
        preserving the detailed error information.

        :param context: The context dictionary provided by Airflow.
        """
        try:
            super().execute(context)
        except AirflowException as e:
            # Shorten the error message for clearer reporting
            msg = str(e)
            short_msg = textwrap.shorten(msg, width=160)
            raise AirflowException(short_msg) from None

class DbtManifestParser:
    """
    A class analyses dbt project and parses manifest.json and creates the respective task groups
    :param manifest_path: Path to the directory containing the manifest files
    :param pod_name: name of Kubercluster pod
    :param dbt_tag: define different parts of a project. Have to be set as
    a list of one or a few values
    :param env_var: airflow variables
    :param image: docker image where define dbt command
    :param namespace: default
    :param PROJECT_ID: identificator of google project project_id.
    Getting from Airflow environment variables {{ var.value.PROJECT_ID }}
    :param CLUSTER_ZONE: Getting from Airflow environment variables {{ var.value.CLUSTER_ZONE }}
    :param CLUSTER_NAME: Getting from Airflow environment variables {{ var.value.CLUSTER_NAME_DBT }}
    """
    def __init__(
            self,
            dbt_tag,
            env_vars,
            airflow_vars,
            manifest_path=None,
            pod_name=None,
            image=None,
            namespace=None,
            project_id=None,
            cluster_zone=None,
            cluster_name=None,
            **kwargs
    ) -> None:
        self.env_vars = env_vars
        self.airflow_vars = airflow_vars
        self.pod_name = pod_name
        self.dbt_tag = utils.check_dbt_tag(dbt_tag)
        self.image = image
        self.namespace = namespace
        self.project_id = project_id
        self.cluster_zone = cluster_zone
        self.cluster_name = cluster_name
        self.manifest_path = manifest_path
        self.dbt_tag_ancestors = kwargs.get("dbt_tag_ancestors", False)
        self.dbt_tag_descendants = kwargs.get("dbt_tag_descendants", False)
        self.manifest_data = utils.load_dbt_manifest(self.manifest_path,
                                                     dbt_tag=self.dbt_tag,
                                                     dbt_tag_ancestors=self.dbt_tag_ancestors,
                                                     dbt_tag_descendants=self.dbt_tag_descendants)
        self.dbt_tasks = {}
        self.fqn_unique_list = []
        self.existing_task_groups = {}

    def is_resource_type_in_manifest(self, resource_type):
        return utils.is_resource_type_in_manifest(self.manifest_data, resource_type)
    
    def get_valid_start_date(self, start_date_raw):
        return utils.get_valid_start_date(start_date_raw)

    def add_additional_env_variables(self, task_params, dbt_command, node_name):
        # create env_vars_with_model list as a copy of env_vars
        # to avoid redefinition of env_vars list
        env_vars_with_model = self.env_vars.copy()
        airflow_var = self.airflow_vars.copy()

        if task_params.get('full_refresh', None):
            if dbt_command != "test":
                dbt_command = task_params['full_refresh']

        env_vars_with_model.append(k8s.V1EnvVar(name="DBT_COMMAND", value=f"{dbt_command}"))
        # add to env_vars_with_model new variable MODEL that equal
        # to current DBT project model node_name
        if node_name:
            env_vars_with_model.append(k8s.V1EnvVar(name="MODEL", value=f"{node_name}"))
        if dbt_command == "seed":
            env_vars_with_model.append(k8s.V1EnvVar(name="SEED", value="true"))
        else:
            env_vars_with_model.append(k8s.V1EnvVar(name="SEED", value="false"))

        if task_params:
            env_vars_with_model_keys = [i.name for i in env_vars_with_model]
            kuber_dag_new_params = [k8s.V1EnvVar(name=k, value=str(v)) for k, v in task_params.items() if
                                    k not in env_vars_with_model_keys]
            env_vars_with_model.extend(kuber_dag_new_params)
            airflow_var = {**task_params, **airflow_var}

        if dbt_command == "snapshot":
            env_vars_with_model.append(k8s.V1EnvVar(name="SNAPSHOT", value="true"))
            if not airflow_var.get('DBT_SNAPSHOT_INTERVAL') or airflow_var['DBT_SNAPSHOT_INTERVAL'] == 'daily':
                env_vars_with_model.append(k8s.V1EnvVar(name="SNAPSHOT_RUN_PERIOD", value="true"))
            else:
                env_vars_with_model.append(k8s.V1EnvVar(name="SNAPSHOT_RUN_PERIOD", value="false"))

            if airflow_var.get('DBT_DAG_RUN_DATE'):
                date_input = datetime.datetime.strptime(airflow_var['DBT_DAG_RUN_DATE'], "%Y-%m-%d")
                if airflow_var.get('DBT_SNAPSHOT_VALID_FROM'):
                    date_input_from = datetime.datetime.strptime(airflow_var['DBT_SNAPSHOT_VALID_FROM'], "%Y-%m-%d")
                    if airflow_var.get('DBT_SNAPSHOT_VALID_TO'):
                        date_input_to = datetime.datetime.strptime(airflow_var['DBT_SNAPSHOT_VALID_TO'], "%Y-%m-%d")

                        if airflow_var['DBT_SNAPSHOT_INTERVAL'] == 'monthly' \
                                and date_input_from.day <= date_input.day <= date_input_to.day:
                            env_vars_with_model.append(k8s.V1EnvVar(name="SNAPSHOT_RUN_PERIOD", value="true"))
                        elif airflow_var['DBT_SNAPSHOT_INTERVAL'] == 'weekly' \
                                and date_input_from.weekday() <= date_input.weekday() <= date_input_to.weekday():
                            env_vars_with_model.append(k8s.V1EnvVar(name="SNAPSHOT_RUN_PERIOD", value="true"))
        else:
            env_vars_with_model.append(k8s.V1EnvVar(name="SNAPSHOT", value="false"))
        return env_vars_with_model

    def create_dbt_task(self, dbt_command, running_rule, task_params={}, node_name=None, node_alias=None, parent_group=None):
        """
        Takes the manifest JSON content and returns a GKEStartPodOperator task
        to run a dbt command.
        Args:
            node_name: The name of the node from manifest.json. By default is equal to None
            running_rule: trigger rules
            dbt_command: dbt command: run, test
            task_params:
        Returns: A GKEStartPodOperator task that runs the respective dbt command
        """
        env_vars_with_model = self.add_additional_env_variables(task_params, dbt_command, node_name)

        if node_name is None:
            node_name = dbt_command + "_all_models"
            node_alias = dbt_command + "_all_models"
            if dbt_command == "source freshness":
                node_name ="freshness_all_sources"
                node_alias = "freshness_all_sources"

        """
        Create GKEStartPodOperator operators
            Args:
              task_id: The ID specified for the task.
              name: Name of task you want to run, used to generate Pod ID
              namespace: The namespace to run within Kubernetes
              image: Docker image specified
              trigger_rule: the conditions that Airflow applies to tasks
              to determine whether they are ready to execute.
              ALL_DONE - all upstream tasks are done with their execution
        """
        affinity = {
            'podAntiAffinity': {
                'preferredDuringSchedulingIgnoredDuringExecution': [
                    {
                        'weight': 100,
                        'podAffinityTerm': {
                            'labelSelector': {
                                'matchExpressions': [
                                    {
                                        'key': 'component',
                                        'operator': 'In',
                                        'values': ['scheduler', 'triggerer', 'worker']
                                    }
                                ]
                            },
                            'topologyKey': 'kubernetes.io/hostname'
                        }
                    }
                ]
            }
        }

        dbt_task = CustomGKEStartPodOperator(
            task_id=node_alias,
            name=self.pod_name + "_" + node_alias,
            project_id=self.project_id,
            location=self.cluster_zone,
            cluster_name=self.cluster_name,
            namespace=self.namespace,
            image=self.image,
            use_internal_ip=True,
            # Debug - uncomment for debug the container.
            # cmds=["bash", "-cx"],
            # arguments=[f" tail -f /dev/null "],
            # trigger_rule=TriggerRule.ALL_DONE,
            # Optional, run with specific K8S SA Account
            # service_account_name="airflow",
            trigger_rule=running_rule,
            secrets=[],
            labels={"app": "dbt"},
            startup_timeout_seconds=240,
            env_vars=env_vars_with_model,
            get_logs=True,
            image_pull_policy="IfNotPresent",
            image_pull_secrets="fast-bi-common-secret",
            annotations={},
            do_xcom_push=False,
            is_delete_operator_pod=True,
            container_resources=k8s.V1ResourceRequirements(
                requests={"memory": "128Mi", "cpu": "100m"},
            ),
            affinity=affinity,
            task_group=parent_group
        )
        return dbt_task

    def create_task_groups(self, parent_group, fqn, node, task_name, task_alias, dbt_command, running_rule,
                           task_params):
        """
        Recursively creates task groups from FQN and adds the task to the final group.
        """
        if not fqn:
            # Base case: If FQN is empty, add a task
            if node not in self.dbt_tasks:
                self.dbt_tasks[node] = self.create_dbt_task(dbt_command=dbt_command,
                                                                          running_rule=running_rule,
                                                                          task_params=task_params,
                                                                          node_name=task_name,
                                                                          node_alias=task_alias,
                                                                          parent_group=parent_group)
            return

        # Get the current level and create a subgroup
        current_level = fqn[0]
        if current_level != "re_data":
            subgroup = getattr(parent_group, current_level, None)

            # If the subgroup does not exist, create it
            if not subgroup:
                subgroup = TaskGroup(group_id=current_level, parent_group=parent_group)
                setattr(parent_group, current_level, subgroup)

            # Recurse into the next level
            self.create_task_groups(subgroup, fqn[1:], node, task_name, task_alias, dbt_command, running_rule,
                                    task_params)

    def set_dependencies(self, resource_type):
        """
         Sets the dependencies between tasks based on the `depends_on` attribute in the manifest data.
        """
        for node in self.manifest_data.keys():
            if resource_type in self.manifest_data[node]['group_type']:
                for upstream_node in self.manifest_data[node].get("depends_on", []):
                    if self.dbt_tasks.get(upstream_node, []):
                        self.dbt_tasks[upstream_node] >> self.dbt_tasks[node]

    def create_dbt_task_groups(
            self,
            group_name,
            resource_type,
            dbt_command,
            running_rule,
            task_params={}):
        """
        Parse out a JSON file and populates the task groups with dbt tasks
        Args:
            group_name: name of Task Groups uses for DAGs graph view in the Airflow UI.
            resource_type: type of manifest nodes group: model, seed, snapshot
            package_name: project name, tag that define by which certain records
            from the manifest nodes will be selected
            dbt_command: dbt command run or test
            running_rule: trigger rule
            task_params: parameters that was added in the task
        Returns: task group
        """
        task_params = {k: v for k, v in task_params.items() if v}  # Filter out empty values
        if "full_refresh_model_name" in task_params:
            self.manifest_data = utils.filter_models(self.manifest_data, task_params["full_refresh_model_name"])

        if utils.is_resource_type_in_manifest(self.manifest_data, resource_type):
            # Initialize the root TaskGroup from `group_name` (should be a TaskGroup instance, not a string)
            with TaskGroup(group_id=group_name, parent_group=None) as root_group:
                for node_id, node_data in self.manifest_data.items():
                    if group_name[:-1] in node_data["group_type"]:
                        # Extract FQN and task name
                        fqn = node_data["fqn"][:-1]  # Remove model name from the FQN
                        task_name = node_data["name"]
                        task_alias = node_data["alias"]
                        if node_data['resource_type'] == "test":
                            dbt_command = "test"
                        if node_data['resource_type'] == "source":
                            task_name = f"source:{node_data['schema']}.{task_name}"
                            dbt_command = "source freshness"
                        # Create the dynamic task groups under root_group
                        self.create_task_groups(root_group, fqn, node_id, task_name, task_alias, dbt_command, running_rule,
                                                task_params)
            self.set_dependencies(resource_type)
            return root_group
