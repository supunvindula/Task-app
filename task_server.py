import logging
from concurrent.futures import ThreadPoolExecutor
from grpc import server
import task_pb2
import task_pb2_grpc
from task_pb2_grpc import Taskapi


class TaskapiImpl(task_pb2_grpc.TaskapiServicer):
    """Dummy implementation of the Taskapi service"""

    def __init__(self):
        # initialise a Tasks attribute to store our tasks.
        self.tasks = task_pb2.Tasks()
        self.removed = 0

    def addTask(self, request, context):
        # TODO: implement this!
        index = len(self.tasks.tasks)
        print("added id: ", index,)
        tempTask = task_pb2.Task(id=index, description=request.description)
        self.tasks.tasks.append(tempTask)
        # print(self.tasks.tasks)
        # print("\n ------------------------------------------")
        return task_pb2.Id(id=tempTask.id)

    def delTask(self, request, context):
        # TODO: implement this!
        # print("removed id: ", request.id)
        tempID = -1
        for i in range(len(self.tasks.tasks)):
            if(self.tasks.tasks[i].id == request.id):
                tempID = i
                # print("tempID: ", tempID)
                print("removed id: ", self.tasks.tasks[i].id)
                break
        if(tempID == -1):
            print("id not found")
            return
        deleted = self.tasks.tasks[tempID]
        self.tasks.tasks.pop(tempID)
        return task_pb2.Task(id=deleted.id, description=deleted.description)

    def listTasks(self, request, context):
        # TODO: implement this!
        return self.tasks


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    taskserver = server(ThreadPoolExecutor(max_workers=10))
    task_pb2_grpc.add_TaskapiServicer_to_server(TaskapiImpl(), taskserver)
    taskserver.add_insecure_port("[::]:50051")
    taskserver.start()
    taskserver.wait_for_termination()
