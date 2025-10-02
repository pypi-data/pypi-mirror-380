import click
import subprocess
import json
import os
from pathlib import Path
import requests
import re
import uuid

@click.group(name='telemetry')
def telemetry_commands():
    '''OASEES Telemetry Management Utilities'''
    pass

def get_telemetry_api():
    try:
        tel_svc = subprocess.run(['kubectl','get','svc','oasees-telemetry-api-svc','-o','jsonpath={.spec.clusterIP}'], 
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        tel_ip = tel_svc.stdout.strip()
        return f"http://{tel_ip}:5005"
    except subprocess.CalledProcessError as e:
        click.secho(f"Error getting Telemetry api service: {e.stderr}", fg="red", err=True)
        return None


def sanitize_k8s_name(name):
    """Sanitize names for Kubernetes (lowercase, replace underscores with hyphens, remove invalid chars)"""
    sanitized = name.lower()
    sanitized = re.sub(r'_', '-', sanitized)
    sanitized = re.sub(r'[^a-z0-9-]', '', sanitized)
    sanitized = re.sub(r'^-+|-+$', '', sanitized)
    return sanitized


def get_thanos_endpoint():
    result = subprocess.run(['kubectl', 'get', 'service', 'thanos-query', '-n', 'default', '-o', 'jsonpath={.spec.clusterIP}'], 
                        capture_output=True, text=True)
    cluster_ip = result.stdout.strip()

    url = f"http://{cluster_ip}:9090/api/v1/query"

    return url


@telemetry_commands.command()
def metrics_index():
    '''List All metric names'''

    metrics = []

    url = get_thanos_endpoint()
    params = {'query': '{__name__=~"oasees_.*"}'}
    response = requests.get(url, params=params)
    data = response.json()

    metric_names = set()
    for result in data['data']['result']:
        metric_name = result['metric'].get('metric_index')
        if metric_name:
            metric_names.add(metric_name)

    for name in sorted(metric_names):
        metrics.append(name)

    for m in metrics:
        print(m)

    return metrics

@telemetry_commands.command()
@click.option('--index', '-i', help='Name of the metric to search for')
def metrics_list(index):
    '''Get All metrics by name'''

    url = get_thanos_endpoint()
    params = {'query': f'{{__name__=~"oasees_.*", metric_index="{index}"}}'}
    response = requests.get(url, params=params)
    data = response.json()

    metric_names = set()
    by_source_dict = {}
    for result in data['data']['result']:
        source = result['metric'].get('source')


        oasees_metric = result['metric'].get('__name__').replace("oasees_","")

        if oasees_metric not in by_source_dict:
            by_source_dict[oasees_metric] = set()

        by_source_dict[oasees_metric].add(source)


        if oasees_metric:
            metric_names.add(oasees_metric)

    for m in by_source_dict:
        print(m,"[",*by_source_dict[m],"]")


@telemetry_commands.command()
@click.argument('metrics', nargs=-1, required=True)
def check_metrics(metrics):
    '''Check metrics with optional thresholds'''
    
    import re, requests
    
    pattern = r'(\w+)\[(.*?)\]'
    threshold_pattern = r'(\w+)\[(\w+)\](>=|<=|>|<|=)(\d+(?:\.\d+)?)'
    
    queries = []
    thresholds = {}
    
    for arg in metrics:
        if re.match(threshold_pattern, arg):
            match = re.match(threshold_pattern, arg)
            metric, source, op, thr = match.groups()
            thresholds[f"{metric}_{source}"] = (op, float(thr))
        else:
            match = re.match(pattern, arg)
            if match:
                index, metrics_str = match.groups()
                for m in metrics_str.split(','):
                    if m.strip():
                        queries.append((index, f"oasees_{m.strip()}"))
    
    url = get_thanos_endpoint()
    
    for index, metric in queries:
        query = f'{metric}{{metric_index="{index}"}}'
        response = requests.get(url, params={"query": query}).json()
        
        for result in response.get("data", {}).get("result", []):
            source = result.get("metric", {}).get("source", "")
            value = float(result.get("value", ["", "0"])[1])
            
            key = f"{metric.replace('oasees_', '')}_{source}"
            if key in thresholds:
                op, thr = thresholds[key]
                ops = {'>': lambda x, y: x > y, '<': lambda x, y: x < y, '>=': lambda x, y: x >= y, 
                       '<=': lambda x, y: x <= y, '=': lambda x, y: x == y}
                if ops[op](value, thr):
                    print(f"{source} | {metric.replace('oasees_', '')} = {value} | {op} {thr}")
            else:
                print(f"{source} | {metric.replace('oasees_', '')} = {value}")


@telemetry_commands.command()
def gen_oasees_collector():
    """Generate the OASEES collector script"""
    
    script_content = '''import socketio
import requests
import time
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-m', '--metric-index', required=True, help='Metric index')
parser.add_argument('-s', '--source', required=True, help='Source identifier')
parser.add_argument('-o', '--oasees-endpoint', required=True, help='OASEES endpoint URL')
parser.add_argument('-e', '--source-endpoint', required=True, help='Source endpoint URL')
parser.add_argument('-i', '--scrape-interval', type=int, default=1, help='Scrape interval in seconds (default: 1)')

args = parser.parse_args()

METRIC_INDEX = args.metric_index
SOURCE = args.source
OASEES_ENDPOINT = 'http://{}:30080'.format(args.oasees_endpoint)
SOURCE_ENDPOINT = args.source_endpoint
SCRAPE_INTERVAL = args.scrape_interval

sio = socketio.Client()

@sio.on('metric_pushed')
def on_response(data):
    print(f"Success: {data}")

@sio.on('error')
def on_error(data):
    print(f"Error: {data}")

sio.connect(OASEES_ENDPOINT)

while True:
    r = requests.get(SOURCE_ENDPOINT)
    data = r.json()
    data.update({'metric_index': METRIC_INDEX, 'source': SOURCE})
    sio.emit('push_metric', data)
    time.sleep(SCRAPE_INTERVAL)
'''
    
    click.echo(script_content)


@telemetry_commands.command()
@click.option('--metric-index','-i',required=True, help='Metric index')
@click.option('--source','-s',required=True, help='Source identifier')
@click.option('--source-endpoint','-se',required=True, help='Source endpoint URL')
@click.option('--scrape-interval','-si',type=int, default=1, help='Scrape interval in seconds (default: 1)')
def deploy_collector(metric_index, source, source_endpoint, scrape_interval):
   """Deploy OASEES metric collector"""
   
   import tempfile
   import os
   import subprocess
   import re
   
   def sanitize_k8s_name(name):
       """Sanitize names for Kubernetes (lowercase, replace underscores with hyphens, remove invalid chars)"""
       sanitized = name.lower()
       sanitized = re.sub(r'_', '-', sanitized)
       sanitized = re.sub(r'[^a-z0-9-]', '', sanitized)
       sanitized = re.sub(r'^-+|-+$', '', sanitized)
       return sanitized
   
   # Get OASEES Telemetry API endpoint
   oasees_endpoint = get_telemetry_api()
   if not oasees_endpoint:
       return
   
   # Generate unique names
#    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
   sanitized_source = sanitize_k8s_name(source)
   
   pod_name = f"collector-{sanitized_source}"
   configmap_name = f"collector-script-{sanitized_source}"
   
   # Display configuration
   click.echo("Deploying OASEES Collector with the following configuration:")
   click.echo(f"  Metric Index: {metric_index}")
   click.echo(f"  Source: {source}")
   click.echo(f"  OASEES Endpoint: {oasees_endpoint}")
   click.echo(f"  Source Endpoint: {source_endpoint}")
   click.echo(f"  Scrape Interval: {scrape_interval} seconds")
   click.echo(f"  Pod Name: {pod_name}")
   click.echo()
   
   # Python collector script content
   collector_script = '''import socketio
import requests
import time
import os

# Get configuration from environment variables
METRIC_INDEX = os.environ['METRIC_INDEX']
SOURCE = os.environ['SOURCE']
OASEES_ENDPOINT = os.environ['OASEES_ENDPOINT']
SOURCE_ENDPOINT = os.environ['SOURCE_ENDPOINT']
SCRAPE_INTERVAL = int(os.environ.get('SCRAPE_INTERVAL', '1'))

print(f"Starting collector with config:")
print(f"  Metric Index: {METRIC_INDEX}")
print(f"  Source: {SOURCE}")
print(f"  OASEES Endpoint: {OASEES_ENDPOINT}")
print(f"  Source Endpoint: {SOURCE_ENDPOINT}")
print(f"  Scrape Interval: {SCRAPE_INTERVAL}s")

sio = socketio.Client()

@sio.on('metric_pushed')
def on_response(data):
   print(f"Success: {data}")

@sio.on('error')
def on_error(data):
   print(f"Error: {data}")

@sio.on('connect')
def on_connect():
   print("Connected to OASEES")

@sio.on('disconnect')
def on_disconnect():
   print("Disconnected from OASEES")

try:
   print(f"Connecting to {OASEES_ENDPOINT}...")
   sio.connect(OASEES_ENDPOINT)
   
   while True:
       try:
           print(f"Scraping data from {SOURCE_ENDPOINT}...")
           r = requests.get(SOURCE_ENDPOINT)
           data = r.json()
           data.update({'metric_index': METRIC_INDEX, 'source': SOURCE})
           print(f"Pushing data: {data}")
           sio.emit('push_metric', data)
           time.sleep(SCRAPE_INTERVAL)
       except requests.exceptions.RequestException as e:
           print(f"Error scraping data: {e}")
           time.sleep(SCRAPE_INTERVAL)
       except Exception as e:
           print(f"Error processing data: {e}")
           time.sleep(SCRAPE_INTERVAL)
           
except Exception as e:
   print(f"Failed to connect to OASEES: {e}")
   exit(1)
'''

   # Create YAML content
   yaml_content = f"""# ConfigMap with collector script
apiVersion: v1
kind: ConfigMap
metadata:
 name: {configmap_name}
 labels:
   app: oasees-collector
   source: {sanitized_source}
   tag: collector
data:
 collector.py: |
{chr(10).join('    ' + line for line in collector_script.split(chr(10)))}

---
# Collector Pod
apiVersion: v1
kind: Pod
metadata:
 name: {pod_name}-{uuid.uuid4()}
 labels:
   app: oasees-collector
   source: {sanitized_source}
   tag: collector
spec:
 nodeSelector:
   kubernetes.io/hostname: {sanitized_source}
 restartPolicy: Always
 containers:
 - name: collector
   image: python:3.9-slim
   command: ["sh", "-c"]
   args:
   - |
     pip install python-socketio requests &&
     python /app/collector.py
   env:
     - name: METRIC_INDEX
       value: "{metric_index}"
     - name: SOURCE
       value: "{source}"
     - name: OASEES_ENDPOINT
       value: "{oasees_endpoint}"
     - name: SOURCE_ENDPOINT
       value: "{source_endpoint}"
     - name: SCRAPE_INTERVAL
       value: "{scrape_interval}"
   volumeMounts:
   - name: script-volume
     mountPath: /app
 volumes:
 - name: script-volume
   configMap:
     name: {configmap_name}
"""

   # Apply to Kubernetes
   temp_file_path = None
   try:
       with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as temp_file:
           temp_file.write(yaml_content)
           temp_file_path = temp_file.name
       
       click.echo("Applying Kubernetes configuration...")
       result = subprocess.run(['kubectl', 'apply', '-f', temp_file_path], 
                             capture_output=True, text=True, check=True)
       
       click.secho("Collector deployment completed successfully!", fg="green")
       
   except subprocess.CalledProcessError as e:
       click.secho("❌ Deployment failed!", fg="red")
       click.secho(f"Error: {e.stderr}", fg="red")
   finally:
       # Clean up temporary file
       if temp_file_path and os.path.exists(temp_file_path):
           os.unlink(temp_file_path)

@telemetry_commands.command()
@click.argument('config_file', type=click.Path(exists=True))
def configure_agents(config_file):
    '''Configure agents by providing the config.json'''
    
    import subprocess
    import json
    import requests
    
    try:
        # Read the config file
        with open(config_file, 'r') as f:
            config_data = json.load(f)
        
        # Run kubectl command to get pods with oasees-agent component label
        cmd = [
            'kubectl', 'get', 'pods', 
            '-l', 'component=oasees-agent',
            '-o', 'json'
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        
        # Parse the JSON output
        pods_data = json.loads(result.stdout)
        
        # Extract pod IPs and node names
        pod_data = []
        for pod in pods_data.get('items', []):
            pod_ip = pod.get('status', {}).get('podIP')
            node_name = pod.get('spec', {}).get('nodeName')
            if pod_ip and node_name:
                pod_data.append((pod_ip, node_name))

        

        # Send config to each pod

        for ip, node_name in pod_data:
            _config = json.loads(json.dumps(config_data))
            for k in config_data['actions_map'].keys():
                
                if('localhost' in config_data['actions_map'][k]['action_endpoint']):
                   

                    cmd2 = [
                        'kubectl','get', 'pods',
                        '--field-selector', f'spec.nodeName={node_name}',
                        '-l', 'component=oasees-app,oasees-action=true',
                        '-o', 'json'
                    ]

                    cmd2_alt = [
                        'kubectl','get', 'pods',
                        '--field-selector', f'spec.nodeName={node_name}',
                        '-l', 'component=oasees-app',
                        '-o', 'json'
                    ]


                    result = subprocess.run(cmd2, capture_output=True, text=True, check=True)
                    pd = json.loads(result.stdout)
                    if not pd.get('items',[]):
                        result = subprocess.run(cmd2_alt, capture_output=True, text=True, check=True)
                        pd = json.loads(result.stdout)

                    for pod in pd.get('items', []):
                        pod_ip = pod.get('status', {}).get('podIP')
                        labels = pod.get('metadata', {}).get('labels', {})
                        if(not labels.get('oasees-ui')):
                            _config['actions_map'][k]['action_endpoint'] = _config['actions_map'][k]['action_endpoint'].replace('localhost',pod_ip)

            
            try:
                url = f"http://{ip}:5100/configure"
                response = requests.post(url, json=_config, timeout=10)
                
                if response.status_code == 200:
                    print(f"Successfully configured agent on {node_name}")
                else:
                    try:
                        error_msg = response.json().get('message', 'Unknown error')
                        print(f"Failed to configure agent on {node_name}: HTTP {response.status_code} - {error_msg}")
                    except:
                        print(f"Failed to configure agent on {node_name}: HTTP {response.status_code}")
                    
            except requests.exceptions.RequestException as e:
                print(f"Error sending config to agent on {node_name}: {e}")
            
    except FileNotFoundError:
        print(f"Config file {config_file} not found")
    except json.JSONDecodeError as e:
        print(f"Error parsing config file: {e}")
    except subprocess.CalledProcessError as e:
        print(f"Error running kubectl command: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


@telemetry_commands.command()
def gen_config():
    '''Generate config.json file with predefined configuration'''
    
    import json
    
    config = {
        "metric_index": " ",
        "propose_on": {
            "events": [
                " "                
            ],
            "proposal_contents": [
               " "
            ],
            "positive_vote_on": [
                " "
            ]
        },
        "actions_map":{
            " ":{
                "action_endpoint": "",
                "args":{

                }
            }
        }    
    }
    
    try:
        with open('config.json', 'w') as f:
            json.dump(config, f, indent=4)
        print("config.json generated")
    except Exception as e:
        print(f"Error generating config.json: {e}")

@telemetry_commands.command()
def get_collectors():
    """Get all collector pods with their deployment nodes"""
    
    try:
        print("Fetching collector information...")
        
        # Run kubectl command
        result = subprocess.run([
            "kubectl", "get", "pods",
            "-o", "wide",
            "-l", "tag=collector"
        ], capture_output=True, text=True, check=True)
        
        # Parse the output
        lines = result.stdout.strip().split('\n')
        
        if len(lines) <= 1 or lines[0].startswith('No resources found'):
            print("No collector pods found.")
            return
        
        collectors = {}
        
        for line in lines:
            if line.startswith('NAME'):
                continue
            
            # Parse pod info: name, ready, status, restarts, age, ip, node
            parts = line.split()
            if len(parts) >= 7:
                pod_name = parts[0]
                status = parts[2]
                node = parts[6]
                collectors[pod_name] = {'status': status, 'node': node}
        
        # Output formatted results
        print("\n" + "="*80)
        print("COLLECTORS DEPLOYMENT SUMMARY")
        print("="*80)
        
        if collectors:
            for pod_name, info in collectors.items():
                print(f"Collector: {pod_name:<30} | Status: {info['status']:<10} | Node: {info['node']}")
        else:
            print("No collector pods found.")
        
        print("="*80)
        print("To delete a collector, use:")
        print("  oasees-sdk telemetry delete-collector <collector-name>")
        print("="*80)
        
    except subprocess.CalledProcessError as e:
        print(f"Error running kubectl command: {e}")
        print(f"Make sure kubectl is installed and cluster is accessible")
    except Exception as e:
        print(f"Error processing collector information: {e}")


@telemetry_commands.command()
@click.argument('collector_name')
def delete_collector(collector_name):
    """Delete a collector pod by name"""
    
    try:
        print(f"Deleting collector pod: {collector_name}")
        
        # Run kubectl delete command with --force flag
        result = subprocess.run([
            "kubectl", "delete", "pod", collector_name, "--force"
        ], capture_output=True, text=True, check=True)
        
        if result.stdout.strip():
            print(f"✓ Successfully deleted collector: {collector_name}")
            
    except subprocess.CalledProcessError as e:
        print(f"✗ Error deleting collector '{collector_name}': {e}")
        if e.stderr:
            print(f"Error details: {e.stderr.strip()}")
        
        # Check if pod exists
        try:
            check_result = subprocess.run([
                "kubectl", "get", "pod", collector_name
            ], capture_output=True, text=True)
            
            if check_result.returncode != 0:
                print(f"Pod '{collector_name}' not found. Use 'oasees-sdk telemetry get-collectors' to see available collectors.")
            
        except Exception:
            pass  # Ignore errors in the check
            
    except Exception as e:
        print(f"✗ Unexpected error deleting collector '{collector_name}': {e}")