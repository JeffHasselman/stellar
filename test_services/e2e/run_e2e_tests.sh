#/bin/bash
# if any of the commands fail, the script will exit
set -e

. ./common_scripts.sh

print_disk_usage

mkdir -p ~/stellar_logs
touch ~/stellar_logs/modelserver.log

print_debug() {
  log "Received signal to stop"
  log "Printing debug logs for server"
  log "===================================="
  tail -n 100 ~/stellar_logs/modelserver.log
  log "Printing debug logs for docker"
  log "===================================="
  tail -n 100 ../build.log
  stellar logs --debug | tail -n 100
}

trap 'print_debug' INT TERM ERR

log starting > ../build.log

log building and running function_callling demo
log ===========================================
cd ../../demos/weather_forecast/
docker compose up weather_forecast_service --build -d
cd -

log building and install model server
log =================================
cd ../../server
poetry install
cd -

log building and installing stellar cli
log ==================================
cd ../../stellar /tools
poetry install
cd -

log building docker image for stellar  gateway
log ======================================
cd ../../
stellar build
cd -

log startup stellar  gateway with function calling demo
cd ../../
tail -F ~/stellar_logs/modelserver.log &
server_tail_pid=$!
stellar down
stellar up demos/weather_forecast/stellar_config.yaml
kill $server_tail_pid
cd -

log running e2e tests
log =================
poetry install
poetry run pytest

log shutting down the stellar  gateway service
log ======================================
stellar down

log shutting down the weather_forecast demo
log =======================================
cd ../../demos/weather_forecast
docker compose down
cd -
