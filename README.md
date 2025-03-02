# decalab2025
evidence for deca lab


## Challenge 1: multiply
### attempt 1: single cycle:

observations: 
- after using pen and paper to optimise a dadda tree multiplier, I saw it would go hugely over the limit for adders
- wanted to do a single cycle approach to be the same as the rest of the instructions

approach:
- generate combinational logic with python file - https://github.com/Original-2/decalab2025/blob/main/veriloggenerator.py
- carries are wholly combinational and therefore dont use adders
- used optimised dadda tree for remaining additions
- see images for hardware

#### datapath
![datapath](https://github.com/user-attachments/assets/c3f6e0cf-b727-4e19-9fb5-5e7d848f924d)

#### multiplier
![multiplier](https://github.com/user-attachments/assets/f54c39bf-80e9-41c5-ae1a-6dfeaca53d74)

#### carry generation
![carry generation](https://github.com/user-attachments/assets/a5b2feb5-4056-46b0-a94d-595352a80122)

#### multiply dot diagram
![dadda](https://github.com/user-attachments/assets/c2c4a9db-b9e4-46e1-bffe-c45f9786877a)


EVERYTHING ELSE SAME AS BELOW. ISSIE FILE LOST SO ONLY ATTEMPT 2 ATTATCHED.



### attempt 2: multi cycle


![image](https://github.com/user-attachments/assets/0daa02c0-c54b-4643-b1cb-714cab9a1127)
![image](https://github.com/user-attachments/assets/d5eafc15-2aed-4f1b-a48e-f468f330057d)
![image](https://github.com/user-attachments/assets/29e770f7-9d5a-4fed-a453-21b430ae3fd8)

method: 

#### sum 4 prtil products t any given time
![image](https://github.com/user-attachments/assets/0dc162b6-1f45-45e8-be27-3fc1fd9f03de)

#### normalise
![image](https://github.com/user-attachments/assets/a047385f-c749-4267-a884-d4df59da2340)

sign is xor, exponent adds (and bis subtracted), and 20 prtial products added each time
![image](https://github.com/user-attachments/assets/9745078b-0da6-4b20-8e79-9fdd4483b772)

#### dont increment PC depending on state of multiply

![image](https://github.com/user-attachments/assets/86f7a28f-56a2-4f1e-9b73-b189de273bcf)
![image](https://github.com/user-attachments/assets/c9667426-700d-4d3f-8920-12b6ef124a32)

#### write on 5th cycle of multiply

![image](https://github.com/user-attachments/assets/b995c42a-e821-4c32-9e86-f63480ce1825)
![image](https://github.com/user-attachments/assets/348b2c41-4580-4d8a-bc11-d8fbee8ef6e2)
![image](https://github.com/user-attachments/assets/f69d139a-5d1b-478a-8411-0d6c438f7a5f)
![image](https://github.com/user-attachments/assets/465086c3-292d-4708-bdbd-3fd555f1b7ba)
![image](https://github.com/user-attachments/assets/391746bf-11e5-4edc-a36d-3049629f402d)
![image](https://github.com/user-attachments/assets/e522392d-bdfc-4c93-8062-ee433603dc06)
![image](https://github.com/user-attachments/assets/eaaf4e4e-4c52-49a3-bf82-fecc38521284)




![image](https://github.com/user-attachments/assets/34779701-b1ad-4fd4-b05f-4b4218e7fb3e)





![image](https://github.com/user-attachments/assets/cf87c06b-e6f8-48a3-af9b-ad512a385c57)
![image](https://github.com/user-attachments/assets/7205911e-9d85-4a19-873e-6c8f1970700e)
![image](https://github.com/user-attachments/assets/b72d6519-c36a-4c53-aa57-03d3c48ac254)
![image](https://github.com/user-attachments/assets/77223ac2-ef2d-47aa-8626-a8e1549716ae)




evcen negatives
![image](https://github.com/user-attachments/assets/c148eaa0-d7c3-40f6-a8d3-a115b4b90fef)




BOTH ROUNDED BY TRUNCATION (ROUNDING TOWARDS 0)
