import os
import httpx


def reload_web_api():
    username = 'MaxBulgakov'
    token = os.environ.get("PA_TOKEN")
    host = 'www.pythonanywhere.com'
    domain_name = 'maxbulgakov.pythonanywhere.com'

    with httpx.Client(timeout=30.0) as client:
        response = client.post(
            f'https://{host}/api/v0/user/{username}/webapps/{domain_name}/reload/',
            headers={'Authorization': f'Token {token}'}
        )
        if response.status_code == 200:
            print('Web reloaded')


reload_web_api()