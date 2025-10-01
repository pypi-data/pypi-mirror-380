# async-lambda

`async-lambda` is a framework for creating `AWS Lambda` applications with built
in support for asynchronous invocation via a SQS Queue. This is useful if you
have workloads you need to split up into separate execution contexts.

`async-lambda` converts your application into a `Serverless Application Model (SAM)`
template which can be deployed with the `SAM` cli tool.

An `async-lambda` application is comprised of a `controller` object and `tasks`.

```python
import json
from async_lambda import AsyncLambdaController, ScheduledEvent, ManagedSQSEvent, config_set_name

app = AsyncLambdaController()
config_set_name("project-name")
lambda_handler = app.async_lambda_handler # This "export" is required for lambda.

@app.scheduled_task('ScheduledTask1', schedule_expression="rate(15 minutes)")
def scheduled_task_1(event: ScheduledEvent):
    app.async_invoke("AsyncTask1", payload={"foo": "bar"}) # Payload must be JSON serializable and < 2560Kb

@app.async_task('AsyncTask1')
def async_task_2(event: ManagedSQSEvent):
    print(event.payload)  #{"foo": "bar"}

```

**When the app is packaged for lambda, only the main module, and the `vendor` and `src` directories are included.**

# Tasks

The core abstraction in `async-lambda` is a `task`. Each task will result in a separate lambda function.
Tasks have a `trigger_type` which determines what event triggers them. A task is identified by its unique `task_id`.

All task decorators share common arguments for configuring the underlying lambda function:

- `memory: int = 128` Sets the memory allocation for the function.
- `timeout: int = 60` Sets the timeout for the function (max 900 seconds).
- `ephemeral_storage: int = 512` Sets the ephemeral storage allocation for the function.
- `maximum_concurrency: Optional[int | List[int]] = None` Sets the maximum concurrency value for the SQS trigger for the function. (only applies to `async_task` and `sqs_task` tasks.) When using the `lanes` feature, this can be a list of maximum concurrency for each lane. The length of the list must equal the # of lanes.

It is often useful to run code during the `INIT_START` phase of the lambda lifecycle.
This is achieved by placing that code outside of the lambda handler, this will
result in this code being run for all tasks within the application as it is
executed on import. `async-lambda` provides a utility `init_tasks` argument which
will run given functions during the `INIT_START` phase only for that specific task.

The functions should have either 0 or 1 arguments, if they have 1 argument then
the `task_id` will be passed in.

`async-lambda` also provides a helper class for when a value needs to be stored
from this execution. The `Defer` class takes a function, and args/kwargs and
will only execute the function when its value is requested. This can be used in
combination with `init_tasks` to cache values during the `INIT_START` phase.

EX:

```python

def get_a_value(a: int, b: int) -> int:
    return random.randint(a, b)

cache = Defer(get_a_value, 10, 100)

@controller.async_task("Task", init_tasks=[cache.execute])
def task(event: ManagedSQSEvent):
    for i in range(cache.value):
        # Do Something
        ...
```

For all lambda executions which share a container `cache.value` will be the same
and `get_a_value` will only be called once.

## Async Task

All async tasks have a matching SQS queue which the lambda function consumes from (1 message per invocation).
All async task queues share a DLQ. Async tasks can be invoked from anywhere within the app by using the
`AsyncLambdaController.async_invoke` method. Calling this method sends a message into the queue for the given task.
The task function should have a single parameter of the `ManagedSQSEvent` type.

```python
app = AsyncLambdaController()

@app.async_task("TaskID")
def async_task(event: ManagedSQSEvent):
    event.payload # payload sent via the `async_invoke` method
    event.source_task_id # the task_id where the event originated
```

**It is quite easy to get into infinite looping situations when utilizing `async-lambda` and care should be taken.**

**INFINITE LOOP EXAMPLE**

