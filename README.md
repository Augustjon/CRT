# CRT
A python program that solves systems of congruent equations using the Chinese remainder theorem (CRT)

The program solves systems of congruent equations on the form:

 X $\equiv$ $a_1$  mod $m_1$  
 X $\equiv$ $a_2$  mod $m_2$  
 X $\equiv$ $a_3$  mod $m_3$  
 .  
 .  
 X $\equiv$ $a_k$ mod $m_k$  
 
 #### input
 input is the txt file `problem.txt` on the form:  
 $a_1$ $m_1$  
 $a_2$ $m_2$  
 .  
 .  
 .  
 $a_k$ $m_k$  
 where the $a_i$ and $m_i$ is seperated by a whitespace.  
 
 the system can not solve systems where the $m_i$ are not pair wise relative prime. Later implementations will be able to solve these systems because you can rewrite the system in relative prime factors.

#### output
the output is simply the $X$ that satisfies all the equations in the system mod m where $m$ is the product of $m_i$ 
