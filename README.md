# Diabetes Prediction using Machine Learning
![Diabetes Image](https://healthitanalytics.com/images/site/article_headers/_normal/2019-08-07-GettyImages-1127363880.png)

## Overview
This project aims to predict the likelihood of diabetes in individuals based on various health features. It employs three different machine learning algorithms: Support Vector Machines (SVM), Decision Trees, and Random Forest.

## Table of Contents
- [Introduction](#introduction)
- [Dataset](#dataset)
- [Algorithms](#algorithms)
- [Results](#results)
- [Contributing](#contributing)


## Introduction
Explain the purpose of the project and its significance. Briefly describe the machine learning algorithms used and their roles in predicting diabetes.

## Dataset
The dataset is originally from the National Institute of Diabetes and Digestive and Kidney Diseases. The objective of the dataset is to diagnostically predict whether or not a patient has diabetes, based on certain diagnostic measurements included in the dataset. Several constraints were placed on the selection of these instances from a larger database. In particular, all patients here are females at least 21 years old of Pima Indian heritage.
### Algorithms
## Support Vector Machines (SVM)
Support Vector Machine or SVM is one of the most popular Supervised Learning algorithms. which is used for Classification as well as Regression problems. However, primarily, it is used for Classification problems in Machine Learning. The goal of the SVM algorithm is to create the best line or decision boundary that can segregate n-dimensional space into classes so that we can easily put the new data points in the correct category in the future. This best decision boundary is called a hyperplane. SVM chooses the extreme points/vectors that help in creating the hyperplane. These extreme cases are called as support vectors, and hence algorithm is termed as Support Vector Machine.
In SVM algorithm, we plot each data item as a point in n-dimensional space (where n is the number of features) with the value of each feature being the value of a particular coordinate. Then, we perform classification by finding the hyper-plane that differentiates the two classes very well.
The SVM algorithm is presented with a set of training examples (xi, yi) where xi are the real- world data instances and the yi are the labels indicating which class the instance belongs to For the two-class pattern recognition problem, yi = +1 or yi=-1. A training example (xi, yi) is called positive if yi=+1 and negative otherwise.
SVM construct a hyper plane that separates two classes and tries to achieve maximum separation between the classes. Separating the classes with a large margin minimizes a bound on the expected generalization error. Figure in pdf shows how SVM separates the positive and negative samples using optimal hyperplane.
The hyperplane is used to segregate the dataset into two classes. The hyper plane is a straightline. The compact form of the equation is given as:
X + b = 0
The SVM classifies data according to the following:
yi = 1 Ifw. xi + b >= 1
yi = 0 If w. xi - b <= 1
Margin is the distance between hyperplane and the support vector. The margin will berepresented as: M = 1 / |w|
For optimal classification the margin should be maximum i.e., max (1 / ||w||) or min (||w||)
For non-linear distribution of data, kernel trick can be used for classification. The kernel justmap the nonlinear data into high dimensional space for easier classification. Different Kernelsthat can be used are Linear Kernel, Polynomial Kernel and Radial Bias Filter (RBF) Kernel.
employs scikit-learn's Support Vector Machine (SVM) classifier (SVC) with a linear kernel for training. The kernel='linear' signifies the use of a linear decision boundary. The svmclassifier is instantiated and trained with the provided training data (x_train for features and y_train for labels). During training, the SVM algorithm optimizes a hyperplane to separate data points based on class labels. SVMs are effective for both linear and non-linear classification tasks, making them versatile in capturing intricate decision boundaries. The trained svmclassifier is now capable of making predictions on new data, demonstrating the power of SVMs in supervised machine learning.

## Decision Trees
Decision Tree is a Supervised learning technique that can be used for both classification and Regression problems, but mostly it is preferred for solving Classification problems. It is a tree-structured classifier, where internal nodes represent the features of a dataset, branches represent the decision rules and each leaf node represents the outcome.
In a Decision tree, there are two nodes, which are the Decision Node and Leaf Node. Decision nodes are used to make any decision and have multiple branches, whereas Leaf nodes are the output of those decisions and do not contain any further branches.
The decisions or the test are performed on the basis of features of the given dataset.
It is a graphical representation for getting all the possible solutions to a problem/decision based on given conditions.
It is called a decision tree because, similar to a tree, it starts with the root node, which expands on further branches and constructs a tree-like structure.
In order to build a tree, we use the CART algorithm, which stands for Classification and Regression Tree algorithm.
A decision tree simply asks a question, and based on the answer (Yes/No), it further split the tree into subtrees.
 diagram in pdf explains the general structure of a decision tree:
Note: A decision tree can contain categorical data (YES/NO) as well as numeric data.
There are various algorithms in Machine learning, so choosing the best algorithm for the given dataset and problem is the main point to remember while creating a machine learning model. Below are the two reasons for using the Decision tree:
Decision Trees usually mimic human thinking ability while making a decision, so it is easy to understand.
The logic behind the decision tree can be easily understood because it shows a tree-like structure.
Decision Tree Terminologies
•  Root Node: Root node is from where the decision tree starts. It represents the entire dataset, which further gets divided into two or more homogeneous sets.
•  Leaf Node: Leaf nodes are the final output node, and the tree cannot be segregated further after getting a leaf node.
•  Splitting: Splitting is the process of dividing the decision node/root node into sub-nodes according to the given conditions.
•  Branch/Sub Tree: A tree formed by splitting the tree.
•  Pruning: Pruning is the process of removing the unwanted branches from the tree.
•  Parent/Child node: The root node of the tree is called the parent node, and other nodes are called the child nodes.
How does the Decision Tree algorithm Work?
In a decision tree, for predicting the class of the given dataset, the algorithm starts from the root node of the tree. This algorithm compares the values of root attribute with the record (real dataset) attribute and, based on the comparison, follows the branch and jumps to the next node.
For the next node, the algorithm again compares the attribute value with the other sub-nodes and move further. It continues the process until it reaches the leaf node of the tree. The complete process can be better understood using the below algorithm:
Step-1: Begin the tree with the root node, says S, which contains the complete dataset.
Step-2: Find the best attribute in the dataset using Attribute Selection Measure (ASM).
Step-3: Divide the S into subsets that contains possible values for the best attributes.
Step-4: Generate the decision tree node, which contains the best attribute.
Step-5: Recursively make new decision trees using the subsets of the dataset created in step -3. Continue this process until a stage is reached where you cannot further classify the nodes and called the final node as a leaf node.
Example: Suppose there is a candidate who has a job offer and wants to decide whether he should accept the offer or Not. So, to solve this problem, the decision tree starts with the root node (Salary attribute by ASM). The root node splits further into the next decision node (distance from the office) and one leaf node based on the corresponding labels. The next decision node further gets split into one decision node (Cab facility) and one leaf node. Finally, the decision node splits into two leaf nodes (Accepted offers and Declined offer). Consider the below diagram:
 
Attribute Selection Measures
While implementing a Decision tree, the main issue arises that how to select the best attribute for the root node and for sub-nodes. So, to solve such problems there is a technique which is called as Attribute selection measure or ASM. By this measurement, we can easily select the best attribute for the nodes of the tree. There are two popular techniques for ASM, which are:
Information Gain
Gini Index
1. Information Gain:
Information gain is the measurement of changes in entropy after the segmentation of a dataset based on an attribute.
It calculates how much information a feature provides us about a class.
According to the value of information gain, we split the node and build the decision tree.
A decision tree algorithm always tries to maximize the value of information gain, and a node/attribute having the highest information gain is split first. It can be calculated using the below formula:
Information Gain= Entropy(S)- [(Weighted Avg) *Entropy(each feature)  
Entropy: Entropy is a metric to measure the impurity in a given attribute. It specifies randomness in data. Entropy can be calculated as:
Entropy(s)= -P(yes)log2 P(yes)- P(no) log2 P(no)
Where,
S= Total number of samples
P(yes)= probability of yes
P(no)= probability of no
2. Gini Index:
Gini index is a measure of impurity or purity used while creating a decision tree in the CART(Classification and Regression Tree) algorithm.
An attribute with the low Gini index should be preferred as compared to the high Gini index.
It only creates binary splits, and the CART algorithm uses the Gini index to create binary splits.
Gini index can be calculated using the below formula:
Gini Index= 1- ∑jPj2
Pruning: Getting an Optimal Decision tree
Pruning is a process of deleting the unnecessary nodes from a tree in order to get the optimal decision tree.
A too-large tree increases the risk of overfitting, and a small tree may not capture all the important features of the dataset. Therefore, a technique that decreases the size of the learning tree without reducing accuracy is known as Pruning. There are mainly two types of tree pruning technology used:
Cost Complexity Pruning
Reduced Error Pruning.

 
 utilizes scikit-learn's `DecisionTreeClassifier` to instantiate and train a Decision Tree model for classification. This classifier learns decision rules from the training data (`x_train` for features and `y_train` for labels). The model recursively splits the dataset based on features, constructing a tree structure that captures decision logic. This process allows the model to make predictions on new data. The Decision Tree, with its interpretability and ability to handle both categorical and numerical features, serves as a powerful tool for understanding and solving classification problems in machine learning.



## Random Forest
Random Forest is a classifier that contains a number of decision trees on various subsets of the given dataset and takes the average to improve the predictive accuracy of that dataset. Instead of relying on one decision tree, the random forest takes the prediction from each tree and based on the majority votes of predictions, it predicts the final output. The greater number of trees in the forest leads to higher accuracy and prevents the problem of overfitting. Since the random forest combines multiple decision trees to predict the class of the dataset, it is possible that some decision trees may predict the correct output, while others may not. But together, all the trees predict the correct output. Therefore, below are two assumptions for a better Random Forest classifier:
1. There should be some actual values in the feature variable of the dataset so that the classifier can predict accurate results rather than a guessed result.
2. The predictions from each tree must have very low correlations.
Random Forest works in two-phases:
⚫ First is to create the random forest by combining N decision trees, and
⚫ Second is to make predictions for each tree created in the first phase as shown in figure in PDF
 

 
Utilizes scikit-learn's `RandomForestClassifier` to create a Random Forest model for classification. Key parameters are configured:
- `n_estimators`: Specifies the number of decision trees in the forest (100 in this case).
- `criterion`: The criterion for splitting nodes is set to 'entropy,' which measures the information gain.
- `random_state`: Ensures reproducibility of results.
- `max_features`: Determines the number of features considered for splitting nodes ('auto' uses all features).
- `max_depth`: Sets the maximum depth of the decision trees to 10, controlling model complexity.
The Random Forest (`rfc`) is then trained on the training data (`x_train` and `y_train`) to create an ensemble of decision trees for robust classification.




## Results
Random Forests:
Random Forests stand out for their ensemble nature, combining multiple decision trees to enhance predictive accuracy and robustness. The model's accuracy typically ranges between 96% and 97%, showcasing its ability to capture complex relationships within the data. The ensemble approach mitigates overfitting and provides stability, making Random Forests particularly adept at handling noisy datasets and achieving high accuracy across various scenarios.

Decision Trees:
Decision Trees, characterized by their transparent and interpretable structure, also exhibit commendable accuracy, ranging from 96% to 98%. The simplicity of Decision Trees lies in their hierarchical decision-making process, where each node represents a feature and each branch a decision rule. While susceptible to overfitting, careful pruning and tuning can balance accuracy with model complexity, offering insights into the most influential features.

Support Vector Machines:
Support Vector Machines, known for their effectiveness in capturing non-linear decision boundaries, demonstrate accuracy in the range of 79% to 80%. SVMs excel in scenarios where data exhibits complex relationships, but their performance may be affected by the choice of kernel and hyperparameter tuning. SVMs are sensitive to the scale of features and may require preprocessing steps for optimal results. Despite slightly lower accuracy compared to ensemble methods, SVMs remain valuable for specific use cases, especially in high-dimensional spaces.

Comparative Analysis:
The observed variations in accuracy across models highlight the importance of understanding the underlying characteristics of the dataset. Random Forests and Decision Trees showcase remarkable accuracy, making them suitable for a broad spectrum of applications. Their interpretability and ability to handle both categorical and numerical features contribute to their popularity.
Support Vector Machines, while slightly trailing in accuracy, bring unique capabilities to the table. Their strength lies in capturing intricate decision boundaries and handling non-linear relationships, making them well-suited for tasks where other models may falter.

Considerations for Model Selection:
Choosing the most appropriate model depends on the nature of the data and the specific requirements of the task. Random Forests and Decision Trees, with their high accuracy and interpretability, are preferable when insight into decision-making processes is crucial. On the other hand, Support Vector Machines offer a powerful solution for tasks demanding nuanced decision boundaries and can be optimized through careful kernel selection and parameter tuning.
Conclusion:
In conclusion, the choice between Random Forests, Decision Trees, and Support Vector Machines hinges on the balance between accuracy, interpretability, and the complexity of decision boundaries required for the task at hand. The nuanced strengths of each model underscore the significance of thoughtful model selection based on the inherent characteristics of the dataset and the specific goals of the machine learning application. As the field evolves, understanding the strengths and limitations of these models becomes essential for practitioners seeking optimal predictive performance.



## Contributing
# Contributing to Diabetes Prediction Project

Thank you for considering contributing to the Diabetes Prediction project! Your help is greatly appreciated. Before you start contributing, please take a moment to review the following guidelines.

## How to Contribute

1. Fork the repository.
2. Clone the forked repository to your local machine.
    ```bash
     git clone https://github.com/khaja-50/Diabetes_prediction.git
    ```
3. Create a new branch for your changes.
    ```bash
    git checkout -b feature/add-new-feature
    ```
4. Make your changes and commit them.
    ```bash
    git commit -m "Add new feature: XYZ"
    ```
5. Push the changes to your fork.
    ```bash
    git push origin feature/add-new-feature
    ```
6. Open a pull request on GitHub from your fork to the main repository.

## Code Style Guidelines

- Follow the existing code style and structure.
- Use meaningful variable and function names.
- Add comments where necessary to explain complex sections of code.

## Reporting Issues

If you encounter any issues or bugs, please open an issue on the GitHub repository. Provide detailed information about the problem, including steps to reproduce it.

## Feature Requests

If you have a feature request, please open an issue on the GitHub repository. Clearly describe the new feature and explain why it would be beneficial.

## License

By contributing to this project, you agree that your contributions will be licensed under the project's [LICENSE](LICENSE).

Thank you for your contributions!





