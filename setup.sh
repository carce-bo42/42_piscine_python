MYPATH="/goinfre/$USER/miniconda3"

# MAC
curl -LO "https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh"
sh Miniconda3-latest-MacOSX-x86_64.sh -b -p $MYPATH

#LINUX
#curl -LO "https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh"
#sh Miniconda3-latest-Linux-x86_64.sh -b -p $MYPATH

# For zsh
$MYPATH/bin/conda init zsh
$MYPATH/bin/conda config --set auto_activate_base false
source ~/.zshrc

# For bash
#$MYPATH/bin/conda init bash
#$MYPATH/bin/conda config --set auto_activate_base false
#source ~/.bash_profile

#create an environment for 42AI
conda create --name 42AI-$USER python=3.7 jupyter pandas pycodestyle numpy

#check your environment
conda info --envs
conda activate 42AI-$USER
which python
python -V
python -c "print('Hello World!')"

