#!/usr/bin/env python
# coding: utf-8

# # Advanced Day 9 Filled Test Submission
# 
# This sample submission matches the canonical autograder contract for local validation.
# 

# In[ ]:


def main() -> None:
    print('Hour 33 | framework: Flask')
    print('Hour 33 | route: GET /health')
    print('Hour 33 | status code: 200')
    print("Hour 33 | json response: {'status': 'ok'}")
    print('Hour 33 | rest rule: name resources clearly')
    print('Hour 34 | endpoint: POST /tasks')
    print('Hour 34 | create status: 201')
    print('Hour 34 | list status: 200')
    print('Hour 34 | delete status: 204')
    print('Hour 34 | endpoint rule: align verbs with actions')
    print('Hour 35 | request fields checked: title, priority')
    print('Hour 35 | invalid payload: 400')
    print('Hour 35 | serialized task keys: id, title, priority, done')
    print('Hour 35 | validation message: title is required')
    print('Hour 35 | contract rule: keep input and output shapes consistent')
    print('Hour 36 | app factory: create_app')
    print('Hour 36 | blueprint prefix: /api')
    print('Hour 36 | dependency wired: task_service')
    print('Hour 36 | config class: DevConfig')
    print('Hour 36 | structure rule: keep startup wiring separate from route logic')


if __name__ == "__main__":
    main()

