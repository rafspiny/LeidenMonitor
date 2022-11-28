# Leiden open position notifier
I wanted to know when a position would open at the faculty of science at the Leiden University.

Not being able to find a subscribe button to get an update, I built one.

## Tiny scraper with notifier
This tiny project uses Python and Mailjet library to check the website with a certain frequency (i.e monthly) and send 
an email whenever there is a new opening. 

The project structure is
```bash
.
├── business
│   ├── email_provider.py
│   ├── __init__.py
│   └── logic.py
├── conf
│   ├── constants.py
│   ├── email_config.py
│   ├── __init__.py
│   └── secrets.py
├── data_layer
│   ├── data_storage.py
│   └── __init__.py
├── existing_vacancies.json
├── main.py
├── model
│   ├── __init__.py
│   └── models.py
├── poetry.lock
├── pyproject.toml
└── README.md
```

It uses poetry to set up the virtual environment.
You can see that I tried to give a tiny bit of structure to the FS.

## Configure and run
Before you run it, you should check out the `conf` folder.

You can set up the integration with Mailjet in the `conf/secrets.py` with your API key/secret.

In the `conf/email_config.py` you can set up the recipient of your notification.

Lastly, you can tweak the request to the Leiden open position page by applying filters in the `conf/constants.py`

#### Running it
Just run the main.py file.

I set up a cron job to run it once per week.
```bash
40 07 * * 1 cd <PATH_TO_PROJECT>/LeidenMonitor && <PATH_TO_POETRY_IF_NOT_STANDARD>/poetry run python main.py >/tmp/cronlog
```