import os

from jinja2 import Environment, FileSystemLoader

# Capture our current directory
THIS_DIR = os.path.dirname(os.path.abspath(__file__))

def get_services():
    services = []
    with open('service_port_mapping_atl1.txt') as f:
        for line in f:
            services.append(line.split()[0])
    return services

service_port = []
with open('service_port_mapping_atl1.txt', 'r') as f:
    for line in f:
        service = line.split()[0]
        port = line.split()[1]
        service_port.append((service, port))

#print service_port

def print_html_doc():
    # Create the jinja2 environment.
    # Notice the use of trim_blocks, which greatly helps control whitespace.
    j2_env = Environment(loader=FileSystemLoader(THIS_DIR),
                         trim_blocks=True)
    print j2_env.get_template('template.conf').render(
        services=get_services(), fc='atl1', fc_ip='10.159.164.45', service_port=service_port
        # services=['customerOrderService', 'webDialogPickModuleService']
    )

if __name__ == '__main__':
    print_html_doc()
    #print get_services()


