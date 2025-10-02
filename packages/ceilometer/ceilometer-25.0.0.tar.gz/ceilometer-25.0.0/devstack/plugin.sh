# Install and start **Ceilometer** service in devstack
#
# To enable Ceilometer in devstack add an entry to local.conf that
# looks like
#
# [[local|localrc]]
# enable_plugin ceilometer https://opendev.org/openstack/ceilometer
#
# By default all ceilometer services are started (see devstack/settings)
# except for the ceilometer-aipmi service. To disable a specific service
# use the disable_service function.
#
# NOTE: Currently, there are two ways to get the IPMI based meters in
# OpenStack. One way is to configure Ironic conductor to report those meters
# for the nodes managed by Ironic and to have Ceilometer notification
# agent to collect them. Ironic by default does NOT enable that reporting
# functionality. So in order to do so, users need to set the option of
# conductor.send_sensor_data to true in the ironic.conf configuration file
# for the Ironic conductor service, and also enable the
# ceilometer-anotification service.
#
# The other way is to use Ceilometer ipmi agent only to get the IPMI based
# meters. To make use of the Ceilometer ipmi agent, it must be explicitly
# enabled with the following setting:
#
# enable_service ceilometer-aipmi
#
# To avoid duplicated meters, users need to make sure to set the
# option of conductor.send_sensor_data to false in the ironic.conf
# configuration file if the node on which Ceilometer ipmi agent is running
# is also managed by Ironic.
#
# Several variables set in the localrc section adjust common behaviors
# of Ceilometer (see within for additional settings):
#
#   CEILOMETER_PIPELINE_INTERVAL:  Seconds between pipeline processing runs. Default 300.
#   CEILOMETER_BACKENDS:           List of database backends (e.g. 'gnocchi', 'sg-core', 'gnocchi,sg-core', 'none')
#   CEILOMETER_COORDINATION_URL:   URL for group membership service provided by tooz.
#   CEILOMETER_EVENT_ALARM:        Set to True to enable publisher for event alarming

# Save trace setting
XTRACE=$(set +o | grep xtrace)
set -o xtrace

# Support potential entry-points console scripts in VENV or not
if [[ ${USE_VENV} = True ]]; then
    PROJECT_VENV["ceilometer"]=${CEILOMETER_DIR}.venv
    CEILOMETER_BIN_DIR=${PROJECT_VENV["ceilometer"]}/bin
else
    CEILOMETER_BIN_DIR=$(get_python_exec_prefix)
fi

# Test if any Ceilometer services are enabled
# is_ceilometer_enabled
function is_ceilometer_enabled {
    [[ ,${ENABLED_SERVICES} =~ ,"ceilometer-" ]] && return 0
    return 1
}


function gnocchi_service_url {
    echo "$GNOCCHI_SERVICE_PROTOCOL://$GNOCCHI_SERVICE_HOST/metric"
}


# _ceilometer_install_redis() - Install the redis server and python lib.
function _ceilometer_install_redis {
    if is_ubuntu; then
        install_package redis-server
        restart_service redis-server
    else
        # This will fail (correctly) where a redis package is unavailable
        install_package redis
        restart_service redis
    fi

    pip_install_gr redis
}

# Install required services for coordination
function _ceilometer_prepare_coordination {
    if echo $CEILOMETER_COORDINATION_URL | grep -q '^memcached:'; then
        install_package memcached
    elif [[ "${CEILOMETER_COORDINATOR_URL%%:*}" == "redis" || "${CEILOMETER_CACHE_BACKEND##*.}" == "redis" || "${CEILOMETER_BACKENDS}" =~ "gnocchi" ]]; then
        _ceilometer_install_redis
    fi
}

# Create ceilometer related accounts in Keystone
function ceilometer_create_accounts {
    local gnocchi_service
    create_service_user "ceilometer" "admin"

    if is_service_enabled swift; then
        # Ceilometer needs ResellerAdmin role to access Swift account stats.
        get_or_add_user_project_role "ResellerAdmin" "ceilometer" $SERVICE_PROJECT_NAME
    fi

    if [[ "$CEILOMETER_BACKENDS" =~ "gnocchi" ]]; then
        create_service_user "gnocchi"
        gnocchi_service=$(get_or_create_service "gnocchi" "metric" "OpenStack Metric Service")
        get_or_create_endpoint $gnocchi_service \
            "$REGION_NAME" \
            "$(gnocchi_service_url)" \
            "$(gnocchi_service_url)" \
            "$(gnocchi_service_url)"
    fi
}


