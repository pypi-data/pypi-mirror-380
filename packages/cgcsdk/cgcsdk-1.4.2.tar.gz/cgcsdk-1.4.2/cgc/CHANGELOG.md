# Change Log

## 1.4.2

Release on Sept 29, 2025

* Fix error on job create with repository-secret

## 1.4.1

Release on Sept 25, 2025

* CGC SDK updated with `volume` commands
* CGC SDK docs and examples
* Fix `resource_create`
  * remove requirement for `image_name` if `entity` is not `custom` or `job`
* CGC SDK `resource` added:
  * `get_available_compute_templates`
  * `get_available_database_templates`
  * `get_available_gpu_types`

## 1.4.0

Release on Sept 16, 2025

* refactor resource creation, to support ANY arguments and ANY environment variables
  * `cgc compute create`
  * `cgc job create`
* refactor CLI command structure to check version only for specific subcommands
* fixed message for `cgc api-keys create` command
* CGC SDK has been adjusted to support new arguments and environment variables
* `startup command` argument has been removed from `cgc compute create` and `cgc job create`
  * available as piped argument
* within SDK defined new functions:
  * `resource.resource_create`
  * `resource.get_entity_list`
  * `context.switch_context`
  * `context.list_contexts`
* changes to existing functions within SDK:
  * `resource.compute_create_custom` now uses `resource.resource_create`
  * `resource.compute_create_custom` highlights deprecation warning
* complete documentation with examples for the CGC SDK

## 1.3.2

Release on July 18, 2025

* remove `pkg_resources` dependency, use `importlib.resources` instead

## 1.3.1

Release on July 10, 2025

* removal of hardcoded `4096 GB` limit for volumes

## 1.3.0

Release on July 08, 2025

* stop events are not longer supported
* billing endpoints v1 are not longer supported
* added support for v2 billing endpoints
* added `cgc billing pricing` command
* error messages are now more descriptive

## 1.2.6

Release on Apr 30, 2025

* `cgc resource scale up` scales up the resource replicas, with the given name
* `cgc resource scale down` scales down the resource replicas, with the given name
* modified error message displayed - uses custom_exceptions
* listing of `TurnedOff` resources is now available
* `TurnedOn` available if the resource is not running, but it is scaled up

## 1.2.5

Release on Apr 16, 2025

* `cgc register` now invokes **version check** within registered cluster, to refresh cluster configuration

## 1.2.4

Release on Apr 11, 2025

* added optional parameter `-t` to `cgc logs`, for timestamps

## 1.2.3

Release on Apr 07, 2025

* support for the `RTX6000` cards

## 1.2.2

Release on Apr 01, 2025

* updated handling of server configuration data
* update node_port logic for on-premises
* updated response message, when working with LLM api keys
* updated logic for non main CGC clusters
* updated aggregation of one-off events in billing status
* user config permissions updated to 600
* added CorruptedConfigFile exception

## 1.2.1

Release on Nov 26, 2024

* `cgc register` now correctly saves api-keys into user configuration file

## 1.2.0

Release on Nov 20, 2024

* `cgc job list` now process more information from the job payload data
* processing resource labels in the `list` endpoints
* `cgc api-keys create` allows managing API keys levels (CGC, LLM)
* `cgc api-keys list` now shows more information about the API keys
* support for one-off billing events
* `gpu-label` and `gpu-count` retrieval from jobs
* `cgc api-keys create` does not overwrite existing keys by default

## 1.1.0

Release on Oct 02, 2024

* fix: not required `app-token` label for computes
* update: grant_type for JWT authentication

## 1.0.18

Release on Aug 28, 2024

* `cgc job list` now also uses information from the job status
* `cgc compute port list` now shows full ingress path in the new column
* `cgc status` now shows user defined quotas

## 1.0.17

Release on Aug 19, 2024

* `cgc port list` now shows which ports are ingress (`cgc resource ingress app_name`)
* fix bug for the `cgc keys ssh create` command
* `cgc context list` now shows which context is active
* `cgc context list` now shows context server address

## 1.0.16

Release on Aug 02, 2024

* dynamic storage classes for volumes
* dynamic templates available for compute
* dynamic templates available for databases
* fixed bug: context switched to cfg.json after CGC update
* updated command: `cgc status`, now it is fully dynamic
* add flag `-y` to `cgc compute port` group commands
* `active_deadline_seconds` to `cgc job create` command
* `cgc db create` now have option `-d` available
* updated displayed values with `cgc job list`
* updated version control messages

