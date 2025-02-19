# decalab2025
evidence for deca lab


## Challenge 1: multiply
### attempt 1: single cycle:

observations: 
- after using pen and paper to optimise a dadda tree multiplier, I saw it would go hugely over the limit for adders
- wanted to do a single cycle approach to be the same as the rest of the instructions

approach:
- generate combinational logic with python file
- carries are wholly combinational and therefore dont use adders
- used optimised dadda tree for remaining additions
- see images for hardware

#### datapath
![datapath](https://github.com/user-attachments/assets/c3f6e0cf-b727-4e19-9fb5-5e7d848f924d)

#### ALU
![ALU](https://github.com/user-attachments/assets/9641b742-4a12-4fa1-92b2-479148915db3)

#### normalise
![normalise](https://github.com/user-attachments/assets/ca9e6c08-7b94-4be7-99bf-5dedb0710993)

#### multiplier
![multiplier](https://github.com/user-attachments/assets/f54c39bf-80e9-41c5-ae1a-6dfeaca53d74)

#### carry generation
![carry generation](https://github.com/user-attachments/assets/a5b2feb5-4056-46b0-a94d-595352a80122)

#### multiply dot diagram

![dadda](https://github.com/user-attachments/assets/c2c4a9db-b9e4-46e1-bffe-c45f9786877a)


### attempt 2: multi cycle
