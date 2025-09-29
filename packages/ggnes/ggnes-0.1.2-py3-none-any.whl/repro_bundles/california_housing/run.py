#!/usr/bin/env python3
"""
California Housing GGNES Repro Bundle Runner

This script runs the GGNES neural architecture search on the California Housing
dataset with configurable parameters.
"""

import json
import os
import time
from pathlib import Path

from demo.california_housing import GGNESConfig, GGNESEvolution, load_data


def load_config(config_path="config.json"):
    """Load configuration from JSON file."""
    if os.path.exists(config_path):
        with open(config_path) as f:
            config_dict = json.load(f)

        # Create config object
        config = GGNESConfig(**config_dict)
        return config
    else:
        # Use default configuration
        return GGNESConfig(
            population_size=20,
            n_generations=10,
            n_workers=4,
            max_iterations=10,
            base_epochs=20,
            full_train_epochs=100,
            output_dir="california_housing_results"
        )


def main():
    """Main execution function."""
    print("="*80)
    print("GGNES CALIFORNIA HOUSING REPRO BUNDLE")
    print("="*80)
    print("\nThis reproduction bundle demonstrates GGNES neural architecture search")
    print("on the California Housing dataset for regression tasks.\n")

    # Load configuration
    config = load_config()

    # Handle timestamped output directory
    if hasattr(config, 'use_timestamp') and config.use_timestamp:
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        output_dir = f"{config.output_dir}/run_{timestamp}"
        config.output_dir = output_dir
        print(f"Creating timestamped output directory: {output_dir}\n")
    else:
        output_dir = config.output_dir
        print(f"Using output directory: {output_dir}\n")

    print("Configuration:")
    print(f"  Population Size: {config.population_size}")
    print(f"  Generations: {config.n_generations}")
    print(f"  Workers: {config.n_workers}")
    print(f"  Max Iterations: {config.max_iterations}")
    print(f"  Base Epochs: {config.base_epochs}")
    print(f"  Full Train Epochs: {config.full_train_epochs}")
    print(f"  Output Directory: {config.output_dir}")
    print()

    # Create output directory
    Path(config.output_dir).mkdir(parents=True, exist_ok=True)

    # Load data
    print("Loading California Housing dataset...")
    train_data, val_data, test_data = load_data(subset_fraction=1.0)

    # Run evolution
    print("\nStarting GGNES Evolution...")
    evolution = GGNESEvolution(config)
    evolution.run_evolution(train_data, val_data, test_data)

    print("\n" + "="*80)
    print("REPRO BUNDLE EXECUTION COMPLETE")
    print("="*80)
    print(f"\nResults saved to: {config.output_dir}/")
    print("\nKey outputs:")
    print("  - best_genotype.pkl: Evolved architecture (can be imported)")
    print("  - best_model_trained.pth: Trained PyTorch model")
    print("  - comprehensive_analysis_report.txt: Detailed text report")
    print("  - complete_analysis.png: Visual dashboard")
    print("  - test_performance.png: Performance on unseen data")
    print("  - final_report.json: Summary metrics")


if __name__ == "__main__":
    main()
