import subprocess
import sys
import json
import pprint
import sqlite3
import os
import html
import datetime

print("I'm interested in: startDate, description, url, image, location, name")

try:
    db = sqlite3.connect("file:tranzac.db?mode=rw", uri=True)
    cursor = db.cursor()
except sqlite3.OperationalError:
    db = sqlite3.connect("tranzac.db")
    cursor = db.cursor()
    cursor.execute("""create table artist (
        artist_id integer,
        artist_name text,
        primary key (artist_id),
        unique(artist_name collate nocase)
    );""")
    cursor.execute("""create table show (
        show_id integer,
        date text,
        time text,
        fk_artist_id integer,
        description text,
        venue text,
        image_url text,
        event_url text,
        primary key (show_id),
        foreign key (fk_artist_id)
            references artist (artist_id)
            on update cascade
            on delete cascade
            );""")
    db.commit()

start = datetime.datetime.now()

for item in os.listdir('raw_data'):
    one_month_list = json.loads(subprocess.check_output('grep "https://schema.org" raw_data/{}'.format(item), shell=True))
    for show in one_month_list:
        try:
            date = show['startDate'][:10]
            time = show['startDate'][12:]
            artist_name = html.unescape(show['name'].replace("'", "''"))
            show_description = html.unescape(show['description'].replace("'", "''"))
            try:
                location = show['location']['name']
            except KeyError:
                location = "NULL_REMARKABLE_PLACEHOLDER"
            try:
                image = show['image']
            except KeyError:
                image = "NULL_REMARKABLE_PLACEHOLDER"
            try:
                url = show['url']
            except KeyError:
                url = "NULL_REMARKABLE_PLACEHOLDER"
            cursor.execute("insert or ignore into artist (artist_name) values ('{}');".format(artist_name))
            cursor.execute("""
                    insert into show (date, time, fk_artist_id, description, venue, image_url, event_url)
                    values
                    (
                        '{}',
                        '{}',
                        (
                            select artist_id
                            from artist
                            where artist_name = '{}'
                        ),
                        '{}',
                        '{}',
                        '{}',
                        '{}'
                    );
                    """.format(
                        date, 
                        time, 
                        artist_name,
                        show_description, 
                        location, 
                        image, 
                        url
                        )
                    )
            db.commit()
        except sqlite3.OperationalError as e:
            pprint.pprint(show)
            print(e)            
            print("error at", show['name'], show['startDate'])
            break

cursor.close()
db.close()

print("time elapsed during DB loading:", datetime.datetime.now() - start)