```python
# If task_1 where to ever get invoked, then it would start an infinite loop with
# task 1 invoking task 2, task 2 invoking task 1, and repeat...

@app.async_task("Task1")
def task_1(event: ManagedSQSEvent):
    app.async_invoke("Task2", {})

@app.async_task("Task2")
def task_1(event: ManagedSQSEvent):
    app.async_invoke("Task1", {})
```

### Lanes

Sometimes you may want multiple "lanes" for events to travel through, especially when you have constrained throughput with `maximum_concurrency`. Utilize the `lanes` feature to open up multiple paths to an `async-task`. This can be useful if you have a large backlog of messages you need to process, but you don't want to interrupt the normal message flow.

The # of lanes can be controlled at the controller, sub-controller, and/or task level. With the configuration propagating down the tree, but it can be overridden at any of the levels. The # of lanes can be set with the `lane_count` parameter.

By default all usages of `async_invoke` will place the message in the default lane (`0`). To change this specify `lane=` in the `async_invoke` call. By default, any further calls of `async_invoke` down the call stack will continue to put the messages into the same lane if it is available. You can turn of this behavior by setting `propagate_lane_assignment=False` at the controller level.

For example, we will use a payload field to determine which lane processing should occur in. We will set the maximum concurrency for the default lane at 10, and for the other lane at `2`.

```python
app = AsyncLambdaController(lane_count=2)

@app.async_task("SwitchBoard")
def switch_board(event: ManagedSQSEvent):
    value = event.payload['value']
    lane = 0
    if value > 50_000:
        lane = 1
    app.async_invoke("ProcessingTask", event.payload, lane=lane)

@app.async_task("ProcessingTask", maximum_concurrency=[10, 2])
def processing_task(event: ManagedSQSEvent):
    ...
```

`async-lambda` creates `n` queues and lambda triggers per `async-task` where `n = lane_count`. All of the `n` queues are still consumed by a single lambda function.

## Unmanaged SQS Task

Unmanaged SQS tasks consume from any arbitrary SQS queue (1 message per invocation).
The task function should have a single parameter of the `UnmanagedSQSEvent` type.

```python
app = AsyncLambdaController()

@app.sqs_task("TaskID", queue_arn='queue-arn')
def sqs_task(event: UnmanagedSQSEvent):
    event.body # sqs event body
```

## Scheduled Task

Scheduled tasks are triggered by an eventbridge schedule. The schedule expression can be
a [cron expression](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-cron-expressions.html)
or a [rate expression](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-rate-expressions.html).
The task function should have a single parameter of the `ScheduledEvent` type.

```python
app = AsyncLambdaController()

@app.scheduled_task("TaskID", schedule_expression='rate(15 minutes)')
def scheduled_task(event: ScheduledEvent):
    ...
```

## API Task

API tasks are triggered by a Web Request. `async-lambda` creates an APIGateway endpoint matching the
`method` and `path` in the task definition. It is possible to configure a custom domain and certificate
for all API tasks within an `async-lambda` app.
The task function should have a single parameter of the `APIEvent` type.

```python
app = AsyncLambdaController()

@app.api_task("TaskID", path='/test', method='get')
def api_task(event: APIEvent):
    event.headers # request headers
    event.querystring_params # request querystring params
    event.body # request body
    event.headers # This is a case insensitive dict
```

# Middleware

Middleware functions can be registered with controllers which will wrap the execution of tasks.
These functions can be configured to trigger on specific types of tasks and can trigger
side effects and modify the `event` or `response` objects.

Middleware functions must have the signature `Callable[[BaseEvent, Callable[[BaseEvent], T]], T]`.
The first argument is the `event`, and the second argument (`call_next`) is a function which will propagate the
calls down the middleware/task stack. The `call_next` function must be called, and its result in most cases be returned.
If this is not done then tasks will not run as expected.

**Extreme care should be taken with middleware as a simple mistake can have catastrophic effects.**

- Middleware functions are run in the order which they were registered and parent controller middleware will be run first.

- Middleware functions which are registered more than once will only be run once.

Registration can be done when the `AsyncLambdaController` is initialized with the parameter `middleware` or by using the `add_middleware` method.

Middleware functions have three sections:

