#!/usr/bin/env python
# coding: utf-8

# # Advanced Day 1 Homework — Sample Filled Submission
# 
# This sample submission demonstrates one valid way to satisfy the Advanced Day 1 autograder markers.

# In[ ]:


import sys

student_name: str = 'Jane Doe'
weekly_goal: str = 'strengthen class design'
python_version: str = '3.11.5'

print(f'Student: {student_name}')
print(f'Goal: {weekly_goal}')
print(f'Python Version: {python_version}')
print('Project folders: src, tests, data, reports')
print('Git workflow: clone -> pull -> status -> add -> commit -> push')

class DiagnosticCheck:
    def __init__(self, status: str) -> None:
        self.status = status

    def as_record(self) -> dict[str, str]:
        return {'status': self.status}

try:
    diagnostic = DiagnosticCheck('ready')
    record = diagnostic.as_record()
    if record['status'] != 'ready':
        raise ValueError('diagnostic check failed')
    print('Diagnostic status: ready')
except ValueError as exc:
    print(f'Diagnostic failed: {exc}')


# In[ ]:


from dataclasses import dataclass

@dataclass
class Task:
    task_id: str
    title: str
    priority: int = 2
    done: bool = False

    def mark_done(self) -> None:
        self.done = True

class TaskRepository:
    def __init__(self) -> None:
        self._tasks: dict[str, Task] = {}

    def add(self, task: Task) -> None:
        self._tasks[task.task_id] = task

    def get(self, task_id: str) -> Task | None:
        return self._tasks.get(task_id)

class TaskService:
    def __init__(self, repository: TaskRepository) -> None:
        self.repository = repository

    def create_task(self, task_id: str, title: str, priority: int = 2) -> Task:
        task = Task(task_id=task_id, title=title, priority=priority)
        self.repository.add(task)
        return task

repository = TaskRepository()
service = TaskService(repository)
task = service.create_task('TASK-101', 'Draft syllabus')

print('Domain classes: Task, TaskRepository, TaskService')
print('Boundary rule: service validates, model protects invariants')
print(f'Task summary: {task.task_id} | {task.title} | priority={task.priority} | done={task.done}')


# In[ ]:


class ValidationError(Exception):
    """Raised when a domain rule is violated."""

class NotFoundError(Exception):
    """Raised when a requested record cannot be found."""

class ValidatedTask:
    def __init__(self, task_id: str, title: str, priority: int = 2) -> None:
        self.task_id = task_id
        self.title = title
        self.priority = priority

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, value: str) -> None:
        cleaned = value.strip()
        if not cleaned:
            raise ValidationError('title cannot be empty')
        self._title = cleaned

    @property
    def priority(self) -> int:
        return self._priority

    @priority.setter
    def priority(self, value: int) -> None:
        if not isinstance(value, int) or not 1 <= value <= 5:
            raise ValidationError('priority must be an integer between 1 and 5')
        self._priority = value

class LookupRepository:
    def __init__(self, tasks: dict[str, ValidatedTask]) -> None:
        self._tasks = tasks

    def require(self, task_id: str) -> ValidatedTask:
        if task_id not in self._tasks:
            raise NotFoundError(f'task {task_id} was not found')
        return self._tasks[task_id]

validated_task = ValidatedTask('TASK-101', 'Draft syllabus', priority=3)
print(f'Priority set to: {validated_task.priority}')

try:
    ValidatedTask('TASK-102', '   ', priority=2)
except ValidationError as exc:
    print(f'ValidationError: {exc}')

lookup_repository = LookupRepository({'TASK-101': validated_task})
try:
    lookup_repository.require('404')
except NotFoundError as exc:
    print(f'NotFoundError: {exc}')


# In[ ]:


class TextExporter:
    def export(self, task: Task) -> str:
        return f'{task.task_id} | {task.title}'

class DictExporter:
    def export(self, task: Task) -> dict[str, str]:
        return {'id': task.task_id, 'title': task.title}

class ConsoleNotifier:
    def send(self, message: str) -> str:
        return f'Composed notifier sent: {message}'

class TaskPresenter:
    def __init__(self, exporter) -> None:
        self.exporter = exporter

    def present(self, task: Task):
        return self.exporter.export(task)

notifier = ConsoleNotifier()
text_presenter = TaskPresenter(TextExporter())
dict_presenter = TaskPresenter(DictExporter())

print(notifier.send('Task created'))
print(f'Export text: {text_presenter.present(task)}')
print(f'Export dict: {dict_presenter.present(task)}')

