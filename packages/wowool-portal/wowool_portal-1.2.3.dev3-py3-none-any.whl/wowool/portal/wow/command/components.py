from argparse import Namespace

from wowool.portal.client.portal import Portal


def command(arguments: Namespace):
    portal = Portal(host=arguments.host, api_key=arguments.api_key)
    components = Components(portal=portal)
    for component in components:
        print(f"{component.name:<35}| {component.type:<8}| {component.description}")
