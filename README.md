# trello-points-counter
A simple python script that computes card points statistics for one trello board.

It searches for pattern in the card title
`\[\d+\]`

It computes total points, points on time, points overdue and points per member. It also updates a card with the computed stats.

## Usage
1. Install dependencies: `pip install -r requirements.txt`
2. Update `config.py` with your Trello API key, token, and the IDs of the lists and card you want to use for stats.
3. Run the script: `python main.py`
4. The script will print the total points, points on time, points overdue, and points per member. It will also update the stats card with the computed stats.

## Note
Script assumes a `config.py` file with the following fields:
- `API_KEY`: Your Trello API key
- `API_TOKEN`: Your Trello API token
- `BOARD_ID`: The ID of the Trello board you want to analyze
- `ON_TIME_LIST`: The ID of the list where on-time cards are located
- `OVERDUE_LIST`: The ID of the list where overdue cards are located
- `STATS_LIST`: The ID of the list where the stats card is located
- `STATS_CARD`: The ID of the card where the stats will be updated