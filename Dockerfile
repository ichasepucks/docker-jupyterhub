FROM jupyterhub/jupyterhub:0.8.0

RUN pip install mysql-connector==2.1.4
COPY jupyterhub_config.py /srv/jupyterhub

CMD ["jupyterhub", "--debug", "--config=/srv/jupyterhub/jupyterhub_config.py"]