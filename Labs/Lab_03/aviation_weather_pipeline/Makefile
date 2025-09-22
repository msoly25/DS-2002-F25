.PHONY: all fetch analyze clean

all: analyze

fetch:
	@echo "Starting fetch step: fetching METAR data..."
	./fetch_metars.sh
	@echo "Fetch step complete: data saved in 'raw_metars/' directory."

analyze: fetch
	@echo "Starting analyze step: processing METAR JSON data..."
	./analyze_data.sh
	@echo "Analyze step complete: results saved in 'weather_report.csv'."
	@echo "Pipeline completed successfully."

clean:
	@echo "Cleaning up generated files..."
	rm -rf raw_metars/ weather_report.csv
	@echo "Clean complete: removed 'raw_metars/' directory and 'weather_report.csv'."


