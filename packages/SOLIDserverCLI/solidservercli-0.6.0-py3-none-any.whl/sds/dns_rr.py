import typer
from typing_extensions import Annotated
from typing import List, Optional

from rich import print
from rich.text import Text

import ipaddress
import uuid
import json
import re
import time

from SOLIDserverRest import *
from SOLIDserverRest import adv as sdsadv

import sds.config as config
from sds.config import log
import sds.classparams as cp

app = typer.Typer()


def convert_dict(dns_rr: sdsadv.DNS_record = None) -> dict:
    """convert the DNS record adv object to a dictionary structure
       for easy output as json

    Args:
        dns_rr (sdsadv.DNS_record, optional): record object to convert.

    Returns:
        dict: the dictionary object
    """
    if dns_rr:
        _j = dns_rr.__dict__

        # print(_j)
        _jr = {
            'id': _j['myid'],
            'name': _j['name'],
            'server': _j['dns_server'].name,
            'zone': _j['zone'].name,
            'ttl': _j['ttl'],
            'type': _j['rr_type'],
            'values': _j['values']
        }

        if _j['dns_view']:
            _jr['view'] = _j['dns_view'].name

        _cparam = {}
        for _k, _v in _j['_ClassParams__class_params'].items():
            _cparam[_k] = _v

        for _k, _v in _j['_ClassParams__private_class_params'].items():
            _cparam[_k] = _v

        if len(_cparam) > 0:
            _jr['class_params'] = _cparam

        return _jr

    return {}


@app.command()
def create(fqdn: Annotated[str,
                           typer.Argument(
                               help='fqdn')],

           server: Annotated[str,
                             typer.Option(help='server or smart name')],




           val: Annotated[Optional[List[str]],
                          typer.Option(help='values of the record, can be provided multiple times')],

           rr_type: Annotated[str,
                              typer.Option('--type',
                                           help='the type of the record')
                              ] = "A",

           ttl: Annotated[int,
                          typer.Option(help='TTL in seconds')] = 3600,

           view: Annotated[str,
                           typer.Option(help='view to create the record in')] = "",

           meta: Annotated[str,
                           typer.Option(
                               help='class params: a=\'1\',b1=\'foo bar\' ')
                           ] = ""):
    _start_time = time.time()

    dns = sdsadv.DNS(name=server, sds=config.vars['sds'])
    try:
        dns.refresh()
    except:
        log.critical("DNS server or Smart not found")
        exit()

    dns_rr = sdsadv.DNS_record(sds=config.vars['sds'],
                               name=fqdn,
                               rr_type=rr_type)

    dns_rr.set_values(val)

    dns_rr.set_dns(dns)

    dns_rr.set_ttl(ttl)

    if view != "":
        dns_view = sdsadv.DNS_view(sds=config.vars['sds'],
                                   name=view)

        dns_view.set_dns(dns)
        try:
            dns_view.refresh()
        except:
            log.critical("DNS view not found")
            exit()

        dns_rr.set_view(dns_view)

    if meta != "":
        cp.add_classparams_from_string(dns_rr, meta)

    try:
        dns_rr.create()
    except SDSDNSError as e:
        log.error(f"[red]create failed[/red] {e.message}")


@app.command()
def info(fqdn: Annotated[str,
                         typer.Argument(
                             help='fqdn')],

         server: Annotated[str,
                           typer.Option(help='server or smart name')],

         view: Annotated[str,
                         typer.Option(help='view to create the record in')] = "",

         rr_type: Annotated[str,
                            typer.Option('--type',
                                         help='the type of the record')
                            ] = "A",
         ):

    _start_time = time.time()

    dns = sdsadv.DNS(name=server, sds=config.vars['sds'])
    try:
        dns.refresh()
    except:
        log.critical("DNS server or Smart not found")
        exit()

    dns_rr = sdsadv.DNS_record(sds=config.vars['sds'],
                               name=fqdn,
                               rr_type=rr_type)

    dns_rr.set_dns(dns)

    if view != "":
        dns_view = sdsadv.DNS_view(sds=config.vars['sds'],
                                   name=view)

        dns_view.set_dns(dns)
        try:
            dns_view.refresh()
        except:
            log.critical("DNS view not found")
            exit()

        dns_rr.set_view(dns_view)

    try:
        dns_rr.refresh()
    except SDSError as e:
        log.error(f"[red]refresh failed[/red] {e.message}")
        exit()

    if not dns_rr:
        exit()

    if config.vars['json_output']:
        _jr = convert_dict(dns_rr)
        _jr['_elapsed'] = round(time.time()-_start_time, 4)
        print(json.dumps(_jr))
    else:
        text = f"DNS record: [green]{dns_rr.name}[/green]"
        if dns_rr.myid and dns_rr.myid != -1:
            text += f" \[#{dns_rr.myid}]"

        if dns_rr.zone:
            text += f"\n server={dns_rr.dns_server.name}"
            if dns_rr.zone:
                text += f"\n zone={dns_rr.zone.name}"

        text += f"\n type={dns_rr.rr_type}"

        if dns_rr.rr_type:
            text += f" {dns_rr.rr_type}"
            if dns_rr.rr_type in ['A', 'AAAA', 'CNAME', 'DNAME']:
                if '1' in dns_rr.values:
                    text += f"={dns_rr.values['1']}"
            elif dns_rr.rr_type == 'TXT':
                if '1' in dns_rr.values:
                    text += f"='{dns_rr.values['1']}'"
            elif dns_rr.rr_type == 'MX':
                if '1' in dns_rr.values and '2' in dns_rr.values:
                    text += f"='{dns_rr.values['2']} [{dns_rr.values['1']}]'"
            elif dns_rr.rr_type == 'SRV':
                if (
                    '1' in dns_rr.values and
                    '2' in dns_rr.values and
                    '3' in dns_rr.values and
                    '4' in dns_rr.values
                ):
                    text += f"='p={dns_rr.values['1']}"
                    text += f", w={dns_rr.values['2']}"
                    text += f", {dns_rr.values['4']}:{dns_rr.values['3']}"

        text += f"\n TTL={dns_rr.ttl}"

        if dns_rr.class_name and dns_rr.class_name != "":
            text += f", class={dns_rr.class_name}"

        _jr = convert_dict(dns_rr)

        if 'class_params' in _jr:
            text += "\n meta=" + json.dumps(_jr['class_params'])

        log.info(text)


if __name__ == "__main__":
    app()
