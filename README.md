# bloc_01_kayak

Jedha certification bloc 01 Kayak Project

"This project fetches data for hotels, weather conditions, and city information, processing the data into both CSV and DB files. It also identifies top hotels and cities, and presents them on a map of France."

You can watch the presentation video [here](https://share.vidyard.com/watch/hw4PmBhy5DN7gmxykSDjx5?)

You can download the datasets from the following links:
- [French Hotels CSV](https://frenchhotels.s3.eu-west-3.amazonaws.com/frenchhotels.csv)
- [French Hotels DB](https://frenchhotels.s3.eu-west-3.amazonaws.com/french_hotels.db)

Here are some key files in this project and what they do:

- `hotels_fetching.ipynb`: This notebook contains the hotel, weather, and location fetching codes
- `hotels_sql.py`: This script is used to convert data to SQL
- `French_map.ipynb`: This notebook presents French maps with city, weather, and hotel information
- `s3_store.ipynb`: This notebook contains information about using S3. If you encounter any issues uploading to S3, the print commands in this notebook can help identify the problem.
