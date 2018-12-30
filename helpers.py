def dict_creator(json):
    """Format the json to a dict with specific items."""

    response_dict = {
        'numero-do-voo': json.get('flight_number'),
        'nome-da-missao': json.get('mission_name'),
        'ano-de-lancamento': json.get('launch_year'),
        'data-lancamento-utc': json.get('launch_date_utc'),
        'nome-foguete': json.get('rocket').get('rocket_name'),
        'plataforma-de-lancamento': json.get('launch_site').get('site_name'),
    }

    return response_dict