function install_gnocchi {
    echo_summary "Installing Gnocchi"
    if use_library_from_git "gnocchi"; then
        # we need to git clone manually to ensure that the git repo is added
        # to the global git repo list and ensure its cloned as the current user
        # not as root.
        git_clone ${GNOCCHI_REPO} ${GNOCCHI_DIR} ${GNOCCHI_BRANCH}
        pip_install -e ${GNOCCHI_DIR}[redis,${DATABASE_TYPE},keystone] uwsgi
    else
        pip_install gnocchi[redis,${DATABASE_TYPE},keystone] uwsgi
    fi
}

function configure_gnocchi {
    echo_summary "Configure Gnocchi"

    recreate_database gnocchi
    sudo install -d -o $STACK_USER -m 755 $GNOCCHI_CONF_DIR

    iniset $GNOCCHI_CONF DEFAULT debug "$ENABLE_DEBUG_LOG_LEVEL"
    iniset $GNOCCHI_CONF indexer url `database_connection_url gnocchi`
    iniset $GNOCCHI_CONF storage driver redis
    iniset $GNOCCHI_CONF storage redis_url redis://localhost:6379
    iniset $GNOCCHI_CONF metricd metric_processing_delay "$GNOCCHI_METRICD_PROCESSING_DELAY"

    iniset $GNOCCHI_CONF api auth_mode keystone
    configure_keystone_authtoken_middleware $GNOCCHI_CONF gnocchi

    gnocchi-upgrade

    rm -f "$GNOCCHI_UWSGI_FILE"

    write_uwsgi_config "$GNOCCHI_UWSGI_FILE" "$CEILOMETER_BIN_DIR/gnocchi-api" "/metric"

    if [ -n "$GNOCCHI_COORDINATOR_URL" ]; then
        iniset $GNOCCHI_CONF coordination_url "$GNOCCHI_COORDINATOR_URL"
    fi
}

# Activities to do before ceilometer has been installed.
function preinstall_ceilometer {
    echo_summary "Preinstall not in virtualenv context. Skipping."
}

