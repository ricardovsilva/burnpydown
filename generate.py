import argparse

import matplotlib.pyplot as plt
import numpy

parser = argparse.ArgumentParser(description='Generate burndown based on number of tasks and number of days')
parser.add_argument('--tasks', metavar='t', type=int, help='quantity of tasks to generate the burndown, also is the Y axis', required=True)
parser.add_argument('--days', metavar='d', type=int, help='number of working days of sprint', default=10)
parser.add_argument('--title', type=str, help='title of the burndown', default='sprint')
parser.add_argument('--tasksLeft', type=str, help='tasks remaining per day, separated by comma', default='')
parser.add_argument('--newTasks', type=str, help='tasks created per day, separated by comma', default='')

args = parser.parse_args()

tasks = args.tasks
days = args.days

tasksList = list(map(int, args.tasksLeft.split(','))) if args.tasksLeft != '' else []
newTasks = list(map(int, args.newTasks.split(','))) if args.newTasks != '' else []
daysList = range(len(tasksList))

figure = plt.figure()
plt.ylabel('tasks')
plt.xlabel('days')
axis = figure.gca()
axis.set_title(args.title)
plt.axis([0, days, 0, tasks])
axis.set_xticks(range(0, days + 1))
axis.set_yticks(range(tasks, -1, -1))
plt.plot(list(range(0, days + 1)), numpy.linspace(tasks, 0, days + 1))
plt.grid()
tasksRemaining, = plt.plot(daysList, tasksList, color = 'green', linestyle='solid', linewidth=2, marker = 'o')
newTasks, =plt.plot(daysList, newTasks, color = 'red', linestyle='solid', linewidth=2, marker = 'o')

plt.legend([tasksRemaining, newTasks], ["Tasks Remaining", "Tasks Created"])

plt.show()

