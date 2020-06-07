import click
import requests
import json



import configparser


def read_artifactory_from_config():
    config = configparser.RawConfigParser()
    config.read('config.properties')
    config_dict = dict(config.items('CONFIG'))
    print('config_dict {}'.format(config_dict['artifactory']))
    return(config_dict['artifactory'])


@click.group()
#@click.option('--username',prompt=True)
#@click.option('--password',prompt=True,hide_input=True)
@click.option('--username',default = 'admin')
@click.option('--password',default = '9odPOM90quGZZjmdtKXC2w')
@click.pass_context
def main(ctx,username,password):
    artifactory = read_artifactory_from_config()
    print(username,password)
    #create token using username/password
#    artifactory = "https://esiesel.jfrog.io/artifactory"  # artifactory URL
    print('artifactory ='.format(artifactory))
    api = "/api/security/token"

    url = artifactory + api
    response = requests.get(url, auth=(username, password))
    print('status code = {}'.format(response.status_code))
    if response.status_code == 200:
#        auth_dic = json.loads(response.text)
        token_id = json.loads(response.text)['tokens'][0]['token_id']
#        print('token_id = {}'.format(auth_dic['tokens'][0]['token_id']))
        print('tokenid = {}'.format(token_id))

    else:
        print(" Can't create token : Sorry: Please try again later")
        exit(1)




    ctx.obj = {'token_id': token_id}
    ctx.obj.update({'artifactory' : artifactory})
    ctx.obj.update({'username': username})
    ctx.obj.update({'password': password})
    print('ctx = tokenid {}'.format(ctx.obj['token_id']))

@main.command()
@click.pass_context
def system_ping(ctx):
    api = '/api/system/ping'
    url = ctx.obj['artifactory'] + api
    print('in systemping url = {}'.format(url))
    headers = { 'Authorization' : 'Bearer' + ctx.obj['token_id']}
    response = requests.get(url, headers=headers )
#    response = requests.get(url, auth = (ctx.obj['username'] , ctx.obj['password']) )
    print('status code = {}'.format(response.status_code))
    if response.status_code == 200:
        print('OK')
    else:
        print(" Ping Error: Please try again later")

@main.command()
@click.pass_context
def system_version(ctx):

    api = '/api/system/version'
    url = ctx.obj['artifactory'] + api
    print('in systemping url = {}'.format(url))
    #headers = {'Authorization': 'Bearer' + ctx.obj['token_id']}
    #    response = requests.get(url, headers=headers )
    response = requests.get(url, auth=(ctx.obj['username'], ctx.obj['password']))
    print('status code = {}'.format(response.status_code))
    if response.status_code == 200:
        print('result = '.format(response.text))
        print(response.text.split(',')[0][1:])
    else:
        print(" System Version Api Error: Please try again later")
        exit(1)

@main.command()
@click.option('--new_user',prompt=True)
@click.pass_context
def create_user(ctx,new_user):
    api = "/api/security/users/" + new_user
    url = ctx.obj['artifactory'] + api
    params = {}
    params["name"] = new_user
    params["admin"] = "false"
    params["email"] = new_user + "@kuku.com"
    params["password"] = "kukupassword"
    params["Content-Type"] = "application/json"
    response = requests.put(url, auth=(ctx.obj['username'], ctx.obj['password']), json =params)
    if response.status_code == 201:
        print('status code = {} text ={}'.format(response.status_code, response.text))
    else:
        print('Failed to Create User status code = {} text ={}'.format(response.status_code, response.text))

@main.command()
@click.option('--user_to_delete',prompt=True, help ='Insert Username to be deleted')
@click.pass_context
def delete_user(ctx,user_to_delete):
    api = "/api/security/users/" + user_to_delete
    url = ctx.obj['artifactory'] + api

    response = requests.delete(url, auth=(ctx.obj['username'], ctx.obj['password']))
    if response.status_code == 200:
        print('status code = {} text ={}'.format(response.status_code, response.text))
    else:
        print('Failed to Delete status code = {} text ={}'.format(response.status_code, response.text))

@main.command()
@click.pass_context
def get_storage_info(ctx):

    api = '/api/storageinfo'
    url = ctx.obj['artifactory'] + api
    print('in systemping url = {}'.format(url))
    #headers = {'Authorization': 'Bearer' + ctx.obj['token_id']}
    #    response = requests.get(url, headers=headers )
    response = requests.get(url, auth=(ctx.obj['username'], ctx.obj['password']))
    if response.status_code == 200:
        print('status code = {} text ={}'.format(response.status_code, response.text))
    else:
        print('Failed to Get Storage Info status code = {} text ={}'.format(response.status_code, response.text))


if __name__ == '__main__':
    main(obj="")
