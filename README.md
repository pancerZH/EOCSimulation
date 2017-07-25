# EOCSimulation
一个封闭的简单生态系统模拟器

## 模拟情况描述

在一个封闭的生态系统中，存在且`仅存在`着一条`草->食草动物->食肉动物`的简单食物链，这里的任务就是模拟这个生态系统的发展过程    
为了便于模拟，我制订了几条简单的规则  
1. 模拟场地为正方形
2. 每个地块有四个选择：空地(Space)，草(Grass)，食草动物(GrassEater)，食肉动物(MeatEater)
3. 地块对应矩阵中的位置，不同属性的地块活动不同    
    - 空地不会移动，不会繁殖，不需要进食
    - 草不会移动，会繁殖，不需要进食
    - 食草动物和食肉动物会移动，会繁殖，需要进食
4. 活动说明(在一次迭代中)    
    - 活动范围：以生物在迭代开始时所处地块为中心的九宫格   
    - 如果能够进食，则必定先进食。捕食者会移动到被捕食者所在的地块上，原来的地块成为空地。若周围没有食物，此地块上的生物死亡，地块变为空地    
	- 如果能够繁殖，则在九宫格内的空地上产生一同类型生物
	- 进食和繁殖所选取的地块的位置是随机的
	
*本项目所有代码均在Python3.6.0下测试通过*
	
## 使用的模块

- matplotlib(2.0.0)
- numpy(1.11.3)

## 模拟结果展示

- 生物比较集中的结果		

	 - 开局    
	 ![image](https://github.com/pancerZH/EOCSimulation/blob/master/image/start1.png)
	 - 结束  
	 ![image](https://github.com/pancerZH/EOCSimulation/blob/master/image/end1.png)
	 
- 生物比较分散的结果

	- 开局  
	![image](https://github.com/pancerZH/EOCSimulation/blob/master/image/start2.png)
	- 结束  
	![image](https://github.com/pancerZH/EOCSimulation/blob/master/image/end2.png)
