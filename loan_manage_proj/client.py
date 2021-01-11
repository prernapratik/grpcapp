import grpc

# import the generated classes
import loan_manage_pb2
import loan_manage_pb2_grpc

# open a gRPC channel
channel = grpc.insecure_channel('localhost:50051')

# create a stub (client)
stub = loan_manage_pb2_grpc.SaveLoanServiceStub(channel)

# create a valid request message
# (a@test.com”, 10, 2, 1000)
response_1 = loan_manage_pb2.UserDetails(email="a@test.com")
# interest_rate = loan_manage_pb2.UserDetails(interest_rate="10")
# repayment_terms = loan_manage_pb2.UserDetails(repayment_terms="2")
# loan_amount = loan_manage_pb2.UserDetails(loan_amount="1000")


# make the call
response = stub.SaveLoan(response_1)

# et voilà
# print(response.value)