# cleanup_ceilometer() - Remove residual data files, anything left over
# from previous runs that a clean run would need to clean up
function cleanup_ceilometer {
    sudo rm -f "$CEILOMETER_CONF_DIR"/*
    sudo rmdir "$CEILOMETER_CONF_DIR"
}

# Set configuration for cache backend.
# NOTE(cdent): This currently only works for redis. Still working
# out how to express the other backends.
function _ceilometer_configure_cache_backend {
    iniset $CEILOMETER_CONF cache enabled True
    iniset $CEILOMETER_CONF cache backend $CEILOMETER_CACHE_BACKEND

    inidelete $CEILOMETER_CONF cache backend_argument
    iniadd $CEILOMETER_CONF cache backend_argument url:$CEILOMETER_CACHE_URL
    iniadd $CEILOMETER_CONF cache backend_argument distributed_lock:True
    if [[ "${CEILOMETER_CACHE_BACKEND##*.}" == "redis" ]]; then
        iniadd $CEILOMETER_CONF cache backend_argument db:0
        iniadd $CEILOMETER_CONF cache backend_argument redis_expiration_time:600
    fi
}


# Set configuration for storage backend.
function _ceilometer_configure_storage_backend {
    # delete any "," characters used for delimiting individual backends before checking for "none"
    if [ $(echo "$CEILOMETER_BACKENDS" | tr -d ",") = 'none' ] ; then
        echo_summary "All Ceilometer backends seems disabled, set \$CEILOMETER_BACKENDS to select one."
    else
        head -n -1 $CEILOMETER_CONF_DIR/pipeline.yaml > $CEILOMETER_CONF_DIR/tmp ; mv $CEILOMETER_CONF_DIR/tmp $CEILOMETER_CONF_DIR/pipeline.yaml
        head -n -1 $CEILOMETER_CONF_DIR/event_pipeline.yaml > $CEILOMETER_CONF_DIR/tmp ; mv $CEILOMETER_CONF_DIR/tmp $CEILOMETER_CONF_DIR/event_pipeline.yaml

        BACKENDS=$(echo $CEILOMETER_BACKENDS | tr "," "\n")
        for CEILOMETER_BACKEND in ${BACKENDS[@]}; do
            if [ "$CEILOMETER_BACKEND" = 'gnocchi' ] ; then
                echo "          - gnocchi://?archive_policy=${GNOCCHI_ARCHIVE_POLICY}&filter_project=service" >> $CEILOMETER_CONF_DIR/event_pipeline.yaml
                echo "          - gnocchi://?archive_policy=${GNOCCHI_ARCHIVE_POLICY}&filter_project=service" >> $CEILOMETER_CONF_DIR/pipeline.yaml
                configure_gnocchi
            elif [ "$CEILOMETER_BACKEND" = 'sg-core' ] ; then
                echo "          - tcp://127.0.0.1:4242" >> $CEILOMETER_CONF_DIR/event_pipeline.yaml
                echo "          - tcp://127.0.0.1:4242" >> $CEILOMETER_CONF_DIR/pipeline.yaml
            else
                die $LINENO "Unable to configure unknown CEILOMETER_BACKEND $CEILOMETER_BACKEND"
            fi
        done
    fi

}

# Configure Ceilometer
function configure_ceilometer {
    iniset_rpc_backend ceilometer $CEILOMETER_CONF

    iniset $CEILOMETER_CONF oslo_messaging_notifications topics "$CEILOMETER_NOTIFICATION_TOPICS"
    iniset $CEILOMETER_CONF DEFAULT debug "$ENABLE_DEBUG_LOG_LEVEL"

    if [[ -n "$CEILOMETER_COORDINATION_URL" ]]; then
        iniset $CEILOMETER_CONF coordination backend_url $CEILOMETER_COORDINATION_URL
        iniset $CEILOMETER_CONF notification workers $API_WORKERS
    fi

    if [[ -n "$CEILOMETER_CACHE_BACKEND" ]]; then
        _ceilometer_configure_cache_backend
    fi

    # Install the policy file and declarative configuration files to
    # the conf dir.
    # NOTE(cdent): Do not make this a glob as it will conflict
    # with rootwrap installation done elsewhere and also clobber
    # ceilometer.conf settings that have already been made.
    # Anyway, explicit is better than implicit.
    cp $CEILOMETER_DIR/etc/ceilometer/polling_all.yaml $CEILOMETER_CONF_DIR/polling.yaml

    cp $CEILOMETER_DIR/ceilometer/pipeline/data/*.yaml $CEILOMETER_CONF_DIR

    if [ "$CEILOMETER_PIPELINE_INTERVAL" ]; then
        sed -i "s/interval:.*/interval: ${CEILOMETER_PIPELINE_INTERVAL}/" $CEILOMETER_CONF_DIR/polling.yaml
    fi
    if [ "$CEILOMETER_EVENT_ALARM" == "True" ]; then
        if ! grep -q '^ *- notifier://?topic=alarm.all$' $CEILOMETER_CONF_DIR/event_pipeline.yaml; then
            sed -i '/^ *publishers:$/,+1s|^\( *\)-.*$|\1- notifier://?topic=alarm.all\n&|' $CEILOMETER_CONF_DIR/event_pipeline.yaml
        fi
    fi

    # The compute and central agents need these credentials in order to
    # call out to other services' public APIs.
    iniset $CEILOMETER_CONF service_credentials auth_type password
    iniset $CEILOMETER_CONF service_credentials user_domain_id default
    iniset $CEILOMETER_CONF service_credentials project_domain_id default
    iniset $CEILOMETER_CONF service_credentials project_name $SERVICE_PROJECT_NAME
    iniset $CEILOMETER_CONF service_credentials username ceilometer
    iniset $CEILOMETER_CONF service_credentials password $SERVICE_PASSWORD
    iniset $CEILOMETER_CONF service_credentials region_name $REGION_NAME
    iniset $CEILOMETER_CONF service_credentials auth_url $KEYSTONE_SERVICE_URI

    _ceilometer_configure_storage_backend

    if is_service_enabled ceilometer-aipmi; then
        # Configure rootwrap for the ipmi agent
        configure_rootwrap ceilometer
    fi

    if [[ "$VIRT_DRIVER" = 'libvirt' ]]; then
        if ! getent group $LIBVIRT_GROUP >/dev/null; then
            sudo groupadd $LIBVIRT_GROUP
        fi
        add_user_to_group $STACK_USER $LIBVIRT_GROUP
    fi
}