## 1.0.15

Release on June 27, 2024

* added new compute template: `unsloth-cu121`

## 1.0.14

Release on June 13, 2024

* fixed DB creation issue with a client
* fixed client handling when your context server is not available

## 1.0.13

Release on June 05, 2024

* increase volume create size to 4 TB (4096 GB)
* cgc volume list now shows which disk type is used for the volume

## 1.0.12

Release on May 09, 2024

* hotfix: allow secret upper cased, during registration process

## 1.0.11

Release on April 25, 2024

* hotfix: user registration process for the first time

## 1.0.10

Release on April 24, 2024

* added new command group: cgc secrets
  * add - add new secret
  * list - list all secrets in the namespace
  * delete - delete secret (requires to be owner of the secret)
  * update - update secret (requires to be owner of the secret)

## 1.0.9

Release on April 23, 2024

* updated cgc to work with cgc-server 1.0.10
* updated registration process
* updated available apps, so it reflects changes in cgc-server
* hotfix: listening jobs, which are not Running

## 1.0.8

Release on April 11, 2024

* added new command group: cgc keys
  * ssh create - create new ssh key, for ssh access
  * ssh list - list all ssh keys
  * ssh delete - delete ssh key
  * ssh update - update ssh key

## 1.0.7

Release on April 04, 2024

* speed of resource creation with volumes / shared memory, has been improved
* added jobs creation: cgc job create
* added jobs list: cgc job list
* added jobs delete: cgc job delete
* added logs (STDOUT, STDERR) reader for spawned applications: cgc logs
* added SDK for logs & jobs

## 1.0.6

Release on March 13, 2024

* updated exception handling for SDK
* fix for cgc CLI command: compute create
* ensure encode("utf-8") for all payloads generated by CLI/SDK

## 1.0.5

Release on March 7, 2024

* added new compute template: custom
* custom template can be any docker image
* custom template can use docker registry, that requires authentication
* during compute create, new flag available: -fp, --full-path
  * allows to mount volume with full path; works with one volume only
* added support for adding for compute create config_map_data
* added for compute create
  * startup_command as a STDIN on second argument
  * --repository-secret flag to set docker registry secret from namespace
  * --image flag to set docker image for custom template
* managing compute ports, require user confirmation
* resource commands
* add compute custom create and resource delete to cgc sdk
* add compute port add, delete, update, list to cgc sdk
* add compute and db **list** to cgc sdk
* add resource ready command to cgc sdk
* on-premises support for node_port_enabled
* added new command: cgc context get-env-path
* added new command: cgc compute list-mounts

## 1.0.4

Release on December 12, 2023

* fixed typos
* command group "cgc compute port" updated logic
* added "--shm size" option to "cgc compute create" command
* add support for: weaviate (db, no gpu), t2v-transformers (compute, gpu enabled)
* weaviate can work with t2v-transformers
  * requires added -d flag: weaviate_enable_modules=text2vec-transformers
  * requires added -d flag: weaviate_transformers_inference_api=<http://name-of-t2v-app:8080>

## 1.0.3

Release on November 21, 2023

* minor changes to increase level of user experience with CLI
* added new command group: cgc compute port
  * ports can be: added/deleted/updated/listed
* added new command: cgc resource ingress

## 1.0.2

Release on October 30, 2023

* api-keys management enabled (create, list, delete)

## 1.0.1

Release on October 27, 2023

* added new compute template: comfy-ui
* added new compute template: rag
* added new compute template: deepstream
* updated compute.create.filebrowser with flags to specify user_id and group_id
* added new parameter to compute.create, multiple allowed: --resource-data
* modified volume.mount command
  * -p flag changed to -sp
  * new flag: -fp which equals to full path

## 1.0.0

Release on July 18, 2023

* updated cgc compute create payload
* updated cgc db create payload
* create type endpoint accept specific extra data for resource creation
  * more described in comments at compute_create function

## 0.9.2

Release on July 17, 2023

* hotfix to message when cgc compute filebrowser create due to default username changes
* added notes for compute.create in code
* hotfix for cgc.sdk.redis

## 0.9.1

Release on June 14, 2023

