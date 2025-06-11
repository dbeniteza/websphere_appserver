# iim

The `iim` role will install the IBM Installation Manager agent. See `iim_package` module for installing packages

## Requirements

None

## Role Variables

| Property Name           | Default value                                         |
| -------------------     | ----------------------------------------------------- |
| `iim_agent_version`     | `1.9.2002.20220323_1321`                              |
| `iim_install_path`      | `/opt/IBM/InstallationManager`                        |
| `iim_install_user`      | `wasadmin`                                            |
| `iim_install_cmd`       | `installc`                                            |
| `iim_remote_repo`       | `(empty string)` Set this if license and installer is being downloaded from network repository (repository.config file)|
| `iim_download_url`      | Set this if license and installer is being downloaded from a http server|
| `iim_download_header`   | Use this in conjunction with `iim_download_url` |
| `iim_installer_path`    | Set this to your downloaded installers filepath if copying from local. Set to remote filepath if downloading installers|
| `iim_offering_id`       | `com.ibm.cic.agent`                                   |
| `iim_features`          | `agent_core,agent_jre`                                |


## Dependencies

None

## Example Playbook

```
- name: Install IBM Installation Manager
  hosts: servers
  roles:
    - dbeniteza.websphere_appserver.iim
```

## IBM Installation Manager Documentation
- [Installation Manager and Packaging Utility download documents](https://www.ibm.com/support/pages/installation-manager-and-packaging-utility-download-documents)
- [System Requirements for IBM Installation Manager and Packaging Utility](https://www.ibm.com/support/pages/system-requirements-ibm-installation-manager-and-packaging-utility)
- [Commands to install Installation Manager](https://www.ibm.com/docs/en/installation-manager/current?topic=group-commands-install-installation-manager)
- [Installation Manager command-line arguments for silent mode](https://www.ibm.com/docs/en/installation-manager/current?topic=mode-installation-manager-command-line-arguments-silent)
- [Response files](https://www.ibm.com/docs/en/installation-manager/current?topic=mode-response-files)
- [Response file variables](https://www.ibm.com/docs/en/installation-manager/current?topic=files-response-file-variables)
- [Sample response file: Installing Installation Manager and packages](https://www.ibm.com/docs/en/installation-manager/current?topic=files-sample-response-file-installing-installation-manager-packages)
- [Searching for updates in silent mode](https://www.ibm.com/docs/en/installation-manager/current?topic=keys-searching-updates-in-silent-mode)
- [IBM Installation Manager Repositories](https://www.ibm.com/docs/en/installation-manager/current?topic=files-repositories)

## License

MIT
