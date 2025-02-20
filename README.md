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

#### multiply examples
![image](https://github.com/user-attachments/assets/15b7919d-65e7-40c9-8b18-e29b5d4178c6)
![image](https://github.com/user-attachments/assets/4102c7af-7fc7-45a9-bbd5-97c47db9b63f)

#### shift exmples

![image](https://github.com/user-attachments/assets/8426d469-1e5c-4789-badc-d160611705eb)
![image](https://github.com/user-attachments/assets/03eb919e-129a-42a7-97db-dbf2506f227e)
![image](https://github.com/user-attachments/assets/3afb273a-e41a-4931-8c3a-74ca61a34deb)


### attempt 2: multi cycle: Work in progress
