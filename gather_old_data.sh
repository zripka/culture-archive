#! /bin/bash

if [ ! -d raw_data ]; then
	mkdir raw_data
fi

curl "https://www.tranzac.org/events/month/2023-04/" > raw_data/2023-04.txt
curl "https://www.tranzac.org/events/month/2023-05/" > raw_data/2023-05.txt
curl "https://www.tranzac.org/events/month/2023-06/" > raw_data/2023-06.txt
curl "https://www.tranzac.org/events/month/2023-07/" > raw_data/2023-07.txt
curl "https://www.tranzac.org/events/month/2023-08/" > raw_data/2023-08.txt
curl "https://www.tranzac.org/events/month/2023-09/" > raw_data/2023-09.txt
curl "https://www.tranzac.org/events/month/2023-10/" > raw_data/2023-10.txt
curl "https://www.tranzac.org/events/month/2023-11/" > raw_data/2023-11.txt
curl "https://www.tranzac.org/events/month/2023-12/" > raw_data/2023-12.txt
curl "https://www.tranzac.org/events/month/2024-01/" > raw_data/2024-01.txt
curl "https://www.tranzac.org/events/month/2024-02/" > raw_data/2024-02.txt
curl "https://www.tranzac.org/events/month/2024-03/" > raw_data/2024-03.txt
curl "https://www.tranzac.org/events/month/2024-04/" > raw_data/2024-04.txt
curl "https://www.tranzac.org/events/month/2024-05/" > raw_data/2024-05.txt
curl "https://www.tranzac.org/events/month/2024-06/" > raw_data/2024-06.txt
