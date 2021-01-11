import grpc
from concurrent import futures
import time

# import the generated classes
import loan_manage_pb2
import loan_manage_pb2_grpc

# import the original calculator.py
import save_loan

# create a class to define the server functions, derived from
# calculator_pb2_grpc.CalculatorServicer
class CalculatorServicer(loan_manage_pb2_grpc.SaveLoanService):

    # calculator.square_root is exposed here
    # the request and response are of the data type
    # calculator_pb2.Number
    def SaveLoan(self, request, context):
        response = loan_manage_pb2.UserDetails()
        response.value = save_loan.save_loan_details(request.value)
        return response


# create a gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

# use the generated function `add_SaveLoanServiceServicer_to_server`
# to add the defined class to the server
loan_manage_pb2_grpc.add_SaveLoanServiceServicer_to_server(
        CalculatorServicer(), server)

# listen on port 50051
print('Starting server. Listening on port 50051.')
server.add_insecure_port('[::]:50051')
server.start()

# since server.start() will not block,
# a sleep-loop is added to keep alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)