# init_ceilometer() - Initialize etc.
function init_ceilometer {
    # Nothing to do
    :
}

# Install Ceilometer.
# The storage and coordination backends are installed here because the
# virtualenv context is active at this point and python drivers need to be
# installed. The context is not active during preinstall (when it would
# otherwise makes sense to do the backend services).
function install_ceilometer {
    if is_service_enabled ceilometer-acentral ceilometer-acompute ceilometer-anotification gnocchi-api gnocchi-metricd; then
        _ceilometer_prepare_coordination
    fi

    if [[ "$CEILOMETER_BACKENDS" =~ 'gnocchi' ]]; then
        install_gnocchi
    fi
    setup_develop $CEILOMETER_DIR
    sudo install -d -o $STACK_USER -m 755 $CEILOMETER_CONF_DIR
}

# start_ceilometer() - Start running processes, including screen
function start_ceilometer {

    if [[ "$CEILOMETER_BACKENDS" =~ "gnocchi" ]] ; then
        run_process gnocchi-api "$CEILOMETER_BIN_DIR/uwsgi --ini $GNOCCHI_UWSGI_FILE" ""
        run_process gnocchi-metricd "$CEILOMETER_BIN_DIR/gnocchi-metricd --config-file $GNOCCHI_CONF"
        wait_for_service 30 "$(gnocchi_service_url)"
        $CEILOMETER_BIN_DIR/ceilometer-upgrade
    fi

    run_process ceilometer-acentral "$CEILOMETER_BIN_DIR/ceilometer-polling --polling-namespaces central --config-file $CEILOMETER_CONF"
    run_process ceilometer-aipmi "$CEILOMETER_BIN_DIR/ceilometer-polling --polling-namespaces ipmi --config-file $CEILOMETER_CONF"

    # run the notification agent after restarting apache as it needs
    # operational keystone if using gnocchi
    run_process ceilometer-anotification "$CEILOMETER_BIN_DIR/ceilometer-agent-notification --config-file $CEILOMETER_CONF"

    run_process ceilometer-acompute "$CEILOMETER_BIN_DIR/ceilometer-polling --polling-namespaces compute --config-file $CEILOMETER_CONF" $LIBVIRT_GROUP
}

# stop_ceilometer() - Stop running processes
function stop_ceilometer {

    # Kill the ceilometer and gnocchi services
    for serv in ceilometer-acompute ceilometer-acentral ceilometer-aipmi ceilometer-anotification gnocchi-api gnocchi-metricd; do
        stop_process $serv
    done
}

# This is the main for plugin.sh
if is_service_enabled ceilometer; then
    if [[ "$1" == "stack" && "$2" == "pre-install" ]]; then
        # Set up other services
        echo_summary "Configuring system services for Ceilometer"
        preinstall_ceilometer
    elif [[ "$1" == "stack" && "$2" == "install" ]]; then
        echo_summary "Installing Ceilometer"
        # Use stack_install_service here to account for virtualenv
        stack_install_service ceilometer
    elif [[ "$1" == "stack" && "$2" == "post-config" ]]; then
        echo_summary "Configuring Ceilometer"
        configure_ceilometer
        # Get ceilometer keystone settings in place
        ceilometer_create_accounts
    elif [[ "$1" == "stack" && "$2" == "extra" ]]; then
        echo_summary "Initializing Ceilometer"
        # Tidy base for ceilometer
        init_ceilometer
        # Start the services
        start_ceilometer
    elif [[ "$1" == "stack" && "$2" == "test-config" ]]; then
        iniset $TEMPEST_CONFIG telemetry alarm_granularity $CEILOMETER_ALARM_GRANULARITY
        iniset $TEMPEST_CONFIG telemetry alarm_threshold $CEILOMETER_ALARM_THRESHOLD
        iniset $TEMPEST_CONFIG telemetry alarm_metric_name $CEILOMETER_ALARM_METRIC_NAME
        iniset $TEMPEST_CONFIG telemetry alarm_aggregation_method $CEILOMETER_ALARM_AGGREGATION_METHOD
    fi

    if [[ "$1" == "unstack" ]]; then
        echo_summary "Shutting Down Ceilometer"
        stop_ceilometer
    fi

    if [[ "$1" == "clean" ]]; then
        echo_summary "Cleaning Ceilometer"
        cleanup_ceilometer
    fi
fi

# Restore xtrace
$XTRACE
