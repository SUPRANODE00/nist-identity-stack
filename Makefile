run:
	mkdir -p output
	cat data/sample_eeg.csv | sed 's/NaN/0/g' > output/normalized.csv
	cat output/normalized.csv | awk -F, 'NR>1 && $$3>40 {print $$1","$$3}' > output/filtered.csv
	cat output/normalized.csv | awk -F, 'NR>1 {print $$1","$$4","$$3}' > output/inverted.csv

test: run
	diff output/filtered.csv tests/expected_filtered.csv
	diff output/inverted.csv tests/expected_inverted.csv

clean:
	rm -rf output/*
