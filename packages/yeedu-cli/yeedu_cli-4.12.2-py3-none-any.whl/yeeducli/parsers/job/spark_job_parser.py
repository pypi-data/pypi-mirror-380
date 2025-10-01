from yeeducli.constants import SPARK_JOB_STATUS, SPARK_JOB_TYPE, JOB_TYPE_LANG
from yeeducli.utility.json_utils import check_boolean, check_non_empty_string, validate_array_of_intgers, check_choices
from argparse import SUPPRESS, ArgumentDefaultsHelpFormatter

class SparkJobInstanceParser:
    def spark_job_parser(subparser):
        start_spark_job_run = subparser.add_parser(
            'start',
            help='To run a Spark Job run.',
            formatter_class=ArgumentDefaultsHelpFormatter)
        start_spark_job_run.add_argument(
            "--job_id",
            type=int,
            nargs=1,
            default=SUPPRESS,
            help="To run a Spark Job run, enter job_id."
        )
        start_spark_job_run.add_argument(
            "--job_name",
            type=check_non_empty_string,
            nargs=1,
            default=SUPPRESS,
            help="To run a Spark Job run, enter job_name."
        )
        start_spark_job_run.add_argument(
            "--arguments",
            type=check_non_empty_string,
            nargs='?',
            default=SUPPRESS,
            help="Specifies the runtime arguments to run a Spark Job run."
        )
        start_spark_job_run.add_argument(
            "--conf",
            type=check_non_empty_string,
            nargs='+',
            action='append',
            default=SUPPRESS,
            help="Specifies the runtime configurations to run a Spark Job run."
        )
        start_spark_job_run.add_argument(
            "--workspace_id",
            type=int,
            nargs=1,
            default=SUPPRESS,
            required=True,
            help="To run a Spark Job run, enter workspace_id."
        )
        start_spark_job_run.add_argument(
            "--follow",
            action='store_true',
            help="Continuously fetch job status until job reaches terminal state (ERROR, STOPPED,TERMINATED or DONE)."
        )
        start_spark_job_run.add_argument(
            "--json-output",
            type=check_non_empty_string,
            nargs='?',
            choices=['pretty', 'default'],
            default='pretty',
            help="Specifies the format of JSON output."
        )
        start_spark_job_run.add_argument(
            "--yaml-output",
            type=check_boolean,
            nargs='?',
            choices=['true', 'false'],
            default='false',
            help="Displays the information in YAML format if set to 'true'."
        )

        list_spark_job_inst = subparser.add_parser(
            'list-runs',
            help='To list all the available Spark Job runs.',
            formatter_class=ArgumentDefaultsHelpFormatter)
        list_spark_job_inst.add_argument(
            "--workspace_id",
            type=int,
            nargs=1,
            default=SUPPRESS,
            required=True,
            help="To list Spark Job runs of a specific workspace_id."
        )
        list_spark_job_inst.add_argument(
            "--cluster_ids",
            type=validate_array_of_intgers,
            nargs='?',
            default=SUPPRESS,
            help="To list Spark Job runs for optional set of cluster Ids."
        )
        list_spark_job_inst.add_argument(
            "--job_ids",
            type=validate_array_of_intgers,
            nargs='?',
            default=SUPPRESS,
            help="To list Spark Job runs for optional set of Spark job Ids."
        )
        list_spark_job_inst.add_argument(
            "--run_status",
            type=lambda values: check_choices(
                values, choices=SPARK_JOB_STATUS),
            nargs='?',
            default=SUPPRESS,
            help="To list Spark Job runs for optional set of run_status. Choices are: " +
            ", ".join(SPARK_JOB_STATUS)
        )
        list_spark_job_inst.add_argument(
            "--job_type",
            type=lambda values: check_choices(
                values, choices=SPARK_JOB_TYPE),
            nargs='?',
            default=SUPPRESS,
            help="To list Spark Job runs for optional set of job_type. Choices are: " +
            ", ".join(SPARK_JOB_TYPE)
        )
        list_spark_job_inst.add_argument(
            "--job_type_langs",
            type=lambda values: check_choices(values, choices=JOB_TYPE_LANG),
            nargs='?',
            default=SUPPRESS,
            help="An optional set of language filter for Spark job runs. Choices are: " +
            ", ".join(JOB_TYPE_LANG)
        )
        list_spark_job_inst.add_argument(
            "--created_by_ids",
            type=validate_array_of_intgers,
            nargs='?',
            default=SUPPRESS,
            help="To list Spark Job runs for optional set of created by user Ids."
        )
        list_spark_job_inst.add_argument(
            "--modified_by_ids",
            type=validate_array_of_intgers,
            nargs='?',
            default=SUPPRESS,
            help="To list Spark Job runs for optional set of modified by user Ids."
        )
        list_spark_job_inst.add_argument(
            "--page_number",
            type=int,
            nargs=1,
            default=1,
            help="To list Spark Job runs for a specific page_number."
        )
        list_spark_job_inst.add_argument(
            "--limit",
            type=int,
            nargs=1,
            default=100,
            help="Provide limit to list number of job runs."
        )
        list_spark_job_inst.add_argument(
            "--json-output",
            type=check_non_empty_string,
            nargs='?',
            choices=['pretty', 'default'],
            default='pretty',
            help="Specifies the format of JSON output."
        )
        list_spark_job_inst.add_argument(
            "--yaml-output",
            type=check_boolean,
            nargs='?',
            choices=['true', 'false'],
            default='false',
            help="Displays the information in YAML format if set to 'true'."
        )

        search_job_inst = subparser.add_parser(
            'search-runs',
            help='To search Spark Job runs by similar job id.',
            formatter_class=ArgumentDefaultsHelpFormatter)
        search_job_inst.add_argument(
            "--workspace_id",
            type=int,
            nargs=1,
            default=SUPPRESS,
            required=True,
            help="Provide workspace id to search Spark Job runs in it."
        )
        search_job_inst.add_argument(
            "--job_name",
            type=check_non_empty_string,
            nargs=1,
            default=SUPPRESS,
            required=True,
            help="To search Spark Job runs of a specific job_name."
        )
        search_job_inst.add_argument(
            "--cluster_ids",
            type=validate_array_of_intgers,
            nargs='?',
            default=SUPPRESS,
            help="To search Spark Job runs for optional set of cluster Ids."
        )
        search_job_inst.add_argument(
            "--job_ids",
            type=validate_array_of_intgers,
            nargs='?',
            default=SUPPRESS,
            help="To Search Spark Job runs for optional set of Spark job Ids."
        )
        search_job_inst.add_argument(
            "--run_status",
            type=lambda values: check_choices(
                values, choices=SPARK_JOB_STATUS),
            nargs='?',
            default=SUPPRESS,
            help="To search Spark Job runs for optional set of run_status. Choices are: " +
            ", ".join(SPARK_JOB_STATUS)
        )
        search_job_inst.add_argument(
            "--job_type",
            type=lambda values: check_choices(
                values, choices=SPARK_JOB_TYPE),
            nargs='?',
            default=SUPPRESS,
            help="To search Spark Job runs for optional set of job_type. Choices are: " +
            ", ".join(SPARK_JOB_TYPE)
        )
        search_job_inst.add_argument(
            "--job_type_langs",
            type=lambda values: check_choices(values, choices=JOB_TYPE_LANG),
            nargs='?',
            default=SUPPRESS,
            help="An optional set of language filter for Spark job runs. Choices are: " +
            ", ".join(JOB_TYPE_LANG)
        )
        search_job_inst.add_argument(
            "--created_by_ids",
            type=validate_array_of_intgers,
            nargs='?',
            default=SUPPRESS,
            help="To search Spark Job runs for optional set of created by user Ids."
        )
        search_job_inst.add_argument(
            "--modified_by_ids",
            type=validate_array_of_intgers,
            nargs='?',
            default=SUPPRESS,
            help="To search Spark Job runs for optional set of modified by user Ids."
        )
        search_job_inst.add_argument(
            "--page_number",
            type=int,
            nargs=1,
            default=1,
            help="To search Spark Job runs for a specific page_number."
        )
        search_job_inst.add_argument(
            "--limit",
            type=int,
            nargs=1,
            default=100,
            help="Provide limit to search number of Spark Job runs."
        )
        search_job_inst.add_argument(
            "--json-output",
            type=check_non_empty_string,
            nargs='?',
            choices=['pretty', 'default'],
            default='pretty',
            help="Specifies the format of JSON output."
        )
        search_job_inst.add_argument(
            "--yaml-output",
            type=check_boolean,
            nargs='?',
            choices=['true', 'false'],
            default='false',
            help="Displays the information in YAML format if set to 'true'."
        )

        get_job_instance = subparser.add_parser(
            'get-run',
            help='To get information about a specific Spark Job run.',
            formatter_class=ArgumentDefaultsHelpFormatter)
        get_job_instance.add_argument(
            "--run_id",
            type=int,
            nargs=1,
            default=SUPPRESS,
            required=True,
            help="Provide run_id to get information about a specific Spark Job run."
        )
        get_job_instance.add_argument(
            "--workspace_id",
            type=int,
            nargs=1,
            default=SUPPRESS,
            required=True,
            help="Provide workspace_id to get information about a specific Spark Job run."
        )
        get_job_instance.add_argument(
            "--json-output",
            type=check_non_empty_string,
            nargs='?',
            choices=['pretty', 'default'],
            default='pretty',
            help="Specifies the format of JSON output."
        )
        get_job_instance.add_argument(
            "--yaml-output",
            type=check_boolean,
            nargs='?',
            choices=['true', 'false'],
            default='false',
            help="Displays the information in YAML format if set to 'true'."
        )

        stop_spark_job_inst = subparser.add_parser(
            'stop',
            help='To stop a specific Spark Job run.',
            formatter_class=ArgumentDefaultsHelpFormatter)
        stop_spark_job_inst.add_argument(
            "--run_id",
            type=int,
            nargs=1,
            default=SUPPRESS,
            required=True,
            help="Provide run_id to stop a specific Spark Job run."
        )
        stop_spark_job_inst.add_argument(
            "--workspace_id",
            type=int,
            nargs=1,
            default=SUPPRESS,
            required=True,
            help="Provide workspace_id to stop a specific Spark Job run."
        )
        stop_spark_job_inst.add_argument(
            "--json-output",
            type=check_non_empty_string,
            nargs='?',
            choices=['pretty', 'default'],
            default='pretty',
            help="Specifies the format of JSON output."
        )
        stop_spark_job_inst.add_argument(
            "--yaml-output",
            type=check_boolean,
            nargs='?',
            choices=['true', 'false'],
            default='false',
            help="Displays the information in YAML format if set to 'true'."
        )

        get_workflow_job_inst = subparser.add_parser(
            'get-workflow-job-instance',
            help='To get information about a specific Workflow Job run.',
            formatter_class=ArgumentDefaultsHelpFormatter)
        get_workflow_job_inst.add_argument(
            "--application_id",
            type=check_non_empty_string,
            nargs=1,
            default=SUPPRESS,
            required=True,
            help="Provide a application_id to get information about a specific Workflow Job run."
        )
        get_workflow_job_inst.add_argument(
            "--workspace_id",
            type=int,
            nargs=1,
            default=SUPPRESS,
            required=True,
            help="Provide a workspace_id to get information about a specific Workflow Job run."
        )
        get_workflow_job_inst.add_argument(
            "--json-output",
            type=check_non_empty_string,
            nargs='?',
            choices=['pretty', 'default'],
            default='pretty',
            help="Specifies the format of JSON output."
        )
        get_workflow_job_inst.add_argument(
            "--yaml-output",
            type=check_boolean,
            nargs='?',
            choices=['true', 'false'],
            default='false',
            help="Displays the information in YAML format if set to 'true'."
        )

        get_job_instance_status = subparser.add_parser(
            'run-status',
            help='To get all the status information about a specific Spark Job run.',
            formatter_class=ArgumentDefaultsHelpFormatter)
        get_job_instance_status.add_argument(
            "--run_id",
            type=int,
            nargs=1,
            default=SUPPRESS,
            required=True,
            help="Provide run_id to get all the status information about a specific Spark Job run."
        )
        get_job_instance_status.add_argument(
            "--workspace_id",
            type=int,
            nargs=1,
            default=SUPPRESS,
            required=True,
            help="Provide workspace_id to get all the status information about a specific Spark Job run."
        )
        get_job_instance_status.add_argument(
            "--json-output",
            type=check_non_empty_string,
            nargs='?',
            choices=['pretty', 'default'],
            default='pretty',
            help="Specifies the format of JSON output."
        )
        get_job_instance_status.add_argument(
            "--yaml-output",
            type=check_boolean,
            nargs='?',
            choices=['true', 'false'],
            default='false',
            help="Displays the information in YAML format if set to 'true'."
        )
