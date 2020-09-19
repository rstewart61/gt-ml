# Machine Learning Assignment 1

# First, get the package
sudo apt-get install wget unzip python3 gcc
wget https://www.dropbox.com/s/k0dk99tlalwyrsa/rstewart61-assignment1.zip?dl=0 -O rstewart61-assignment1.zip
unzip rstewart61-assignment1.zip

# Install basic requirements
# pip install -r requirements.txt


# Install these packages IN THIS ORDER:
pip install -U pandas
pip install -U scikit-learn
pip install -U matplotlib
pip install -U scikit-hubness
pip install -U imbalanced-learn

# Ignore the following error:
# "ERROR: scikit-hubness 0.21.2 has requirement scikit-learn==0.21.3, \
#  but you'll have scikit-learn 0.23.2 which is incompatible."

# To generate plots used for the analysis report, run:
python3 project1.py

# Expect project1.py to take 6-24 hours, depending on available CPU.

# To generate data used for exploratory data analysis, run:
python3 data.py

# Expect data.py to take 4-8 hours, depending on available CPU.

# If you have ImageMagick, plots can be glued together with
./plots/glue_plots.sh
