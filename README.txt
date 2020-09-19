# Machine Learning Assignment 1

# First, get the package
git clone https://github.com/rstewart61/gt-ml.git
cd gt-ml

# Install basic requirements
pip install -r requirements.txt

# To generate plots used for the analysis report, run:
python3 project1.py

# Expect project1.py to take 6-24 hours, depending on available CPU.

# To generate data used for exploratory data analysis, run:
python3 data.py

# Expect data.py to take 4-8 hours, depending on available CPU.

# If you have ImageMagick, plots can be glued together with
./plots/glue_plots.sh
