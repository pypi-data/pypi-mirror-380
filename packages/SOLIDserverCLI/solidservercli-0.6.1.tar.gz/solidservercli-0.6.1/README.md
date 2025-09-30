# SOLIDserver cli

This package contains a command to manage the SOLIDserver and its objects.

## install

* in a virtual environment
* install the package: `pip install SOLIDserverCLI`
* configure the access to the SOLIDserver by creating a file named `sds.ini` which contains:

```text
[server]
name = server
token_id = xxx
token_key = yyy
```

## Usage

The command `sds` can be used directly from the shell. It is organized with commands and subcommands, you can at each level add the `--help` option to get more information.

By using the `--json` at the top level, all outputs will be in the json format, providing the ability to use jq to manipulate the result.

Examples:

```text
> sds server status
SOLIDserver: sds-test.intranet, authentication: token, version: 8.4.2, timeout: 10s

> sds --json server status
{"host": "sds-test.intranet", "auth_method": "token", "timeout": 10, "version": "8.4.2", "user": "ukn (token)"}
```

```
sds ipam space create test-sds-cli --description "only for testing purposes"
sds --json ipam space info test-sds-cli

sds ipam network create 192.168.0.0/16 --name "top" --space test-sds-cli --block --meta "made_with='cli'"
sds --json ipam network info 192.168.0.0/16 --space test-sds-cli

sds ipam network create 192.168.16.0/20 --space test-sds-cli --name middle
sds ipam network create 192.168.18.0/24 --space test-sds-cli --terminal --parent middle --name bottom

sds ipam ip create 192.168.18.12 --name device01 --macaddress 0e:01:02:03:04:05 --space test-sds-cli
sds --json ipam ip info 192.168.18.12 --space test-sds-cli

sds ipam ip delete 41402_to_change
```

## Commands

```text
├─ server
│  └─ status
├─ ipam
│  ├─ space
│  │  ├─ create
│  │  ├─ info
│  │  ├─ update
│  │  ├─ delete
│  │  └─ list
│  ├─ ip
│  │  ├─ create
│  │  ├─ delete
│  │  └─ info
│  └─ network
│     ├─ create
│     ├─ list
│     └─ info
└─ dns
   └─ rr
      ├─ create
      └─ info
```