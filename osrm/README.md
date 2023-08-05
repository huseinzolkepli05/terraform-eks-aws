# how-to

1. Download and process data,

```bash
file=malaysia-singapore-brunei-latest
# ~174MB
wget http://download.geofabrik.de/asia/${file}.osm.pbf
docker run -t -v "${PWD}:/data" osrm/osrm-backend osrm-extract -p /opt/car.lua /data/${file}.osm.pbf
docker run -t -v "${PWD}:/data" osrm/osrm-backend osrm-partition /data/${file}.osrm
docker run -t -v "${PWD}:/data" osrm/osrm-backend osrm-customize /data/${file}.osrm
```

2. Serve backend,

```bash
file=malaysia-singapore-brunei-latest
docker run -t -i -p 5000:5000 -v "${PWD}:/data" osrm/osrm-backend osrm-routed --algorithm mld /data/${file}.osrm
```

Read API documentation at http://project-osrm.org/docs/v5.5.1/api/#route-service

3. Push to Dockerhub,

```bash
file=malaysia-singapore-brunei-latest
docker build -t mesoliticadev/osrm-image:${file} .
docker run -p 5000:5000 mesoliticadev/osrm-image:${file}
docker push mesoliticadev/osrm-image:${file}
```