import yaml

with open('config.yml','w') as yaml_file:
    yaml.dump({
        'web_server': {
            'host': '127.0.0.1',
            'port': 80
        },
        'db_server': {
            'host': '127.0.0.1',
            'port': 3306
        }
    }, yaml_file, default_flow_style=False)

with open('config.yml', 'r') as yaml_file:
    # yaml.load()를 사용할 때 보안상의 이유로 Python 3.6 이후부터는 반드시 Loader를 지정해줘야 함
    data = yaml.load(yaml_file, Loader=yaml.SafeLoader)
    print(data, type(data))
    print(data['web_server']['host'])
    print(data['web_server']['port'])
    print(data['db_server']['host'])
    print(data['db_server']['port'])