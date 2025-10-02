"""CLI for working with IMF datasets."""

import argparse
import sys
import json
import threading
import time
from colorama import init, Fore, Style
from . import wrappers
import importlib.resources
from contextlib import contextmanager

init(autoreset=True)


# Formatting helpers
def bold(text):
    """Return bold styled text for CLI output."""
    return Style.BRIGHT + text + Style.NORMAL


def header(text):
    """Return header styled text for CLI output."""
    return Fore.CYAN + Style.BRIGHT + f"\n{text} \n" + Style.RESET_ALL


def green(text):
    """Return green styled text for CLI output."""
    return Fore.GREEN + text + Style.RESET_ALL


def yellow(text):
    """Return yellow styled text for CLI output."""
    return Fore.YELLOW + text + Style.RESET_ALL


def red(text):
    """Return red styled text for CLI output."""
    return Fore.RED + text + Style.RESET_ALL


def cyan(text):
    """Return cyan styled text for CLI output."""
    return Fore.CYAN + Style.BRIGHT + text + Style.RESET_ALL


def load_json_resource(package, resource):
    """Load JSON resource from package (i.e., world_economic_outlook)."""
    resource_path = importlib.resources.files(package).joinpath(resource)
    with resource_path.open("r", encoding="utf-8") as f:
        return json.load(f)


def list_datasets():
    """List all available datasets."""
    datasets = load_json_resource("world_economic_outlook.structures", "DATASETS.json")
    print(cyan(f"\n{'Dataset':<22} {'Name'}"))
    print(f"{'_'*21} {'_'*40}" + Style.RESET_ALL)
    for ds_id, ds in sorted(datasets.items(), key=lambda x: x[0].lower()):
        print((f"{ds_id.lower():<22}") + ds.get("name", ds_id))


def show_dataset(dataset_id):
    """Show details for a specific dataset."""
    datasets = load_json_resource("world_economic_outlook.structures", "DATASETS.json")
    dimensions = load_json_resource(
        "world_economic_outlook.structures", "DIMENSIONS.json"
    )
    ds = datasets.get(dataset_id.upper())
    if not ds:
        print(red(f"Dataset '{dataset_id}' not found."))
        return
    print(header(f"Dataset: {dataset_id.upper()}"))
    print(bold("Name: ") + ds.get("name", ""))
    print(bold("Description: ") + ds.get("description", ""))
    print(header("Dimensions and possible values"))
    ds_dims = dimensions.get(dataset_id.upper(), {})
    for dim, values in ds_dims.items():
        print(green(f"  {dim}: "))
        print(values)


def print_dataset_info(dataset_id):
    import json
    from textwrap import fill

    all_ds = load_json_resource("world_economic_outlook.structures", "DATASETS.json")
    ds_entry = all_ds.get(dataset_id.upper(), {})
    ds_name = ds_entry.get("name", dataset_id.upper())
    ds_info = ds_entry.get("description", None)
    print(f"{Fore.CYAN}{Style.BRIGHT}\n{ds_name}\n{Style.RESET_ALL}")
    if ds_info:
        print(f"{bold('Description:')} {ds_info}\n")
    else:
        print(
            f"{bold('Description:')} No description found for dataset '{dataset_id}'.\n"
        )
    all_dims = load_json_resource(
        "world_economic_outlook.structures", "DIMENSIONS.json"
    )
    dims = all_dims.get(dataset_id.upper(), {})
    dim_map = {
        "COUNTRY": "isos",
        "REF_AREA": "isos",
        "JURISDICTION": "isos",
        "COUNTERPART_COUNTRY": "isos_star",
    }
    printed_isos = False
    for key, values_list in dims.items():
        arg_name = dim_map.get(key) or key.lower()
        if arg_name == "isos":
            if not printed_isos:
                values = ", ".join(values_list)
                values_wrapped = fill(values, width=80, subsequent_indent="    ")
                print(
                    f"{Fore.CYAN}{Style.BRIGHT}--isos:{Style.RESET_ALL}\n    {values_wrapped}\n"
                )
                printed_isos = True
        else:
            values = ", ".join(values_list)
            values_wrapped = fill(values, width=80, subsequent_indent="    ")
            print(
                f"{Fore.CYAN}{Style.BRIGHT}--{arg_name}:{Style.RESET_ALL}\n    {values_wrapped}\n"
            )


