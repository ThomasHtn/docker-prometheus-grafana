**Structure du projet :**

```
docker-compose-app/
├── .env
├── .gitignore
├── README.md
├── docker-compose.yml
│
├── fastapi_app/
│   ├── main.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── streamlit_app/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── prometheus/
│   └── prometheus.yml
│
├── grafana/
│   ├── dashboards.py
│   │   ├── dashboards.json
│   │   └── dashboards.yml
└── └── datasources
        └── datasources.yml
```


Grafana :  http://localhost:9501
login : admin
mdp : mon mdp