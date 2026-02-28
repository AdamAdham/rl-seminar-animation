# Reinforcement Learning Animations (Manim)

Manim animations created for a reinforcement learning seminar presentation.  
The project visually develops reinforcement learning theory **in the same logical order as the presentation**, starting from the question of how an agent should act in a stochastic world and progressively building toward value functions, optimality, and policy iteration.

The animations emphasize **derivation, intuition, and probabilistic reasoning**, not only final equations.

- **Raw Animation Videos**: [Drive Link](https://drive.google.com/drive/folders/10fbtTik8zXx8eGEc9q577p96tIxE_oJc?usp=sharing)
- **Presentation Slides**: [Canva Presentation](https://www.canva.com/design/DAHCGA1bB1U/5y2plROEb7JIJullfFFxow/edit?utm_content=DAHCGA1bB1U&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)

## Presentation Flow

The animations follow a dependency-based progression: each concept is introduced only after the mathematical tools required to understand it are established.

---

## 1. Transition — From World Model to Agent Behavior

Previous material described **how the environment works** (states, transitions, stochastic outcomes).

The central question becomes:

> **How should an agent act inside this world?**

The objective is to maximize the **return**:

$$
G_t
$$

the accumulated future rewards.  
The first step toward this goal is understanding the **expected reward of the next timestep**.

---

## 2. Expected Reward

In the environment model, rewards are stochastic:

- The same state–action pair may produce different rewards.
- Example intuition: identical actions in Blackjack can yield different outcomes.

### Expected Reward Definition

$$
r(s,a) =
\mathbb{E}[R_{t+1}\mid S_t=s, A_t=a]
=
\sum_{r} r \sum_{s'} p(s',r\mid s,a)
$$

This defines the average immediate reward obtained when taking action \(a\) in state \(s\).

---

## 3. Expectation

To understand the reward equation, expectation is introduced formally.

### Discrete Expectation

$$
\mathbb{E}[X] = \sum_x x\,p(x)
$$

### Example: Fair/Unfair Dice

This demonstrates how expectation weights outcomes by probability.

## 4. Marginalization

The appearance of the next state $s$ requires introducing marginalization.

### Definition

$$
P(X=x)=\sum_y P(X=x,Y=y)
$$

Marginalization removes variables that are not of interest by summing over them.

### Card Deck Example

Summing over card numbers yields the probability of drawing a specific suit:

$$
P(\text{hearts})
=
\sum_{n=1}^{13} P(SUIT=\text{hearts}, NUM=n)
=
\frac{1}{4}
$$

---

### Applying Marginalization to Rewards

$$
p(r\mid s,a)=\sum_{s'} p(r,s'\mid s,a)
$$

Substituting gives:

$$
r(s,a)=\sum_r r \sum_{s'} p(s',r\mid s,a)
$$

Thus the expected reward follows directly from probability rules.

## 5. Policy

A **policy** defines how an agent behaves.

$$
\pi(a\mid s)
$$

It is a probability distribution over actions given a state.

Example intuition:

- Multi-armed bandit

## 6. Value Functions

The agent ultimately wants to maximize **return**, not immediate reward.

### State Value Function

$$
v_\pi(s)=\mathbb{E}_\pi[G_t\mid S_t=s]
$$

where the return is

$$
G_t=\sum_{k=0}^{\infty}\gamma^k R_{t+k+1}
$$

The equation is explained intuitively in the presentation.

## 7. Optimality

Introducing optimal behavior replaces expectation over actions with maximization:

- Optimal state value function

The intuition:

> choose the policy producing the highest expected future return.

## 9. Policy Iteration (Example Process)

The presentation concludes with the iterative improvement procedure:

1. Random policy initialization
2. Policy evaluation
3. Policy improvement
4. Repeat evaluation and improvement

This process is known as **Policy Iteration**.

## Disclaimer

This repository was developed solely to produce animations for a reinforcement learning seminar presentation.  
The code prioritizes **visual output and rapid iteration** over software engineering practices.

As a result:

- The project does **not** strictly follow clean code principles.
- Structure and abstractions were designed for animation convenience rather than reuse or scalability.
- Naming conventions, modularity, and organization may be inconsistent.
- Some implementations are presentation-specific and not intended as general-purpose Manim components.

The repository should therefore be viewed as **presentation support code**, not a reference implementation or production-quality project.
