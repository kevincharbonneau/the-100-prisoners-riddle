# The 100 Prisoners Riddle

## Introduction
A friend of mine shared [a very interesting video](https://www.youtube.com/watch?v=iSNsgj1OCLA) with me containing an explanation of "The 100 Prisoners Riddle". 

This problem was proposed by Danish computer scientist [Peter Bro Miltersen](https://ve42.co/GalMiltersen) back in 2003. 

>The 100 prisoners problem is a mathematical problem in probability theory and combinatorics. In this problem, 100 numbered prisoners must find their own numbers in one of 100 drawers in order to survive. The rules state that each prisoner may open only 50 drawers and cannot communicate with other prisoners. At first glance, the situation appears hopeless, but a clever strategy offers the prisoners a realistic chance of survival.

Essentially, by using a stragegy which involves every prisoners first picking their own number and then proceeding to picking the number inside the box. The prisoners raise their chances from a ~0.000 000 000 000 000 000 000 000 000 000 8 chance to a ~0.31183 chance ! 

## Rationale

It's not that I did not believe the mathematics behind the video but it was rather in a spirit of putting this theory to practice that I took upon myself to create a Python script which allowed the user to run a simulation of this riddle multiple time. 

I'm sure that many did this in the past and I, in no way, pretend that my code is perfectly optimized. But it was a fun little experimentation nontheless for an hour or so.

## Conclusions

![math-checks-ouf-gif](./resources/math-checks-out.gif)

I have executed the code multiple time and in most cases we really stay in a general area of one victory out of three, which seems to validate the hypothesis !

```bash
$ python run.py run --run_count=1000 --prisoners_count=100 --strategize 
100%|█████████████████████████████████████████████████████████████████████████████████████████| 1000/1000 [00:03<00:00, 277.92it/s]

final results: 0.309% time freed
```

## Usage
Here are further instructions on how to execute the code.

### Requirements
* Have Python installed (https://www.python.org/downloads/)
* (Recommended but optional) Using a [virtualenv](https://virtualenv.pypa.io/en/latest/) to install your Python Packages

### Instructions

You first clone this repository 
```bash
git clone https://github.com/kevincharbonneau/ ....
cd ....
```

Then you want to install the python packages
```bash
pip install -r requirements.txt
```

Finally, you want to execute the code (be careful, by default the code will use the random approach see below)
```bash
python run.py run
```

### Parameters
* `--run_count`: Allows the user to execute the specified amount of simulations to be run
* `--prisoners_count`: Allows the user to specify the quantity of prisoners (must be an even number)
* `--strategize`: Using this will use the strategy mentionned above to improve chances (otherwise we simply pick numbers at random)

## References 

* [The Riddle That Seems Impossible Even If You Know The Answer](https://www.youtube.com/watch?v=iSNsgj1OCLA) -- [Veritasium](https://www.youtube.com/c/veritasium)
* Original paper: Gál, A., & Miltersen, P.B. (2003). The Cell Probe Complexity of Succinct Data Structures. BRICS, Department of Computer Science, University of Aarhus. All rights reserved. – https://ve42.co/GalMiltersen
* https://en.wikipedia.org/wiki/100_prisoners_problem