1. Pre task
2. Task execution
3. Post task

```python
def async_lambda_middleware(event: BaseEvent, call_next):
    # pre task
    result = call_next(event) # task execution
    # post task
    return result
```

If there are multiple middleware functions then `call_next` will actually be calling the next middleware function in the stack.

For example if there is middleware functions `A` and `B` registered in that order.
Then the execution order would go:

`A(Pre)` -> `B(Pre)` -> `Task` -> `B(Post)` -> `A(Post)`

EX:

```python
def async_task_only_middleware(event: ManagedSQSEvent, call_next):
    print(f"Invocation Payload: {event}")
    result = call_next(event)
    print(f"Invocation Result: {result}")
    return result

def all_task_types_middleware(event: BaseEvent, call_next):
    print(f"This event is of the type {type(event)}")
    result = call_next(event)
    print(f"The result is of the type {type(result)}")
    return event

controller = AsyncLambdaController(middleware=[([BaseEvent], all_task_types_middleware)])

controller.add_middleware([ManagedSQSEvent], async_task_only_middleware)

@controller.async_task("ATask")
def a_task(event: ManagedSQSEvent):
    pass

@controller.api_task("BTask", "/test", "get")
def b_task(event: APIEvent):
    return "hello world"
```

In this scenario when `ATask` is invoked first `all_task_types_middleware` will be run, then
`async_task_only_middleware` will be run and finally the `a_task` function will be executed.

When `BTask` is invoked first `all_task_types_middleware` will be run, and then the `b_task`
function will be executed

# `async-lambda` config

Configuration options can be set with the `.async_lambda/config.json` file.
The configuration options can be set at the app, stage, and task level. A configuration option set
will apply unless overridden at a more specific level (app -> stage -> task -> stage).
The override logic attempts to non-destructive so if you have a `layers` of `['layer_1']` at the app level,
and `[layer_2]` at the stage level, then the value will be `['layer_1', 'layer_2']`.

**Config file levels schema**

```
{
    # APP LEVEL
    "stages": {
        "stage_name": {
            # STAGE LEVEL
        }
    },
    "tasks": {
        "task_id": {
            # TASK LEVEL
            "stages": {
                "stage_name": {
                    # TASK STAGE LEVEL
                }
            }
        }
    }
}
```

**At any of these `levels` any of the configuration options can be set:**
With the exception of `domain_name`, `tls_version`, and `certificate_arn` which can not be set at the task level.

## `environment_variables`

```
{
    "ENV_VAR_NAME": "ENV_VAR_VALUE"
}
```

This config value will set environment variables for the function execution.
These environment variables will also be available during build time.

