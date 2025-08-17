# CMPS 6100  Lab 03

In this lab, you will practice and build up an intuition around asymptotic analysis.

Some prompts will require you to edit `main.py` and others will require answers to go in `answers.md`.

Refer back to the [README.md](README.md) for instruction on git, how to test your code, and how to submit properly to get all the points you've earned.

## Asymptotic Analysis Problems (14 pts)

Conventions: 


$$
\begin{aligned}
&\lg n  = \log_2 n      \nonumber \\
&\ln n = \log_e n       \nonumber \\
&\log n = \log_{10} n   \nonumber \\
&\log^c n = (\log n)^c  \nonumber \\
&\lg \lg n = \lg(\lg n) \nonumber
\end{aligned}
$$

Using the asymptotic definitions or the limit theorem, prove (or disprove) the following statements. Add all answers to `answers.md`. Each of the following problems are worth one point, except for 4 and 10 which are worth two points each.

1. $32n \in O(n)$

<br>

2. $\ln n \in \Omega(n)$

<br>

3. $\lg n \in \Theta(\ln n)$

<br>

4. $\log_c n \in \Theta(\ln n)$, $~~c > 1$

<br>

5. $n^2 \in O(2^n)$

<br>

6. $n^3 \in \Omega(n^2)$

<br>

7. $4^{\lg n} \in \Theta(n)$

<br>

8. $\ln^2 n \in O(n)$

<br>

9. $\ln^2 n \in O(\sqrt n)$

<br>

10. $\ln^c n \in O(n^k)$, $~~\forall ~ c,k > 0$ 

<br>

11. $\ln \ln n \in O(\ln n)$

<br>

12.  $2^n \in \Omega(2^{n+1})$

<br>

## The Ghost Game, Ghost Busters Add-on (13 pts)

For this programming assignment, you will add a new feature to your Ghost 
Game from the previous lab.

To start, copy over your Ghost Game source file from the previous lab into
this one.

Now, in this lab, you will add combat to your game! Previously, if the player
encountered the ghost, they lost. Now you will give them a chance to
defeat the ghost and still win.

If the player encounters the ghost, the game should enter a combat loop.
Both the player and ghost should have hp (health points). The combat
loop always starts with the player getting an opportunity to attack
the ghost. The player should be presented with a set of atleast three
options for attacks with each dealing a different amount of damage
and/or having other effects. What these attacks are, the damage they
deal, and their potential effects are up to you.

13. Detail the attack options for the player in `answers.md` 

After the player attacks, if the ghost has not been defeated, the ghost
will then perform an attack that decreases the player's hp by a set amount
plus a random value. For example, the ghost's base damage could be 8 with a 
random amount of additional damage up to 4 points. The ghost would thus 
deal between 8 to 12 damage on each attach.

The combat ends when either the ghost or player are defeated.

If the player is defeated, they lose the game.

If the ghost is defeated, exploration is resumed, and the player must still 
find the portkey to win the game.

Don't forget to include useful messages thoughout combat. Well formatted,
concise, and informative messages make all the difference in a text-based
game. A player who knows nothing about your implementation should be able
to play your game.

If the player gets to the portkey without encountering the ghost, the player
must defeat the ghost in the portkey room in order to win.

### Bonus: Ghost Attack Options (5 points)

Rather than having the ghost perform a simple attack every round, give the
ghost atleast two options for attacks and have the ghost automatically choose
what to do.

You automatic choice can be as simple as a random choice. You could also have
the ghost choose its attack based on other information.

These attacks and how the choice is made is up to you.

14. If implemented, detail the ghost attack options and game logic for 
ghost attack selection in `answers.md`.

## Epilogue

In this lab, you have built up a facility in asymptotic analysis and an 
intuition around these common functions. I hope that you've noticed some common 
general patterns which you can broadly apply.

With experience and practice, you will be able to consider an algorithm, 
determine its runtime, and quickly rank it relative to other algorithms and 
runtimes. We will continue to work on this in the coming weeks.