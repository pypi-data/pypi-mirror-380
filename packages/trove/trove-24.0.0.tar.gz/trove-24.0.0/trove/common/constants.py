# Copyright 2021 Catalyst Cloud Ltd.
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

BACKUP_TYPE_FULL = 'full'
BACKUP_TYPE_INC = 'incremental'
ETH1_CONFIG_PATH = "/etc/trove/eth1.json"
DOCKER_NETWORK_NAME = "database-network"
DOCKER_HOST_NIC_MODE = "docker-hostnic"
DOCKER_BRIDGE_MODE = "bridge"
MYSQL_HOST_SOCKET_PATH = "/var/lib/mysqld"
POSTGRESQL_HOST_SOCKET_PATH = "/var/lib/postgresql-socket"

REGISTRY_EXT_DEFAULTS = {
    'mysql':
        'trove.guestagent.datastore.mysql.manager.Manager',
    'mariadb':
        'trove.guestagent.datastore.mariadb.manager.Manager',
    'postgresql':
        'trove.guestagent.datastore.postgres.manager.PostgresManager',
    'percona':
        'trove.guestagent.datastore.experimental.percona.manager.Manager',
    'pxc':
        'trove.guestagent.datastore.experimental.pxc.manager.Manager',
    'redis':
        'trove.guestagent.datastore.experimental.redis.manager.Manager',
    'cassandra':
        'trove.guestagent.datastore.experimental.cassandra.manager.Manager',
    'couchbase':
        'trove.guestagent.datastore.experimental.couchbase.manager.Manager',
    'mongodb':
        'trove.guestagent.datastore.experimental.mongodb.manager.Manager',
    'couchdb':
        'trove.guestagent.datastore.experimental.couchdb.manager.Manager',
    'vertica':
        'trove.guestagent.datastore.experimental.vertica.manager.Manager',
    'db2':
        'trove.guestagent.datastore.experimental.db2.manager.Manager',
}
