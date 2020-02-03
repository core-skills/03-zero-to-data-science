[Overview](./00_overview.md) | [Data Culture](./01_culture.md) |
[From Here to There](./02_fromheretothere.md) | [Data Projects](./03_projects.md) | [Data Exploration](./04_dataexploration.md) | [Closeout](./05_closeout.md)

# Data Science Projects


## Data Science Workflows

While there are a wide range of ways to come at any individual data science project,
most incorporate a series of steps before any model building magic occurs.
These steps are key to making the most of you data. Roughly, a series of steps you'd proceed through might look like the following:

1. Define the Problem
1. Define a Question
1. Input Data
1. Explore Data
1. Clean & Format Data
1. Transform Data ready for ML Pipeline

> Garbage in, garbage out.


| :question: Can you break down the parts of your project to fit into a workflow? |
| ------------------------------------------------------------------------------- |


## Structuring Your Data Project

Data science projects involve the use and creation of a number of on-disk components.
This typically includes data, code, models, outputs, references and documentation.
Before getting too far into a data science project, it's a good idea to organise these into some kind of consistent structure.

This organisation step - when you stick with it - has a number of benefits, but it's particularly important for working with others.

### Reproducibility

Being able to repeat the experiment down the road.
* environments
* metadata and documentation
* Versioning
* Keep processed data separate from raw data


### Maintainability

* segmentation/modularization
* branches
* error messages, logging and reporting

### Things to Watch Out For

In most instances you don't want to add data or images to a git repository.
### Templates

There are also tools which provide templates for you, such as [cookiecutter](https://cookiecutter.readthedocs.io). One of
these such templates is for a general data science project
([cookiecutter-data-science](https://github.com/drivendata/cookiecutter-data-science)),
and gives you places to put all the key components.

## Prototyping

[Overview](./00_overview.md) | [Data Culture](./01_culture.md) |
[From Here to There](./02_fromheretothere.md) | [Data Projects](./03_projects.md) | [Data Exploration](./04_dataexploration.md) | [Closeout](./05_closeout.md)
