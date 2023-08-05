FROM osrm/osrm-backend

WORKDIR /data

COPY . /data

CMD ["osrm-routed", "--algorithm", "mld", "/data/malaysia-singapore-brunei-latest.osrm"]