[The value is passed to the `Environment` property on `SAM::Serverless::Function`](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-resource-function.html#sam-function-environment)

## `policies`

```
[
    'IAM_POLICY_ARN' | STATEMENT
]
```

Use this config option to attach any arbitrary policies to the lambda functions execution role.

[The value is passed to the `Policies` property on `SAM::Serverless::Function`](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-resource-function.html#sam-function-policies), in addition to the `async-lambda` created inline policies.

## `layers`

```
[
    "LAYER_ARN"
]
```

Use this config option to add any arbitrary lambda layers to the lambda functions. Ordering matters,
and merging is done thru concatenation.

[The value is passed to the `Layers` property on `SAM::Serverless::Function`](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-resource-function.html#sam-function-layers)

## `subnet_ids`

```
[
    "SUBNET_ID
]
```

Use this config option to put the lambda function into a vpc/subnet.

The value is passed into the [`SubnetIds`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-vpcconfig.html) field of the [`VpcConfig` property on `SAM::Serverless::Function`](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-resource-function.html#sam-function-vpcconfig)

## `security_group_ids`

```
[
    "SECURITY_GROUP_ID"
]
```

Use this config option to attach a security group to the lambda function.

The value is passed into the [`SecurityGroupIds`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-vpcconfig.html) field of the [`VpcConfig` property on `SAM::Serverless::Function`](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-resource-function.html#sam-function-vpcconfig)

## `managed_queue_extras`

```
[
    {
        # Cloudformation resource
    }
]
```

Use this config option to add extra resources for managed SQS queues (`async_task` tasks.)

For example this might be used to attach alarms to these queues.

Each item in the list should be a complete cloudformation resource. `async-lambda` provides a few custom substitutions
so that you can reference the extras and the associated managed sqs resource by `LogicalId`.

- `$QUEUEID"` will be replaced with the `LogicalId` of the associated Managed SQS queue.
- `$EXTRA<index>` will be replaced with the `LogicalId` of the extra at the specified index.

## `method_settings`

**This config value can only be set at the app or stage level.**

```
[
    {...}
]
```

If your `async-lambda` app contains any `api_task` tasks, then a `AWS::Serverless::Api` resource is created.

The value is passed into the [`MethodSettings`](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-resource-api.html#sam-api-methodsettings) property of the `AWS::Serverless::Api`. The spec for `MethodSetting` can be found [here](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigateway-stage-methodsetting.html).

## `domain_name`

**This config value can only be set at the app or stage level.**

```
"domain_name"
```

If your `async-lambda` app contains any `api_task` tasks, then a `AWS::Serverless::Api` resource is created.

This config value will set the [`DomainName`](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-api-domainconfiguration.html) field of the [`Domain` property](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-resource-api.html#sam-api-domain)

## `tls_version`

**This config value can only be set at the app or stage level.**

```
"tls_version"
```

If your `async-lambda` app contains any `api_task` tasks, then a `AWS::Serverless::Api` resource is created.

This config value will set the [`SecurityPolicy`](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-api-domainconfiguration.html) field of the [`Domain` property](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-resource-api.html#sam-api-domain)

Possible values are `TLS_1_0` and `TLS_1_2`

## `certificate_arn`

**This config value can only be set at the app or stage level.**

```
"certificate_arn"
```

If your `async-lambda` app contains any `api_task` tasks, then a `AWS::Serverless::Api` resource is created.

This config value will set the [`CertificateArn`](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-api-domainconfiguration.html) field of the [`Domain` property](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-resource-api.html#sam-api-domain)

## `tags`

```
{
    "TAG_NAME": "TAG_VALUE"
}
```

This config value will set the `Tags` field of all resources created by async-lambda. This will not set the field on `managed_queue_extras` resources.

The keys `framework` and `framework-version` will always be set and the system values will override any values set by the user.

For managed queues the tags `async-lambda-queue-type` will be set to `dlq`, `dlq-task`, or `managed` depending on the queue type.

For `async_task` queues (non dlq-task) the `async-lambda-lane` will be set.

## `logging_config`

```
{
    "ApplicationLogLevel": "TRACE" | "DEBUG" | "INFO" | "WARN" | "ERROR" | "FATAL",
    "LogFormat": "Text" | "JSON",
    "LogGroup": "",
    "SystemLogLevel": "DEBUG" | "INFO" | "WARN"
}
```

The value is passed directly to the [`LoggingConfig`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-loggingconfig) Cloudformation parameter for lambda function/s.

# Building an `async-lambda` app

**When the app is packaged for lambda, only the main module, and the `vendor` and `src` directories are included.**

From the project root directory, utilize the `async-lambda` CLI tool to generate
a SAM template and function bundle. Optionally specify the `stage` to use `stage` specific configs.

```bash
# app.py contains the root AsyncLambdaController
async-lambda build app --stage <stage-name>
```

This will generate a SAM template `template.json` as well as an `deployment.zip` file.
This template and zip file can then be deployed or transformed into regular cloudformation
via the `sam` or `aws` cli tools.

# Known Limitations

- Lambda Configuration - not all of the lambda configuration spec is present in `async-lambda`. It is relatively trivial to add in configuration options. Make an issue if there is a feature you would like to see implemented.
- The `async_invoke` payload must be `JSON` serializable with `json.dumps`.
- It is possible to get into infinite loops quite easily. (Task A invokes Task B, Task B invokes Task A)
