# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import seventiny_cloud_faas_proto_pb2 as seventiny__cloud__faas__proto__pb2


class DynamicScriptExecutorStub(object):
  """动态脚本执行器
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.CheckScript = channel.unary_unary(
        '/SevenTiny.Cloud.FaaS.DynamicScriptExecutor/CheckScript',
        request_serializer=seventiny__cloud__faas__proto__pb2.DynamicScript.SerializeToString,
        response_deserializer=seventiny__cloud__faas__proto__pb2.DynamicScriptExecuteResult.FromString,
        )
    self.Execute = channel.unary_unary(
        '/SevenTiny.Cloud.FaaS.DynamicScriptExecutor/Execute',
        request_serializer=seventiny__cloud__faas__proto__pb2.DynamicScript.SerializeToString,
        response_deserializer=seventiny__cloud__faas__proto__pb2.DynamicScriptExecuteResult.FromString,
        )


class DynamicScriptExecutorServicer(object):
  """动态脚本执行器
  """

  def CheckScript(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Execute(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_DynamicScriptExecutorServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'CheckScript': grpc.unary_unary_rpc_method_handler(
          servicer.CheckScript,
          request_deserializer=seventiny__cloud__faas__proto__pb2.DynamicScript.FromString,
          response_serializer=seventiny__cloud__faas__proto__pb2.DynamicScriptExecuteResult.SerializeToString,
      ),
      'Execute': grpc.unary_unary_rpc_method_handler(
          servicer.Execute,
          request_deserializer=seventiny__cloud__faas__proto__pb2.DynamicScript.FromString,
          response_serializer=seventiny__cloud__faas__proto__pb2.DynamicScriptExecuteResult.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'SevenTiny.Cloud.FaaS.DynamicScriptExecutor', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
