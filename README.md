# haproxy

Ansible role to install and configure HA-Proxy, HA-Proxy is a TCP/HTTP reverse proxy.

## Requirements

This role requires Ansible 2.5 or higher.

Supported platforms:

```yaml
  platforms:
    - name: EL
      versions:
        - 7
```

## Default role variables

| Variable name                            | Required? |  Type  | Description                                                                                                |
|:---------------------------------------- |:---------:|:------:|:---------------------------------------------------------------------------------------------------------- |
| haproxy__pacakge_name                    |    yes    | string | installed package name                                                                                     |
| haproxy__package_state                   |    yes    | string | Package state (present or latest). Default: 'present'                                                      |
| haproxy__user_shell                      |    yes    | string | haproxy user login shell                                                                                   |
| haproxy__config_file                     |    no     | string | path to haproxy config file, if null ansible don\`t generate this config                                   |
| haproxy__config_extra_file               |   no      |  list|  paths to extra haproxy service configuration files, to override haproxy unit
| haproxy__ssl_default_ciphers             |    no     |  list  | Default ssl ciphers                                                                                        |
| haproxy__ssl_default_options             |    no     |  list  | Default ssl options                                                                                        |
| haproxy__stats_timeout                   |    no     | string | The default timeout on the stats socket is set to n seconds.                                               |
| haproxy__tune_ssl_default_dh_param       |    no     |  int   | Sets the maximum size of the Diffie-Hellman                                                                |
| haproxy__stats_socket                    |    no     | string | stats unix socket parameters                                                                               |
| haproxy__log                             |    no     | string | logs servers options                                                                                       |
| haproxy__global_maxconn                  |    yes    |  int   | Specifies the maximal number of concurrent connections that will be sent to all servers                     |
| haproxy__nbproc                          |    no     |  int   | This restricts the list of processes and/or threads on which this listener is allowed to run.              |
| haproxy__default_maxconn                 |    no     |  int   | maxconn" parameter specifies the maximal number of concurrent connections that will be sent to this server |
| haproxy__default_fullconn                |    no     |  int   | Specify at what backend load the servers will reach their maxconn                                          |
| haproxy__default_mode                    |    no     | string | Set the running mode or protocol                                                                           |
| haproxy__default_log                     |    no     | string | Enable per-instance logging of events and traffic.                                                         |
| haproxy__default_timeout_connect         |    no     | string | Set the maximum time to wait for a connection attempt to a server to succeed.                              |
| haproxy__default_timeout_client          |    no     | string | Set the maximum inactivity time on the client side.                                                        |
| haproxy__default_timeout_server          |    no     | string | Set the maximum inactivity time on the server side.                                                        |
| haproxy__default_timeout_queue           |    no     | string | Set the maximum time to wait in the queue for a connection slot to be free                                 |
| haproxy__default_timeout_http_request    |    no     | string | timeout for the client to send a whole request                                                             |
| haproxy__default_timeout_client_fin      |    no     | string | Set the inactivity timeout on the client side for half-closed connections.                                 |
| haproxy__default_timeout_server_fin      |    no     | string | Set the inactivity timeout on the server side for half-closed connections.                                 |
| haproxy__default_timeout_http_keep_alive |    no     | string | Set the maximum allowed time to wait for a new HTTP request to appear                                      |
| haproxy__default_timeout_tunnel          |    no     | string | Set the maximum inactivity time on the client and server side for tunnels.                                 |
| haproxy__default_default_server          |    no     | string | default options added to servers definitions                                                             |
| haproxy__default_error_file              |    no     |  dict  | list of defaults error files                                                                               |
| haproxy__default_options                 |    no     |  list  | list of options in default options                                                                       |
| haproxy__default_crt_base                |    no     | string | default path to certificates                                                                               |
| haproxy__default_retries                 |    no     | string | Set the number of retries to perform on a server after a connection failure                                |
| haproxy__mailers                         |    no     |  dict  | List of defined mailers                                                                                    |
| haproxy__listen                          |    no     |  dict  | Listen of services in listen section                                                                       |
| haproxy__frontend                        |    no     |  dict  | List of frontends                                                                                          |
| haproxy__backends                        |    no     |  dict  | List of backends                                                                                           |
| haproxy__map_files                       |    no     |  dict  | List of map files                                                                                          |
| haproxy__ssl_files                       |    no     |  dict  | list of certificate to upload                                                                              |
| haproxy__resolvers                       |    no     |  dict  | List of resolvers                                                                                          |

`* All variables are described in [defaults/main.yml](defaults/main.yml) file

## Static role variables

| Variable name                      |  Type  | Description                                                      |
|:---------------------------------- |:------:|:----------------------------------------------------------------|
| haproxy__config_path               | string | config path                                                      |
| haproxy__config_name               | string | config file name                                                 |
| haproxy__service_name              | string | service name                                                     |
| haproxy__user                      | string | system user                                                      |
| haproxy__group                     | string | system group                                                     |
| haproxy__chroot                    | string | path to chroot environment                                       |
|haproxy__override_service_file_path | string | path to the file to override haproxy unit                        |
| haproxy__service_command_config    | string | command to start haproxy with, used in unit template(templates)  |
| haproxy__shell_nologin             | string | nologin shell                                                    |

`* All static variables are described in [vars/main.yml](vars/main.yml) file

## Example Playbook

```yaml
    - hosts: all
      become: true
      roles:

      - role: haproxy

```

## License

[Apache License 2.0](LICENSE)

## Support

ZeroDowntime Team <support@zdt.io>

For more information about the project, please visit <https://www.zdt.io/building-blocks/>.
