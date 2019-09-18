# libraries needed
import mpi
import random


array = [0]*5

#sending info from master to children
#### change info to model ####
# if mpi.rank == 0:
#     for i in range(1, mpi.size):
#         j = random.randint(1,100)
#         print 'sending ', j, ' to rank ', i
#         mpi.send(j,i)
# elif mpi.rank == 1:
#     n, rc = mpi.recv(0)
#     print 'rank 1 received ', n
# elif mpi.rank == 2:
#     m, rc = mpi.recv(0)
#     print 'rank 2 received ', m
# mpi.barrier()

print ('')


for j in range(3):

    # Running neural networks from Ursula Directory 
    # depending on what iteration j is on
    if mpi.rank == 0:
        #for every child core, a result is received
        for i in range(1, mpi.size):
            #result is called 's'
            s, rc = mpi.recv(i)
            print 'received ', s, 'from rank ', i
            #saving what is received to array
            array[i] = s
    elif mpi.rank == 1:
        if (j != 0): #if it is not the first time runnning
            print 'rank 1 running network '
        #    exec(open('./paths.sh').read())
            exec(open('./apple_stock_price_predictor_iterative1.py').read())
            # result needed is the Mean Squared Error to determine best network
            result = (np.mean(mse_test_loss_seq))
            print 'rank 1 sending result'
            # sending result to Master Core
            mpi.send(result, 0)
        else: #if it is the first time it is running
            print 'rank 1 running network '
        #    exec(open('./paths.sh').read())
            exec(open('./apple_stock_price_predictor_initial1.py').read())
            result = (np.mean(mse_test_loss_seq))
            print 'rank 1 sending result'
            mpi.send(result, 0)
    elif mpi.rank == 2:
        if (j != 0):
            print 'rank 2 running network '
        #    exec(open('./paths.sh').read())
            exec(open('./apple_stock_price_predictor_iterative2.py').read())
            result = (np.mean(mse_test_loss_seq))
            print 'rank 2 sending result'
            mpi.send(result, 0)
        else:
            print 'rank 2 running network '
        #    exec(open('./paths.sh').read())
            exec(open('./apple_stock_price_predictor_initial2.py').read())
            result = (np.mean(mse_test_loss_seq))
            print 'rank 2 sending result'
            mpi.send(result, 0)
    elif mpi.rank == 3:
        if (j != 0):
            print 'rank 3 running network '
        #    exec(open('./paths.sh').read())
            exec(open('./apple_stock_price_predictor_iterative3.py').read())
            result = (np.mean(mse_test_loss_seq))
            print 'rank 3 sending result'
            mpi.send(result, 0)
        else:
            print 'rank 3 running network '
        #    exec(open('./paths.sh').read())
            exec(open('./apple_stock_price_predictor_initial3.py').read())
            result = (np.mean(mse_test_loss_seq))
            print 'rank 3 sending result'
            mpi.send(result, 0)
    elif mpi.rank == 4:
        if (j != 0):
            print 'rank 4 running network '
        #    exec(open('./paths.sh').read())
            exec(open('./apple_stock_price_predictor_iterative4.py').read())
            result = (np.mean(mse_test_loss_seq))
            print 'rank 4 sending result'
            mpi.send(result, 0)
        else:
            print 'rank 4 running network '
        #    exec(open('./paths.sh').read())
            exec(open('./apple_stock_price_predictor_initial4.py').read())
            result = (np.mean(mse_test_loss_seq))
            print 'rank 4 sending result'
            mpi.send(result, 0)
    mpi.barrier() #used to sync cores

    # printing by checking max in array and sending 0 or 1 to children
    # where 1 had the best result
    if mpi.rank == 0:
        print 'array=', array
        best = 1000 # Made this big number so that it master core would not interfere
        # Looks for minimum value within array in Master core
        for i in range(1, mpi.size):
            if (array[i] < best):
                best = array[i]
        print 'min of array: ', best
        bestInd = array.index(best)
        print 'index of max: ', bestInd
        # Iterating through child cores to give them a 0 or 1
        for i in range(1, mpi.size):
            # If the child core number is the same as the index of the best result
            # That child core is sent a 1
            if (i == bestInd):
                mpi.send(1, i)
            else:
                mpi.send(0, i)
    elif mpi.rank == 1:
        code, rc = mpi.recv(0)
        print 'rank 1 received ', code, ' from master'

    elif mpi.rank == 2:
        code, rc = mpi.recv(0)
        print 'rank 2 received ', code, ' from master'
    elif mpi.rank == 3:
        code, rc = mpi.recv(0)
        print 'rank 3 received ', code, ' from master'
    elif mpi.rank == 4:
        code, rc = mpi.recv(0)
        print 'rank 4 received ', code, ' from master'
    mpi.barrier()


    # best child sends info back to master and checking
    ##### send model back to master #####
    if mpi.rank == 0:
        for i in range(1, mpi.size):
            if (i == bestInd):
                bestRes, rc = mpi.recv()
        print 'Received ', bestRes, ' from ', i, ' rank'
    elif mpi.rank == 1:
        if code == 1:
            print 'rank 1 sending info'
            mpi.send('information', 0)
    elif mpi.rank == 2:
        if code == 1:
            print 'rank 2 sending info'
            mpi.send('information', 0)
    elif mpi.rank == 3:
        if code == 1:
            print 'rank 3 sending info'
            mpi.send('information', 0)
    elif mpi.rank == 4:
        if code == 1:
            print 'rank 4 sending info'
            mpi.send('information', 0)
    mpi.barrier()

###### doDONE HALLELUJAHHHH YAYYYY CELEBRATION #######
