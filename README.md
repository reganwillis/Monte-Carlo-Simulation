# Monte-Carlo-Simulation

## Monte Carlo Method
The [Monte Carlo method](https://en.wikipedia.org/wiki/Monte_Carlo_method) was named after the [city's tourist gambling culture](https://en.wikipedia.org/wiki/Monte_Carlo_Casino). It uses randomness to solve problems that aren't random by nature and could be solved mathematically. Sometimes, the Monte Carlo method is easier to implement than the complicated equation. And by using computers to quickly generate thousands of experiements (this one uses 20,000), it is usually accurate.

## The Question
This program uses the concept of a [random walk](https://en.wikipedia.org/wiki/Random_walk#:~:text=In%20mathematics%2C%20a%20random%20walk,space%20such%20as%20the%20integers.) in conjunction with the Monte Carlo method. A walk is simulated randomly to be a certain number of blocks away from home. The walker does not want to call a transport service to get back home at the end of their walk, but it's too far to walk home if they are more than 5 blocks away at the end of the walk. The question is: what is the longest random walk you can take so that on average you will end up 5 blocks or fewer from home?

## Methodology
This program is a variation of this [tutorial](https://www.youtube.com/watch?v=BfS2H1y6tzQ). My program simulates random walks from block-length of 1 to 50. Each walk length is computed 20,000 times and the program finds the percentage of walks that were a short enough distance from home at the end. The walks with a percentage of 50 or greater will end up 5 blocks or fewer from home on average (walks of length 1-5 will be 100% because the walker can't be more than 5 blocks away). The answer is returned as the longest walk with a percentage of 50 or greater.