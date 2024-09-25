#!/usr/bin/env bash

# wait-for-it.sh: Espera até que um host e uma porta estejam prontos
# Fonte: https://github.com/vishnubob/wait-for-it

set -e

host="$1"
shift
port="$1"
shift
cmd="$@"

until nc -z "$host" "$port"; do
  >&2 echo "Aguardando o $host:$port estar disponível..."
  sleep 1
done

>&2 echo "$host:$port está pronto!"
exec $cmd
