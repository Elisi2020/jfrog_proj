import click
import requests
import json


import configparser


def read_artifactory_from_config(configfile):
    config = configparser.RawConfigParser()
    config.read("config.properties")
    config_dict = dict(config.items("CONFIG"))

    return config_dict["artifactory"]


@click.group()
@click.option(
    "--configfile",
    prompt=True,
    default="config.properties",
    help=" Please insert configuration file location if other then default",
)
@click.option("--username", prompt=True, default="admin")
@click.option("--password", prompt=True, default="9odPOM90quGZZjmdtKXC2w")
@click.pass_context
def main(ctx, username, password, configfile):
    artifactory = read_artifactory_from_config(configfile)
    api = "/api/security/token"

    url = artifactory + api
    data = {"username": "admin", "scope": "member-of-groups:admingroup"}
    response = requests.post(url, auth=(username, password), data=data)
    if response.status_code == 200:
        access_token = json.loads(response.text)["access_token"]
    else:
        print(
            "Failed to Create Access Token status code = {} text ={}".format(
                response.status_code, response.text
            )
        )
        exit(1)

    ctx.obj = {"access_token": access_token}
    ctx.obj.update({"artifactory": artifactory})
    ctx.obj.update({"username": username})
    ctx.obj.update({"password": password})


@main.command()
@click.pass_context
def system_ping(ctx):
    api = "/api/system/ping"
    url = ctx.obj["artifactory"] + api
    response = requests.get(url)
    print("status code = {}".format(response.status_code))
    if response.status_code == 200:
        print(response.text)
    else:
        print(
            "Failed to Ping  status code = {} text ={}".format(
                response.status_code, response.text
            )
        )


@main.command()
@click.pass_context
def system_version(ctx):

    api = "/api/system/version"
    url = ctx.obj["artifactory"] + api
    headers = {"Authorization": "Bearer {}".format(ctx.obj["access_token"])}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print("result = ".format(response.text))
        print(response.text.split(",")[0][1:])
    else:
        print(
            "Failed to Get System Version status code = {} text ={}".format(
                response.status_code, response.text
            )
        )


@main.command()
@click.option("--new_user", prompt=True)
@click.pass_context
def create_user(ctx, new_user):
    api = "/api/security/users/" + new_user
    url = ctx.obj["artifactory"] + api
    params = {}
    params["name"] = new_user
    params["admin"] = "false"
    params["email"] = new_user + "@kuku.com"
    params["password"] = "kukupassword"
    params["Content-Type"] = "application/json"
    headers = {"Authorization": "Bearer {}".format(ctx.obj["access_token"])}
    response = requests.put(url, headers=headers, json=params)
    if response.status_code == 201:
        print("status code = {} text ={}".format(response.status_code, response.text))
    else:
        print(
            "Failed to Create User status code = {} text ={}".format(
                response.status_code, response.text
            )
        )


@main.command()
@click.option("--user_to_delete", prompt=True, help="Insert Username to be deleted")
@click.pass_context
def delete_user(ctx, user_to_delete):
    api = "/api/security/users/" + user_to_delete
    url = ctx.obj["artifactory"] + api
    headers = {"Authorization": "Bearer {}".format(ctx.obj["access_token"])}
    response = requests.delete(url, headers=headers)
    if response.status_code == 200:
        print("status code = {} text ={}".format(response.status_code, response.text))
    else:
        print(
            "Failed to Delete User status code = {} text ={}".format(
                response.status_code, response.text
            )
        )


@main.command()
@click.pass_context
def get_storage_info(ctx):

    api = "/api/storageinfo"
    url = ctx.obj["artifactory"] + api
    headers = {"Authorization": "Bearer {}".format(ctx.obj["access_token"])}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print("status code = {} text ={}".format(response.status_code, response.text))
    else:
        print(
            "Failed to Get Storage Info status code = {} text ={}".format(
                response.status_code, response.text
            )
        )


if __name__ == "__main__":
    main(obj="")
