import importlib
import sys

if __name__ == "__main__":
    subcommands = {
        "train",
        "synthetic_sft",
        "synthetic_dpo",
    }
    if len(sys.argv) < 2:
        raise ValueError(f"CLI requires a subcommand in {subcommands}")
    subcommand = sys.argv.pop(1)
    if subcommand not in subcommands:
        raise ValueError(f"CLI requires a subcommand in {subcommands}")
    submodule = importlib.import_module(f"mlx_lm_lora.{subcommand}")
    submodule.main()
