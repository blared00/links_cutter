#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    CREATE USER devuser;
    GRANT ALL PRIVILEGES ON DATABASE links_cutter TO devuser;
EOSQL