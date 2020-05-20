'Problem'---
Expose the sample dataset through a single generic HTTP API endpoint, which is capable of filtering, grouping and sorting. Dataset represents performance metrics (impressions, clicks, installs, spend, revenue) for a given date, advertising channel, country and operating system. Dataset is expected to be stored and processed in a relational database.

Client of this API should be able to:

filter by time range (date_from / date_to is enough), channels, countries, operating systems
group by one or more columns: date, channel, country, operating system
sort by any column in ascending or descending order
see derived metric CPI (cost per install) which is calculated as cpi = spend / installs


install----
-clone of repo
install dependancies from requirements file.
    ``` 
    $ pip install -r requirements.txt

    python manage.py migrate


run django app,
    ```
    $ python manage.py runserver



username-ankita.kapoor
paswrd-adjust


-> i have imported the data through python shell
-> if you want to add more data, you can follow theses commands
-> in cmd
    python manage.py shell
    import os
    import csv
    path="give dir path"
    os.chdir(path)
    from apiapp.models import dataset
    with open('daatset.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            p = Dataset(date=row['date'], channel=row['channel'],country=row['country'],os=row['os'],impressions=row['impressions'],clicks=row['clicks'],installs=row['installs'],spend=row['spend'],revenue=row['revenue'])
             p.save()

             exit()


->localhost:8000/admin
here we can see data
