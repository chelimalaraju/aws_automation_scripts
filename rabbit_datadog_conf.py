import yaml
import argparse
 
parser = argparse.ArgumentParser(description='This is a demo script')
parser.add_argument('-u','--username', help='rabbitmq username',required=True)
parser.add_argument('-p','--password',help='rabbitmq password', required=True)
args = parser.parse_args()

data = dict(
    init_config = '',
    instances = dict(
        rabbitmq_api_url = 'http://localhost:15672/api/',
        rabbitmq_user = args.username,
        rabbitmq_pass = args.password
    )
)

with open('/etc/datadog/rabbitmq/conf.yaml', 'w') as outfile:
    yaml.dump(data, outfile, default_flow_style=False)



