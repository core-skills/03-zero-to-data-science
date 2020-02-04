[Overview](./00_overview.md) | [Data Culture](./01_culture.md) |
[From Here to There](./02_fromheretothere.md) | [Data Projects](./03_projects.md) | [Data Exploration](./04_dataexploration.md) | [Closeout](./05_closeout.md)

# Data Science Projects: The Workflow

| 90 Minutes |
| ---------- |

The way in which data science projects are typically conducted differs in some regards relative to your typical project workflow.
As we mentioned earlier, data science moves at a different pace, is iterative,
and often involves rapidly developing a series of prototypes.

While there are a wide range of ways to come at any individual data science project,
most incorporate a series of steps before any model building magic occurs.
These steps are key to making the most of you data. Roughly, a series of steps you'd proceed through might look like the following:

1. Define the Problem
1. Define a Question
1. Explore Data
1. Clean & Format Data
1. Transform Data ready for ML Pipeline

These are the steps we'll consider at a high level this afternoon.

| :question: Does your project easily break down to parts of a workflow? |
| ---------------------------------------------------------------------- |

## Structuring Your Data Project

Data science projects involve the use and creation of a number of on-disk components.
This typically includes data, code, models, outputs, references and documentation.
Before getting too far into a data science project, it's a good idea to organise these into some kind of consistent structure.

This organisation step - when you stick with it - has a number of benefits, but it's particularly important for working with others.

When coupled to some good coding practises<sup>[#]</sup>, one of the key advantages is **repeatability**, being able to easily repeat the workflow. This is particularly important for iterative development processes.

Following from this is **reproducibility**, being able to repeat the analysis and get the same result. If your analysis isn't reproducible, your confidence in the process is necessarily lowered.

With regard to data management, keeping processed data separate from raw data can save a number of headaches.

Other aspects of the structure of your data science project make it easier to **rapidly develop and maintain** the project in the longer term.

The segmentation or modularisation of your data science project (into some of the components discussed above) allows you to develop them independently.
This can speed up the development process, and allow you to focus time on areas which will actually affect the results or performance of the overall process.
This separation of concerns helps with debugging, as changes are typically only made to one part of the workflow at a time.

As your projects become more complex, there are a variety of tools which can
help separate concerns with respect to different parts of the workflow. For
example, using different `git` branches to manage the stable and development
versions of your code (typically `master` and `develop`, respectively; you could also make branches for new features, or building new versions of workflow components).

Writing appropriate documentation, and starting to leverage some of Python's
inbuilt features for handling and reporting errors (including logging) will
help with debugging when inevitably something does break.

[#]: . "Particularly environment management, appropriate documentation and version control."

### Things to Watch Out For

There's also a few things to keep in mind which might save you some time in the longer run:

* In most instances you don't want to add data or images to a git repository.

  These are good things to add to your `.gitignore` file - whether as file
  extensions or as folders.

### Templates

When it comes to deciding on how to lay out your project on disk, there are some tools which provide templates for you, such as [cookiecutter](https://cookiecutter.readthedocs.io). One of
these such templates is for a general data science project
([cookiecutter-data-science](https://github.com/drivendata/cookiecutter-data-science)),
and gives you places to put all the key components.

## Prototyping

If you're new to coding, one of the things you'll need to get used to is
breaking things. Especially in the field of data science,
aiming to rapidly build prototypes for your project also means
that you'll run into lots of small failures, often accompanied
by lovely red error messages.

We've mentioned some of the places where you might get help with
understanding some of these (we can refresh this afternoon), and
you should expect to spend some time chasing the root causes
of these issues.

Throughout this process, we're aiming to build something practical -
something which works, and ideally works as expected. That's then
a solid foundation from which we can build our data science
workflow. In many cases, chasing 'ideal' will come at the cost of
spending less time on what matters, or spending too much time
on the overall project.

Jupyter notebooks are a particularly useful format for prototyping
parts of workflows. Once you have something working as you'd
like it, it's a good idea to convert this code into separate
`.py` files, as this then allows the code to be effectively
resused, and makes it easier to maintain.

[Overview](./00_overview.md) | [Data Culture](./01_culture.md) |
[From Here to There](./02_fromheretothere.md) | [Data Projects](./03_projects.md) | [Data Exploration](./04_dataexploration.md) | [Closeout](./05_closeout.md)
