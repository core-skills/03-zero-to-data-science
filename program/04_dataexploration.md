[Overview](./00_overview.md) | [Data Culture](./01_culture.md) |
[From Here to There](./02_fromheretothere.md) | [Data Projects](./03_projects.md) | [Data Exploration](./04_dataexploration.md) | [Closeout](./05_closeout.md)

# Data Exploration, Modelling and Reporting

| 90 Minutes |
| ---------- |

**Disclaimer!** Before starting any technical thinking, the very first thing to do is to define the **problem** that you're about to tackle with your data analysis. This is fundamental, as your problem will define many of the questions and choices you'll be making during the analysis.

Once you have a problem, the basic idea of data analysis is simple: *Seeking patterns in data for predictive uses*

The entire workflow for data analysis is built around this idea in 3 main steps:

1. Data exploration, i.e., you explore the data looking for patterns and correlations within and between your variables.
2. Modelling, i.e., you set up an algorithm to recognize those patterns and use them for prediction.
3. Reporting, i.e., you communicate the insights you got from the two previous steps

In practice, this workflow is not sequential: completing a step gives you new insights that can change how you approach any step of the workflow. So each step is iterative, and the workflow as a whole is iterative.
In the end, it is more a set of guidelines to help developing an efficient and structured project rather than a set of strict rules.

## Data Exploration: Understanding what's there

| 35 Minutes |
| ---------- |

The very first step of data exploration is to actually put your hands on some data, and make sure they can be used by a computer.

### Taking a step back from the data

Rather than jumping right away into the data, try to figure out the context of their acquisition. It helps to assess whether the data are in line with the problem you're trying to tackle.

| Determine the source of the data and their link with your problem |
|:----------------------------------------------------------------- |
| :question: **Who collected it & why?**                            |
| :question: **Can it answer the problem I want to tackle?**        |
| :question: **How quickly can I get there?**                       |
| :question: **How can I demonstrate the value of this work?**      |

It also helps to anticipate future issues, such as what uncertainties of the data and how they could affect your analysis.

| Determine the potential pitfalls you'll find along the way           |
|:-------------------------------------------------------------------- |
| :question: **Who is responsible for Quality Assurance and Control?** |
| :question: **Why and when can QA/QC fail?**                          |

### Making the data useful

Once you've found a promising data set to tackle your problem, make sure to organize them to make their use easier.

#### FAIR