* cgc billing - updated which values from response are taken to show
  * cost_total in billing was shown correctly - no changes
  * start, end, time: updated with correct key:value pairs from response

## 0.9.0

Release on June 13, 2023.

* APP TLS update - DNS for API endpoint
* removed self signed certificate, server got signed certificate for cgc-api.comtegra.cloud
* added new compute template: label-studio
* default user for label-studio: admin@localhost
* default user for filebrowser: admin
* default user for postgresql: admin

## 0.8.8, 0.8.9

Release on May 29, 2023.

* hotfix: fixed redis import in cgc.sdk

## 0.8.7

Release on May 23, 2023.

* hotfix: development changed .env file making it broken for new users

## 0.8.6

Release on May 19, 2023.

* added get_redis_client_async() for RedisConnector
* get_redis_access() - async_client: bool, new parameter
* new command: cgc context switch [number]
  * switch between user contexts
* new command: cgc context list
  * list all configuration files
* updated command: cgc register
  * allow to have multiple user contexts
* increased timeout for requests to 30 sec

## 0.8.5

Release on Apr 21, 2023.

* update for cgc status: resource_keys in cgc_status_response

## 0.8.4

Release on Apr 18, 2023.

* fix regarding missing imports

## 0.8.3

Release on Apr 18, 2023.

* minor db sdk update
* added restart optional parameter to client

## 0.8.2

Release on Apr 18, 2023.

* minor bug fixes

## 0.8.1

Release on Apr 17, 2023.

* cgc db list
* cgc compute list
* cgc events APP_NAME
* package cgc.sdk for management of databases templates inside user namespace

## 0.8.0

Release on Apr 14, 2023.

* cgc db - new commands for managing databases
* cgc compute - refactor commands for compute template management
* cgc resource - new command to control db and compute resources

## 0.7.1

Released on Mar 23, 2023.

* endpoints can be disabled on server, client correctly understand error code 302
* api-keys management endpoints are temporary disabled (list, delete)

## 0.7.0

Released on Mar 22, 2023.

* volume host group removed
* added telemetry opt-in/opt-out
* billing cost is set (update cost values for usage)
* storage layout on Kubernetes cluster
* billing usage in namespace managed with multiple users
* triton server enabled to create

## 0.6.7

Released on Mar 10, 2023.

* debug commands group added
* opt-in telemetry for the first time

## 0.6.6

Released on March 03, 2023.

* updated standard error message
* updated version control message
* with `cgc volume create` parameter `-g` is now `-hg`, which is host group
* help message for parameters
* DATASCIENCE_JUPYTER, TENSORFLOW_JUPYTER removed
* telemetry codes updated (fail only on APP errors (client/server))

## 0.6.5

Released on Feb 20, 2023.
Changes from 0.6.0 to 0.6.5

* updated command `cgc api-key create`
* updated command `cgc register`
* updated command `cgc compute list`

## 0.6.0

Released on Feb 15, 2023.

### Added

* TLS support using SSL certificate
* self-signed `server.crt` by Comtegra S.A developers (until another certificate is used)
* server from version **0.6.0** requires *TLS* over *HTTPS*
* utils for handling connection to server with error handling
* utils for server response with error handling
* extra decorator for message parser which catches errors while decoding Json response
  * TypeError
  * KeyError
  * Custom Comtegra exceptions
* Tests for CLI
* `cgc api-key create` - allows to create new API-key pair for current user-id. Currently overwrites existing

### Changed

* Code refactor - created decorators, better exception handling, functions for repeatable tasks
  * `cgc compute` commands
  * `cgc volume` commands
  * `cgc billing` commands
  * `cgc register` commands
* Bug fix - `cgc volume umount <vol_name> -t <app_name>` now correctly unmounts ONLY from that app
  * Endpoint now validates -t as a list of strings which is required to hold mount for every app - unmount from all in list or None
  * Passing None (or not passing -t in CLI client) will unmount from all apps holding this volume
  * Fixed messages displayed on client and responses from server
* Response messages for `cgc compute create` now better describes current status
* Error responses messages are now generated by server, can be displayed by client
* Client error handling
* Allowed GPU's: A100, A5000
* Volume create - HDD disabled temporary

### Removed

* Unnecessary blocks of code
* Temporary removed support for V100
* `cgc login` - same functionality (and updated) available through `cgc api-key create`

## 0.5.3

No changelog for this and previous releases.