def highlight(text, term):
    """Highlight search term in text for CLI output."""
    import re

    def repl(match):
        return Fore.MAGENTA + Style.BRIGHT + match.group(0) + Style.RESET_ALL

    pattern = re.compile(re.escape(term), re.IGNORECASE)
    return pattern.sub(repl, text)


def search_datasets(term):
    """Search datasets by term and display results."""
    datasets = load_json_resource("world_economic_outlook.structures", "DATASETS.json")
    term_lower = term.lower()
    found = False

    # 1. Exact match for dataset ID (case-insensitive)
    for ds_id in datasets:
        if term_lower == ds_id.lower():
            ds = datasets[ds_id]
            print(bold("\nDataset: ") + highlight(ds_id.upper(), term))
            print(bold("Name: ") + yellow(ds.get("name", ds_id)))
            print(bold("Description: ") + ds.get("description", ""))
            found = True
            return  # Only show exact match

    # 2. Substring match in dataset ID, name, or description
    for ds_id, ds in datasets.items():
        name = ds.get("name", "")
        desc = ds.get("description", "")
        if (
            term_lower in ds_id.lower()
            or term_lower in name.lower()
            or term_lower in desc.lower()
        ):
            print(bold("\nDataset: ") + cyan(ds_id.upper()))
            print(bold("Name: ") + highlight(name, term))
            print(bold("Description: ") + highlight(desc, term))
            found = True

    # 3. If *still* no match, try splitting the term and matching any segment in name or description...
    if not found:
        segments = term_lower.split()
        for ds_id, ds in datasets.items():
            name = ds.get("name", "")
            desc = ds.get("description", "")
            for seg in segments:
                if seg and (seg in name.lower() or seg in desc.lower()):
                    print(header(f"{highlight(ds_id.upper(), seg)}"))
                    print(bold("Name: ") + highlight(name, seg))
                    print(bold("Description: ") + highlight(desc, seg))
                    found = True
                    break

    if not found:
        print("\n...")


def search_codelist(term):
    """Search codelist by term and display results."""
    codelists = load_json_resource("world_economic_outlook.codelists", "CODELIST.json")
    term_lower = term.lower()
    found = False
    printed = set()

    def highlight_codelist(text, term):
        import re

        def repl(match):
            return Fore.MAGENTA + Style.BRIGHT + match.group(0) + Style.RESET_ALL

        pattern = re.compile(re.escape(term), re.IGNORECASE)
        return pattern.sub(repl, text)

    # 1. Try exact match first (on id)
    for code in codelists:
        code_id = code.get("id", "")
        desc = code.get("description") or ""
        unique_key = (code["id"], code["name"], desc)
        if term_lower == code_id.lower() and unique_key not in printed:
            print(
                green(f"{highlight_codelist(code['id'], term)}: ")
                + bold(code["name"])
                + yellow(f" - {desc}")
            )
            printed.add(unique_key)
            found = True

    # 2. If no exact match, try exact matches for each segment (split by "_") in id
    if not found:
        segments = term.split("_")
        for seg in segments:
            seg_lower = seg.lower()
            for code in codelists:
                code_id = code.get("id", "")
                desc = code.get("description") or ""
                unique_key = (code["id"], code["name"], desc)
                if seg_lower == code_id.lower() and unique_key not in printed:
                    print(
                        yellow(f"{highlight_codelist(code['id'], seg)}: ")
                        + bold(code["name"])
                        + f" - {desc}"
                    )
                    printed.add(unique_key)
                    found = True

    if not found:
        print("...")


def combined_search(term):
    """Run combined search for datasets and codelists."""
    print(cyan("\nDatasets:"))
    search_datasets(term)
    print(cyan("\nCodelists:\n"))
    search_codelist(term)


