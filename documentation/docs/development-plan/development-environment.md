---
sidebar_position: 4
---

# Development Environment
The Development environment will require both a Python runtime and `npm`. In our case, we used Python 3.10.6 and npm 18.0.0

A developer can create a virtual environment with their Python runtime and install the following dependencies
```
absl-py==1.3.0
anyio==3.6.2
argon2-cffi==21.3.0
argon2-cffi-bindings==21.2.0
asgiref==3.5.2
asttokens==2.1.0
astunparse==1.6.3
async-generator==1.10
attrs==22.1.0
backcall==0.2.0
beautifulsoup4==4.11.1
bleach==5.0.1
cachetools==5.2.0
certifi==2022.9.24
cffi==1.15.1
charset-normalizer==2.1.1
contourpy==1.0.6
coverage==6.5.0
cycler==0.11.0
debugpy==1.6.3
decorator==5.1.1
defusedxml==0.7.1
Django==4.1.2
django-nose==1.4.7
dnspython==2.2.1
entrypoints==0.4
exceptiongroup==1.0.4
executing==1.2.0
fastjsonschema==2.16.2
flatbuffers==22.10.26
fonttools==4.38.0
gast==0.4.0
google-auth==2.13.0
google-auth-oauthlib==0.4.6
google-pasta==0.2.0
grpcio==1.50.0
h11==0.14.0
h5py==3.7.0
idna==3.4
iniconfig==1.1.1
ipykernel==6.17.0
ipython==8.6.0
ipython-genutils==0.2.0
jedi==0.18.1
Jinja2==3.1.2
joblib==1.2.0
jsonschema==4.17.0
jupyter-server==1.21.0
jupyter_client==7.4.4
jupyter_core==4.11.2
jupyterlab-pygments==0.2.2
keras==2.10.0
Keras-Preprocessing==1.1.2
kiwisolver==1.4.4
libclang==14.0.6
Markdown==3.4.1
MarkupSafe==2.1.1
matplotlib==3.6.2
matplotlib-inline==0.1.6
mistune==2.0.4
nbclassic==0.4.7
nbclient==0.7.0
nbconvert==7.2.3
nbformat==5.7.0
nest-asyncio==1.5.6
nose==1.3.7
notebook==6.5.2
notebook_shim==0.2.0
numpy==1.23.4
oauthlib==3.2.2
opencv-python==4.6.0.66
opt-einsum==3.3.0
outcome==1.2.0
packaging==21.3
pandas==1.5.2
pandocfilters==1.5.0
parso==0.8.3
pexpect==4.8.0
pickleshare==0.7.5
Pillow==9.2.0
pluggy==1.0.0
prometheus-client==0.15.0
prompt-toolkit==3.0.31
protobuf==3.19.6
psutil==5.9.3
ptyprocess==0.7.0
pure-eval==0.2.2
pyasn1==0.4.8
pyasn1-modules==0.2.8
pycparser==2.21
Pygments==2.13.0
pymongo==4.3.2
pyparsing==3.0.9
pyrsistent==0.19.1
PySocks==1.7.1
pytest==7.2.0
python-dateutil==2.8.2
pytz==2022.6
pyzmq==24.0.1
requests==2.28.1
requests-oauthlib==1.3.1
rsa==4.9
scikit-learn==1.1.3
scipy==1.9.3
seaborn==0.12.1
selenium==4.6.1
Send2Trash==1.8.0
six==1.16.0
sklearn==0.0
sniffio==1.3.0
sortedcontainers==2.4.0
soupsieve==2.3.2.post1
sqlparse==0.4.3
stack-data==0.6.0
tensorboard==2.10.1
tensorboard-data-server==0.6.1
tensorboard-plugin-wit==1.8.1
tensorflow==2.10.0
tensorflow-estimator==2.10.0
tensorflow-io-gcs-filesystem==0.27.0
termcolor==2.0.1
terminado==0.17.0
threadpoolctl==3.1.0
tinycss2==1.2.1
tomli==2.0.1
tornado==6.2
traitlets==5.5.0
trio==0.22.0
trio-websocket==0.9.2
typing_extensions==4.4.0
urllib3==1.26.12
wcwidth==0.2.5
webencodings==0.5.1
websocket-client==1.4.1
Werkzeug==2.2.2
wrapt==1.14.1
wsproto==1.2.0
```
## Editors and IDEs
VSCode is the preferred editor. Downloading the official MongoDB VSCode extension will aid development

## Languages and Frameworks

### -Python

Django, Django REST Framework, Django REST Auth

PIP Package Management

### -JavaScript

React.js

### -HTML

### -CSS

### -SQLite
Django's builtin SQLite database will be used to store user authentication details.

## Compilers and Interpreters
Webpack will be used to compile React.js into plain javascript to be served to the user.
### -Python3
Python 3.10.6 is used in the environment.
## Documentation Tools

### -Docasaurus
Docusaurus is used to compile the documentation for the project
## Testing Tools

### -Django Testing Framework
The Django Testing Framework is used to implement unit tests and integration tests.
### - Selenium
The Selenium Testing Framework is used to implement functional tests.
## Deployment Platform
The final deployment will be hosted on an AWS EC2 server. SQLite will be hosted on the same machine for user authentication, and MongoDB atlas will be used to host User data and reference Data.
