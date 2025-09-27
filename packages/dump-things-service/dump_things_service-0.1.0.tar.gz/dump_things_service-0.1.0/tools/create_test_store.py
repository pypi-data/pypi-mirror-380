
from pathlib import Path
from dump_things_service.record import RecordDirStore
from dump_things_service.config import (
    mapping_functions,
    MappingMethod,
)
from dump_things_service.model import get_model_for_schema


schema = 'https://concepts.inm7.de/s/flat-data/unreleased.yaml'
model, classes, _ = get_model_for_schema(schema)


store = RecordDirStore(
    root=Path('/home/cristian/tmp/dumpthings/large_test_store'),
    model=model,
    pid_mapping_function=mapping_functions[MappingMethod.digest_md5_p3],
    suffix='yaml',
)


person_template = model.Person(pid='inm7:person_', given_name='person_x')
building_template = model.Building(pid='inm7:building_x', name='Building_x')


for i in range(100 * 1000):
    person_template.pid = 'inm7:person_' + str(i)
    person_template.given_name = 'name_' + str(i)
    building_template.pid = 'inm7:building_' + str(i)
    building_template.name = 'inm7:name_' + str(i)
    tuple(store.store_record(person_template, 'inm7:test_creator', model))
    tuple(store.store_record(building_template, 'inm7:test_creator', model))
    if i % 1000 == 0:
        print(f'Stored {i} records')

print(f'Stored {100 * 1000} records')