[The FAIR Guiding Principles for scientific data management and stewardship](https://www.nature.com/articles/sdata201618) are a good way to start thinking about the issues of data management, storage and accessibility.

FAIR data are **F**indable, **A**ccessible, **I**nteroperable, and **R**eusable *with minimal human intervention*

They are defined around three entities: data, metadata, and infrastructure.

| Map out those who have need for access to data.             |
|:----------------------------------------------------------- |
| :question: **Who do you have to deal with to access data?** |
| :question: **Who needs access to the data?**                |
| :question: **How do their needs differ?**                   |
| :question: **How can we get space to make changes?**        |
| :question: **What do we do with cleaned data?**             |
| :question: **How durable is the storage?**                  |

Think of this as a way to maximize the insight that can be gained from a data set, because more people can access those data more easily, so are gonna be able to further exploit it.

#### Tidy Data

Tidy data follow the concept:

- One column = one variable
- One row = one observation

It provides a more general view of the data, and avoids biases in case they were initially organized with a given problem in mind.

### Exploring the data

Data exploration aims at maximizing the insight you get from a data set. This statement can be broken up in several sub-goals:

 - Uncovering the structure of the data (e.g., patterns, trends, correlations)
 - Determining the most important variables
 - Detecting outliers
 - Detecting anomalies

#### Mindset

| Think about what you usually do when facing new data:          |
|:-------------------------------------------------------------- |
| :question: **What is the first thing you do?**                 |
| :question: **How does it influence your next steps?**          |

Again, this process is iterative, based on two steps:

1. Ask questions about your data (e.g., what are the types of variations within and between my variables?)
2. Answer those questions using visualization and modelling tools

Answering the questions should give you new insight about your data, which should trigger new questions. There is no need for complex questions at the beginning, start with as many simple questions as possible, and grow your insight from there.

#### Tools

| Think about what you would do to explore new data:             |
|:-------------------------------------------------------------- |
| :question: **How can you do it in practice?**                  |
| :question: **What techniques can you use?**                    |

< Example >

| Think about what we just saw                         |
|:---------------------------------------------------- |
| :question: **How do we speed up data exploration?**  |

## Modelling: Summarizing what's there

| 25 Minutes |
| ---------- |

A model applies operations to transform some input values into some output values. Those operations often imply coefficients, which values you need to find. Once that's done, the model can make predictions outside of the known values.

### Modeling goal

| Think about what you expect from a model                   |
|:---------------------------------------------------------- |
| :question: **What do we want to predict?**                 |
| :question: **How to we check success?**                    |
| :question: **Do we need to understand the model?**         |

Modelling is usually done in two steps, which can be both automated:

1. Select a model that express the pattern(s) you've identified during data exploration (e.g., a straight line or a sinusoid)
2. Fit the model by using the data to tune its coefficients (i.e., training)

There are many different possible models, with:

- two main objectives, classification or regression
- two main types of model fitting, supervised or unsupervised

### Data preparation

Data exploration is about formulating hypothesis around your data, modelling is about confirming those hypothesis. While it is perfectly fine to use a sample more than once to formulate several hypothesis, you can only use a sample once during confirmation or you'll be over-optimistic about your predictions.

That's why data are usually divided into three sets:

- A training set to find the coefficients of the model
- A validation set to assess the performance of the model during training
- A test set to assess the performance of the model after training.

If your validation or test set are contaminated by the training set, your model will seem to perform far better than it actually does. A validation and test set also helps to assess overfitting (the model fits the training data perfectly, but fail to make reliable predictions with new data) or underfitting (the model fails to capture the patterns in the data).

### Model selection

The simpler, the better! Training is then faster, it limits chances of overfitting, and it improves the explainability of the model (i.e., understanding what is happening inside the model when you get a particular prediction). For those reasons, it is better to start with a simple model, and only complexify it if the answer to the problem is not satisfying yet (iterations!)

Models may have hypothesis, check them before using one. In a lot of cases, you can still get an output, but your predictions might suffer from ignoring those hypothesis.

### Data fitting

Data fitting is called training in machine learning, it means adjusting the model coefficients until the outputs of the model match the data. This process is done automatically by optimization (e.g., least squares or gradient descent) and requires an objective function (e.g., Euclidean distance between the outputs of the model and the real data) to measure progress.

### Visualizing models

Results from a model can be divided into two components:

- Predictions = what has the model captured
- Residuals = what has the model missed

< Example >

Similarly to the data exploration steps. here the goal is to gain insights on the predicting capabilities of the model. This analysis is more meaningful when carried out on test data.

Another possibility to visualize a model is to look at its coefficients. They can give you some insight on which input variables matter most, and what are the connections between those input variables during predictions. You can then assess whether it fits the observations made during data exploration.

### Programming habits

A programming *language* is just that, a language, and you can use it to communicate with others, and not just with the computer.

| Think about what defines clear code                           |
|:------------------------------------------------------------- |
| :question: **How to organize the code?**                      |
| :question: **How to name variables, functions, and classes?** |
| :question: **Where to add comments, and which ones?**         |

Be careful, it's easy to get lazy with Jupyter Notebooks (e.g., copying/pasting everything instead of writing functions)... Be nice to future you, think FAIR with your code too. Ultimately it helps with reporting and switching to production.

As with data analysis, coding is iterative: start by writing with a code that does what you want, then start thinking about optimizing it.

## Reporting: Communicating what's there

| 15 Minutes |
| ---------- |

Communication is a critical part of any work, and can happen at any time of your analysis, to diverse audiences. It can be oral, written, or both. Focusing on the insights you got from the analysis can help define your message.

### Why reporting

Sometimes to just share your results, mainly to get feedback or approval. Use that knowledge to identify the goals of you report and target your message. Again, your goal is to maximize success.

| Think about your audience                                     |
|:------------------------------------------------------------- |
| :question: **What do they expect from my report?**            |
| :question: **What do I expect from them?**                    |
| :question: **Which features from my analysis matter?**        |
| :question: **What are their data literacy?**                  |

### Tools

The tools used during data exploration and modelling can (and should) help. Try to anticipate which visualization are gonna be useful to share your work with others, and put proper labels on those. You can even go one step further a use the Jupyter Notebooks as a tool to share your results. It's then fundamental to keep your notebooks clean, and to separate the high-level code that actually provide the insightful results from the programming details.

An image is worth a thousand words, so data visualization is fundamental. So be careful, sometimes the visualizations you need to convey an idea can be different from those in data exploration that led you to this idea. Don't forget that the people you're talking too don't know the data as well as you do, so make their life as easy as possible.

There are plenty of work on that perspective, Edward Tufte's books on data visualization and information design are probably the most famous. One of Tufte's core principles is to maximize the data-to-ink ratio. The idea is that everything on a plot should convey meaningful information, the rest is just distraction and should be removed.

| Think about your plot                                           |
|:--------------------------------------------------------------- |
| :question: **What are you trying to say?**                      |
| :question: **Is it clear from your design?**                    |
| :question: **Have you eliminated any non-informative content?** |

[Overview](./00_overview.md) | [Data Culture](./01_culture.md) |
[From Here to There](./02_fromheretothere.md) | [Data Projects](./03_projects.md) | [Data Exploration](./04_dataexploration.md) | [Closeout](./05_closeout.md)
