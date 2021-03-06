# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import calculator_pb2 as calculator__pb2


class CalculatorStub(object):
  """Calculator service decreption.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Add = channel.unary_unary(
        '/adder.Calculator/Add',
        request_serializer=calculator__pb2.CalculatorRequest.SerializeToString,
        response_deserializer=calculator__pb2.CalculatorReply.FromString,
        )


class CalculatorServicer(object):
  """Calculator service decreption.
  """

  def Add(self, request, context):
    """Sends a greeting
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_CalculatorServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Add': grpc.unary_unary_rpc_method_handler(
          servicer.Add,
          request_deserializer=calculator__pb2.CalculatorRequest.FromString,
          response_serializer=calculator__pb2.CalculatorReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'adder.Calculator', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
