#!/usr/bin/env bash

# POST a SLURM job through the REST API
# Compatible with the docker cluster from https://github.com/FoamScience/hpc-makeshift-cluster
# and requires the head node to have an OpenFOAM apptainer container;
# you can get one from https://github.com/FoamScience/openfoam-apptainer-packaging
# something like:
# docker exec -u slurmuser slurm-head \
#        apptainer pull /home/slurmuser/openfoam.sif oras://ghcr.io/foamscience/opencfd-openfoam:latest

casename=$(basename "$PWD")
casecwd="/home/slurmuser/trials/${casename}"

docker exec -u slurmuser slurm-head mkdir -p /home/slurmuser/trials
docker cp "$PWD" "slurm-head:${casecwd}"

cat <<EOF > "${casename}.json"
{
    "script": "#!/bin/bash\n${casecwd}/Allrun /home/slurmuser/imfoam-dev.sif",
    "job": {
        "environment": ["PATH=/bin/:/usr/bin/:/sbin/"],
        "name": "${casename}",
        "current_working_directory": "${casecwd}",
        "tasks": 4
    }
}
EOF

export $(docker exec -it -u slurmuser slurm-head scontrol token | tr -d '\n\r')
export SLURM_REQ_URL=http://localhost:6820/slurm/v0.0.43
curl -s -X POST "$SLURM_REQ_URL/job/submit" \
    -H "X-SLURM-USER-NAME: slurmuser" \
    -H "X-SLURM-USER-TOKEN: $SLURM_JWT" \
    -H "Content-Type: application/json" \
    --data-binary "@${casename}.json"

#sbatch ./Allrun.slurm
