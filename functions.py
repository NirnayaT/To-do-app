from database import *
from database import Task
from abc import ABC, abstractmethod

class AbstractRepository(ABC):#Adding Repository Layer between database interface and main interface 
    
    @abstractmethod
    def get(self):
        raise NotImplementedError()

    @abstractmethod
    def add(self):
        raise NotImplementedError()
    
    @abstractmethod
    def remove(self):
        raise NotImplementedError()

class TaskRepository(AbstractRepository):#inherits Abstractrepository

    def get(self):#get logic
        details= session.query(Task).all()
        return details

    def add(self,new_task):#add logic
        new_task_obj = Task(task=new_task)
        session.add(new_task_obj)
        session.commit()#commiting to the session

    def remove(self,task_id):#remove logic
        remove_task = session.query(Task).filter(Task.id == task_id).first()#filter the task id 
        session.delete(remove_task)
        session.commit()#commiting to the session