FROM gitpod/workspace-full as python_workspace
 
RUN pyenv install 3.11 && pyenv global 3.11
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt
 
FROM gitpod/workspace-mongodb:latest