@contextmanager
def spinner(msg="Downloading"):
    """Show CLI spinner animation while downloading and processing data."""
    spinner_states = ["⣾", "⣽", "⣻", "⢿", "⡿", "⣟", "⣯", "⣷"]
    stop_event = threading.Event()

    def run():
        i = 0
        while not stop_event.is_set():
            print(
                f"\r{msg} {spinner_states[i % len(spinner_states)]}", end="", flush=True
            )
            time.sleep(0.1)
            i += 1
        print("\r" + " " * (len(msg) + 3) + "\r", end="", flush=True)

    t = threading.Thread(target=run)
    t.start()
    try:
        yield
    finally:
        stop_event.set()
        time.sleep(0.1)


def normalise_args(args, sig):
    import re

    kwargs = {}
    for param in sig.parameters.values():
        arg_name = param.name
        if hasattr(args, arg_name):
            val = getattr(args, arg_name)
            # Special handling for 'vintage' argument in <vweo>
            if arg_name == "vintage":
                if isinstance(val, list):
                    # If it's ["April", "2025"], join into "April 2025"
                    if len(val) == 2 and all(isinstance(v, str) for v in val):
                        joined = " ".join(val)
                        # If joined contains a comma, split into list
                        if "," in joined:
                            kwargs[arg_name] = [
                                v.strip() for v in joined.split(",") if v.strip()
                            ]
                        else:
                            kwargs[arg_name] = joined
                    else:
                        # If it's a list of full vintage strings, keep as list
                        # Also handle comma-separated values in any element
                        vintages = []
                        for v in val:
                            if isinstance(v, str) and "," in v:
                                vintages.extend(
                                    [x.strip() for x in v.split(",") if x.strip()]
                                )
                            else:
                                vintages.append(v)
                        kwargs[arg_name] = (
                            vintages if len(vintages) > 1 else vintages[0]
                        )
                elif isinstance(val, str) and "," in val:
                    kwargs[arg_name] = [v.strip() for v in val.split(",") if v.strip()]
                else:
                    kwargs[arg_name] = val
            # Normal handling for other arguments
            elif isinstance(val, list):
                joined = " ".join(val)
                split_vals = [
                    v.strip() for v in re.split(r"[+, ]", joined) if v.strip()
                ]
                kwargs[arg_name] = split_vals if len(split_vals) > 1 else split_vals[0]
            else:
                kwargs[arg_name] = val
    return kwargs


def get_custom_usage():
    """Main CLI custom usage text."""
    return (
        f"\n"
        f"{Fore.CYAN}{Style.BRIGHT}World Economic Outlook CLI{Style.RESET_ALL}\n\n"
        f"{bold('Usage:')}\n"
        f"  imf <command> [options]\n\n"
        f"{bold('Commands:')}\n"
        f"  <dataset>         {{weo, er, cpi, ...}}\n"
        f"  list              List all datasets\n"
        f"  show              Show dataset info\n"
        f"  search            Search datasets & indicators\n"
        f"  help              Show this help message\n\n"
        f"{bold('Options:')}\n"
        f"  --help [-h]       Show this help message\n"
    )


class CustomArgumentParser(argparse.ArgumentParser):
    def error(self, message):
        from . import wrappers

        dataset_commands = [
            name.lower()
            for name in dir(wrappers)
            if not name.startswith("_") and callable(getattr(wrappers, name))
        ]
        builtin_commands = {"list", "show", "search", "help"}
        if len(sys.argv) > 1:
            cmd = sys.argv[1]
            if cmd in dataset_commands:
                print(f"\n{Fore.RED}{Style.BRIGHT}Error:{Style.RESET_ALL} {message}\n")
                sys.argv = [sys.argv[0], cmd, "--help"]
                main()
                sys.exit(2)
            elif cmd in builtin_commands:
                print(f"\n{Fore.RED}{Style.BRIGHT}Error:{Style.RESET_ALL} {message}\n")
                self.print_help()
                sys.exit(2)
            else:
                print(f"\n{Fore.RED}{Style.BRIGHT}Error:{Style.RESET_ALL} {message}\n")
                self.print_help()
                sys.exit(2)
        else:
            print(f"\n{Fore.RED}{Style.BRIGHT}Error:{Style.RESET_ALL} {message}\n")
            self.print_help()
            sys.exit(2)


