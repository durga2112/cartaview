# Prerequisites

## Install the CARTA scripted client

Starting from the scriptedClient directory, run:

```bash
python setup.py sdist
```

Change to the dist directory and untar the file in it:

```bash
tar -xvf cartavis-alpha.tar.gz
```

Change to the resulting directory and run:

```bash
sudo python setup.py install
```

To test that this has worked, run Python from a directory outside of the CARTA installation and try to import cartavis:

```python
import carta.cartavis
```

If this does not generate any error messages, then the CARTA scripted client has been installed properly on your system and can be imported from anywhere.

## The config.json file

The CARTA `config.json` file needs a few additional entries in order for the cartaview() task to work. They are:

- "port": this can usually be set to "9999" without any problems
- "executable": the full path of the CARTA executable file
- "htmlFile": the full path of the CARTA desktopIndex.html file

A sample config.json file looks like this:

```json
{                                                                               
    "_comment" : "List of plugin directories",                                  
    "pluginDirs": [                                                             
    "$(APPDIR)/../plugins",                                                     
    "$(HOME)/.cartavis/plugins"                                                 
    ],                                                                          
    "port" : "9999",                                                            
    "executable" : "$(HOME)/scratch/build/dev/cpp/desktop/desktop",          
    "htmlFile" : "$(HOME)/dev/CARTAvis/carta/html5/desktop/desktopIndex.html"
}              
```

# Placing the files

The `cartaview()` task consists of two files: `cartaview.xml` and `task_cartaview.py`. Both files need to be placed in their proper locations within the CASA installation. If you are not sure what these locations are, the following instructions should help: [Exploring the built-in CASA tasks](https://casaguides.nrao.edu/index.php?title=Writing_a_CASA_Task#Exploring_the_built-in_CASA_tasks).

# Building the task

Instructions for building a CASA task can be found here: [Building the task](https://casaguides.nrao.edu/index.php?title=Writing_a_CASA_Task#Building_the_task). But note that if the `cartaview()` task is the only one you need to build, you can save a lot of time by passing an argument to `buildmytasks`; e.g.:

```python
os.system('buildmytasks cartaview')
```

# Running the task

After the task has been built, it can be run like any other CASA task. For example:

```python
# In CASA
tget cartaview
inp
raster = '~/CARTA/Images/mexinputtest.fits'
configFile = '~/.cartavis/config.json'
```
