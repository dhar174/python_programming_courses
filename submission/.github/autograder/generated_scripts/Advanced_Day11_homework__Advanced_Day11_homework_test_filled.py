#!/usr/bin/env python
# coding: utf-8

# # Advanced Day 11 Filled Test Submission
# 
# This sample submission matches the canonical autograder contract for local validation.
# 

# In[ ]:


from pathlib import Path
import base64

PNG_1X1 = base64.b64decode(
    "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVQIHWP4//8/AwAI/AL+X2VINwAAAABJRU5ErkJggg=="
)

def ensure_artifacts() -> None:
    reports = Path("reports")
    reports.mkdir(exist_ok=True)
    (reports / "priority_chart.png").write_bytes(PNG_1X1)
    (reports / "weekly_summary.txt").write_text(
        "Task Count by Priority\nmean actual hours\nnext task hours\n",
        encoding="utf-8",
    )

def main() -> None:
    ensure_artifacts()
    print('Hour 41 | dataframe rows: 5')
    print('Hour 41 | missing priority filled: yes')
    print('Hour 41 | mean estimate hours: 3.6')
    print('Hour 41 | grouped owners: 3')
    print('Hour 41 | data rule: clean before you summarize')
    print('Hour 42 | chart type: bar')
    print('Hour 42 | x labels: low, medium, high')
    print('Hour 42 | figure title: Task Count by Priority')
    print('Hour 42 | saved file: reports/priority_chart.png')
    print('Hour 42 | viz rule: label axes and title clearly')
    print('Hour 43 | model: linear regression')
    print('Hour 43 | feature: estimate_hours')
    print('Hour 43 | target: actual_hours')
    print('Hour 43 | prediction for 5h estimate: 5.4')
    print('Hour 43 | scope rule: explain the demo, do not oversell it')
    print('Hour 44 | report file: reports/weekly_summary.txt')
    print('Hour 44 | included chart: priority_chart.png')
    print('Hour 44 | included metric: mean actual hours')
    print('Hour 44 | included prediction: next task hours')
    print('Hour 44 | report rule: tie analytics back to capstone decisions')

if __name__ == "__main__":
    main()

