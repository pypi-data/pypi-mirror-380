import sys
from pathlib import Path

import tomli_w  # for writing TOML files

CONFIG_DIR = Path.home() / ".sqlai"
CONFIG_FILE = CONFIG_DIR / "config.toml"


def write_config(provider: str, api_key: str, model: str, sql_dialect: str):
    """Write the global config file."""
    CONFIG_DIR.mkdir(exist_ok=True)  # create ~/.sqlai if missing
    config_data = {
        "ai_provider": provider,
        "api_key": api_key,
        "model": model,
        "sql_dialect": sql_dialect,
    }
    with open(CONFIG_FILE, "wb") as f:
        tomli_w.dump(config_data, f)
    print(f"Config saved to {CONFIG_FILE}")


def read_config():
    """Read the global config file."""
    if not CONFIG_FILE.exists():
        print("⚠️   No global config found. Run `sqlai set_config` first.")
        sys.exit(0)
    import tomli

    with open(CONFIG_FILE, "rb") as f:
        return tomli.load(f)


def userinput_selection(options, prompt):

    # convert list into dic with numeric keys starting with 1
    options_dic = {i + 1: value for i, value in enumerate(options)}

    for key, value in options_dic.items():
        print(f"[{key}] {value}")

    error_message = (
        f"⚠️   Invalid input. Please enter a number between 1 and {len(options)}."
    )

    try:
        userinput = int(input(f"➡️  {prompt}: ").strip())

        if userinput not in list(range(1, len(options) + 1)):
            print(error_message)
            sys.exit(0)

    except ValueError:
        print(error_message)
        sys.exit(0)

    print()
    return options_dic[userinput]


def set_config():
    print("Configure your SQL AI settings (global).")

    provider = userinput_selection(["Google"], prompt="Select an AI provider")

    model = userinput_selection(
        [
            "gemini-2.5-flash",
            "gemini-2.5-pro",
            "gemini-1.5-flash",
            "gemini-1.5-pro",
        ],
        prompt="Select a model",
    )

    api_key = input("API Key (https://aistudio.google.com/): ").strip()

    sql_dialect = userinput_selection(
        [
            "Amazon Redshift",
            "Google BigQuery SQL",
            "IBM Db2",
            "MariaDB",
            "Microsoft SQL Server (Transact-SQL, T-SQL)",
            "MySQL",
            "Oracle SQL (PL/SQL)",
            "PostgreSQL",
            "Snowflake SQL",
            "SQLite",
        ],
        prompt="Select a SQL dialect",
    )

    write_config(provider, api_key, model, sql_dialect)
    print("✅ Success")
