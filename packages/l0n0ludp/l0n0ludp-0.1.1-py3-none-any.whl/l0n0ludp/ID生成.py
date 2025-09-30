class 循环ID生成器:
    def __init__(self, 最大值: int) -> None:
        self.当前ID = 0
        self.最大值 = 最大值

    def __call__(self):
        ret = self.当前ID
        self.当前ID = (self.当前ID + 1) % self.最大值
        return ret
