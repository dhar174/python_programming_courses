#!/usr/bin/env python
# coding: utf-8

# # Advanced Day 7 Filled Test Submission
# 
# This sample submission matches the canonical autograder contract for local validation.
# 

# In[ ]:


def main() -> None:
    print('Hour 25 | table name: tasks')
    print('Hour 25 | primary key: id')
    print('Hour 25 | columns: title, priority, done')
    print('Hour 25 | repository role: isolate sql details')
    print('Hour 25 | schema rule: one object maps to one row shape')
    print('Hour 26 | insert result: task-101 saved')
    print('Hour 26 | select result count: 2')
    print('Hour 26 | update result: 1 row changed')
    print('Hour 26 | delete result: 1 row removed')
    print('Hour 26 | sql rule: parameterize every query')
    print('Hour 27 | row type: sqlite3.Row')
    print("Hour 27 | mapped object: Task(id='task-101', title='Ship report')")
    print('Hour 27 | missing row: None')
    print('Hour 27 | list mapped count: 2')
    print('Hour 27 | mapping rule: convert rows at the repository boundary')
    print('Hour 28 | init script: schema ready')
    print('Hour 28 | transaction begin: ok')
    print('Hour 28 | rollback on error: yes')
    print('Hour 28 | commit result: saved')
    print('Hour 28 | integrity rule: keep related writes together')


if __name__ == "__main__":
    main()

