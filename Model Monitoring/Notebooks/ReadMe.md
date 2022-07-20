### How to run the notebook on local

**Prerequisites**
- Conda

##### Step 1: Create a Python virtual environment
```
$ conda create -n monitor python=3.9 jupyterlab
```

##### Step 2: Activate Python virtual environment
```
$ conda activate monitor
```

##### Step 3: Install all required Python packages
```
$ pip install -r requirements.txt
```

##### Step 4: Display dashboards in a Jupyter notebook inline
```
$ jupyter nbextension install --sys-prefix --symlink --overwrite --py evidently
$ jupyter nbextension enable evidently --py --sys-prefix
```