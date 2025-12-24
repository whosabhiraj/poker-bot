# Exact EV Optimization in a Finite Poker Game

## Overview
This project models a simplified 3-card poker variant as a **finite zero-sum decision problem** and computes the **exact expected value (EV)** of available actions using full combinatorial enumeration.

The objective is to select the action — **Fold**, **Call**, or **Raise** — that maximizes EV under asymmetric payoff rules. The emphasis is on correctness, clarity, and decision-theoretic reasoning rather than simulation or learning-based approaches.

## Problem Statement
Each player is dealt:
* Two private hole cards
* One shared community card

Given this 3-card hand, the player must choose one of three actions. The game is zero-sum, and payoffs are asymmetric across actions. The goal is to **maximize expected value**, not win probability.

| Action | Nature of Outcome | Description |
| :--- | :--- | :--- |
| **Fold** | Deterministic | The hand ends immediately with a fixed payoff. |
| **Call** | Stochastic | The hand proceeds to showdown with moderate payoffs. |
| **Raise** | Stochastic | The hand proceeds to showdown with higher upside and downside. |

At showdown, hands are compared deterministically according to standard 3-card poker rankings.

## Core Insight
The decision problem decomposes cleanly into **deterministic** and **stochastic** components:

* **Fold** is terminal and deterministic, with a fixed payoff.
* **Call** and **Raise** lead to stochastic outcomes at showdown, determined solely by the probabilities of **win**, **loss**, or **tie**.

Once the probabilities $P(\text{win})$, $P(\text{loss})$, and $P(\text{tie})$ are known, the expected value of each action is a **linear function** of these quantities.

As a result:
1.  All strategic complexity lies in probability computation.
2.  EV calculation is deterministic and inexpensive.
3.  Optimal play reduces to simple inequalities in win–loss probability space.

## Method
* **Exact Enumeration:** Iterating $\binom{N}{2}$ of all possible opponent hands from the remaining deck.
* **Deterministic Evaluation:** Using a strict hand evaluator for 3-card poker rankings.
* **Exact Probability Computation:** Deriving $P(\text{win})$, $P(\text{loss})$, and $P(\text{tie})$ without approximation.
* **Linear EV Computation:** Calculating values for Fold, Call, and Raise using the payoff table.
* **Worst-Case Modeling:** Assuming the opponent never folds voluntarily to guarantee a conservative lower bound on EV.

*No Monte Carlo simulation, heuristics, or machine learning techniques are used.*

## Example Output

**Input Hand:**
* Hole cards: `Q♠`, `A♥`
* Community card: `2♣`

**Output:**
```text
Computed Probabilities:
P(win)  = 0.7295918367346939
P(loss) = 0.26360544217687076
P(tie)  = 0.006802721088435374

Expected Values:
EV(Fold)    = -1.00
EV(call)    = 0.9319727891156462
EV(raise)   = 1.397959183673469

>> Chosen Action: Raise