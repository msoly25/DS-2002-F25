import sys
import update_portfolio
import generate_summary

def run_production_pipeline():
    print("--- Starting Full Production Pipeline ---", file=sys.stderr)

    print("Step 1: Updating Portfolio...", file=sys.stderr)
    update_portfolio.main()

    print("Step 2: Generating Summary Report...", file=sys.stderr)
    generate_summary.main()

    print("--- Pipeline Complete ---", file=sys.stderr)

if __name__ == "__main__":
    run_production_pipeline()