def print_custom_help():
    print(get_custom_usage())
    sys.exit(0)


def parse_args():
    class CustomHelpFormatter(argparse.RawTextHelpFormatter):
        def add_usage(self, usage, actions, groups, prefix=None):
            self._add_item(lambda *args: get_custom_usage(), [])

        def format_help(self):
            return get_custom_usage()

    parser = CustomArgumentParser(
        prog="imf",
        description="World Economic Outlook CLI",
        add_help=False,
        formatter_class=CustomHelpFormatter,
    )
    subparsers = parser.add_subparsers(dest="command")
    subparsers.add_parser("list", help="List all datasets")
    show_parser = subparsers.add_parser("show", help="Show dataset info")
    show_parser.add_argument("dataset", help="Dataset ID")
    search_parser = subparsers.add_parser("search", help="Combined search")
    search_parser.add_argument("term", help="Search term")
    for name in dir(wrappers):
        if not name.startswith("_"):
            func = getattr(wrappers, name)
            if callable(func):
                ds_parser = subparsers.add_parser(
                    name.lower(), help=f"{name} dataset", add_help=False
                )
                import inspect

                sig = inspect.signature(func)
                for param in sig.parameters.values():
                    if param.default is param.empty:
                        ds_parser.add_argument(
                            f"--{param.name}",
                            nargs="+",
                            required=True,
                            help=f"{param.name} (required, accepts multiple values: FIN SWE NOR DNK or FIN,SWE,NOR,DNK or FIN+SWE+NOR+DNK)",
                        )
                    else:
                        ds_parser.add_argument(
                            f"--{param.name}",
                            nargs="+",
                            default=param.default,
                            help=f"{param.name} (default: {param.default}, accepts multiple values)",
                        )
                    if param.name == "save_path":
                        ds_parser.add_argument(
                            "-s",
                            dest="save_path",
                            nargs="+",
                            help="Short for save_path",
                        )
                    elif param.name == "database":
                        ds_parser.add_argument(
                            "-d", dest="database", nargs="+", help="Short for database"
                        )
                    elif param.name == "table":
                        ds_parser.add_argument(
                            "-t", dest="table", nargs="+", help="Short for table"
                        )
    subparsers.add_parser("help", help="Show this help message")
    return parser


def handle_command(args):
    from . import wrappers
    import inspect

    dataset_commands = [
        name.lower()
        for name in dir(wrappers)
        if not name.startswith("_") and callable(getattr(wrappers, name))
    ]
    if args.command == "list":
        list_datasets()
    elif args.command == "show":
        print_dataset_info(args.dataset)
    elif args.command == "search":
        combined_search(args.term)
    elif args.command == "help" or args.command is None:
        print_custom_help()
    elif args.command in dataset_commands:
        func = getattr(wrappers, args.command.upper(), None) or getattr(
            wrappers, args.command, None
        )
        sig = inspect.signature(func)
        kwargs = normalise_args(args, sig)
        if len(sys.argv) > 2 and sys.argv[2] == "*":
            for param in sig.parameters.values():
                if param.default is param.empty:
                    kwargs[param.name] = "*"
        with spinner():
            result = func(**kwargs)
        suppress_output = any(
            kwargs.get(flag) for flag in ["save_path", "database", "table"]
        )
        if not suppress_output:
            print(json.dumps(result, indent=2, sort_keys=True))
    else:
        print_custom_help()


