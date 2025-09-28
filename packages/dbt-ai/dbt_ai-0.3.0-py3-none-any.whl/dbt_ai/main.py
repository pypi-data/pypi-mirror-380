import argparse
import os

from dbt_ai.dbt import DbtModelProcessor
from dbt_ai.report import generate_html_report


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate improvement suggestions and check metadata coverage for dbt models"
    )
    parser.add_argument("-f", "--dbt-project-path", help="Path to the dbt project directory")
    parser.add_argument(
        "--create-models",
        help="Create dbt models using the provided prompt",
        default=None,
    )
    parser.add_argument(
        "-a",
        "--advanced-rec",
        action="store_true",
        help="Generate only advanced recommendations for dbt models",
    )
    parser.add_argument(
        "-d",
        "--database",
        help="Specify the type of database system the dbt project is built on",
        choices=["snowflake", "postgres", "redshift", "bigquery"],
        default="snowflake",
    )
    parser.add_argument(
        "--metadata-only",
        action="store_true",
        help="Check only metadata coverage without generating AI suggestions",
    )
    args = parser.parse_args()

    if not args.create_models:
        processor = DbtModelProcessor(args.dbt_project_path, args.database)

        if args.metadata_only:
            # Metadata-only mode: skip AI suggestions
            models, missing_metadata = processor.process_dbt_models(advanced=False, metadata_only=True)

            models_without_metadata = [model["model_name"] for model in models if not model["metadata_exists"]]

            if models_without_metadata:
                print("The following models are missing metadata:")
                for model_name in models_without_metadata:
                    print(f"  - {model_name}")
            else:
                print("All models have associated metadata.")

            print(f"\nMetadata check complete. {len(models)} models analyzed.")
        else:
            # Normal mode: full processing with AI suggestions
            models, missing_metadata = processor.process_dbt_models(advanced=args.advanced_rec)

            output_path = os.path.join(args.dbt_project_path, "dbt_model_suggestions.html")

            lineage_description, graph = processor.generate_lineage(models)
            # processor.plot_directed_graph(graph)

            print(f"Lineage description:\n {lineage_description}")

            generate_html_report(models, output_path, missing_metadata)
            advancedprint = "advanced " if args.advanced_rec else ""
            print(f"Generated {advancedprint}improvement suggestions report at: {output_path}")

            models_without_metadata = [model["model_name"] for model in models if not model["metadata_exists"]]

            if models_without_metadata:
                print("\nThe following models are missing metadata:")
                for model_name in models_without_metadata:
                    print(f"  - {model_name}")
            else:
                print("\nAll models have associated metadata.")
    else:
        processor = DbtModelProcessor(args.dbt_project_path, args.database)
        prompt = args.create_models
        processor.create_dbt_models(prompt)


if __name__ == "__main__":
    main()
