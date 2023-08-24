from dagster import Config, RunConfig, graph, job, op

class InputsAndOutputsConfig(Config):
    param1: int
    param2: int

@op
def return_one(context) -> int:
    print(f'context in return_one - ${context}')
    return 1


@op
def add_one(context, number: int):
    print(f'context in add_one - ${context}')
    return number + 1


@op
def adder(context, config: InputsAndOutputsConfig) -> int:
    print(config.param1 + config.param2)
    return config.param1 + config.param2

@graph
def inputs_and_outputs():
    print(adder())

#DEFAULT_CONFIG = RunConfig(ops = { "inputs_and_outputs": InputsAndOutputsConfig(param1=1, param2=2)})
DEFAULT_CONFIG = RunConfig(ops = { "adder": InputsAndOutputsConfig(param1=1, param2=2)})

if __name__ == "__main__":
    # Will log "config_param: stuff"
    inputs_and_outputs.to_job().execute_in_process(run_config=DEFAULT_CONFIG)#{ 'ops': { 'adder': {}}})
