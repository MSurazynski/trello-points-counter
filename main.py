import requests
import json
import config
import re
import datetime

def update_stats_card(name, desc):
    """
    Updates a card with given name and description in the list with id config.STATS_LIST.
    """

    url = f"https://api.trello.com/1/cards/{config.STATS_CARD}"

    headers = {
        "Accept": "application/json"
    }

    query = {
        'idList': config.STATS_LIST,
        'key': config.API_KEY,
        'token': config.API_TOKEN,
        'name': name,
        'desc': desc,
    }

    response = requests.request(
        "PUT",
        url,
        headers=headers,
        params=query
    )


def get_lists():
    """
    Returns list of lists on the board with given id.
    """

    url = f"https://api.trello.com/1/boards/{config.BOARD_ID}/lists"

    headers = {
        "Accept": "application/json"
    }

    query = {
        'key': config.API_KEY,
        'token': config.API_TOKEN
    }

    response = requests.request(
        "GET",
        url,
        headers=headers,
        params=query
    )

def get_cards():
    """
    Get all cards on the board with given id.
    """
    url = f"https://api.trello.com/1/boards/{config.BOARD_ID}/cards/visible"

    headers = {
        "Accept": "application/json"
    }

    query = {
        'key': config.API_KEY,
        'token': config.API_TOKEN
    }

    response = requests.request(
        "GET",
        url,
        headers=headers,
        params=query
    )

    return response.text

def get_members ():
    """
    Returns list of members of the board with given id.
    """

    url = f"https://api.trello.com/1/boards/{config.BOARD_ID}/members"

    query = {
        'key': config.API_KEY,
        'token': config.API_TOKEN
    }

    response = requests.request(
        "GET",
        url,
        params=query
    )

    members_id_to_name = {}
    members_ids_to_points = {}

    for member in json.loads(response.text):
        members_id_to_name[member.get("id", "")] = member.get("fullName", "")
        members_ids_to_points[member.get("id", "")] = 0

    return members_id_to_name, members_ids_to_points


# Dictionary of members of the board with their points sum
members_id_to_name, members_ids_to_points = get_members()
grand_points_sum = 0
points_on_time = 0
points_on_overdue = 0

# Compute all stats
for card in json.loads(get_cards()):

    # Find point value of the card
    numbers = re.findall(r'\[(\d+)\]', card.get("name", ""))

    # If point values exists, take the first one
    if len(numbers) > 0:
        number = numbers[0]
        grand_points_sum += int(number)
        if card.get("idList", "") == config.ON_TIME_LIST:
            points_on_time += int(number)
            members_ids_to_points[card.get("idMembers")[0]] += int(number)
        elif card.get("idList", "") == config.OVERDUE_LIST:
            points_on_overdue += int(number)


# Print stats
print("Total points:", grand_points_sum)
print(f"On-time points: {points_on_time}, {points_on_time / grand_points_sum * 100 if grand_points_sum > 0 else 0}%")
print(f"Overdue points: {points_on_overdue}, {points_on_overdue / grand_points_sum * 100 if grand_points_sum > 0 else 0}%")

print("\nPoints per member:")

for member_id, points in members_ids_to_points.items():
    print(members_id_to_name[member_id], ":", points)

date_and_time = datetime.datetime.now()

# Update stats card with computed stats
update_stats_card("Statystyki", f"Łączna ilość puntków: {grand_points_sum}\nPunkty zdobyte o czase: {points_on_time}, {points_on_time / grand_points_sum * 100 if grand_points_sum > 0 else 0}%\nPunkty zodbyte po czasie: {points_on_overdue}, {points_on_overdue / grand_points_sum * 100 if grand_points_sum > 0 else 0}%\n\nPunkty zdobyte przez osoby o czasie:\n" + "\n".join([f"{members_id_to_name[member_id]}: {points}" for member_id, points in members_ids_to_points.items()]), f"\nOstatnia aktualizacja: {date_and_time.strftime('%Y-%m-%d %H:%M:%S')}")


