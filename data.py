import datetime
from google.cloud import datastore

datastore_client = datastore.Client()


def store_solution(team_id, task_id, solution):
    entity = datastore.Entity(key = datastore_client.key('solution'))
    entity.update({
        'team': team_id, 'task': task_id, 'solution': solution, 'TS':datetime.datetime.now()
    })

    datastore_client.put(entity)