def main():
    if len(sys.argv) == 2 and sys.argv[1] in ("--help", "-h"):
        print_custom_help()
    parser = parse_args()
    # Pre-parse sys.argv for dataset help before argparse does anything
    from . import wrappers

    dataset_commands = [
        name.lower()
        for name in dir(wrappers)
        if not name.startswith("_") and callable(getattr(wrappers, name))
    ]
    builtin_commands = {"list", "show", "search", "help"}
    if (
        len(sys.argv) > 1
        and sys.argv[1] in dataset_commands
        and sys.argv[1] not in builtin_commands
    ):
        cmd = sys.argv[1]
        info_flag = "--info" in sys.argv
        if info_flag:
            print_dataset_info(cmd)
            sys.exit(0)
        help_trigger = "-h" in sys.argv or "--help" in sys.argv
        no_args_trigger = len(sys.argv) == 2
        help_word_trigger = len(sys.argv) > 2 and sys.argv[2].lower() == "help"
        if help_trigger or no_args_trigger or help_word_trigger:
            func = getattr(wrappers, cmd.upper(), None) or getattr(wrappers, cmd, None)
            import inspect

            sig = inspect.signature(func)
            all_dims = load_json_resource(
                "world_economic_outlook.structures", "DIMENSIONS.json"
            )
            dims = all_dims.get(cmd.upper(), {})
            dim_map = {
                "COUNTRY": "isos",
                "REF_AREA": "isos",
                "JURISDICTION": "isos",
                "COUNTERPART_COUNTRY": "isos_star",
            }
            cus_map = {
                "start_date": "e.g. 2020-01-01",
                "end_date": "e.g. 2028-01-01",
                "database": "e.g. database.db",
                "start_year": "e.g. 2020",
                "end_year": "e.g. 2028",
                "table": f"e.g. {cmd}",
                "save_path": f"e.g. {cmd}.json",
                "full_output": "True/False",
                "use_iso_alpha2": "True/False",
            }
            option_tuples = []
            iso_dim = None
            # IMF treats COUNTRY, REF_AREA, or JURISDICTION as if ISO dimensions
            for iso_key in ("COUNTRY", "REF_AREA", "JURISDICTION"):
                if iso_key in dims:
                    iso_dim = iso_key
                    break
            for param in sig.parameters:
                dim_name = None
                for k, v in dim_map.items():
                    if v == param:
                        dim_name = k
                        break
                if param == "database":
                    option_tuples.append(("  --database [-d]", cus_map["database"]))
                elif param == "table":
                    option_tuples.append(("  --table [-t]", cus_map["table"]))
                elif param == "save_path":
                    option_tuples.append(("  --save_path [-s]", cus_map["save_path"]))
                elif param == "isos" and iso_dim:
                    values_list = dims[iso_dim]
                    if len(values_list) > 5:
                        values = ", ".join(values_list[:5]) + ", ..."
                    else:
                        values = ", ".join(values_list)
                    option_tuples.append((f"  --isos", values))
                elif dim_name and dim_name in dims:
                    values_list = dims[dim_name]
                    if len(values_list) > 5:
                        values = ", ".join(values_list[:5]) + ", ..."
                    else:
                        values = ", ".join(values_list)
                    option_tuples.append((f"  --{param}", values))
                elif param in cus_map:
                    option_tuples.append((f"  --{param}", cus_map[param]))
                elif param.upper() in dims:
                    values_list = dims[param.upper()]
                    if len(values_list) > 5:
                        values = ", ".join(values_list[:5]) + ", ..."
                    else:
                        values = ", ".join(values_list)
                    option_tuples.append((f"  --{param}", values))
                else:
                    option_tuples.append((f"  --{param}", ""))
            option_tuples.append(("  --info", "Show dataset description"))
            option_tuples.append(("  --help [-h]", "Show this help message"))
            max_opt_len = max(len(opt[0]) + 3 for opt in option_tuples)
            options_str = "\n".join(
                f"{opt.ljust(max_opt_len)} {val}" if val else f"{opt}"
                for opt, val in option_tuples
            )
            all_ds = load_json_resource(
                "world_economic_outlook.structures", "DATASETS.json"
            )
            ds_name = all_ds.get(cmd.upper(), {}).get("name", cmd.upper())
            ds_name_colored = f"\n{Fore.CYAN}{Style.BRIGHT}{ds_name}{Style.RESET_ALL}"
            print(
                f"{ds_name_colored}\n\n{bold('Usage')}:\n  imf {cmd} [options]\n\n{bold('Options')}:\n{options_str}"
            )
            sys.exit(0)
    args = parser.parse_args()
    handle_command(args)


if __name__ == "__main__":
    main()
